import argparse
import json
import pickle
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import time

import chromadb
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer

from app.config import (
    CHROMA_PATH,
    CHUNKS_PATH,
    COLLECTION_NAME,
    EMBED_MODEL,
    INITIAL_RETRIEVAL_K,
    DEFAULT_TOP_K,
)

# Local cache paths for BM25
BM25_PATH = CHUNKS_PATH.parent / "bm25.pkl"
BM25_CHUNKS_PATH = CHUNKS_PATH.parent / "bm25_chunks.jsonl"
BM25_META_PATH = CHUNKS_PATH.parent / "bm25_meta.json"
EXPANSION_CACHE_PATH = CHUNKS_PATH.parent / "expansion_cache.json"

# Retrieval sizes
BM25_RETRIEVAL_K = 30
SEMANTIC_RETRIEVAL_K = 10
RRF_K = 60  # reciprocal rank fusion constant
EXPANSION_CACHE: Dict[str, List[str]] = {}

# Explicit bonuses
EARLY_PAGE_BONUS = 0.35
FRONT_PAGE_BONUS = 0.25
PRIORITY_MULTIPLIER = 0.18

model = None
client = chromadb.PersistentClient(path=str(CHROMA_PATH))
collection = client.get_collection(COLLECTION_NAME)

def get_model():
    global model
    if model is None:
        model = SentenceTransformer(EMBED_MODEL)
    return model


def tokenize(text: str) -> List[str]:
    text = text.lower()
    return re.findall(r"[a-z0-9]+", text)


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing: {path}")
    items: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                items.append(json.loads(line))
    return items


def save_jsonl(path: Path, items: List[Dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")


def build_bm25(chunks: List[Dict[str, Any]]) -> BM25Okapi:
    tokenized = [tokenize(c.get("text", "")) for c in chunks]
    return BM25Okapi(tokenized)


def save_bm25(bm25: BM25Okapi, chunks: List[Dict[str, Any]]) -> None:
        with BM25_PATH.open("wb") as f:
            pickle.dump(bm25, f)

        save_jsonl(BM25_CHUNKS_PATH, chunks)

        meta = {
            "chunks_path": str(CHUNKS_PATH),
            "chunks_mtime": CHUNKS_PATH.stat().st_mtime,
        }
        with BM25_META_PATH.open("w", encoding="utf-8") as f:
            json.dump(meta, f, ensure_ascii=False, indent=2)

def load_bm25() -> Tuple[Optional[BM25Okapi], Optional[List[Dict[str, Any]]]]:
    if not BM25_PATH.exists() or not BM25_CHUNKS_PATH.exists() or not BM25_META_PATH.exists():
        return None, None

    try:
        with BM25_META_PATH.open("r", encoding="utf-8") as f:
            meta = json.load(f)

        cached_mtime = meta.get("chunks_mtime")
        current_mtime = CHUNKS_PATH.stat().st_mtime

        if cached_mtime != current_mtime:
            return None, None

        with BM25_PATH.open("rb") as f:
            bm25 = pickle.load(f)

        chunks = load_jsonl(BM25_CHUNKS_PATH)
        return bm25, chunks

    except Exception:
        return None, None

def get_chunks_for_bm25() -> Tuple[BM25Okapi, List[Dict[str, Any]]]:
    bm25, cached_chunks = load_bm25()
    if bm25 is not None and cached_chunks is not None:
        return bm25, cached_chunks

    chunks = load_jsonl(CHUNKS_PATH)
    bm25 = build_bm25(chunks)
    save_bm25(bm25, chunks)
    return bm25, chunks

def is_definition_query(query: str) -> bool:
    q = query.strip().lower()

    if re.search(r"\bwhat\s+is\b", q):
        return True
    if re.search(r"\bwhat\s+are\b", q):
        return True
    if re.search(r"\bdefine\b", q):
        return True
    if re.search(r"\bmeaning\s+of\b", q):
        return True

    japanese_definition_patterns = [
        "とは",
        "何ですか",
        "なんですか",
        "意味",
    ]

    if any(pattern in query for pattern in japanese_definition_patterns):
        return True

    return False

def is_process_query(query: str) -> bool:
    q = query.lower()
    keywords = [
        "process",
        "how to",
        "steps",
        "procedure",
        "certification",
        "certify",
        "workflow",
        "approval",
        "apply",
        "submit",
    ]
    return any(k in q for k in keywords)

def extract_core_term(query: str) -> str:
    raw = query.strip()
    q = raw.lower().strip()

    # Japanese / mixed-language acronym definition queries:
    # BluetoothでICSとは何ですか？ -> ICS
    acronym_match = re.search(r"\b[A-Z][A-Z0-9/\-]{1,9}\b", raw)
    if acronym_match and any(marker in raw for marker in ["とは", "何ですか", "なんですか", "意味"]):
        return acronym_match.group(0)

    for prefix in ["what is ", "what are ", "define "]:
        if q.startswith(prefix):
            q = q[len(prefix):]
            break

    return q.strip(" ?")

def looks_like_term_definition(text: str, term: str) -> bool:
    if not term:
        return False

    raw = text or ""
    term_l = " ".join(term.lower().split())
    text_l = raw.lower()

    # Check line-by-line first — best for Markdown tables / glossary rows
    for line in raw.splitlines():
        line_l = " ".join(line.lower().split())

        if term_l not in line_l:
            continue

        # Markdown table / glossary row with definition-like wording
        if "|" in line_l and (
            "portable device" in line_l
            or "containing one or more access credentials" in line_l
            or "access credentials" in line_l
        ):
            return True

        # Plain glossary line
        if (
            line_l.startswith(term_l)
            and (
                "portable device" in line_l
                or "containing one or more access credentials" in line_l
                or "access credentials" in line_l
            )
        ):
            return True

    # Then check only a small window after the term, not the whole chunk
    idx = text_l.find(term_l)
    if idx == -1:
        return False

    window = " ".join(text_l[idx:idx + 350].split())

    patterns = [
        rf"\b{re.escape(term_l)}\b\s+means\b",
        rf"\b{re.escape(term_l)}\b\s+is\b",
        rf"\b{re.escape(term_l)}\b\s+refers to\b",
        rf"\b{re.escape(term_l)}\b\s+a portable device\b",
        rf"\b{re.escape(term_l)}\b.*?\bcontaining one or more access credentials\b",
    ]

    return any(re.search(p, window, re.IGNORECASE) for p in patterns)

def is_acronym_term(term: str) -> bool:
    term = term.strip()
    return bool(re.fullmatch(r"[a-z0-9/\-]{2,10}", term.lower()))

def load_expansion_cache() -> Dict[str, List[str]]:
    if not EXPANSION_CACHE_PATH.exists():
        return {}
    try:
        with EXPANSION_CACHE_PATH.open("r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            return {str(k): list(v) for k, v in data.items()}
    except Exception:
        pass
    return {}

def save_expansion_cache(cache: Dict[str, List[str]]) -> None:
    with EXPANSION_CACHE_PATH.open("w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

def find_expansion_from_corpus(term: str, chunks: List[Dict[str, Any]]) -> List[str]:
    term_key = term.lower().strip()

    global EXPANSION_CACHE
    if not EXPANSION_CACHE:
        EXPANSION_CACHE = load_expansion_cache()

    if term_key in EXPANSION_CACHE:
        return EXPANSION_CACHE[term_key]

    if not is_acronym_term(term):
        return []

    expansions = []
    seen = set()

    patterns = [
        re.compile(
            rf"([A-Za-z][A-Za-z0-9/&,\-]*(?: [A-Za-z][A-Za-z0-9/&,\-]*){{1,9}})\s*\(\s*{re.escape(term)}\s*\)",
            re.IGNORECASE,
        ),
        re.compile(
            rf"{re.escape(term)}\s*\(\s*([A-Za-z][A-Za-z0-9/&,\- ]{{3,100}}?)\s*\)",
            re.IGNORECASE,
        ),
    ]

    stop_starts = (
        "see ", "via ", "for ", "use ", "using ", "with ", "from ",
        "in ", "on ", "to ", "by ", "if ", "when ", "where "
    )

    for chunk in chunks:
        text = chunk.get("text", "") or ""
        if term.lower() not in text.lower():
            continue

        for pat in patterns:
            for m in pat.finditer(text):
                candidate = " ".join(m.group(1).split()).strip(" ,;:-")

                if len(candidate.split()) < 2:
                    continue
                if candidate.lower().startswith(stop_starts):
                    continue
                if candidate.endswith("."):
                    continue

                words = re.findall(r"[A-Za-z]+", candidate)
                if len(words) < 2:
                    continue

                initials = "".join(w[0].upper() for w in words if w)
                if initials != term.upper():
                    continue

                key = candidate.lower()
                if key not in seen:
                    seen.add(key)
                    expansions.append(candidate)

    result = expansions[:3]
    EXPANSION_CACHE[term_key] = result
    save_expansion_cache(EXPANSION_CACHE)
    return result

def build_query_variants(query: str, chunks: List[Dict[str, Any]]) -> List[str]:
    """
    Expand acronym-like definition queries using the corpus itself,
    not an LLM guess.
    """
    variants = [query]
    raw_query = query.strip()
    term = raw_query.strip(" ?")
    for prefix in ["What is ", "What are ", "Define ", "what is ", "what are ", "define "]:
        if raw_query.startswith(prefix):
            term = raw_query[len(prefix):].strip(" ?")
            break
    if not is_acronym_term(term):
        return variants

    expansions = find_expansion_from_corpus(term, chunks)
    for expanded in expansions:
        expanded_query = re.sub(
            rf"\b{re.escape(term)}\b",
            expanded,
            query,
            flags=re.IGNORECASE,
        )
        if expanded_query not in variants:
            variants.append(expanded_query)

    return variants

def find_exact_acronym_definition_hits(
    query: str,
    items: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    term = extract_core_term(query).strip()
    if not is_acronym_term(term):
        return []

    hits = []
    seen = set()

    # exact acronym-definition patterns:
    #   Profile Tuning Suite (PTS)
    #   PTS (Profile Tuning Suite)
    patterns = [
        re.compile(
            rf"([A-Za-z][A-Za-z0-9/&,\-]*(?: [A-Za-z][A-Za-z0-9/&,\-]*){{1,9}})\s*\(\s*{re.escape(term)}\s*\)",
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
            m = pat.search(text)
            if not m:
                continue

            candidate = " ".join(m.group(1).split()).strip(" ,;:-")
            words = re.findall(r"[A-Za-z]+", candidate)
            if len(words) < 2:
                continue

            initials = "".join(w[0].upper() for w in words if w)
            if initials != term.upper():
                continue

            if item["chunk_id"] not in seen:
                seen.add(item["chunk_id"])
                hits.append(item)
            break

    return hits

def parse_domain_prefix(query: str) -> Tuple[Optional[str], str]:
    q = query.strip()
    lowered = q.lower()

    prefixes = [
        ("in bt", "bluetooth"),
        ("in bluetooth", "bluetooth"),
        ("in matter", "matter"),
        ("in aliro", "aliro"),
    ]

    for prefix, domain in prefixes:
        if lowered.startswith(prefix):
            clean = q[len(prefix):].lstrip(" ,:-")
            return domain, clean or q

    return None, query

def is_comparison_query(query: str) -> bool:
    q = query.lower()
    return any(
        phrase in q
        for phrase in [
            "difference between",
            "compare",
            "comparison",
            "versus",
            " vs ",
            "different from",
        ]
    )

def detect_intent(query: str) -> str:
    if is_process_query(query):
        return "process"
    if is_comparison_query(query):
        return "comparison"
    if is_definition_query(query):
        return "definition"
    if is_advisory_query(query):
        return "advisory"
    return "general"

def extract_exact_lookup_phrases(query: str) -> List[str]:
    q = query.lower()
    phrases = []

    # Existing structured lookup phrases.
    patterns = [
        r"\boption\s+\d+[a-z]?\b",
        r"\btable\s+\d+(?:\.\d+)*\b",
        r"\bsection\s+\d+(?:\.\d+)*\b",
        r"\bclause\s+\d+(?:\.\d+)*\b",
    ]

    for pattern in patterns:
        for match in re.finditer(pattern, q, flags=re.IGNORECASE):
            phrase = " ".join(match.group(0).split()).lower()
            if phrase not in phrases:
                phrases.append(phrase)

    # General meaningful adjacent phrases from the query.
    stop_terms = {
        "what", "which", "when", "where", "who", "why", "how",
        "do", "does", "did", "we", "i", "you", "they",
        "need", "needed", "prepare", "prepared", "include", "included",
        "in", "on", "for", "to", "of", "the", "a", "an",
        "is", "are", "be", "with", "and", "or",
    }

    tokens = [
        token for token in tokenize(q)
        if len(token) >= 3 and token not in stop_terms
    ]

    for size in range(4, 1, -1):
        for i in range(0, len(tokens) - size + 1):
            phrase = " ".join(tokens[i:i + size])
            if phrase not in phrases:
                phrases.append(phrase)

    return phrases[:20]

def extract_topic_heading_phrases(query: str) -> List[str]:
    q = query.lower()

    stop_terms = {
        "what", "which", "when", "where", "who", "why", "how",
        "do", "does", "did", "we", "i", "you", "they",
        "required", "requirement", "requirements",
        "need", "needed", "prepare", "prepared", "include", "included",
        "in", "on", "for", "to", "of", "the", "a", "an",
        "is", "are", "be", "with", "and", "or",
    }

    tokens = [
        token for token in tokenize(q)
        if len(token) >= 3 and token not in stop_terms
    ]

    phrases = []

    for size in range(4, 1, -1):
        for i in range(0, len(tokens) - size + 1):
            phrase = " ".join(tokens[i:i + size])
            if phrase not in phrases:
                phrases.append(phrase)

    return phrases[:10]

def extract_acronyms_for_glossary_lookup(text: str) -> List[str]:
    candidates = re.findall(r"(?<![A-Za-z0-9])[A-Z][A-Z0-9]{1,9}(?![A-Za-z0-9])", text or "")

    skip = {
        "SIG",
        "FAQ",
        "JSON",
        "PDF",
        "URL",
        "HTTP",
        "HTTPS",
    }

    acronyms = []
    for candidate in candidates:
        if candidate in skip:
            continue
        if candidate not in acronyms:
            acronyms.append(candidate)

    return acronyms[:10]

def search_glossary_acronyms(
    query: str,
    chunks: List[Dict[str, Any]],
    top_k: int = 10,
) -> List[Dict[str, Any]]:
    acronyms = extract_acronyms_for_glossary_lookup(query)

    if not acronyms:
        return []

    hits = []

    for chunk in chunks:
        text = chunk.get("text", "") or ""
        text_lower = text.lower()

        doc_type = (chunk.get("doc_type") or "").lower()
        source_type = (chunk.get("source_type") or "").lower()

        if doc_type not in {"policies", "specs", "reference"}:
            continue

        if source_type in {"email_case", "email_thread_analysis", "email"}:
            continue

        doc_name = (chunk.get("doc_name") or "").lower()

        glossaryish = (
            "definitions" in text_lower
            or "acronym" in text_lower
            or "abbreviation" in text_lower
            or "glossary" in text_lower
            or "glossary" in doc_name
        )

        if not glossaryish:
            continue

        matched = []

        for acronym in acronyms:
            definition_patterns = [
                # Markdown heading: ### TCW — Test Coverage Waiver
                rf"^\s*#{{1,6}}\s+{re.escape(acronym)}\s*(?:—|-|:)",

                # Markdown table row: | TCW | Test Coverage Waiver |
                rf"\|\s*{re.escape(acronym)}\s*\|",

                # QPRD split table text: Test Coverage Waiver (TCW)
                rf"\b[A-Z][A-Za-z ]{{2,80}}\s*\(\s*{re.escape(acronym)}\s*\)",
            ]

            if any(re.search(p, text, flags=re.IGNORECASE | re.MULTILINE) for p in definition_patterns):
                matched.append(acronym)

        if not matched:
            continue

        score = 24.0 + len(matched)

        if doc_type == "policies":
            score += 4.0
        elif doc_type == "specs":
            score += 3.0
        elif doc_type == "reference":
            score += 2.0

        meta = {
            "program": chunk.get("program"),
            "doc_type": chunk.get("doc_type"),
            "source_type": chunk.get("source_type"),
            "doc_name": chunk.get("doc_name"),
            "chunk_kind": chunk.get("chunk_kind"),
            "priority": chunk.get("priority", 0),
            "page_start": chunk.get("page_start"),
            "page_end": chunk.get("page_end"),
        }

        hits.append(
            {
                "chunk_id": chunk["chunk_id"],
                "text": chunk["text"],
                "metadata": meta,
                "bm25_score": score,
                "bm25_rank": 1,
                "semantic_distance": None,
                "semantic_rank": None,
                "glossary_score": score,
                "glossary_acronyms": matched,
            }
        )

    return sorted(
        hits,
        key=lambda item: item["glossary_score"],
        reverse=True,
    )[: max(top_k, 30)]

def search_topic_headings(
    query: str,
    chunks: List[Dict[str, Any]],
    top_k: int = 10,
) -> List[Dict[str, Any]]:
    phrases = extract_topic_heading_phrases(query)

    if not phrases:
        return []

    hits = []

    for chunk in chunks:
        text = chunk.get("text", "") or ""
        doc_type = (chunk.get("doc_type") or "").lower()
        source_type = (chunk.get("source_type") or "").lower()

        # Only use structured/official-ish documents for heading matches.
        # Email cases already have their own lane.
        if source_type in {"email_case", "email_thread_analysis", "email"}:
            continue

        matched_phrases = []

        for phrase in phrases:
            heading_pattern = rf"^\s*#{{1,6}}\s+(?:[\d\.]+\s+)?[^\n]*\b{re.escape(phrase)}\b[^\n]*$"

            if re.search(heading_pattern, text, flags=re.IGNORECASE | re.MULTILINE):
                matched_phrases.append(phrase)

        if not matched_phrases:
            continue

        score = 18.0 + len(matched_phrases)

        if doc_type in {"policies", "specs"}:
            score += 8.0
        elif doc_type == "reference":
            score += 4.0

        meta = {
            "program": chunk.get("program"),
            "doc_type": chunk.get("doc_type"),
            "source_type": chunk.get("source_type"),
            "doc_name": chunk.get("doc_name"),
            "chunk_kind": chunk.get("chunk_kind"),
            "priority": chunk.get("priority", 0),
            "page_start": chunk.get("page_start"),
            "page_end": chunk.get("page_end"),
        }

        hits.append(
            {
                "chunk_id": chunk["chunk_id"],
                "text": chunk["text"],
                "metadata": meta,
                "bm25_score": score,
                "bm25_rank": 1,
                "semantic_distance": None,
                "semantic_rank": None,
                "topic_heading_score": score,
                "topic_heading_phrases": matched_phrases,
            }
        )

    return sorted(
        hits,
        key=lambda item: item["topic_heading_score"],
        reverse=True,
    )[: max(top_k, 30)]

def search_exact_phrases(
    query: str,
    chunks: List[Dict[str, Any]],
    top_k: int = 10,
) -> List[Dict[str, Any]]:
    phrases = extract_exact_lookup_phrases(query)

    if not phrases:
        return []

    hits = []

    for chunk in chunks:
        text = chunk.get("text", "") or ""
        text_lower = " ".join(text.lower().split())
        text_for_heading_match = text.lower()

        matched_phrases = [
            phrase for phrase in phrases
            if phrase in text_lower
        ]

        if not matched_phrases:
            continue

        score = 20.0 + len(matched_phrases)

        doc_type = (chunk.get("doc_type") or "").lower()
        source_type = (chunk.get("source_type") or "").lower()

        doc_name = (chunk.get("doc_name") or "").lower()
        query_tokens = set(tokenize(query))

        doc_name_tokens = set(tokenize(doc_name))
        shared_doc_tokens = query_tokens & doc_name_tokens

        if shared_doc_tokens:
            score += 10.0

        # Prefer exact matches in official/reviewed sources over raw email-derived material.
        if doc_type in {"policies", "specs", "reference"} and source_type not in {"email_case", "email_thread_analysis", "email"}:
            score += 8.0

        # Prefer exact matches that appear in headings / section titles.
        for phrase in matched_phrases:
            heading_pattern = rf"^\s*#{{1,6}}\s+.*\b{re.escape(phrase)}\b"
            numbered_heading_pattern = rf"^\s*#{{1,6}}\s+[\d\.]+\s+.*\b{re.escape(phrase)}\b"

            if re.search(numbered_heading_pattern, text_for_heading_match, flags=re.IGNORECASE | re.MULTILINE):
                score += 18.0
                break

            if re.search(heading_pattern, text_for_heading_match, flags=re.IGNORECASE | re.MULTILINE):
                score += 14.0
                break

        # Raw email cases can still help, but should not outrank exact official headings.
        if source_type in {"email_case", "email_thread_analysis", "email"}:
                score -= 4.0

        meta = {
            "program": chunk.get("program"),
            "doc_type": chunk.get("doc_type"),
            "source_type": chunk.get("source_type"),
            "doc_name": chunk.get("doc_name"),
            "chunk_kind": chunk.get("chunk_kind"),
            "priority": chunk.get("priority", 0),
            "page_start": chunk.get("page_start"),
            "page_end": chunk.get("page_end"),
        }

        hits.append(
            {
                "chunk_id": chunk["chunk_id"],
                "text": chunk["text"],
                "metadata": meta,
                "bm25_score": score,
                "bm25_rank": 1,
                "semantic_distance": None,
                "semantic_rank": None,
                "exact_phrase_score": score,
                "exact_phrases": matched_phrases,
            }
        )

    return sorted(
        hits,
        key=lambda item: item["exact_phrase_score"],
        reverse=True,
    )[: max(top_k, 50)]

def format_citation(meta: Dict[str, Any]) -> str:
    doc_name = meta.get("doc_name", "unknown")
    page_start = meta.get("page_start")
    page_end = meta.get("page_end")

    if page_start and page_end:
        if page_start == page_end:
            return f"{doc_name} (p.{page_start})"
        return f"{doc_name} (pp.{page_start}-{page_end})"

    return f"{doc_name} (unpaginated)"

def expand_advisory_query(query: str) -> str:
    if not is_advisory_query(query):
        return query

    expansion_terms = [
        "qualification",
        "qualified product",
        "qualified module",
        "Bluetooth module",
        "new qualification",
        "member account",
        "supplier cannot qualify",
        "complete the Bluetooth Qualification Process",
        "product listing",
        "declaration",
    ]

    return query + " " + " ".join(expansion_terms)

def is_advisory_query(query: str) -> bool:
    q = query.lower()

    definition_markers = [
        "what is",
        "what are",
        "とは",
        "って何",
        "とは何",
        "何ですか",
    ]

    if any(marker in q for marker in definition_markers):
        return False

    advisory_markers = [
        "customer asks",
        "past case",
        "past cases",
        "do they",
        "do we",
        "do i",
        "does this",
        "does it",
        "should",
        "still need",
        "required",
        "need a new",
        "need to",

        "必要ですか",
        "必要でしょうか",
        "必要になりますか",
        "必要か",
        "要りますか",
    ]

    return any(marker in q for marker in advisory_markers)

def metadata_bonus(meta: Dict[str, Any], intent: str, query: str) -> float:
    bonus = 0.0
    doc_type = (meta.get("doc_type") or "").lower()
    doc_name = (meta.get("doc_name") or "").lower()

    page_start = meta.get("page_start")
    chunk_kind = (meta.get("chunk_kind") or "").lower()

    if intent != "definition":
        if page_start is not None and page_start <= 5:
            bonus += EARLY_PAGE_BONUS

        if chunk_kind == "front_page":
            bonus += FRONT_PAGE_BONUS

    priority = meta.get("priority", 0) or 0
    bonus += float(priority) * PRIORITY_MULTIPLIER

    if intent == "definition":
        term = extract_core_term(query)

        if is_acronym_term(term):
            if "_ts" in doc_name or doc_name.endswith("ts.md"):
                bonus -= 4.0

        if term and term in doc_name:
            bonus += 2.0

        if chunk_kind == "definition":
            bonus += 9.0

        if chunk_kind == "glossary":
            bonus += 2.0

        if chunk_kind == "front_page":
            bonus -= 1.5

        if doc_type == "specs":
            bonus += 3.0
            if term and term in doc_name:
                bonus += 1.0
            if chunk_kind in ("glossary", "definition"):
                bonus += 2.5

        if doc_type == "reference":
            bonus += 0.8

        if "faq" in doc_name:
            bonus += 0.6
        if "one pager" in doc_name or "one-pager" in doc_name:
            bonus += 0.5
        if "glossary" in doc_name:
            bonus += 1.0

    elif intent == "process":
        source_type = (meta.get("source_type") or "").lower()
        chunk_kind = (meta.get("chunk_kind") or "").lower()

        if source_type == "email_case":
            bonus += 3.5
        elif source_type == "email_thread_analysis":
            bonus += 1.5

        if chunk_kind == "front_page":
            bonus -= 1.5

        if doc_type == "policies":
            bonus += 1.5

        if doc_type == "specs":
            bonus += 0.7

        if doc_type == "reference":
            bonus += 0.6

        if "certification" in doc_name:
            bonus += 1.2
        if "process" in doc_name:
            bonus += 1.1
        if "guide" in doc_name or "manual" in doc_name:
            bonus += 0.7

    elif intent == "advisory":
        source_type = (meta.get("source_type") or "").lower()

        if doc_type == "reference" and "official faq" in doc_name:
            bonus += 3.0

        if source_type == "email_case":
            bonus += 2.5

        if doc_type == "reference":
            bonus += 0.6

        if "faq" in doc_name:
            bonus += 0.4

    return bonus 

def search_bm25(query: str, chunks: List[Dict[str, Any]], bm25: BM25Okapi, top_k: int) -> List[Dict[str, Any]]:
    t0 = time.perf_counter()

    q_lower = query.lower()
    term = extract_core_term(query).lower()

    q_tokens = tokenize(query)

    if is_definition_query(query) and is_acronym_term(term):
        t_exp = time.perf_counter()
        expansions = find_expansion_from_corpus(term, chunks)
        for expanded in expansions:
            q_tokens.extend(tokenize(expanded))

    if "version date" in q_lower:
        q_tokens += ["version", "date"] * 5

    t1 = time.perf_counter()
    scores = bm25.get_scores(q_tokens)

    scored = []
    for idx, chunk in enumerate(chunks):
        text_lower = (chunk.get("text", "") or "").lower()
        adjusted_score = float(scores[idx])

        if is_definition_query(query) and term and " " in term:
            normalized_text = " ".join(text_lower.split())
            normalized_term = " ".join(term.split())
            if normalized_term in normalized_text:
                adjusted_score += 3.0

        if term and term in text_lower and not is_acronym_term(term):
            adjusted_score += 2.0

        scored.append((idx, adjusted_score))

    ranked = sorted(scored, key=lambda x: x[1], reverse=True)[: max(top_k, 50)]

    out: List[Dict[str, Any]] = []
    for rank, (idx, score) in enumerate(ranked, start=1):
        chunk = chunks[idx]
        out.append({
            "chunk_id": chunk["chunk_id"],
            "text": chunk["text"],
            "metadata": {
                "program": chunk.get("program"),
                "doc_type": chunk.get("doc_type"),
                "source_type": chunk.get("source_type"),
                "doc_name": chunk.get("doc_name"),
                "chunk_kind": chunk.get("chunk_kind"),
                "priority": chunk.get("priority", 0),
                "page_start": chunk.get("page_start"),
                "page_end": chunk.get("page_end"),
            },
            "bm25_score": float(score),
            "bm25_rank": rank,
            "semantic_distance": None,
            "semantic_rank": None,
        })

    return out

def search_semantic(query: str, chunks: List[Dict[str, Any]], top_k: int) -> List[Dict[str, Any]]:
    query_variants = build_query_variants(query, chunks)
    merged: Dict[str, Dict[str, Any]] = {}

    for qv in query_variants:
        query_embedding = get_model().encode(qv).tolist()

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
        )

        docs = results["documents"][0]
        metas = results["metadatas"][0]
        ids = results["ids"][0]
        distances = results.get("distances", [[None] * len(docs)])[0]

        for rank, (doc, meta, chunk_id, distance) in enumerate(zip(docs, metas, ids, distances), start=1):
            distance_val = None if distance is None else float(distance)

            existing = merged.get(chunk_id)
            if existing is None or (
                distance_val is not None and (
                    existing["semantic_distance"] is None or distance_val < existing["semantic_distance"]
                )
            ):
                merged[chunk_id] = {
                    "chunk_id": chunk_id,
                    "text": doc,
                    "metadata": {
                        "program": meta.get("program"),
                        "doc_type": meta.get("doc_type"),
                        "source_type": meta.get("source_type"),
                        "doc_name": meta.get("doc_name"),
                        "chunk_kind": meta.get("chunk_kind"),
                        "priority": meta.get("priority", 0),
                        "page_start": meta.get("page_start"),
                        "page_end": meta.get("page_end"),
                    },
                    "bm25_score": None,
                    "bm25_rank": None,
                    "semantic_distance": distance_val,
                    "semantic_rank": rank,
                }

    out = sorted(
        merged.values(),
        key=lambda x: float("inf") if x["semantic_distance"] is None else x["semantic_distance"]
    )[:top_k]

    for rank, item in enumerate(out, start=1):
        item["semantic_rank"] = rank

    return out


def reciprocal_rank(rank: Optional[int], k: int = RRF_K) -> float:
    if rank is None:
        return 0.0
    return 1.0 / (k + rank)

def text_signature(text: str, limit: int = 500) -> str:
    normalized = " ".join((text or "").lower().split())
    return normalized[:limit]

def merge_and_rerank(
    query: str,
    bm25_results: List[Dict[str, Any]],
    semantic_results: List[Dict[str, Any]],
    top_k: int,
) -> List[Dict[str, Any]]:
    intent = detect_intent(query)
    merged: Dict[str, Dict[str, Any]] = {}

    for item in bm25_results + semantic_results:
        chunk_id = item["chunk_id"]

        if chunk_id not in merged:
            merged[chunk_id] = {
                "chunk_id": chunk_id,
                "text": item["text"],
                "metadata": item["metadata"],
                "bm25_score": item.get("bm25_score"),
                "bm25_rank": item.get("bm25_rank"),
                "semantic_distance": item.get("semantic_distance"),
                "semantic_rank": item.get("semantic_rank"),
                "exact_phrase_score": item.get("exact_phrase_score", 0.0),
                "exact_phrases": item.get("exact_phrases", []),
                "glossary_score": item.get("glossary_score", 0.0),
                "glossary_acronyms": item.get("glossary_acronyms", []),
                "topic_heading_score": item.get("topic_heading_score", 0.0),
                "topic_heading_phrases": item.get("topic_heading_phrases", []),
            }
        else:
            current = merged[chunk_id]
            if current.get("bm25_rank") is None and item.get("bm25_rank") is not None:
                current["bm25_rank"] = item["bm25_rank"]
                current["bm25_score"] = item["bm25_score"]
            if current.get("semantic_rank") is None and item.get("semantic_rank") is not None:
                current["semantic_rank"] = item["semantic_rank"]
                current["semantic_distance"] = item["semantic_distance"]
            if item.get("exact_phrase_score"):
                current["exact_phrase_score"] = max(
                    float(current.get("exact_phrase_score") or 0.0),
                    float(item.get("exact_phrase_score") or 0.0),
                )
                current["exact_phrases"] = item.get("exact_phrases", current.get("exact_phrases", []))
            if item.get("topic_heading_score"):
                current["topic_heading_score"] = max(
                    float(current.get("topic_heading_score") or 0.0),
                    float(item.get("topic_heading_score") or 0.0),
                )
                current["topic_heading_phrases"] = item.get(
                    "topic_heading_phrases",
                    current.get("topic_heading_phrases", []),
                )
            if item.get("glossary_score"):
                current["glossary_score"] = max(
                    float(current.get("glossary_score") or 0.0),
                    float(item.get("glossary_score") or 0.0),
                )
                current["glossary_acronyms"] = item.get(
                    "glossary_acronyms",
                    current.get("glossary_acronyms", []),
                )

    reranked: List[Dict[str, Any]] = []
    for item in merged.values():
        meta = item["metadata"]

        rrf_score = reciprocal_rank(item.get("bm25_rank")) + reciprocal_rank(item.get("semantic_rank"))
        bonus = metadata_bonus(meta, intent, query)

        term = extract_core_term(query).lower()
        text_lower = (item.get("text") or "").lower()
        doc_type = (meta.get("doc_type") or "").lower()

        if intent == "advisory" and doc_type == "specs":
            bonus -= 8.0

        if intent == "definition" and term:
            term_pattern = rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])"

            if re.search(term_pattern, text_lower, re.IGNORECASE):
                bonus += 3.0

            if " " in term:
                normalized_text = " ".join(text_lower.split())
                normalized_term = " ".join(term.split())
                if normalized_term in normalized_text:
                    bonus += 2.0
            
            if looks_like_term_definition(item.get("text") or "", term):
                bonus += 6.0

        semantic_distance = item.get("semantic_distance")
        semantic_bonus = 0.0
        if semantic_distance is not None:
            semantic_bonus = max(0.0, 0.35 - semantic_distance * 0.1)

        exact_phrase_score = float(item.get("exact_phrase_score") or 0.0)
        exact_phrase_bonus = exact_phrase_score * 0.5

        topic_heading_score = float(item.get("topic_heading_score") or 0.0)
        topic_heading_bonus = topic_heading_score * 0.5

        glossary_score = float(item.get("glossary_score") or 0.0)
        if intent == "definition":
            glossary_bonus = glossary_score * 0.9
        elif intent == "comparison":
            glossary_bonus = glossary_score * 0.8
        else:
            glossary_bonus = glossary_score * 0.5

        query_acronyms = {
            acronym.upper()
            for acronym in extract_acronyms_for_glossary_lookup(query)
        }
        matched_glossary_acronyms = {
            acronym.upper()
            for acronym in item.get("glossary_acronyms", [])
        }

        if query_acronyms and matched_glossary_acronyms & query_acronyms:
            glossary_bonus += 8.0

            doc_name = (item["metadata"].get("doc_name") or "").lower()
            if "glossary" in doc_name:
                glossary_bonus += 6.0

        final_score = (
            rrf_score
            + bonus
            + semantic_bonus
            + exact_phrase_bonus
            + topic_heading_bonus
            + glossary_bonus
        )

        item["intent"] = intent
        item["score"] = final_score
        reranked.append(item)           

    reranked.sort(key=lambda x: x["score"], reverse=True)

    selected = []
    email_case_count = 0
    thread_analysis_count = 0
    has_official = False
    doc_name_counts = {}
    max_per_doc = 2
    seen_text_signatures = set()

    for item in reranked:
        meta = item["metadata"]
        source_type = (meta.get("source_type") or "").lower()
        doc_type = (meta.get("doc_type") or "").lower()
        doc_name = meta.get("doc_name") or ""

        if doc_name_counts.get(doc_name, 0) >= max_per_doc:
            continue

        signature = text_signature(item.get("text") or "")

        if signature in seen_text_signatures:
            continue

        is_official = doc_type in {"policies", "specs", "reference"} and source_type not in {"email_case", "email_thread_analysis", "email"}

        if source_type == "email_case":
            if email_case_count >= 2:
                continue
            email_case_count += 1

        elif source_type == "email_thread_analysis":
            if thread_analysis_count >= 1:
                continue
            thread_analysis_count += 1

        if is_official:
            has_official = True

        doc_name_counts[doc_name] = doc_name_counts.get(doc_name, 0) + 1

        seen_text_signatures.add(signature)

        selected.append(item)
        if len(selected) >= top_k:
            break

    if not has_official:
        for item in reranked:
            meta = item["metadata"]
            source_type = (meta.get("source_type") or "").lower()
            doc_type = (meta.get("doc_type") or "").lower()

            is_official = doc_type in {"policies", "specs", "reference"} and source_type not in {"email_case", "email_thread_analysis", "email"}

            if is_official and item["chunk_id"] not in {x["chunk_id"] for x in selected}:
                if len(selected) >= top_k:
                    selected[-1] = item
                else:
                    selected.append(item)
                break

    return selected[:top_k]

def find_exact_acronym_definition_chunks(
    query: str,
    chunks: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    term = extract_core_term(query).strip()
    if not is_acronym_term(term):
        return []

    hits = []
    seen = set()

    patterns = [
        re.compile(
            rf"([A-Za-z][A-Za-z0-9/&,\-]*(?: [A-Za-z][A-Za-z0-9/&,\-]*){{1,9}})\s*\(\s*{re.escape(term)}\s*\)",
            re.IGNORECASE,
        ),
        re.compile(
            rf"\b{re.escape(term)}\b\s*\(\s*([A-Za-z][A-Za-z0-9/&,\- ]{{3,100}}?)\s*\)",
            re.IGNORECASE,
        ),
    ]

    for chunk in chunks:
        text = chunk.get("text", "") or ""
        if term.lower() not in text.lower():
            continue

        matched = False
        for pat in patterns:
            for m in pat.finditer(text):
                candidate = " ".join(m.group(1).split()).strip(" ,;:-")
                words = re.findall(r"[A-Za-z]+", candidate)
                if len(words) < 2:
                    continue

                initials = "".join(w[0].upper() for w in words if w)
                if initials == term.upper():
                    matched = True
                    break

                tail_words = re.findall(r"[A-Za-z][A-Za-z0-9/&,\-]*", candidate)

                initials = "".join(w[0].upper() for w in words if w)
                if initials == term.upper():
                    matched = True
                    break

                if matched:
                    break
            if matched:
                break

        if matched and chunk["chunk_id"] not in seen:
            seen.add(chunk["chunk_id"])
            hits.append({
                "chunk_id": chunk["chunk_id"],
                "text": chunk["text"],
                "metadata": {
                    "program": chunk.get("program"),
                    "doc_type": chunk.get("doc_type"),
                    "doc_name": chunk.get("doc_name"),
                    "chunk_kind": chunk.get("chunk_kind"),
                    "priority": chunk.get("priority", 0),
                    "page_start": chunk.get("page_start"),
                    "page_end": chunk.get("page_end"),
                },
                "bm25_score": None,
                "bm25_rank": None,
                "semantic_distance": None,
                "semantic_rank": None,
                "score": 9.9,
            })

    return hits

def retrieve_email_cases(query: str, top_k: int = 30, program: Optional[str] = None) -> List[Dict[str, Any]]:
    domain_filter, clean_query = parse_domain_prefix(query)

    if program:
        domain_filter = program.lower()

    bm25, chunks = get_chunks_for_bm25()

    if domain_filter:
        filtered_chunks = [
            c for c in chunks
            if (c.get("program") or "").lower() == domain_filter
        ]
    else:
        filtered_chunks = chunks

    email_chunks = [
        c for c in filtered_chunks
        if (c.get("source_type") in {"email_case", "email_thread_analysis", "email"})
        or (c.get("doc_type") == "email")
    ]

    if not email_chunks:
        return []

    email_bm25 = build_bm25(email_chunks)
    results = search_bm25(clean_query, email_chunks, email_bm25, top_k=top_k)

    selected = []
    seen_ids = set()
    seen_signatures = set()

    for item in results:
        chunk_id = item["chunk_id"]

        if chunk_id in seen_ids:
            continue

        signature = text_signature(item.get("text") or "")
        if signature in seen_signatures:
            continue

        item["score"] = float(item.get("bm25_score") or 0.0)

        selected.append(item)
        seen_ids.add(chunk_id)
        seen_signatures.add(signature)

        if len(selected) >= top_k:
            break

    return selected

def retrieve(query: str, top_k: int = DEFAULT_TOP_K, program: Optional[str] = None) -> List[Dict[str, Any]]:
    domain_filter, clean_query = parse_domain_prefix(query)

    if program:
        domain_filter = program.lower()

    retrieval_query = expand_advisory_query(clean_query)

    bm25, chunks = get_chunks_for_bm25()

    bm25_results = search_bm25(clean_query, chunks, bm25, top_k=BM25_RETRIEVAL_K)
    semantic_results = search_semantic(clean_query, chunks, top_k=SEMANTIC_RETRIEVAL_K)

    if retrieval_query != clean_query:
        bm25_results += search_bm25(retrieval_query, chunks, bm25, top_k=BM25_RETRIEVAL_K)
        semantic_results += search_semantic(retrieval_query, chunks, top_k=SEMANTIC_RETRIEVAL_K)

    if domain_filter:
        bm25_results = [
            item for item in bm25_results
            if (item["metadata"].get("program") or "").lower() == domain_filter
        ]
        semantic_results = [
            item for item in semantic_results
            if (item["metadata"].get("program") or "").lower() == domain_filter
        ]
        filtered_chunks = [
            c for c in chunks
            if (c.get("program") or "").lower() == domain_filter
        ]
    else:
        filtered_chunks = chunks

    exact_results = search_exact_phrases(retrieval_query, filtered_chunks, top_k=10)

    topic_heading_results = search_topic_headings(retrieval_query, filtered_chunks, top_k=10)

    glossary_results = search_glossary_acronyms(retrieval_query, filtered_chunks, top_k=10)

    # Force an email-case lane for advisory/process questions
    email_chunks = [
        c for c in filtered_chunks
        if (c.get("source_type") == "email_case") or (c.get("doc_type") == "email")
    ]

    email_results = []
    if email_chunks and detect_intent(clean_query) in {"advisory", "process"}:
        email_bm25 = build_bm25(email_chunks)
        email_results = search_bm25(retrieval_query, email_chunks, email_bm25, top_k=10)

    combined_bm25 = exact_results + topic_heading_results + glossary_results + bm25_results + email_results

    return merge_and_rerank(clean_query, combined_bm25, semantic_results, top_k=top_k)

def format_context(items: List[Dict[str, Any]], max_chars: Optional[int] = None) -> str:
    parts: List[str] = []
    total = 0

    for item in items:
        meta = item["metadata"]
        header = (
            f"chunk_id: {item['chunk_id']}\n"
            f"program: {meta.get('program')}\n"
            f"type: {meta.get('doc_type')}\n"
            f"document: {meta.get('doc_name')}\n"
            f"pages: {meta.get('page_start')}-{meta.get('page_end')}\n"
            f"citation: {format_citation(meta)}\n"
        )
        block = header + "\n" + item["text"].strip()

        if max_chars is not None:
            remaining = max_chars - total
            if remaining <= 0:
                break
            if len(block) > remaining:
                block = block[:remaining]

        parts.append(block)
        total += len(block)

        if max_chars is not None and total >= max_chars:
            break

    return "\n\n---\n\n".join(parts)


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Hybrid retrieval debug tool")
    parser.add_argument("--top-k", type=int, default=DEFAULT_TOP_K)
    parser.add_argument("--program", choices=["bluetooth", "matter", "aliro"], default=None)
    parser.add_argument("query", nargs="+", help="Query text")
    return parser.parse_args(argv)


def main() -> None:
    args = parse_args(sys.argv[1:])
    query = " ".join(args.query).strip()
    if not query:
        print("Usage: python -m app.retrieve <your question>")
        sys.exit(1)

    domain_filter, clean_query = parse_domain_prefix(query)
    if args.program:
        domain_filter = args.program

    results = retrieve(query, top_k=args.top_k, program=args.program)

    print(f"\nQuery: {query}")
    print(f"Intent: {detect_intent(clean_query)}")
    print(f"\nTop {len(results)} results:\n")

    for rank, item in enumerate(results, start=1):
        meta = item["metadata"]
        print(
            f"[{rank}] score={item['score']:.4f}  {format_citation(meta)}  "
            f"id={item['chunk_id']}  priority={meta.get('priority', 0)}  "
            f"kind={meta.get('chunk_kind')}"
        )
        preview = item["text"].replace("\n", " ")
        print(f"    {preview[:180]}...\n")


if __name__ == "__main__":
    main()