import argparse
import sys
from typing import Dict, List, Any
import re
import time
import json
from pathlib import Path
import ollama

from app.config import RAG_LLM_MODEL, GENERAL_LLM_MODEL

from app.retrieve import (
    retrieve,
    retrieve_email_cases,
    format_citation,
    is_definition_query,
    is_advisory_query,
    extract_acronyms_for_glossary_lookup,
)

ANSWER_VARIANT_CHUNKS = None
# Retrieval / context limits
TOP_K_TO_MODEL = 3
MAX_CONTEXT_CHARS = 4500
MAX_SNIPPET_CHARS = 1000
EMAIL_CASES_TO_MODEL = 6

# Weak retrieval guardrails
MIN_TOP_SCORE = 1.20
WEAK_RETRIEVAL_FALLBACK_K = 3

def parse_mode_and_question(raw_question: str) -> tuple[str, str]:
    text = raw_question.lstrip()

    if text.startswith("+ "):
        return "rag", text[2:].strip()
    if text.startswith("- "):
        return "general", text[2:].strip()
    if text.startswith("@ "):
        return "email", text[2:].strip()

    return "auto", raw_question.strip()

def extract_explicit_program_hint(question: str) -> tuple[str | None, str]:
    q = question.strip()

    match = re.match(
        r"^\s*in\s+(bluetooth|bt|ble|matter|aliro)\s*,?\s+(.+)$",
        q,
        flags=re.IGNORECASE,
    )

    if not match:
        return None, question

    raw_program = match.group(1).lower()
    cleaned_question = match.group(2).strip()

    program_map = {
        "bluetooth": "bluetooth",
        "bt": "bluetooth",
        "ble": "bluetooth",
        "matter": "matter",
        "aliro": "aliro",
    }

    return program_map.get(raw_program), cleaned_question

PROGRAM_ALIASES = {
    "bluetooth": ["bluetooth", "ble", "bt", "ブルートゥース"],
    "matter": ["matter", "マター"],
    "aliro": ["aliro", "アリロ"],
}

def infer_program_from_question(question: str) -> str | None:
    """
    Detect the program named anywhere in the question, in any language.
    Returns None only if no program is mentioned at all.
    """
    q = question.lower()
    hits = [
        program
        for program, aliases in PROGRAM_ALIASES.items()
        if any(re.search(rf"(?<![a-z]){re.escape(a)}(?![a-z])", q) for a in aliases)
    ]
    return hits[0] if len(hits) == 1 else None

def looks_like_followup_question(question: str) -> bool:
    q = question.strip().lower()

    followup_signals = [
        "it",
        "this",
        "that",
        "they",
        "them",
        "those",
        "these",
        "how about",
        "what about",
        "compare it",
        "compare this",
        "how is it different",
        "how is this different",
        "tell me more",
        "explain more",
    ]

    if any(re.search(rf"\b{re.escape(signal)}\b", q) for signal in followup_signals):
        return True

    if q.startswith(("and ", "also ", "but ")):
        return True

    return False

def ask_llm_general(question: str) -> str:
    language = resolve_language(question)

    if language == "ja":
        system_prompt = (
            "You are a helpful general assistant. "
            "Answer naturally in Japanese. "
            "Do not mention internal documents, retrieval, or missing specs."
        )
    else:
        system_prompt = (
            "You are a helpful general assistant. "
            "Answer naturally in English. "
            "Do not mention internal documents, retrieval, or missing specs."
        )

    response = ollama.chat(
        model=GENERAL_LLM_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question},
        ],
    )

    answer = response["message"]["content"].strip()

    if answer:
        return answer

    print("⚠️ Empty model output. Retrying with simplified prompt...")

    simple_prompt = (
        "Answer the question using only the evidence below. "
        "Write a concise final answer. Do not include reasoning.\n\n"
        f"Question:\n{question}\n\n"
        f"Evidence:\n{format_context_for_simple_retry(items)}"
    )

    retry_response = ollama.chat(
        model=RAG_LLM_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a technical assistant. Give only the final answer.",
            },
            {
                "role": "user",
                "content": simple_prompt,
            },
        ],
        options={
            "temperature": 0.1,
            "num_predict": 300,
            "num_ctx": 4096,
        },
    )

    return retry_response["message"]["content"].strip()

def resolve_language(query: str) -> str:
    q = query.lower()

    if "in japanese" in q or "日本語" in q:
        return "ja"

    # simple detection
    if any(ord(c) > 128 for c in query):
        return "ja"

    return "en"

def extract_answer_core_term(question: str) -> str:
    q = question.strip()

    # Remove leading domain phrase like "In Aliro,"
    q = re.sub(r"^\s*in\s+[a-z0-9_\- ]+\s*,\s*", "", q, flags=re.IGNORECASE)

    patterns = [
        r"^what\s+is\s+(.+)$",
        r"^what\s+are\s+(.+)$",
        r"^define\s+(.+)$",
    ]

    term = q
    for pattern in patterns:
        m = re.search(pattern, q, re.IGNORECASE)
        if m:
            term = m.group(1)
            break

    acronym_match = re.search(r"(?<![A-Za-z0-9])[A-Z][A-Z0-9/\-]{1,9}(?![A-Za-z0-9])", q)
    if acronym_match:
        term = acronym_match.group(0)

    term = term.strip(" ?.")
    term = re.sub(r"^(a|an|the)\s+", "", term, flags=re.IGNORECASE)

    return term.strip()

def language_instruction(language: str) -> str:
    if language == "ja":
        return (
            "Write the entire answer in Japanese. "
            "Do not answer in English except for source terms that must remain in English. "
            "Keep citations unchanged."
        )
    return "Write the entire answer in English. Keep citations unchanged."

def retrieval_is_weak(items: List[Dict[str, Any]]) -> bool:
    if not items:
        return True

    top = float(items[0].get("score", 0.0))
    if top >= MIN_TOP_SCORE:
        return False

    decent_official_hits = 0
    for item in items[:5]:
        score = float(item.get("score", 0.0))
        doc_type = (item.get("metadata", {}).get("doc_type") or "").lower()
        source_type = (item.get("metadata", {}).get("source_type") or "").lower()

        if (
            score >= 5.0
            and doc_type in {"policies", "faq", "reference", "guides", "explanations", "specs"}
            and source_type not in {"email_case", "email_thread_analysis", "email"}
        ):
            decent_official_hits += 1

    return decent_official_hits < 2

RETRIEVAL_KEYWORDS_DIR = Path(__file__).parent / "retrieval_keywords"
RETRIEVAL_KEYWORD_CACHE: Dict[str, Dict[str, str]] = {}


def load_retrieval_keywords(program: str | None) -> Dict[str, str]:
    if not program:
        return {}

    program_key = program.lower().strip()

    if program_key in RETRIEVAL_KEYWORD_CACHE:
        return RETRIEVAL_KEYWORD_CACHE[program_key]

    path = RETRIEVAL_KEYWORDS_DIR / f"{program_key}.json"

    if not path.exists():
        RETRIEVAL_KEYWORD_CACHE[program_key] = {}
        return {}

    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        keywords = data.get("expansion_keywords", {})
        if not isinstance(keywords, dict):
            keywords = {}

    except Exception:
        keywords = {}

    RETRIEVAL_KEYWORD_CACHE[program_key] = keywords
    return keywords


def expand_retrieval_query_with_keywords(question: str, program: str | None) -> str:
    keywords = load_retrieval_keywords(program)

    if not keywords:
        return question

    matched_terms = []

    question_lower = question.lower()

    for trigger, expansion in keywords.items():
        if trigger.lower() in question_lower:
            matched_terms.append(str(expansion))

    if not matched_terms:
        return question

    return (
        question
        + "\n\nRetrieval keywords: "
        + " ".join(matched_terms)
    )

def load_system_prompt(language: str) -> str:
    return f"""
You are an internal technical consultant.

Use only the provided INTERNAL EVIDENCE unless it is genuinely insufficient.

Rules:
- Treat INTERNAL EVIDENCE as the source of truth.
- CRITICAL: Qualification, certification, listing, declaration, or registration is the compliance status or process. Testing is an activity or evidence source. These are never the same thing. If asked whether qualification/certification/listing/declaration/registration is required, answer that requirement first. Discuss testing scope only after, and separately.
- Do not expand acronyms unless the provided evidence explicitly expands them. If the evidence uses only the acronym, keep only the acronym.
- Do not invent facts, definitions, expansions, translations, examples, or process steps not supported by the evidence.
- Do not mix grounded evidence and model knowledge in the same paragraph.
- If the evidence is sufficient, do not output any "General knowledge (model-based)" section.
- Ground the answer only in the provided INTERNAL EVIDENCE.
- Do not place citations, placeholders, or citation labels inside the prose answer.
- Do not write strings like "[citation needed]" or "[chunk_id | Doc (p.1)]".
- A separate citations section may be added after the prose answer if supported by the evidence provided.
- Do not shorten, rewrite, or omit any part of the citation.

For definition questions:
- Write the answer as one clear paragraph.
- Do not use bullets or numbered lists.
"- If the evidence contains a dedicated explanation or how-it-works source, prefer that as the primary definition source for concept questions.\n"
"- If the evidence contains a spec glossary or definitions section, use it to supplement the explanation, not replace it.\n"
"- Start with the clearest and most direct definition available across all sources.\n"
- After the primary definition, you may add one short contextual sentence grounded in the retrieved evidence to explain how the term is used in practice.
- Use other excerpts only for short clarification after the primary definition.
- Do not replace the glossary definition with protocol behavior, implementation details, key handling, certificate handling, or procedure details.
- If the evidence contains an acronym expansion in the form "Full Term (ACRONYM)" or "ACRONYM (Full Term)", use that exact expansion.
- Do not invent or substitute a different expansion.
- Do not expand acronyms unless the evidence explicitly provides the expansion or approved memory defines it.
- FAQ or reference content may be used only to simplify or clarify, not to override a spec definition.
- Do not repeat the same definition in different words.

For process questions:
- Give steps only if they are supported by the evidence.

Language:
- Answer in the language requested by the user.
- If Japanese is requested, write the prose in Japanese.
- Keep technical source terms exactly as written when needed.
- Do not invent translated technical terms unless the evidence explicitly provides them.
- Keep standard technical terms and acronyms in English (for example: Bluetooth, BLE, SIG, RF PHY, PTS, ICS, IXIT, QDID).

General knowledge:
- Add a "General knowledge (model-based)" section only if internal evidence is genuinely insufficient.
- If internal evidence is sufficient, omit that section entirely.
- Do not restate grounded evidence inside that section.

Output format:
- Write only the final answer prose.
- Never write citations inside the answer paragraph. Put citations only in the final Citations section.
- Avoid repeating the same requirement in different wording. State each requirement once.
- Do not print section headers unless "General knowledge (model-based)" is truly needed.
- If internal evidence is sufficient, output only one grounded paragraph with citations.
""".strip()

def add_glossary_support_sources(
    question: str,
    selected: List[Dict[str, Any]],
    program: str | None,
    max_added: int = 2,
) -> List[Dict[str, Any]]:
    selected_ids = {item["chunk_id"] for item in selected}

    effective_program = program or (
        selected[0].get("metadata", {}).get("program") if selected else None
    )

    evidence_text = question + "\n" + "\n".join(
        item.get("text") or "" for item in selected
    )

    acronyms = extract_acronyms_for_glossary_lookup(evidence_text)

    if not acronyms:
        return selected

    added = 0

    for acronym in acronyms:
        query = f"in {effective_program} what is {acronym}?"

        glossary_hits = retrieve(
            query,
            top_k=8,
            program=effective_program,
        )

        for hit in glossary_hits:
            if hit["chunk_id"] in selected_ids:
                continue

            meta = hit.get("metadata", {})
            doc_type = (meta.get("doc_type") or "").lower()
            source_type = (meta.get("source_type") or "").lower()
            doc_name = (meta.get("doc_name") or "").lower()
            text = hit.get("text") or ""
            text_lower = text.lower()

            if doc_type not in {"policies", "specs", "reference"}:
                continue

            if is_email_source(hit):
                continue

            if acronym.lower() not in text_lower:
                continue

            looks_like_glossary = (
                "glossary" in doc_name
                or "definitions" in text_lower
                or "acronym" in text_lower
                or "abbreviation" in text_lower
            )

            if not looks_like_glossary:
                continue

            selected.append(hit)
            selected_ids.add(hit["chunk_id"])
            added += 1
            break

        if added >= max_added:
            break

    return selected

def compact_email_case_text(text: str) -> str:
    """
    Convert email-case JSON chunks into compact evidence notes.
    Keeps the useful advisory content and removes JSON noise.
    """
    if not text:
        return ""

    try:
        import json

        data = json.loads(text)
        cases = data.get("cases", [])

        if not cases:
            return text

        case = cases[0]

        fields = [
            ("Customer question", case.get("customer_question")),
            ("Actual issue", case.get("actual_issue")),
            ("Plain explanation", case.get("plain_english_explanation")),
            ("Consultant answer", case.get("consultant_answer")),
            ("Decision logic", case.get("decision_logic")),
            ("Final recommendation", case.get("final_recommendation")),
            ("Risk if done wrong", case.get("risk_if_done_wrong")),
        ]

        lines = []
        for label, value in fields:
            if value:
                lines.append(f"{label}: {value}")

        return "\n".join(lines) if lines else text

    except Exception:
        return text

def is_practical_requirement_query(question: str) -> bool:
    q = question.lower()
    practical_terms = [
        "what do we need",
        "what should we",
        "prepare",
        "include",
        "required",
        "requirements",
        "need to",
        "必要",
        "入れる",
        "準備",
        "含める",
    ]
    return any(term in q for term in practical_terms)

def build_model_input(
    question: str,
    items: List[Dict[str, Any]],
    language: str,
    grounded_expansion: str | None = None,
    detail_mode: str = "normal",
) -> str:
    parts: List[str] = []

    parts.append(
        "\nSource synthesis guidance:\n"
        "- Use all relevant retrieved excerpts, not only the first one.\n"
        "- Treat source_role: PRIMARY as the main source; use SUPPORTING sources only to clarify, add conditions, or provide examples.\n"
        "- Prefer official policy/spec sources for requirements, rules, definitions, tables, and procedures. Use FAQ/reference sources to clarify them. Use email/case sources only as practical examples unless no official source is available.\n"
        "- For exact-label questions such as Option, Table, Section, or Clause questions, answer from the exact heading/table source first, then add nearby details only if they are directly relevant.\n"
        "- For yes/no decision questions, start with Yes/No when the evidence supports it. Use It depends / 場合によります only when the required outcome itself depends on conditions.\n"
        "- Do not conflate testing with qualification, certification, listing, declaration, registration, or approval. Testing is an activity or evidence source; qualification/certification/listing/declaration/registration/approval is the compliance status or process. If the user asks whether qualification/certification/listing/declaration/registration/approval is required, answer that requirement first, then discuss testing scope separately.\n"
        "- Separate the required outcome from its scope. If the question asks whether something is required, answer the requirement first; then explain whether the work, testing, documentation, or review scope may be reduced, limited, or conditional.\n"
        "- If a general requirement has exceptions or variable scope, state the general requirement first, then explain the exception, reduced scope, or changed-part-only condition. Apply an exception only when the user's facts clearly match it.\n"
        "- When scope varies, say that work/testing/documentation may vary; do not imply the requirement disappears unless the evidence explicitly says so.\n"
        "- If the user asks in Japanese, start with はい or いいえ for direct requirement answers when supported.\n"
        "- If email/case evidence is used, keep it in a separate 'Case reference:' or '参考事例:' section and do not present it as official policy.\n"
        "- If sources disagree, say so clearly and prefer official policy/spec text for requirements.\n"
        "- For official tables, extract only the table row labels and conditions stated in the table; do not infer extra contents unless another excerpt explicitly defines them.\n"
    )

    if language == "ja":
        parts.append("Requested output language: Japanese (日本語 only).")
    else:
        parts.append("Requested output language: English.")

    parts.append(f"\nQuestion:\n{question}")

    if grounded_expansion:
        parts.append(
            f"\nGrounded acronym expansion found in the evidence:\n"
            f"- Use this exact expansion: {grounded_expansion}\n"
            f"- Do not invent a different expansion.\n"
            f"- Explain only what is supported by the provided excerpts.\n"
        )

    if is_definition_query(question) and not is_practical_requirement_query(question):
        parts.append("\n" + definition_mode_instruction(detail_mode))

        if detail_mode == "wide":
            sentence_limit = 6
        elif detail_mode == "deep":
            sentence_limit = 4
        else:
            sentence_limit = 2

        definition_sentences = extract_glossary_definition_lines(
            question,
            items,
            max_lines=1,
        )

        if not definition_sentences:
            definition_sentences = extract_definition_sentences(
                question,
                items,
                max_sentences=sentence_limit,
            )

        if definition_sentences:
            parts.append(
                "\nDefinition clue:\n"
                + "\n".join(f"- {s}" for s in definition_sentences)
                + "\nUse this only to identify the term. For the actual answer, use the most relevant retrieved excerpts, include any conditions, required inputs, or limitations, and avoid repeating the same definition in different wording."
            )

    parts.append(
        "\nAllowed citations:\n"
        + "\n".join(
            f"- [{item['chunk_id']} | {format_citation(item['metadata'])}]"
            for item in items
        )
        + "\nUse only these citations. Do not invent any other citation."
    )
    
    parts.append("\nINTERNAL EVIDENCE EXCERPTS:")

    total_chars = 0
    for idx, item in enumerate(items):
        meta = item["metadata"]

        citation = format_citation(meta)
        header = (
            "\n---\n"
            f"use_this_citation_exactly: [{item['chunk_id']} | {citation}]\n"
            f"program: {meta.get('program')}\n"
            f"type: {meta.get('doc_type')}\n"
            f"chunk_kind: {meta.get('chunk_kind')}\n"
            f"priority: {meta.get('priority', 0)}\n"
            f"score: {item.get('score', 0.0):.4f}\n"
            f"source_role: {'PRIMARY' if idx == 0 else 'SUPPORTING'}\n"
        )

        text = (item.get("text") or "").strip()
        source_type = (meta.get("source_type") or "").lower()

        if is_email_source(item):
            text = compact_email_case_text(text).strip()
        
        remaining = MAX_CONTEXT_CHARS - total_chars
        doc_type = (meta.get("doc_type") or "").lower()

        chunk_kind = (meta.get("chunk_kind") or "").lower()

        if doc_type in {"policies", "specs"}:
            remaining = min(remaining, 2200)
        elif chunk_kind == "body":
            remaining = min(remaining, 2200)
        else:
            remaining = min(remaining, MAX_SNIPPET_CHARS)
        if remaining <= 0:
            break

        raw_terms = [w.lower() for w in re.findall(r"[A-Za-z0-9/\-]+", question) if len(w) >= 3]

        stop_terms = {
            "what", "which", "when", "where", "who", "why", "how",
            "is", "are", "do", "does", "did", "can", "could", "should",
            "would", "if", "the", "a", "an", "for", "to", "of", "in",
            "on", "with", "and", "or", "we", "you", "need", "used", "use",
            "run", "test", "tool"
        }
        question_terms = sorted(
            [t for t in raw_terms if t not in stop_terms],
            key=len,
            reverse=True,
        )

        text_lower = text.lower()

        hit_pos = -1
        for term in question_terms:
            pos = text_lower.find(term)
            if pos != -1:
                hit_pos = pos
                break

        if hit_pos != -1 and len(text) > remaining:
            window_half = max(remaining // 2, 200)
            start = max(0, hit_pos - window_half)
            end = min(len(text), start + remaining)
            start = max(0, end - remaining)
            snippet = text[start:end]
        else:
            snippet = text[:remaining]

        parts.append(header + snippet)
        total_chars += len(snippet)

    if language == "ja":
        parts.append(
            "\nInstructions:\n"
            "- Write the entire answer in Japanese.\n"
            "- Do not answer in English except for document names and citations.\n"
            "- Translate the grounded answer into natural Japanese.\n"
            "- Do not say that Japanese translation is unavailable unless the user explicitly asks whether an official Japanese term exists.\n"
            "- Do not append 'Not clearly specified in retrieved internal evidence.' unless some required part of the question truly cannot be answered from the excerpts.\n"
            "- Answer strictly from the excerpts when possible.\n"
            "- When reporting table values, preserve labels exactly. If a table cell says 'As required', write 'As required', not 'required as required' or 'required as necessary'.\n"
            "- Write clean prose only.\n"
            "- Do not write inline citations, placeholder citations, or '[citation needed]'.\n"
            "- Do not write 'chunk_id:' anywhere in the answer.\n"
            "- Omit 'General knowledge (model-based)' if internal evidence is sufficient.\n"
        )
    else:
        parts.append(
            "\nInstructions:\n"
            "- Write the entire answer in English.\n"
            "- Answer strictly from the excerpts when possible.\n"
            "- When answering a follow-up question, preserve the main subject from the recent conversation. If you narrow the subject to a subtype or example, say so clearly.\n"
            "- Write clean prose only.\n"
            "- Do not write inline citations, placeholder citations, or '[citation needed]'.\n"
            "- Do not write 'chunk_id:' anywhere in the answer.\n"
            "- Do not append 'Not clearly specified in retrieved internal evidence.' unless some required part of the question truly cannot be answered from the excerpts.\n"
            "- Omit 'General knowledge (model-based)' if internal evidence is sufficient.\n"
        )

    return "\n".join(parts)

def format_context_for_simple_retry(items: List[Dict[str, Any]], max_chars: int = 4000) -> str:
    parts = []
    total = 0

    for item in items:
        meta = item["metadata"]
        citation = format_citation(meta)

        text = (item.get("text") or "").strip()
        source_type = (meta.get("source_type") or "").lower()

        if is_email_source(item):
            text = compact_email_case_text(text).strip()

        block = (
            f"[{item['chunk_id']} | {citation}]\n"
            f"{text}\n"
        )

        remaining = max_chars - total
        if remaining <= 0:
            break

        parts.append(block[:remaining])
        total += len(block[:remaining])

    return "\n---\n".join(parts)

def ask_llm(
    question: str,
    items: List[Dict[str, Any]],
    weak_retrieval: bool = False,
    grounded_expansion: str | None = None,
    detail_mode: str = "normal",
    language_override: str | None = None,
) -> str:
    language = language_override or resolve_language(question)
    system_prompt = load_system_prompt(language)

    case_requested = any(
        phrase in question.lower()
        for phrase in [
            "case",
            "past",
            "email",
            "customer case",
            "past case",
            "in practice",
        ]
    )

    if not case_requested:
        items = [
            item for item in items
            if not is_email_source(item)
        ]

    user_prompt = build_model_input(
        question,
        items,
        language,
        grounded_expansion=grounded_expansion,
        detail_mode=detail_mode,
    )

    if any(
        phrase in question.lower()
        for phrase in [
            "difference between",
            "compare",
            "comparison",
            "versus",
            " vs ",
            "different from",
        ]
    ):
        user_prompt += (
            "\n\nComparison answer requirement:\n"
            "- Explicitly explain each item separately.\n"
            "- State the practical difference between them.\n"
            "- Do not answer only that they are related or used together.\n"
            "- If one source is only an example, do not describe the concept as limited to that example.\n"
            "- End with one explicit sentence beginning with: 'In short, the difference is:'\n"
        )

    Path("/tmp/rag_prompt_debug.txt").write_text(user_prompt, encoding="utf-8")
    if weak_retrieval:
        user_prompt += (
            "\n\nNote: retrieval quality is weak. "
            "Use the evidence cautiously. "
            "If the excerpts only partially support the answer, say so clearly."
        )

    response = ollama.chat(
        model=RAG_LLM_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        think=False,
        options={
            "temperature": 0.1,
            "top_p": 0.9,
            "top_k": 40,
            "num_predict": 900,
            "num_ctx": 8192,
        },
    )

    print("RAW OLLAMA RESPONSE:")
    print(response)

    return response["message"]["content"].strip()

def separate_citations(answer: str, items: List[Dict[str, Any]]) -> str:
    citation_map = {}
    for item in items:
        meta = item["metadata"]
        full_citation = f"[{item['chunk_id']} | {format_citation(meta)}]"
        citation_map[item["chunk_id"]] = full_citation

    for chunk_id, full_citation in citation_map.items():
        doc_name = chunk_id.split(":")[-1]
        answer = answer.replace(f"[{chunk_id}]", full_citation)
        answer = answer.replace(f"[Citation: {chunk_id}]", full_citation)
        answer = answer.replace(f"[citation: {chunk_id}]", full_citation)
        answer = answer.replace(f"[chunk_id: {chunk_id}]", full_citation)
        answer = answer.replace(f"[chunk_id: {chunk_id} | {doc_name}]", full_citation)

    found = []

    for full_citation in citation_map.values():
        if full_citation in answer and full_citation not in found:
            found.append(full_citation)

    for full_citation in found:
        answer = answer.replace(full_citation, "").strip()

    answer = re.sub(
        r"\s*\[[^\]\n]*bluetooth:[^\]\n]*(?:\]|\n|$)",
        "",
        answer,
        flags=re.IGNORECASE,
    )

    answer = re.sub(r"\[citation needed[^\]]*\]", "", answer, flags=re.IGNORECASE)
    answer = re.sub(r"\[source needed[^\]]*\]", "", answer, flags=re.IGNORECASE)
    answer = re.sub(r"\[reference needed[^\]]*\]", "", answer, flags=re.IGNORECASE)
    answer = re.sub(r"\[citation:\s*[^\]]+\]", "", answer, flags=re.IGNORECASE)
    answer = re.sub(r"\n+\**Answer:\**\s*", "\n\n", answer, flags=re.IGNORECASE)

    answer = re.sub(r"[ \t]+", " ", answer)
    answer = re.sub(r"\s+([.,;:!?])", r"\1", answer)
    answer = re.sub(r"\n{3,}", "\n\n", answer).strip()
    answer = re.sub(r"\n*Citations:\s*(?:-|\n-\s*)*", "", answer, flags=re.IGNORECASE).strip()
    answer = re.sub(r"(?m)^[\*\-\s]+$", "", answer).strip()

    if not found and items:
        item = items[0]
        found = [
            f"[{item['chunk_id']} | {format_citation(item['metadata'])}]"
        ]

    found = found[:5]

    if found:
        answer += "\n\nCitations:\n" + "\n".join(f"- {c}" for c in found)

    return answer

def find_exact_acronym_items(question: str, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    if not is_definition_query(question):
        return []
    return items

def extract_exact_acronym_expansion(question: str, items: List[Dict[str, Any]]) -> str | None:
    q = question.strip()
    lower = q.lower()

    prefixes = ["what is ", "what are ", "define "]
    term = q
    for prefix in prefixes:
        if lower.startswith(prefix):
            term = q[len(prefix):].strip(" ?")
            break
    term = term.strip(" ?")

    acronym_match = re.search(r"\b[A-Z][A-Z0-9/\-]{1,9}\b", q)
    if acronym_match:
        term = acronym_match.group(0)

    if not re.fullmatch(r"[A-Za-z0-9/\-]{2,10}", term):
        return None

    patterns = [
        re.compile(
            rf"([A-Za-z][A-Za-z0-9/&,\-]*(?: [A-Za-z][A-Za-z0-9/&,\-]*){{1,12}})\s*\(\s*{re.escape(term)}\s*\)",
            re.IGNORECASE,
        ),
        re.compile(
            rf"\b{re.escape(term)}\b\s*\(\s*([A-Za-z][A-Za-z0-9/&,\- ]{{3,100}}?)\s*\)",
            re.IGNORECASE,
        ),
    ]

    for item in items:
        text = item.get("text", "") or ""
        for pat in patterns:
            for m in pat.finditer(text):
                candidate = " ".join(m.group(1).split()).strip(" ,;:-")
                words = re.findall(r"[A-Za-z]+", candidate)
                if len(words) < 2:
                    continue

                initials = "".join(w[0].upper() for w in words if w)
                if initials == term.upper():
                    return candidate

                for n in range(2, min(5, len(words) + 1)):
                    tail = words[-n:]
                    tail_initials = "".join(w[0].upper() for w in tail)
                    if tail_initials == term.upper():
                        return " ".join(tail)

    return None

def get_answer_variant_chunks():
    global ANSWER_VARIANT_CHUNKS
    if ANSWER_VARIANT_CHUNKS is None:
        from app.retrieve import get_chunks_for_bm25
        _, ANSWER_VARIANT_CHUNKS = get_chunks_for_bm25()
    return ANSWER_VARIANT_CHUNKS

def choose_best_definition_items(
    question: str,
    items: List[Dict[str, Any]],
    grounded_expansion: str | None = None,
    limit: int = 2,
) -> List[Dict[str, Any]]:
    if not items:
        return []

    phrases = []
    if grounded_expansion:
        phrases.append(" ".join(grounded_expansion.lower().split()))
    else:
        from app.retrieve import build_query_variants
        variants = build_query_variants(question, get_answer_variant_chunks())
        for v in variants:
            vq = v.strip()
            vl = vq.lower()
            for prefix in ["what is ", "what are ", "define "]:
                if vl.startswith(prefix):
                    vq = vq[len(prefix):].strip(" ?")
                    break

            v_norm = " ".join(vq.lower().split())
            if " " in v_norm:
                phrases.append(v_norm)

    core = extract_answer_core_term(question)

    core_norm = " ".join(core.lower().split())
    if " " in core_norm:
        phrases.append(core_norm)

    def parse_chunk_index(chunk_id: str) -> int | None:
        m = re.search(r":c(\d+)$", chunk_id)
        if not m:
            return None
        return int(m.group(1))

    def score_item(item: Dict[str, Any]) -> tuple:
        text = item.get("text", "") or ""
        text_norm = " ".join(text.lower().split())
        meta = item.get("metadata", {})
        chunk_id = item.get("chunk_id", "")
        doc_name = (meta.get("doc_name") or "").lower()
        chunk_kind = (meta.get("chunk_kind") or "").lower()
        doc_type = (meta.get("doc_type") or "").lower()

        phrase_hits = sum(1 for p in phrases if p and p in text_norm)
        text_len = len(text_norm)

        looks_toc = (
            "table of contents" in text_norm
            or "consolidated table of contents" in text_norm
            or "................................" in text
        )

        pipe_count = text.count("|")
        colon_count = text.count(":")
        definition_like = 1 if (pipe_count <= 8 and colon_count <= 6 and text_len < 1200) else 0

        term_hits = 0
        if core_norm:
            for term in core_norm.split():
                if len(term) >= 3:
                    pattern = rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])"
                    if re.search(pattern, text_norm, re.IGNORECASE):
                        term_hits += 1

        # Bonus for chunks that open with a direct definition of the term
        definition_opener = 0
        if core_norm and text_norm.startswith(core_norm):
            definition_opener = 5
        elif core_norm and re.search(rf"^[^.]*\b{re.escape(core_norm)}\b[^.]*(?:refers to|is the process|is a process|means|is defined)", text_norm):
            definition_opener = 4

        chunk_index = parse_chunk_index(chunk_id)
        proximity_bonus = 0
        if chunk_index is not None:
            proximity_bonus = -abs(chunk_index - 11)

        helpful_context_bonus = 0
        if (doc_type == "glossary" or chunk_kind in {"definition", "glossary"}) and term_hits > 0:
            helpful_context_bonus = 5
        elif doc_type in {"explanations", "faq", "guides", "reference"} and term_hits > 0:
            helpful_context_bonus = 3
        testplan_penalty = -5 if ("testplan" in doc_name or "testplans" in doc_name) else 0

        definition_score = (
            term_hits
            + helpful_context_bonus
            + testplan_penalty
            + definition_opener
        )

        return (
            definition_score,
            phrase_hits,
            3 if chunk_kind in {"definition", "glossary"} and (phrase_hits > 0 or term_hits > 0) else 0,
            float(item.get("score", 0.0)),
            definition_like,
            proximity_bonus,
            -int(looks_toc),
            -pipe_count,
            -text_len,
            doc_name,
        )

    ranked = sorted(items, key=score_item, reverse=True)

    if limit <= 2:
        return ranked[:limit]

    selected: List[Dict[str, Any]] = []
    selected_indexes: List[int] = []

    # take the best two first
    for item in ranked:
        selected.append(item)
        idx = parse_chunk_index(item.get("chunk_id", ""))
        if idx is not None:
            selected_indexes.append(idx)
        if len(selected) >= 2:
            break

    # for the rest, prefer chunks outside the immediate local cluster
    for item in ranked:
        if item["chunk_id"] in {x["chunk_id"] for x in selected}:
            continue

        idx = parse_chunk_index(item.get("chunk_id", ""))
        if idx is None:
            continue

        if all(abs(idx - sidx) >= 2 for sidx in selected_indexes):
            selected.append(item)
            selected_indexes.append(idx)
            if len(selected) >= limit:
                return selected[:limit]

    # fallback: fill remaining slots normally
    for item in ranked:
        if item["chunk_id"] in {x["chunk_id"] for x in selected}:
            continue
        selected.append(item)
        if len(selected) >= limit:
            break

    return selected[:limit]

def extract_glossary_definition_lines(question, items, max_lines=2):
    term = extract_answer_core_term(question)
    term_norm = " ".join(term.lower().split())

    hits = []
    seen = set()

    for item in items:
        text = item.get("text", "") or ""

        for line in text.splitlines():
            cleaned = " ".join(line.split()).strip()
            if not cleaned:
                continue

            line_norm = cleaned.lower()

            # Markdown table row: | Term | Definition |
            if "|" in cleaned:
                cells = [c.strip() for c in cleaned.split("|") if c.strip()]
                if len(cells) >= 2:
                    first_cell = " ".join(cells[0].lower().split())
                    if first_cell == term_norm:
                        candidate = f"{term}: {' '.join(cells[1:])}"
                    else:
                        continue
                else:
                    continue

            # Colon/dash glossary style
            elif re.match(rf"^{re.escape(term)}\s*[:\-–—]\s+\S+", cleaned, re.IGNORECASE):
                candidate = cleaned

            # Plain glossary style: Term followed by definition
            elif line_norm.startswith(term_norm + " "):
                rest = cleaned[len(term):].strip()
                if len(rest.split()) < 3:
                    continue
                candidate = f"{term}: {rest}"

            else:
                continue

            # Generic quality filters only
            if len(candidate.split()) < 4:
                continue
            if len(candidate) > 500:
                continue
            if candidate.lower() in seen:
                continue

            seen.add(candidate.lower())
            hits.append(candidate)

            if len(hits) >= max_lines:
                return hits

    return hits

def extract_definition_sentences(question: str, items: List[Dict[str, Any]], max_sentences: int = 4) -> List[str]:
    
    term = extract_answer_core_term(question)

    term_norm = " ".join(term.lower().split())
    if not term_norm:
        return []

    candidates = []
    seen = set()

    for item in items:
        text = (item.get("text") or "").strip()
        if not text:
            continue

        parts = re.split(r'(?<=[\.\!\?])\s+|\n+', text)
        for part in parts:
            cleaned = " ".join(part.split()).strip()
            if not cleaned:
                continue
            if len(cleaned) < 50:
                continue

            if cleaned.endswith((" in th", " in t", " of th", " of t")):
                continue

            if cleaned.count(" ") < 6:
                continue

            if not re.search(r"[a-zA-Z]", cleaned):
                continue

            if cleaned[-1].isalnum() and not re.search(r"[.!?]$", cleaned):
                continue

            norm = cleaned.lower()
            if term_norm not in norm:
                continue
            if cleaned in seen:
                continue

            # reject obvious mid-sentence fragments
            if not cleaned[:1].isupper():
                continue
            if re.match(r"^[a-z]", cleaned):
                continue
            if cleaned.startswith(("ciated", "ociated", "tted", "nd", "ing ")):
                continue

            # prefer clean starts for definition text
            starts_clean = (
                norm.startswith(term_norm)
                or norm.startswith(f"a {term_norm}")
                or norm.startswith(f"an {term_norm}")
                or norm.startswith(f"the {term_norm}")
                or re.search(rf"\b{re.escape(term_norm)}\b\s+(is|refers to|can|may)\b", norm)
            )

            if not starts_clean and len(candidates) == 0:
                # allow contextual mentions only if we found nothing cleaner yet
                pass
            elif not starts_clean:
                continue

            seen.add(cleaned)

            bad_markers = [
                "###", "<span", "</span>", "shall follow the format",
                "x.509", "ecc p-256", "sha-256", "es256", "issuer_cert"
            ]
            if any(marker in norm for marker in bad_markers):
                continue

            score = 0

            if norm.startswith(term_norm):
                score += 20
            if norm.startswith(f"a {term_norm}") or norm.startswith(f"an {term_norm}") or norm.startswith(f"the {term_norm}"):
                score += 18
            if re.search(rf"\b{re.escape(term_norm)}\s+is\b", norm):
                score += 15
            if re.search(rf"\b{re.escape(term_norm)}\s+refers to\b", norm):
                score += 14
            if re.search(rf"\b{re.escape(term_norm)}\s+can\b", norm):
                score += 8

            # penalize contextual mentions that are not actually defining the term
            if "signed by a credential issuer" in norm:
                score -= 3
            if norm.startswith("this access document"):
                score -= 8
            if "access rights" in norm:
                score += 1
            if "public key" in norm:
                score += 1

            if "shall" in norm:
                score -= 3
            if len(cleaned) > 280:
                score -= 2
            if len(cleaned) < 40:
                score -= 1

            candidates.append((score, cleaned))

    candidates.sort(key=lambda x: x[0], reverse=True)
    return [text for _, text in candidates[:max_sentences]]

def definition_mode_instruction(detail_mode: str) -> str:
    if detail_mode == "wide":
        return (
            "Definition answer style:\n"
            "- Start with one clear definition sentence.\n"
            "- Then broaden the explanation using the wider retrieved evidence.\n"
            "- Explain how the term relates to other important concepts mentioned in the evidence.\n"
            "- It is acceptable to introduce additional related concepts if they help explain the term and are grounded in the retrieved excerpts.\n"
            "- Make the answer broader and more contextual than deep mode.\n"
            "- Do not invent unsupported background or examples.\n"
        )
    if detail_mode == "deep":
        return (
            "Definition answer style:\n"
            "- Start with one clear definition sentence.\n"
            "- Then explain the term more fully in simpler language.\n"
            "- Stay centered on the same concept using the currently retrieved evidence.\n"
            "- Make the concept easier to understand for a non-expert.\n"
            "- After the definition, add a short plain-language explanation of what it practically means.\n"
            "- You may include one simple analogy or one small illustrative example, but only as an explanatory aid and not as a factual claim about the spec.\n"
            "- Clearly keep the analogy/example separate from the grounded factual explanation.\n"
            "- Do not broaden into unrelated surrounding architecture.\n"
            "- Make the answer noticeably fuller and more understandable than normal mode.\n"
        )
    return (
        "Definition answer style:\n"
        "- Give one clear definition.\n"
        "- For acronym terms, include the exact expansion if the evidence provides it.\n"
        "- Add one short explanatory sentence about what the term is used for, if the evidence supports it.\n"
        "- Keep it concise.\n"
        "- Do not add unsupported background.\n"
    )

def build_definition_answer(
    question: str,
    items: List[Dict[str, Any]],
    detail_mode: str,
) -> str:
    if detail_mode == "wide":
        sentence_limit = 6
    elif detail_mode == "deep":
        sentence_limit = 4
    else:
        sentence_limit = 2

    sentences = extract_definition_sentences(
        question,
        items,
        max_sentences=sentence_limit,
    )

    if not sentences:
        return ""

    if detail_mode == "normal":
        body = " ".join(sentences[:1])
    elif detail_mode == "deep":
        body = " ".join(sentences[:3])
    else:
        body = " ".join(sentences[:5])

    return separate_citations(body, items)

def is_email_source(item: Dict[str, Any]) -> bool:
    return (item["metadata"].get("source_type") or "").lower() in {
        "email_case",
        "email_thread_analysis",
        "email",
    }

def is_official_source(item: Dict[str, Any]) -> bool:
    meta = item["metadata"]
    doc_type = (meta.get("doc_type") or "").lower()
    return (
        doc_type in {"policies", "specs", "reference"}
        and not is_email_source(item)
    )

def filter_email_sources(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [item for item in items if is_email_source(item)]

def preserve_relevant_email_case(
    question: str,
    selected: List[Dict[str, Any]],
    items: List[Dict[str, Any]],
    limit: int,
) -> List[Dict[str, Any]]:

    email_count = sum(
        1
        for item in selected
        if is_email_source(item)
    )

    if email_count >= 2:
        return selected
    
    official_or_reference_count = sum(
        1
        for item in selected
        if is_official_source(item)
    )

    has_only_official_sources = official_or_reference_count == len(selected)

    has_retrieved_email_candidate = any(
        (item["metadata"].get("source_type") or "").lower()
        in {"email_case", "email_thread_analysis", "email"}
        for item in items
    )
    
    has_official_source = any(
        is_official_source(item)
        for item in selected
    )

    if has_official_source:
        selected_text = "\n".join(item.get("text") or "" for item in selected)

        official_supports = supports_query_semantically(
            question,
            {"text": selected_text, "metadata": {}},
        )

        has_email_candidate = any(
            (item["metadata"].get("source_type") or "").lower()
            in {"email_case", "email_thread_analysis", "email"}
            for item in items
        )

        if official_supports and not has_email_candidate:
            return selected

    for item in items:
        source_type = (item["metadata"].get("source_type") or "").lower()

        if not is_email_source(item):
            continue

        if item["chunk_id"] in {x["chunk_id"] for x in selected}:
            continue

        if not supports_query_semantically(question, item):
            continue

        # Prefer replacing weak front-page/abstract sources instead of appending.
        # Appending can push the email evidence beyond the context budget.
        replaced = False

        for idx in range(len(selected) - 1, -1, -1):
            chunk_kind = (selected[idx]["metadata"].get("chunk_kind") or "").lower()
            existing_source_type = (selected[idx]["metadata"].get("source_type") or "").lower()

            existing_doc_type = (selected[idx]["metadata"].get("doc_type") or "").lower()

            if (
                chunk_kind == "front_page"
                and not is_email_source(selected[idx])
                and existing_doc_type not in {"reference", "specs"}
            ):
                selected[idx] = item
                replaced = True
                break

        if replaced:
            email_count += 1
            if email_count >= 2:
                return selected
            continue

        return selected

    return selected

def supports_query_semantically(question: str, item: Dict[str, Any]) -> bool:
    text = (item.get("text") or "").lower()
    q = question.lower()

    stop_terms = {
        "what", "which", "when", "where", "who", "why", "how",
        "is", "are", "do", "does", "did", "can", "could", "should",
        "would", "if", "the", "a", "an", "for", "to", "of", "in",
        "on", "with", "and", "or", "already",
    }

    latin_terms = [
        t for t in re.findall(r"[a-z0-9/\-]+", q)
        if len(t) >= 3 and t not in stop_terms
    ]

    # CJK has no spaces: use character bigrams from each CJK run.
    cjk_terms = []
    for run in re.findall(r"[\u3040-\u30ff\u4e00-\u9fff]{2,}", q):
        cjk_terms.extend(run[i:i + 2] for i in range(len(run) - 1))

    terms = set(latin_terms) | set(cjk_terms)
    if not terms:
        return False

    hits = 0
    for term in terms:
        if re.search(r"[\u3040-\u30ff\u4e00-\u9fff]", term):
            if term in text:
                hits += 1
        elif re.search(rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])", text, re.IGNORECASE):
            hits += 1

    # A single strong match is enough when the query is short
    # (e.g. one acronym plus a program name).
    required = 2 if len(terms) > 2 else 1
    return hits >= required

def contains_any_query_acronym(question: str, item: Dict[str, Any]) -> bool:
    text = (item.get("text") or "").lower()
    acronyms = re.findall(r"\b[A-Z][A-Z0-9]{1,9}\b", question)

    return any(acronym.lower() in text for acronym in acronyms)

def is_advisory_decision_question(question: str) -> bool:
    q = question.lower()
    return any(
        phrase in q
        for phrase in [
            "customer asks",
            "do they still need",
            "do we need",
            "do i need",
            "is it required",
            "必要ですか",
            "必要か",
            "必要でしょうか",
        ]
    )

def supports_advisory_query_strictly(question: str, item: Dict[str, Any]) -> bool:
    text = (item.get("text") or "").lower()
    q = question.lower()

    decision_terms = [
        "qualification",
        "declaration",
        "listing",
        "member",
        "account",
        "end product",
        "final product",
        "qualified product",
        "qdidd",
        "qdid",
    ]

    question_has_decision_intent = any(
        term in q
        for term in [
            "customer asks",
            "do they still need",
            "do we need",
            "new qualification",
            "need a new qualification",
        ]
    )

    if not question_has_decision_intent:
        return supports_query_semantically(question, item)

    return any(term in text for term in decision_terms)

def select_exact_label_items(items: List[Dict[str, Any]], limit: int = 5) -> List[Dict[str, Any]]:
    selected: List[Dict[str, Any]] = []
    selected_ids = set()

    def add_first_matching(predicate) -> None:
        for item in items:
            if item["chunk_id"] in selected_ids:
                continue
            if predicate(item):
                selected.append(item)
                selected_ids.add(item["chunk_id"])
                return

    # 1. Primary exact policy/spec/reference heading/source
    for item in items:
        if len(selected) >= 3:
            break
        if item["chunk_id"] in selected_ids:
            continue

        exact_score = float(item.get("exact_phrase_score") or 0.0)
        doc_type = (item["metadata"].get("doc_type") or "").lower()

        if exact_score > 0.0 and doc_type in {"policies", "specs", "explanations", "guides"}:
            selected.append(item)
            selected_ids.add(item["chunk_id"])

    # 2. Second official source from a different document if available.
    # Avoid letting a child subsection from the same document redefine the parent heading.
    primary_doc_name = ""
    if selected:
        primary_doc_name = selected[0]["metadata"].get("doc_name") or ""

    add_first_matching(
        lambda item: is_official_source(item)
        and (item["metadata"].get("doc_name") or "") != primary_doc_name
    )

    # 3. FAQ/reference clarification
    add_first_matching(
        lambda item: (
            (item["metadata"].get("doc_type") or "").lower() == "reference"
            or "faq" in (item["metadata"].get("doc_name") or "").lower()
        )
    )

    # 5. Fill remaining by rank, but do not add email cases for exact-label answers.
    for item in items:
        if len(selected) >= limit:
            break
        if item["chunk_id"] in selected_ids:
            continue

        source_type = (item["metadata"].get("source_type") or "").lower()
        if is_email_source(item):
            continue

        # Skip test plan chunks for definition questions
        doc_name = (item["metadata"].get("doc_name") or "").lower()
        if "testplan" in doc_name or "test plan" in doc_name or "testplans" in doc_name:
            continue

        selected.append(item)
        selected_ids.add(item["chunk_id"])

    return selected[:limit]

def source_authority_rank(item: Dict[str, Any]) -> int:
    meta = item.get("metadata", {})
    doc_type = (meta.get("doc_type") or "").lower()
    doc_name = (meta.get("doc_name") or "").lower()
    source_type = (meta.get("source_type") or "").lower()

    if doc_type == "faq" and "official faq" in doc_name:
        return 0

    if doc_type == "policies":
        chunk_kind = (meta.get("chunk_kind") or "").lower()
        text = (item.get("text") or "").lower()

        if chunk_kind == "front_page":
            return 2

        if "abstract" in text and "qualification program reference document" in text:
            return 2

        return 1
    
    if doc_type == "glossary":
        return 1

    if doc_type == "reference" and "official faq" in doc_name:
        return 1

    if doc_type in {"faq", "guides", "explanations", "reference"}:
        return 2

    if is_email_source(item):
        return 3

    if doc_type == "specs":
        return 4

    return 5

def is_weak_navigation_chunk(item: Dict[str, Any]) -> bool:
    text = (item.get("text") or "").strip()
    if not text:
        return False

    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return False

    word_count = len(text.split())
    heading_count = sum(1 for line in lines if line.startswith("#"))
    short_line_count = sum(1 for line in lines if len(line.split()) <= 8)

    # Generic navigation/index/link-list chunk:
    # mostly short lines, usually with a heading, and little explanatory prose.
    return (
        word_count <= 140
        and heading_count >= 1
        and short_line_count >= 4
    )

def item_supports_answer(question: str, item: Dict[str, Any]) -> bool:
    if is_weak_navigation_chunk(item):
        return False

    return supports_query_semantically(question, item)

def apply_source_hierarchy(
    question: str,
    selected: List[Dict[str, Any]],
    items: List[Dict[str, Any]],
    limit: int,
) -> List[Dict[str, Any]]:
    candidates = [
        item for item in items
        if item_supports_answer(question, item)
        and not (
            "abstract" in (item.get("text") or "").lower()
            and len((item.get("text") or "").split()) < 180
        )
    ] 

    if not candidates:
        # Fallback for non-English / weak lexical matching:
        # keep retrieval order, but do not return weak generic Official FAQ/link pages.
        fallback = []
        seen = set()

        for item in items:
            if item["chunk_id"] in seen:
                continue

            if not item_supports_answer(question, item):
                meta = item.get("metadata", {})
                doc_name = (meta.get("doc_name") or "").lower()
                text = (item.get("text") or "").lower()

                is_weak_official_faq = (
                    "official faq" in doc_name
                    and (
                        "links to helpful information" in text
                        or "helpful information" in text
                    )
                )

                if is_weak_official_faq:
                    continue

            fallback.append(item)
            seen.add(item["chunk_id"])

            if len(fallback) >= limit:
                break

        return fallback[:limit] if fallback else selected[:limit]

    # Authority is a bounded preference, not an override.
    # A tier-0 source scoring 4 must not outrank a tier-3 source scoring 50.
    AUTHORITY_WEIGHT = 6.0

    candidates = sorted(
        candidates,
        key=lambda item: -(
            float(item.get("score", 0.0))
            - AUTHORITY_WEIGHT * source_authority_rank(item)
        ),
    )

    output = []
    seen = set()

    for item in candidates:
        if item["chunk_id"] in seen:
            continue

        output.append(item)
        seen.add(item["chunk_id"])

        if len(output) >= limit:
            break

    body_docs = {
        item["metadata"].get("doc_name")
        for item in output
        if (item["metadata"].get("chunk_kind") or "").lower() == "body"
    }

    output = [
        item for item in output
        if not (
            (item["metadata"].get("chunk_kind") or "").lower() == "front_page"
            and item["metadata"].get("doc_name") in body_docs
        )
    ]

    seen = {item["chunk_id"] for item in output}
    # For advisory questions, keep the official source as anchor,
    # then add practical support from top retrieved case/reference sources.
    if is_advisory_query(question) and len(output) < limit:
        for item in items:
            if len(output) >= limit:
                break

            if item["chunk_id"] in seen:
                continue

            meta = item.get("metadata", {})
            doc_name = (meta.get("doc_name") or "").lower()
            source_type = (meta.get("source_type") or "").lower()
            doc_type = (meta.get("doc_type") or "").lower()

            if "official faq" in doc_name and item["chunk_id"] not in seen:
                continue

            text = (item.get("text") or "").lower()

            if is_advisory_query(question):
                wants_module = "モジュール" in question or "module" in question.lower()

                if wants_module and "module" not in text:
                    continue

            if is_email_source(item) or doc_type == "reference":
                output.append(item)
                seen.add(item["chunk_id"])

    return output[:limit]

def short_field(value: Any, limit: int = 280) -> str:
    text = str(value or "").strip()
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "..."

def format_email_case_card(item: Dict[str, Any]) -> str:
    import json

    meta = item["metadata"]
    citation = format_citation(meta)
    text = item.get("text") or ""

    try:
        data = json.loads(text)
        cases = data.get("cases") or []

        if cases:
            case = cases[0]
            parts = [
                f"citation: {citation}",
                f"case_id: {case.get('case_id', item['chunk_id'])}",
                f"customer_question: {short_field(case.get('customer_question'), 240)}",
                f"decision_logic: {short_field(case.get('decision_logic'), 280)}",
                f"final_recommendation: {short_field(case.get('final_recommendation'), 280)}",
                f"risk_if_done_wrong: {short_field(case.get('risk_if_done_wrong'), 220)}",
            ]
            return "\n".join(part for part in parts if not part.endswith(": "))

        analysis = data.get("case_analysis") or {}
        if analysis:
            parts = [
                f"citation: {citation}",
                f"case_id: {item['chunk_id']}",
                f"key_decision_logic: {short_field(analysis.get('key_decision_logic'), 320)}",
                f"consulting_takeaway: {short_field(analysis.get('consulting_takeaway'), 280)}",
                f"risk_if_done_wrong: {short_field(analysis.get('risk_if_done_wrong'), 220)}",
            ]
            return "\n".join(part for part in parts if not part.endswith(": "))

    except Exception:
        pass

    return (
        f"citation: {citation}\n"
        f"case_id: {item['chunk_id']}\n"
        f"text: {text[:1200]}"
    )

def filter_items_to_cited(answer: str, selected: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    cited_items = [
        item for item in selected
        if re.search(rf"\[{re.escape(item['chunk_id'])}(\s|\||\])", answer)
    ]

    return cited_items if cited_items else selected

def answer_question(
    question: str,
    top_k: int = TOP_K_TO_MODEL,
    debug: bool = False,
    detail_mode: str = "normal",
    preloaded_items: List[Dict[str, Any]] | None = None,
    program: str | None = None,
    chat_history: List[Dict[str, str]] | None = None,
) -> Dict[str, Any]:
    mode, clean_question = parse_mode_and_question(question)
    print(f"DEBUG answer_question called: question={question!r} program={program!r} mode={detail_mode!r}")
    prompt_question = clean_question
    retrieval_question = clean_question
    hint_program, hint_clean_question = extract_explicit_program_hint(clean_question)

    if program is None and hint_program:
        program = hint_program
        clean_question = hint_clean_question
        prompt_question = clean_question
        retrieval_question = clean_question

    if program is None:
        inferred = infer_program_from_question(clean_question)
        if inferred:
            program = inferred
            if debug:
                print(f"DEBUG inferred program from question: {program}")

    if program:
        retrieval_question = expand_retrieval_query_with_keywords(
            retrieval_question,
            program,
        )
    
    if debug and retrieval_question != clean_question:
        print("\nExpanded retrieval query:")
        print(retrieval_question)

    if chat_history and looks_like_followup_question(clean_question):
        previous_user_messages = [
            message.get("content", "").strip()
            for message in chat_history
            if message.get("role") == "user" and message.get("content", "").strip()
        ]

        if previous_user_messages:
            if previous_user_messages[-1] == clean_question and len(previous_user_messages) >= 2:
                previous_user_question = previous_user_messages[-2]
            else:
                previous_user_question = previous_user_messages[-1]
            previous_subject = extract_answer_core_term(previous_user_question)

            resolved_question = clean_question

            if previous_subject:
                resolved_question = re.sub(
                    r"\bit\b",
                    previous_subject,
                    resolved_question,
                    flags=re.IGNORECASE,
                )
                resolved_question = re.sub(
                    r"\bthat\b",
                    previous_subject,
                    resolved_question,
                    flags=re.IGNORECASE,
                )
                resolved_question = re.sub(
                    r"\bthis\b",
                    previous_subject,
                    resolved_question,
                    flags=re.IGNORECASE,
                )

            prompt_question = resolved_question

            retrieval_question = (
                previous_user_question
                + "\n\nFollow-up question:\n"
                + resolved_question
            )

    if not clean_question:
        return {
            "answer": "No question provided.",
            "items": [],
            "weak_retrieval": False,
            "mode": mode,
        }

    if mode == "general":
        print("\n🤖 General mode...")
        answer = ask_llm_general(clean_question)
        print("✅ Done.\n")
        return {
            "answer": answer,
            "items": [],
            "weak_retrieval": False,
            "mode": mode,
        }
    
    if mode == "email":
        print("\n📧 Email/case-only mode...")
        print("\n🔍 Retrieving relevant email/case evidence...")

        retrieve_k = 100

        email_queries = [
            retrieval_question,
            clean_question,
        ]

        # Add a broader version by removing the "past cases" framing.
        broad_question = re.sub(
            r"\b(in )?past (bluetooth )?cases\b[:,]?\s*",
            "",
            clean_question,
            flags=re.IGNORECASE,
        ).strip()

        if broad_question and broad_question not in email_queries:
            email_queries.append(broad_question)

        # Add existing query variants if available.
        try:
            from app.retrieve import build_query_variants, get_chunks_for_bm25
            _, chunks_for_variants = get_chunks_for_bm25()
            for variant in build_query_variants(clean_question, chunks_for_variants):
                if variant not in email_queries:
                    email_queries.append(variant)
        except Exception:
            pass

        merged_items = []
        seen_ids = set()

        for q in email_queries:
            for item in retrieve_email_cases(q, top_k=retrieve_k, program=program):
                if item["chunk_id"] in seen_ids:
                    continue
                seen_ids.add(item["chunk_id"])
                merged_items.append(item)

        items = merged_items
        email_items = filter_email_sources(items)

        if not email_items:
            return {
                "answer": "No relevant email or case evidence found.",
                "items": [],
                "weak_retrieval": True,
                "mode": mode,
            }

        email_case_k = EMAIL_CASES_TO_MODEL
        selected = email_items[:email_case_k]

        if debug:
            print("\nSelected sources for model:")
            for item in selected:
                meta = item["metadata"]
                print(
                    f"- score={item['score']:.4f}  "
                    f"{format_citation(meta)}  "
                    f"id={item['chunk_id']}  "
                    f"priority={meta.get('priority', 0)}  "
                    f"kind={meta.get('chunk_kind')}"
                )

        print("🧠 Building email-grounded prompt...")
        print("🤖 Generating answer with local model...")

        case_count = len(selected)
        case_source_list = "\n".join(
            f"{idx}. {format_citation(item['metadata'])} | {item['chunk_id']}"
            for idx, item in enumerate(selected, start=1)
        )

        if resolve_language(question) == "ja":
            email_prefix = (
                "email/case参照モードです。\n"
                "過去のemail/case事例に基づき、公式ポリシーではなく実務上の参考情報として日本語で答えてください。\n"
                f"{case_count}件のcandidate case sourceが提供されています。\n"
                "ユーザーの質問に明確に関連するcaseだけを使ってください。\n"
                "ユーザーがyes/noまたは要否を聞いている場合は、最初にcase evidenceに基づく結論を1文で答えてください。"
                "条件付きの傾向がある場合は、通常何が必要で、何が軽減され、何が製品固有の条件に依存するのかを明確に述べてください。\n"
                "テストと、認証・資格取得・リスティング・宣言・登録・承認を混同しないでください。"
                "テストは作業または証拠であり、認証・資格取得・リスティング・宣言・登録・承認はコンプライアンス上の状態または手続きです。\n"
                "その後、関連するcaseを'参考事例:'として簡潔な番号付き箇条書きで示してください。\n"
                "各箇条書きは、case topic + 実務上の教訓 + source orderに表示された完全なcitationで構成してください。bluetooth:email:... のidを含める必要があります。\n"
                "質問に直接関係する場合は、許可された事例と許可されなかった事例の両方を含めてください。\n"
                "関連が弱いcaseの教訓を作らない、同じcaseを繰り返さない、ファイル名だけでcitationしない、長い前置きや結論を追加しないでください。\n"
                "次のsource orderを使ってください:\n"
                f"{case_source_list}\n\n"
            )
            
        else:
            email_prefix = (
                "You are in email/case-reference mode.\n"
                "Answer in English using past email/case examples as practical reference only, not official policy.\n"
                f"You have been given {case_count} candidate case sources.\n"
                "Use only cases that clearly relate to the user's question.\n"
                "If the user asks a yes/no or requirement question, start with a direct one-sentence conclusion based on the case evidence. Do not open with 'it depends' or 'whether' — commit to what the cases show as the general pattern first, then explain conditions or exceptions after.\n"
                "State what the cases show generally remained required, what could be reduced, and what depended on specific facts — but always lead with the requirement status first.\n"
                "Do not conflate testing with qualification, certification, listing, declaration, registration, or approval.\n"
                "Testing is an activity or evidence; qualification/certification/listing/declaration/registration/approval is the compliance status or process.\n"
                "Use this output structure exactly:\n"
                "<One to two sentences synthesized pattern from the cases.>\n"
                "\n"
                "Case reference:\n"
                "1. <case topic>: <practical lesson>. <full citation>\n"
                "2. <case topic>: <practical lesson>. <full citation>\n"
                "Each bullet must state: case topic + practical lesson + full source citation exactly as shown in the source order, including the bluetooth:email:... id.\n"
                "Include both positive and negative examples when they directly address the question.\n"
                "Do not invent lessons for weak cases, repeat the same case, cite only filenames, or add a long introduction/conclusion.\n"
                "Use this exact source order:\n"
                f"{case_source_list}\n\n"
            )

        email_prompt_question = email_prefix + clean_question

        case_card_items = []

        for item in selected:
            card_item = dict(item)
            card_item["text"] = format_email_case_card(item)
            case_card_items.append(card_item)

        answer = separate_citations(
            ask_llm(
                email_prompt_question,
                case_card_items,
                weak_retrieval=False,
                detail_mode=detail_mode,
                language_override=resolve_language(question),
            ),
            selected,
        )

        cited_ids = {
            item["chunk_id"]
            for item in selected
            if re.search(rf"\[{re.escape(item['chunk_id'])}(\s|\||\])", answer)
        }

        cited_items = [
            item for item in selected
            if item["chunk_id"] in cited_ids
        ]

        print("✅ Done.\n")

        return {
            "answer": answer,
            "items": cited_items,
            "weak_retrieval": False,
            "mode": mode,
        }    

    if (
        mode == "auto"
        and program is None
        and preloaded_items is None
        and not (chat_history and looks_like_followup_question(clean_question))
    ):
        print("\n🤖 Auto mode chose general...")
        answer = ask_llm_general(clean_question)
        print("✅ Done.\n")
        return {
            "answer": answer,
            "items": [],
            "weak_retrieval": False,
            "mode": mode,
        }

    if preloaded_items is None:
        print("\n🔍 Retrieving relevant evidence...")
        
        if detail_mode == "wide":
            retrieve_k = 12
        elif detail_mode == "deep":
            retrieve_k = 8
        elif is_advisory_query(clean_question) or is_advisory_decision_question(clean_question):
            retrieve_k = max(top_k, 30)
        else:
            retrieve_k = max(top_k, 8)
        items = retrieve(retrieval_question, top_k=retrieve_k, program=program)
        print(f"DEBUG retrieval_question: {retrieval_question!r}")
        print(f"DEBUG top retrieved: {[(item['chunk_id'], item['score']) for item in items[:5]]}")

        if is_advisory_decision_question(clean_question):
            def advisory_decision_item_rank(item):
                meta = item.get("metadata", {})
                doc_type = (meta.get("doc_type") or "").lower()
                doc_name = (meta.get("doc_name") or "").lower()
                chunk_kind = (meta.get("chunk_kind") or "").lower()

                if is_email_source(item):
                    return 9

                if chunk_kind in {"front_page", "glossary"}:
                    return 8

                if is_weak_navigation_chunk(item):
                    return 8

                if doc_type == "faq" and "official faq" in doc_name:
                    return 0

                if doc_type in {"policies", "reference", "guides", "explanations", "faq"}:
                    return 1

                return 5

            items = sorted(
                items,
                key=lambda item: (
                    advisory_decision_item_rank(item),
                    -float(item.get("score", 0.0)),
                ),
            )

    else:
        items = preloaded_items

    asks_for_case_evidence = any(
        phrase in clean_question.lower()
        for phrase in [
            "case",
            "example",
            "past",
            "email",
            "in practice",
            "practical example",
        ]
    )

    if clean_question.lower().strip().startswith(("how ", "how do ", "how does ")):
        non_glossary_items = [
            item for item in items
            if "glossary" not in (item.get("metadata", {}).get("doc_name") or "").lower()
        ]
        if non_glossary_items:
            items = non_glossary_items

    exact_acronym_items = []
    
    grounded_expansion = None
    if is_definition_query(clean_question):
        grounded_expansion = extract_exact_acronym_expansion(clean_question, items)
        if grounded_expansion:
            expansion_norm = " ".join(grounded_expansion.lower().split())
            exact_acronym_items = [
                item for item in items
                if expansion_norm in " ".join((item.get("text") or "").lower().split())
            ]

    if retrieval_is_weak(items):
        if items:
            print("⚠️ Retrieval is weak, using fallback evidence anyway...")
            if exact_acronym_items:
                selected = exact_acronym_items[:2]
            else:
                selected = items[:WEAK_RETRIEVAL_FALLBACK_K]

            if is_definition_query(clean_question) and not is_practical_requirement_query(clean_question) and not comparison_query:
                selected = add_glossary_support_sources(
                    clean_question,
                    selected,
                    program=program,
                    max_added=1,
                )

            if debug:
                print("\nSelected sources for model:")
                for item in selected:
                    meta = item["metadata"]
                    print(
                        f"- score={item['score']:.4f}  "
                        f"{format_citation(meta)}  "
                        f"id={item['chunk_id']}  "
                        f"priority={meta.get('priority', 0)}  "
                        f"kind={meta.get('chunk_kind')}"
                    )
            
            case_requested = any(
                phrase in clean_question.lower()
                for phrase in [
                    "case",
                    "past",
                    "email",
                    "customer case",
                    "past case",
                    "in practice",
                ]
            )

            if not case_requested:
                non_email_candidates = [
                    item for item in items
                    if not is_email_source(item)
                    and (item["metadata"].get("doc_type") or "").lower()
                    in {"faq", "policies", "guides", "explanations"}
                    and (item["metadata"].get("chunk_kind") or "").lower() != "front_page"
                ]

                if non_email_candidates:
                    selected = non_email_candidates[:WEAK_RETRIEVAL_FALLBACK_K]
                else:
                    selected = [
                        item for item in selected
                        if not is_email_source(item)
                    ]

            print("🧠 Building grounded prompt...")
            print(f"DEBUG selected chunks: {[item['chunk_id'] for item in selected]}")
            print("🤖 Generating answer with local model...")

            answer = separate_citations(
                ask_llm(
                    clean_question,
                    selected,
                    weak_retrieval=True,
                    grounded_expansion=grounded_expansion,
                    detail_mode=detail_mode,
                ),
                selected,
            )

            print("✅ Done.\n")

            return {
                "answer": answer,
                "items": selected,
                "weak_retrieval": True,
                "mode": mode,
            }

        if mode == "auto":
            print("🤖 Auto mode fell back to general...")
            answer = ask_llm_general(clean_question)
            print("✅ Done.\n")
            return {
                "answer": answer,
                "items": items,
                "weak_retrieval": True,
                "mode": mode,
            }

        return {
            "answer": "Not enough information in the indexed documents.",
            "items": items,
            "weak_retrieval": True,
            "mode": mode,
        }

    comparison_query = any(
        phrase in clean_question.lower()
        for phrase in [
            "difference between",
            "compare",
            "comparison",
            "versus",
            " vs ",
            "different from",
        ]
    )

    intent = (
        "definition"
        if (
            is_definition_query(clean_question)
            and not comparison_query
            and not is_practical_requirement_query(clean_question)
        )
        else "other"
    )

    if intent == "definition":
        has_exact_phrase_hits = any(
            float(item.get("exact_phrase_score") or 0.0) > 0.0
            for item in items
        )

        if has_exact_phrase_hits:
            if detail_mode == "wide":
                definition_limit = 6
            elif detail_mode == "deep":
                definition_limit = 4
            else:
                definition_limit = 3

            selected = select_exact_label_items(items, limit=definition_limit)

        else:
            if detail_mode == "wide":
                definition_limit = 6
            elif detail_mode == "deep":
                definition_limit = 4
            else:
                definition_limit = 3

            if grounded_expansion:
                # Chunks containing the expansion, best-first: prefer real
                # definition/glossary chunks, then retrieval score.
                exact_acronym_items = sorted(
                    exact_acronym_items,
                    key=lambda item: (
                        0 if (item["metadata"].get("chunk_kind") or "").lower()
                             in {"definition", "glossary"} else 1,
                        -float(item.get("score", 0.0)),
                    ),
                )
                selected = exact_acronym_items[:max(1, min(2, definition_limit))]

            elif exact_acronym_items:
                exact_acronym_items = sorted(
                    exact_acronym_items,
                    key=lambda item: (
                        0 if (item["metadata"].get("chunk_kind") or "").lower()
                             in {"definition", "glossary"} else 1,
                        -float(item.get("score", 0.0)),
                    ),
                )
                selected = exact_acronym_items[:min(2, definition_limit)]

            else:
                selected = choose_best_definition_items(
                    clean_question,
                    items,
                    grounded_expansion,
                    limit=definition_limit,
                )

        # Keep the definition-specific ranking from choose_best_definition_items().
        # Raw retrieval score can over-promote narrow spec/test-plan chunks.

    else:
        if detail_mode == "wide":
            model_k = 6
        elif detail_mode == "deep":
            model_k = 5
        else:
            model_k = 6 if comparison_query else top_k

        selected = items[:model_k]

        if any(phrase in clean_question.lower() for phrase in ["what do we need to prepare", "what must be prepared", "what needs to be prepared", "what should we prepare", "何を入れる", "何を準備"]):
            policy_items = [
                item for item in items
                if (item["metadata"].get("doc_type") or "").lower() == "policies"
                and supports_query_semantically(clean_question, item)
            ]

            if policy_items:
                selected_ids = {item["chunk_id"] for item in selected}
                for item in policy_items:
                    if item["chunk_id"] not in selected_ids:
                        selected.insert(0, item)
                        selected_ids.add(item["chunk_id"])

                selected = selected[:model_k]

        top_item = items[0] if items else None

        if top_item:
            top_kind = (top_item["metadata"].get("chunk_kind") or "").lower()
            top_score = float(top_item.get("score", 0.0))

            if top_kind not in {"front_page", "glossary"} and top_score >= 10.0:
                if top_item["chunk_id"] not in {item["chunk_id"] for item in selected}:
                    selected.insert(0, top_item)
                    selected = selected[:model_k]

        if not comparison_query and any(
            (item["metadata"].get("doc_type") or "").lower() == "reference"
            for item in selected
        ):
            selected_ids = {item["chunk_id"] for item in selected}

            for item in items:
                if item["chunk_id"] in selected_ids:
                    continue

                doc_type = (item["metadata"].get("doc_type") or "").lower()
                if doc_type not in {"policies", "specs"}:
                    continue

                if supports_query_semantically(clean_question, item):
                    selected[-1] = item
                    break

        if comparison_query:
            acronyms = [
                a for a in re.findall(r"\b[A-Z][A-Z0-9]{1,9}\b", clean_question)
                if a.upper() not in {"SIG", "BLE", "BT"}
            ]

            selected_ids = set()
            comparison_selected = []

            for acronym in acronyms:
                acronym_lower = acronym.lower()

                acronym_candidates = [
                    item for item in items
                    if acronym_lower in (item.get("text") or "").lower()
                    and (
                        "glossary" in (item["metadata"].get("doc_name") or "").lower()
                        or (item["metadata"].get("chunk_kind") or "").lower() in {"definition", "glossary"}
                        or (item["metadata"].get("doc_type") or "").lower() in {"reference", "policies"}
                    )
                ]

                acronym_candidates = sorted(
                    acronym_candidates,
                    key=lambda item: (
                        0 if (item.get("text") or "").lower().lstrip("# ").startswith(acronym_lower) else
                        1 if "glossary" in (item["metadata"].get("doc_name") or "").lower() else
                        2 if (item["metadata"].get("chunk_kind") or "").lower() in {"definition", "glossary"} else
                        3 if (item["metadata"].get("doc_type") or "").lower() == "policies" else
                        4,
                        -float(item.get("score", 0.0)),
                    ),
                )

                for item in acronym_candidates:
                    if item["chunk_id"] not in selected_ids:
                        comparison_selected.append(item)
                        selected_ids.add(item["chunk_id"])
                        break

            for item in items:
                if len(comparison_selected) >= model_k:
                    break
                if item["chunk_id"] in selected_ids:
                    continue
                comparison_selected.append(item)
                selected_ids.add(item["chunk_id"])

            if comparison_selected:
                selected = comparison_selected[:model_k]                

        has_email_case = any(
            (item["metadata"].get("source_type") or "").lower() == "email_case"
            for item in selected
        )

        has_policy_or_spec = any(
            (item["metadata"].get("doc_type") or "").lower() in {"policies", "specs"}
            for item in selected
        )

        if has_email_case and not has_policy_or_spec:
            selected_ids = {x["chunk_id"] for x in selected}

            for item in items:
                if item["chunk_id"] in selected_ids:
                    continue
                if (
                    (item["metadata"].get("doc_type") or "").lower() in {"policies", "specs"}
                    and supports_query_semantically(clean_question, item)
                ):
                    if len(selected) >= model_k:
                        selected[-1] = item
                    else:
                        selected.append(item)
                    break
        
        if intent != "definition" and not comparison_query:
            selected = sorted(
                selected,
                key=lambda item: (
                    0 if (item["metadata"].get("doc_type") or "").lower() in {"policies", "specs"} else
                    1 if (item["metadata"].get("doc_type") or "").lower() == "reference" else
                    2,
                    -float(item.get("score", 0.0)),
                ),
            )

        has_practical_source = any(
            (item["metadata"].get("doc_type") or "").lower() == "reference"
            or (item["metadata"].get("source_type") or "").lower()
            in {"email_case", "email_thread_analysis", "email"}
            for item in selected
        )

        if has_practical_source and not comparison_query:
            selected = [
                item for item in selected
                if (
                    (item["metadata"].get("doc_type") or "").lower()
                    not in {"specs", "policies"}
                )
                or supports_advisory_query_strictly(clean_question, item)
            ]

        asks_for_practical_case = any(
            phrase in clean_question.lower()
                for phrase in [
                    "example",
                    "case",
                    "customer",
                    "practical",
                    "in practice",
                    "actual",
                    "email",
                ]
            )

        has_strong_official_or_reference = any(
            is_official_source(item)
            and float(item.get("score", 0.0)) >= 5.0
            for item in selected
        )

        has_retrieved_email_candidate = any(
            (item["metadata"].get("source_type") or "").lower()
            in {"email_case", "email_thread_analysis", "email"}
            for item in items
        )

        if (
            intent != "definition"
            and has_strong_official_or_reference
            and not asks_for_practical_case
            and not has_retrieved_email_candidate
        ):
            selected_ids = {item["chunk_id"] for item in selected}

            selected = [
                item for item in selected
                if (item["metadata"].get("source_type") or "").lower()
                not in {"email_case", "email_thread_analysis", "email"}
            ]

            for item in items:
                if len(selected) >= model_k:
                    break
                if item["chunk_id"] in selected_ids:
                    continue

                source_type = (item["metadata"].get("source_type") or "").lower()
                if source_type in {"email_case", "email_thread_analysis", "email"}:
                    continue

                if not supports_query_semantically(clean_question, item):
                    continue

                selected.append(item)

        has_body_source = any(
            (item["metadata"].get("chunk_kind") or "").lower() != "front_page"
            for item in selected
        )

        if has_body_source:
            selected = [
                item for item in selected
                if (
                    (item["metadata"].get("chunk_kind") or "").lower() != "front_page"
                    or "official faq" in (item["metadata"].get("doc_name") or "").lower()
                    or float(item.get("score", 0.0)) >= 10.0
                )
            ]

        if is_definition_query(clean_question) and not is_practical_requirement_query(clean_question) and not comparison_query:
            selected = add_glossary_support_sources(
                clean_question,
                selected,
                program=program,
                max_added=1,
            )

        if is_advisory_query(clean_question) or is_advisory_decision_question(clean_question):
            selected = apply_source_hierarchy(
                retrieval_question,
                selected,
                items,
                limit=max(model_k, top_k),
            )

        selected = preserve_relevant_email_case(
            clean_question,
            selected,
            items,
            limit=max(top_k, 5),
        )

    top_item = None if intent == "definition" or comparison_query else (items[0] if items else None)

    if top_item:
        top_kind = (top_item["metadata"].get("chunk_kind") or "").lower()
        top_score = float(top_item.get("score", 0.0))

        if (
            top_kind not in {"front_page", "glossary"}
            and top_score >= 10.0
            and not is_weak_navigation_chunk(top_item)
        ):
            selected_ids = {item["chunk_id"] for item in selected}
            if top_item["chunk_id"] not in selected_ids:
                selected.insert(0, top_item)
                selected = selected[:max(top_k, 5)]

    if debug:
        print("\nSelected sources for model:")
        print("DEBUG selected final before model:", [item["chunk_id"] for item in selected])
        for item in selected:
            meta = item["metadata"]
            print(
                f"- score={item['score']:.4f}  "
                f"{format_citation(meta)}  "
                f"id={item['chunk_id']}  "
                f"priority={meta.get('priority', 0)}  "
                f"kind={meta.get('chunk_kind')}"
            )

    if (
        intent == "definition"
        and exact_acronym_items
    ):
        term_matches = re.findall(r"(?<![A-Za-z0-9])[A-Z][A-Z0-9/\-]{1,9}(?![A-Za-z0-9])", clean_question)
        term_matches = [t for t in term_matches if t not in {"BLUETOOTH", "SIG"}]
        term = term_matches[-1] if term_matches else extract_answer_core_term(clean_question)


        definition_items = [
            item for item in items
            if (
                term
                and term.lower() in (item.get("text") or "").lower()
                and (
                    (item["metadata"].get("doc_name") or "").lower() == "glossary.md"
                    or (item["metadata"].get("chunk_kind") or "").lower()
                    in {"definition", "glossary"}
                    or "acronyms and abbreviations" in (item.get("text") or "").lower()
                )
            )
        ]

        if definition_items:
            def has_exact_acronym_table_row(item: Dict[str, Any]) -> bool:
                text = item.get("text") or ""
                return bool(
                    term
                    and re.search(
                        rf"^\s*\|\s*{re.escape(term)}\s*\|",
                        text,
                        flags=re.IGNORECASE | re.MULTILINE,
                    )
                )

            definition_items = sorted(
                definition_items,
                key=lambda item: (
                    0 if (item["metadata"].get("chunk_kind") or "").lower() in {"definition", "glossary"} else 1,
                    0 if has_exact_acronym_table_row(item) else 1,
                    1 if (item["metadata"].get("chunk_kind") or "").lower() == "front_page" else 0,
                    -float(item.get("score", 0.0)),
                ),
            )
            selected = definition_items[:3]
    
    if debug and is_definition_query(clean_question):
        print("\nSelected sources after definition fast path:")
        for item in selected:
            meta = item["metadata"]
            print(
                f"- score={item['score']:.4f}  "
                f"{format_citation(meta)}  "
                f"id={item['chunk_id']}  "
                f"priority={meta.get('priority', 0)}  "
                f"kind={meta.get('chunk_kind')}"
            )

    t1 = time.perf_counter()

    print("🧠 Building grounded prompt...")
    print(f"DEBUG selected chunks: {[item['chunk_id'] for item in selected]}")
    print("🤖 Generating answer with local model...")

    answer = separate_citations(
        ask_llm(
            prompt_question,
            selected,
            grounded_expansion=grounded_expansion,
            detail_mode=detail_mode,
        ),
        selected,
    )

    print(f"DEBUG timing: generate={time.perf_counter() - t1:.2f}s")
    print("✅ Done.\n")

    return {
        "answer": answer,
        "items": filter_items_to_cited(answer, selected),
        "weak_retrieval": False,
        "mode": mode,
    }

def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Production-grade local answer tool")
    parser.add_argument("--top-k", type=int, default=TOP_K_TO_MODEL, help="How many chunks to send to the model")
    parser.add_argument("--debug", action="store_true", help="Print retrieval diagnostics")
    parser.add_argument("--program", choices=["bluetooth", "matter", "aliro"], default=None)
    parser.add_argument("question", nargs="+", help="Question to answer")
    return parser.parse_args(argv)


def main() -> None:
    args = parse_args(sys.argv[1:])
    question = " ".join(args.question).strip()

    if not question:
        print("Usage: python -m app.answer <your question>")
        sys.exit(1)

    t0 = time.perf_counter()
    result = answer_question(
        question,
        top_k=args.top_k,
        debug=args.debug,
        program=args.program,
    )
    elapsed = time.perf_counter() - t0

    print(f"\n⏱ Total elapsed: {elapsed:.2f}s")

    print("=== ANSWER ===\n")
    print(result["answer"])

    if args.debug and result["items"]:
        print("\n=== SOURCES ===\n")
        seen = set()
        for item in result["items"]:
            meta = item["metadata"]
            key = (item["chunk_id"], meta.get("doc_name"), meta.get("page_start"), meta.get("page_end"))
            if key in seen:
                continue
            seen.add(key)
            print(
                f"- {format_citation(meta)}  "
                f"[{item['chunk_id']}]  "
                f"score={item.get('score', 0.0):.4f}  "
                f"priority={meta.get('priority', 0)}"
            )


if __name__ == "__main__":
    main()