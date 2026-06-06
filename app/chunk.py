import json
from collections import defaultdict
from typing import List, Dict, Any
import re

from app.config import (
    PAGES_PATH,
    CHUNKS_PATH,
    MAX_CHARS,
    OVERLAP_CHARS,
    FIRST_N_PAGES,
    ensure_directories,
)

def detect_chunk_kind(text: str) -> str:
    stripped = text.strip()

    # Section-level glossary/definitions headings.
    # These are useful, but they are not the same as atomic definition chunks.
    if re.search(
        r"^\s{0,3}#{1,6}\s+(glossary|definitions)\b",
        stripped,
        re.IGNORECASE | re.MULTILINE,
    ):
        return "glossary"

    return "body"

def load_pages() -> List[Dict[str, Any]]:
    if not PAGES_PATH.exists():
        raise FileNotFoundError(f"Missing: {PAGES_PATH}. Run ingest first.")

    pages: List[Dict[str, Any]] = []
    with PAGES_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                pages.append(json.loads(line))

    pages.sort(key=lambda r: (r["program"], r["doc_type"], r["doc_name"], r["page"]))
    return pages


def write_chunks(chunks: List[Dict[str, Any]]) -> None:
    ensure_directories()
    with CHUNKS_PATH.open("w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")


def infer_priority(doc_type: str, doc_name: str, chunk_kind: str) -> int:
    name = doc_name.lower()
    dt = doc_type.lower()

    priority = 0

    if dt == "reference":
        priority += 2
    elif dt == "policies":
        priority += 1
    elif dt == "specs":
        priority += 2   # ← important: specs boosted

    if "faq" in name:
        priority += 3
    elif "one pager" in name or "one-pager" in name:
        priority += 2
    elif "glossary" in name:
        priority += 3
    elif "certification process" in name or "process" in name:
        priority += 2
    elif "guide" in name or "manual" in name:
        priority += 1

    # NEW: content-aware boosts
    if chunk_kind == "front_page":
        priority += 1
    elif chunk_kind == "glossary":
        priority += 3
    elif chunk_kind == "definition":
        priority += 2

    return priority

def split_reference_sections(text: str) -> List[str]:
    """
    Split reference-style docs into section chunks using markdown headings first.
    Falls back to paragraph grouping if headings are sparse.
    """
    text = text.strip()
    if not text:
        return []

    # Split on markdown headings while preserving the heading with its section
    parts = re.split(r'(?=^\s{0,3}#{2,6}\s+)', text, flags=re.MULTILINE)
    parts = [p.strip() for p in parts if p.strip()]

    # If headings produced useful sections, use them
    if len(parts) >= 3:
        return parts

    # Fallback: split on blank lines and group paragraphs up to MAX_CHARS
    paras = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
    sections: List[str] = []
    current = ""

    for para in paras:
        candidate = f"{current}\n\n{para}".strip() if current else para
        if len(candidate) <= MAX_CHARS:
            current = candidate
        else:
            if current:
                sections.append(current)
            current = para

    if current:
        sections.append(current)

    return sections


def page_range_for_span(page_spans, start_char: int, end_char: int) -> tuple:
    pages_in_chunk = [
        page_no for (page_no, s, e) in page_spans
        if not (e <= start_char or s >= end_char)
    ]
    if not pages_in_chunk:
        return None, None
    return min(pages_in_chunk), max(pages_in_chunk)

def infer_source_type(doc_type: str, doc_name: str) -> str:
    if doc_type != "email":
        return doc_type

    name = doc_name.lower()
    if "thread_analysis" in name:
        return "email_thread_analysis"
    if "_case_" in name:
        return "email_case"
    return "email"

def make_front_page_chunks(doc_pages: List[Dict[str, Any]], first_n_pages: int = FIRST_N_PAGES) -> List[Dict[str, Any]]:
    """
    Preserve first N pages as standalone chunks.
    This is very helpful for definitions, scope, summaries, policies, and intros.
    """
    first = doc_pages[0]
    program = first["program"]
    doc_type = first["doc_type"]
    doc_name = first["doc_name"]

    chunks: List[Dict[str, Any]] = []

    for p in doc_pages:
        if p["page"] > first_n_pages:
            break

        text = p["text"].strip()
        if not text:
            continue

        chunk_kind = "front_page"
        chunk_id = f"{program}:{doc_type}:{doc_name}:p{p['page']:05d}"

        chunks.append({
            "chunk_id": chunk_id,
            "program": program,
            "doc_type": doc_type,
            "source_type": infer_source_type(doc_type, doc_name),
            "doc_name": doc_name,
            "chunk_kind": chunk_kind,
            "priority": infer_priority(doc_type, doc_name, chunk_kind),
            "page_start": p["page"],
            "page_end": p["page"],
            "text": text,
        })

    return chunks


def make_body_chunks(doc_pages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Build body chunks.
    - For reference/policies docs: split by sections/headings first.
    - For other docs: keep sliding-window chunking.
    """
    first = doc_pages[0]
    program = first["program"]
    doc_type = first["doc_type"]
    doc_name = first["doc_name"]

    parts: List[str] = []
    page_spans = []  # (page_no, start_char, end_char)
    cursor = 0

    for p in doc_pages:
        text = p["text"].strip()
        if not text:
            continue

        page_text = text + "\n\n"
        start = cursor
        parts.append(page_text)
        cursor += len(page_text)
        end = cursor
        page_spans.append((p["page"], start, end))

    full_text = "".join(parts).strip()
    if not full_text:
        return []

    chunks: List[Dict[str, Any]] = []
    chunk_index = 0

    # Synthetic records from Markdown table rows should become standalone chunks.
    # These are created by ingest.py with large page numbers (100000+).
    normal_pages = []
    synthetic_pages = []

    for p in doc_pages:
        if p.get("page", 0) >= 100000:
            synthetic_pages.append(p)
        else:
            normal_pages.append(p)

    for p in synthetic_pages:
        text = p["text"].strip()
        if not text:
            continue

        chunk_kind = "definition"

        chunk_id = f"{program}:{doc_type}:{doc_name}:t{p['page']:05d}"

        chunks.append({
            "chunk_id": chunk_id,
            "program": program,
            "doc_type": doc_type,
            "source_type": infer_source_type(doc_type, doc_name),
            "doc_name": doc_name,
            "chunk_kind": chunk_kind,
            "priority": infer_priority(doc_type, doc_name, chunk_kind),
            "page_start": p["page"],
            "page_end": p["page"],
            "text": text,
        })

    doc_pages = normal_pages

    # Section-aware chunking for FAQ/reference/policy-like docs
    if doc_type in {"reference", "policies"}:
        sections = split_reference_sections(full_text)

        search_pos = 0
        for section in sections:
            section = section.strip()
            if not section:
                continue

            start_char = full_text.find(section, search_pos)
            if start_char == -1:
                start_char = full_text.find(section)
            if start_char == -1:
                continue

            end_char = start_char + len(section)
            search_pos = end_char

            page_start, page_end = page_range_for_span(page_spans, start_char, end_char)
            chunk_kind = detect_chunk_kind(section)
            chunk_id = f"{program}:{doc_type}:{doc_name}:c{chunk_index:05d}"

            chunks.append({
                "chunk_id": chunk_id,
                "program": program,
                "doc_type": doc_type,
                "source_type": infer_source_type(doc_type, doc_name),
                "doc_name": doc_name,
                "chunk_kind": chunk_kind,
                "priority": infer_priority(doc_type, doc_name, chunk_kind),
                "page_start": page_start,
                "page_end": page_end,
                "text": section,
            })
            chunk_index += 1

        return chunks

    # Default sliding-window chunking for specs/reports/etc.
    start_char = 0
    while start_char < len(full_text):
        end_char = min(start_char + MAX_CHARS, len(full_text))
        chunk_text = full_text[start_char:end_char].strip()

        if not chunk_text:
            break

        page_start, page_end = page_range_for_span(page_spans, start_char, end_char)

        chunk_kind = detect_chunk_kind(chunk_text)
        chunk_id = f"{program}:{doc_type}:{doc_name}:c{chunk_index:05d}"

        chunks.append({
            "chunk_id": chunk_id,
            "program": program,
            "doc_type": doc_type,
            "source_type": infer_source_type(doc_type, doc_name),
            "doc_name": doc_name,
            "chunk_kind": chunk_kind,
            "priority": infer_priority(doc_type, doc_name, chunk_kind),
            "page_start": page_start,
            "page_end": page_end,
            "text": chunk_text,
        })

        chunk_index += 1

        if end_char == len(full_text):
            break

        start_char = max(0, end_char - OVERLAP_CHARS)

    return chunks


def main() -> None:
    pages = load_pages()
    print(f"Loaded {len(pages)} page records from {PAGES_PATH}")

    grouped: Dict[tuple, List[Dict[str, Any]]] = defaultdict(list)
    for p in pages:
        key = (p["program"], p["doc_type"], p["doc_name"])
        grouped[key].append(p)

    all_chunks: List[Dict[str, Any]] = []

    for (program, doc_type, doc_name), doc_pages in grouped.items():
        front_chunks = make_front_page_chunks(doc_pages)
        body_chunks = make_body_chunks(doc_pages)
        doc_chunks = front_chunks + body_chunks

        all_chunks.extend(doc_chunks)
        print(
            f"Chunked {program}/{doc_type}/{doc_name}: "
            f"{len(doc_chunks)} chunks "
            f"(front={len(front_chunks)}, body={len(body_chunks)})"
        )

    write_chunks(all_chunks)
    print(f"✅ Wrote {len(all_chunks)} chunks to {CHUNKS_PATH}")

    if all_chunks:
        s = all_chunks[0]
        print("\nSample chunk:")
        print(
            f"{s['chunk_id']} | kind={s['chunk_kind']} | priority={s['priority']} | "
            f"pp.{s['page_start']}-{s['page_end']}"
        )
        print(s["text"][:400] + "...")


if __name__ == "__main__":
    main()