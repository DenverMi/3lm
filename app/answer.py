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
        "bluetooth",
        "sig",
        "qualification",
        "qdid",
        "qdl",
        "epl",
        "pts",
        "ics",
        "ixit",
        "rf phy",
        "rf",
        "le audio",
        "auracast",
        "br/edr",
        "hci",
        "gatt",
        "profile",
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
- Every grounded claim must include the exact citation string provided in use_this_citation_exactly.
- Do not place citations inside the prose answer.
- Put supporting citations in a separate "Citations:" section after the answer.
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
            "- Cite every key statement.\n"
            "- Use citations exactly like: [chunk_id | Doc (p.X)] or [chunk_id | Doc (pp.X-Y)]\n"
            "- Do not write 'chunk_id:' inside the citation.\n"
            "- Omit 'General knowledge (model-based)' if internal evidence is sufficient.\n"
        )
    else:
        parts.append(
            "\nInstructions:\n"
            "- Write the entire answer in English.\n"
            "- Answer strictly from the excerpts when possible.\n"
            "- Cite every key statement.\n"
            "- Use citations exactly like: [chunk_id | Doc (p.X)] or [chunk_id | Doc (pp.X-Y)]\n"
            "- Do not write 'chunk_id:' inside the citation.\n"
            "- Do not append 'Not clearly specified in retrieved internal evidence.' unless some required part of the question truly cannot be answered from the excerpts.\n"
            "- Omit 'General knowledge (model-based)' if internal evidence is sufficient.\n"
        )

    return "\n".join(parts)


def ask_llm(
    question: str,
    items: List[Dict[str, Any]],
    weak_retrieval: bool = False,
    grounded_expansion: str | None = None,
) -> str:
    language = resolve_language(question)
    system_prompt = load_system_prompt(language)
    user_prompt = build_model_input(
        question,
        items,
        language,
        grounded_expansion=grounded_expansion,
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

    def score_item(item: Dict[str, Any]) -> tuple:
        text = item.get("text", "") or ""
        text_norm = " ".join(text.lower().split())

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

        return (
            phrase_hits,          # more exact phrase hits is better
            definition_like,      # cleaner chunk is better
            -int(looks_toc),      # TOC-like chunks are worse
            -pipe_count,          # huge table-ish chunks are worse
            -text_len,            # shorter is usually cleaner for definitions
            item.get("score", 0), # final tiebreaker
        )

    ranked = sorted(items, key=score_item, reverse=True)
    return ranked[:limit]

def answer_question(question: str, top_k: int = TOP_K_TO_MODEL, debug: bool = False) -> Dict[str, Any]:
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

    print("\n🔍 Retrieving relevant evidence...")
    items = retrieve(clean_question, top_k=max(top_k, 5))
    print(f"DEBUG timing: retrieve={time.perf_counter() - t0:.2f}s")

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
        if grounded_expansion:
            selected = exact_acronym_items[:1]
        elif exact_acronym_items:
            selected = exact_acronym_items[:2]
        else:
            selected = choose_best_definition_items(
                clean_question,
                items,
                grounded_expansion,
                limit=2,
            )
    else:
        selected = items[:top_k]

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
        ask_llm(clean_question, selected, grounded_expansion=grounded_expansion),
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