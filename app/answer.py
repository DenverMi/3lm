import argparse
import sys
from typing import Dict, List, Any
import re
import time
import ollama

from app.config import RAG_LLM_MODEL, GENERAL_LLM_MODEL
from app.retrieve import retrieve, format_citation, is_definition_query

ANSWER_VARIANT_CHUNKS = None
# Retrieval / context limits
TOP_K_TO_MODEL = 3
MAX_CONTEXT_CHARS = 12000

# Weak retrieval guardrails
MIN_TOP_SCORE = 1.20
WEAK_RETRIEVAL_FALLBACK_K = 3

def parse_mode_and_question(raw_question: str) -> tuple[str, str]:
    text = raw_question.lstrip()

    if text.startswith("+ "):
        return "rag", text[2:].strip()
    if text.startswith("- "):
        return "general", text[2:].strip()

    return "auto", raw_question.strip()


def looks_like_rag_query(question: str) -> bool:
    q = question.lower()

    rag_keywords = [
    "bt",
    "bluetooth",
    "ble",
    "sig",
    "qualification",
    "qualify",
    "qualified",
    "qdid",
    "qdl",
    "epl",
    "pts",
    "ics",
    "ixit",
    "iopt",
    "tcrl",
    "tcw",
    "bqtf",
    "brtf",
    "rf phy",
    "rf",
    "le audio",
    "l2cap",
    "auracast",
    "br/edr",
    "hci",
    "gatt",
    "profile",
    "module",
    "aliro",
    "matter",
    "hdmi",
    "wifi",
    "access document",
    "user device",
    "credential issuer",
]

    return any(k in q for k in rag_keywords)


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
        model=RAG_LLM_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question},
        ],
    )

    return response["message"]["content"].strip()

def resolve_language(query: str) -> str:
    q = query.lower()

    if "in japanese" in q or "日本語" in q:
        return "ja"

    # simple detection
    if any(ord(c) > 128 for c in query):
        return "ja"

    return "en"

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
    return top < MIN_TOP_SCORE


def load_system_prompt(language: str) -> str:
    return f"""
You are an internal technical consultant.

Use only the provided INTERNAL EVIDENCE unless it is genuinely insufficient.

Rules:
- Treat INTERNAL EVIDENCE as the source of truth.
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
- If the evidence contains an acronym expansion in the form "Full Term (ACRONYM)" or "ACRONYM (Full Term)", use that exact expansion.
- Do not invent or substitute a different expansion.
- Prefer spec-based definitions when a spec definition is present.
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
- Do not print section headers unless "General knowledge (model-based)" is truly needed.
- If internal evidence is sufficient, output only one grounded paragraph with citations.
""".strip()

def build_model_input(
    question: str,
    items: List[Dict[str, Any]],
    language: str,
    grounded_expansion: str | None = None,
    detail_mode: str = "normal",
) -> str:
    parts: List[str] = []

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

    if is_definition_query(question):
        parts.append("\n" + definition_mode_instruction(detail_mode))

        if detail_mode == "wide":
            sentence_limit = 6
        elif detail_mode == "deep":
            sentence_limit = 4
        else:
            sentence_limit = 2

        definition_sentences = extract_definition_sentences(
            question,
            items,
            max_sentences=sentence_limit,
        )

        if definition_sentences:
            parts.append(
                "\nPrimary definition evidence:\n"
                + "\n".join(f"- {s}" for s in definition_sentences)
                + "\nUse these sentences as the primary grounding for the definition."
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
    for item in items:
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
        )

        text = (item.get("text") or "").strip()
        remaining = MAX_CONTEXT_CHARS - total_chars
        if remaining <= 0:
            break

        raw_terms = [w.lower() for w in re.findall(r"[A-Za-z0-9/\-]+", question) if len(w) >= 3]
        stop_terms = {
            "what", "which", "when", "where", "who", "why", "how",
            "test", "tool", "used", "use", "run", "does", "do", "you"
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
            "- Write clean prose only.\n"
            "- Do not write inline citations, placeholder citations, or '[citation needed]'.\n"
            "- Do not write 'chunk_id:' anywhere in the answer.\n"
            "- Do not append 'Not clearly specified in retrieved internal evidence.' unless some required part of the question truly cannot be answered from the excerpts.\n"
            "- Omit 'General knowledge (model-based)' if internal evidence is sufficient.\n"
        )

    return "\n".join(parts)


def ask_llm(
    question: str,
    items: List[Dict[str, Any]],
    weak_retrieval: bool = False,
    grounded_expansion: str | None = None,
    detail_mode: str = "normal",
) -> str:
    language = resolve_language(question)
    system_prompt = load_system_prompt(language)
    user_prompt = build_model_input(
        question,
        items,
        language,
        grounded_expansion=grounded_expansion,
        detail_mode=detail_mode,
    )
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
    )

    return response["message"]["content"].strip()

def separate_citations(answer: str, items: List[Dict[str, Any]]) -> str:
    citation_map = {}
    for item in items:
        meta = item["metadata"]
        full_citation = f"[{item['chunk_id']} | {format_citation(meta)}]"
        citation_map[item["chunk_id"]] = full_citation

    # normalize a few model-made citation variants into the full citation form
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
            answer = answer.replace(full_citation, "").strip()

    answer = re.sub(r"[ \t]+", " ", answer)
    answer = re.sub(r"\n{3,}", "\n\n", answer).strip()
    answer = re.sub(r"\n*Citations:\s*(?:-|\n-\s*)*", "", answer, flags=re.IGNORECASE).strip()
    answer = re.sub(r"(?m)^[\*\-\s]+$", "", answer).strip()

    if not found:
        found = list(citation_map.values())

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

    q = question.strip()
    lower = q.lower()
    prefixes = ["what is ", "what are ", "define "]
    core = q
    for prefix in prefixes:
        if lower.startswith(prefix):
            core = q[len(prefix):].strip(" ?")
            break

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

        chunk_index = parse_chunk_index(chunk_id)
        proximity_bonus = 0
        if chunk_index is not None:
            proximity_bonus = -abs(chunk_index - 11)

        return (
            phrase_hits,
            term_hits,
            1 if chunk_kind in {"definition", "glossary"} else 0,
            definition_like,
            proximity_bonus,
            -int(looks_toc),
            -pipe_count,
            -text_len,
            item.get("score", 0),
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

def extract_definition_sentences(question: str, items: List[Dict[str, Any]], max_sentences: int = 4) -> List[str]:
    q = question.strip()

    term = q
    m = re.search(r"\bwhat\s+is\s+(.+)$", q, re.IGNORECASE)
    if not m:
        m = re.search(r"\bwhat\s+are\s+(.+)$", q, re.IGNORECASE)
    if not m:
        m = re.search(r"\bdefine\s+(.+)$", q, re.IGNORECASE)
    if m:
        term = m.group(1).strip(" ?")

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
        "- Give one short, clear definition.\n"
        "- Keep it concise.\n"
        "- Do not expand unless necessary.\n"
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

def is_official_source(item: Dict[str, Any]) -> bool:
    meta = item["metadata"]
    doc_type = (meta.get("doc_type") or "").lower()
    source_type = (meta.get("source_type") or "").lower()
    return (
        doc_type in {"policies", "specs", "reference"}
        and source_type not in {"email_case", "email_thread_analysis", "email"}
    )

def supports_query_semantically(question: str, item: Dict[str, Any]) -> bool:
    text = (item.get("text") or "").lower()
    q = question.lower()

    raw_terms = re.findall(r"[a-z0-9/\-]+", q)
    stop_terms = {
        "what", "which", "when", "where", "who", "why", "how",
        "is", "are", "do", "does", "did", "can", "could", "should",
        "would", "if", "the", "a", "an", "for", "to", "of", "in",
        "on", "with", "and", "or", "already",
    }
    terms = [t for t in raw_terms if len(t) >= 3 and t not in stop_terms]

    if not terms:
        return False

    hits = 0
    for term in set(terms):
        pattern = rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])"
        if re.search(pattern, text, re.IGNORECASE):
            hits += 1

    return hits >= 2

def answer_question(
    question: str,
    top_k: int = TOP_K_TO_MODEL,
    debug: bool = False,
    detail_mode: str = "normal",
    preloaded_items: List[Dict[str, Any]] | None = None,
) -> Dict[str, Any]:
    mode, clean_question = parse_mode_and_question(question)

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

    if mode == "auto" and not looks_like_rag_query(clean_question):
        print("\n🤖 Auto mode chose general...")
        answer = ask_llm_general(clean_question)
        print("✅ Done.\n")
        return {
            "answer": answer,
            "items": [],
            "weak_retrieval": False,
            "mode": mode,
        }

    t0 = time.perf_counter()

    if preloaded_items is None:
        print("\n🔍 Retrieving relevant evidence...")
        if detail_mode == "wide":
            retrieve_k = 12
        elif detail_mode == "deep":
            retrieve_k = 8
        else:
            retrieve_k = max(top_k, 5)

        items = retrieve(clean_question, top_k=retrieve_k)
        print(f"DEBUG timing: retrieve={time.perf_counter() - t0:.2f}s")
    else:
        items = preloaded_items

    if debug:
        print("\nTop retrieved sources (debug):")
        for item in items:
            meta = item["metadata"]
            print(
                f"- score={item['score']:.4f}  "
                f"{format_citation(meta)}  "
                f"id={item['chunk_id']}  "
                f"priority={meta.get('priority', 0)}  "
                f"kind={meta.get('chunk_kind')}"
            )

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

            print("🧠 Building grounded prompt...")
            print("🤖 Generating answer with local model...")

            answer = ask_llm(
                clean_question,
                selected,
                weak_retrieval=True,
                grounded_expansion=grounded_expansion,
                detail_mode=detail_mode,
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

    intent = "definition" if is_definition_query(clean_question) else "other"

    if intent == "definition":
        if detail_mode == "wide":
            definition_limit = 6
        elif detail_mode == "deep":
            definition_limit = 4
        else:
            definition_limit = 2

        if grounded_expansion:
            selected = exact_acronym_items[:max(1, min(2, definition_limit))]
        elif exact_acronym_items:
            selected = exact_acronym_items[:min(2, definition_limit)]
        else:
            selected = choose_best_definition_items(
                clean_question,
                items,
                grounded_expansion,
                limit=definition_limit,
            )

    else:
        if detail_mode == "wide":
            model_k = 6
        elif detail_mode == "deep":
            model_k = 5
        else:
            model_k = top_k

        selected = items[:model_k]

        has_email_case = any(
            (item["metadata"].get("source_type") or "").lower() == "email_case"
            for item in selected
        )
        has_official = any(is_official_source(item) for item in selected)

        if has_email_case and not has_official:
            selected_ids = {x["chunk_id"] for x in selected}

            for item in items:
                if item["chunk_id"] in selected_ids:
                    continue
                if is_official_source(item) and supports_query_semantically(clean_question, item):
                    if len(selected) >= model_k:
                        selected[-1] = item
                    else:
                        selected.append(item)
                    break

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

    t1 = time.perf_counter()

    print("🧠 Building grounded prompt...")
    print("🤖 Generating answer with local model...")

    answer = separate_citations(
        ask_llm(
            clean_question,
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
        "items": selected,
        "weak_retrieval": False,
        "mode": mode,
    }

def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Production-grade local answer tool")
    parser.add_argument("--top-k", type=int, default=TOP_K_TO_MODEL, help="How many chunks to send to the model")
    parser.add_argument("--debug", action="store_true", help="Print retrieval diagnostics")
    parser.add_argument("question", nargs="+", help="Question to answer")
    return parser.parse_args(argv)


def main() -> None:
    args = parse_args(sys.argv[1:])
    question = " ".join(args.question).strip()

    if not question:
        print("Usage: python -m app.answer <your question>")
        sys.exit(1)

    result = answer_question(question, top_k=args.top_k, debug=args.debug)

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