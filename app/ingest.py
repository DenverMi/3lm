import json
import re
from pathlib import Path

from pypdf import PdfReader

from app.config import DATA_DIR, PAGES_PATH, SUPPORTED_EXTENSIONS, ensure_directories

VALID_DOC_TYPES = {
    "email",
    "specs",
    "policies",
    "guides",
    "explanations",
    "faq",
    "glossary",
    "reports",
    "memory",
    "reference",  # temporary backward compatibility while we migrate folders
}


def normalize_text(text: str) -> str:
    text = text.replace("\\(", "(").replace("\\)", ")")
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def normalize_markdown_text(text: str) -> str:
    text = text.replace("\\(", "(").replace("\\)", ")")
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def extract_pdf(path: Path):
    reader = PdfReader(path)
    pages = []

    for i, page in enumerate(reader.pages, start=1):
        text = normalize_text(page.extract_text() or "")
        if not text:
            continue

        pages.append({
            "page": i,
            "text": text,
        })

    return pages

def extract_markdown(path: Path):
    raw = path.read_text(encoding="utf-8")

    pages = []

    # 1. Extract heading-based sections
    doc_type = path.parent.name
    
    if doc_type in {"reference", "policies"}:
        text = normalize_markdown_text(raw)
    else:
        text = normalize_text(raw)
    if text:
        sections = re.split(r"\n(?=#{1,6}\s+)", text)

        for i, section in enumerate(sections, start=1):
            section = section.strip()
            if not section:
                continue

            pages.append({
                "page": i,
                "text": section,
            })

    # 2. Extract ONLY glossary / definition-style Markdown table rows
    raw_lines = raw.splitlines()
    table_record_index = 100000

    for idx, line in enumerate(raw_lines):
        stripped = line.strip()

        if not stripped.startswith("|"):
            continue

        # skip separator rows
        if re.fullmatch(r"[:\-\s|]+", stripped):
            continue

        cells = [c.strip() for c in stripped.split("|") if c.strip()]
        if len(cells) < 2:
            continue

        term = cells[0]
        definition = " ".join(cells[1:])

        term_l = term.lower()
        definition_l = definition.lower()

        # Reject common non-glossary technical table rows
        bad_term_markers = [
            "tag",
            "length",
            "octet",
            "field",
            "value",
            "condition",
            "index",
            "step",
            "test",
            "status",
            "command",
            "response",
            "bit",
            "byte",
            "id",
            "identifier",
            "parameter",
            "feature",
            "cluster",
            "attribute",
            "event",
            "enum",
            "opcode",
            "type",
        ]

        if term_l in bad_term_markers:
            continue

        if any(term_l.startswith(marker + " ") for marker in bad_term_markers):
            continue

        # Glossary terms are usually short human terms, not long table descriptions
        if len(term.split()) > 5:
            continue

        # Definition should be prose-like, not mostly symbols/numbers
        if len(definition.split()) < 4:
            continue

        alpha_chars = sum(ch.isalpha() for ch in definition)
        if alpha_chars < 20:
            continue

        # Strong generic definition signals, not domain-specific cheat words
        definition_signals = [
            " means ",
            " refers to ",
            " defined as ",
            " used to ",
            " used for ",
            " contains ",
            " containing ",
        ]

        if not any(sig in f" {definition_l} " for sig in definition_signals):
            continue

        continuation_lines = []
        j = idx + 1

        while j < len(raw_lines):
            nxt = raw_lines[j].strip()

            if not nxt:
                j += 1
                continue

            if nxt.startswith("#"):
                break

            if nxt.startswith("|"):
                break

            if nxt.startswith("![]"):
                break

            # stop if continuation looks like a new numbered/list/table-ish item
            if re.match(r"^(\d+[\.\)]|[-*]\s+)", nxt):
                break

            continuation_lines.append(nxt)
            j += 1

            if len(" ".join(continuation_lines)) > 300:
                break

        continuation = " ".join(continuation_lines)

        row_text = f"{term}: {definition}"
        if continuation:
            row_text += f" {continuation}"

        row_text = row_text.replace("<br>", " ")
        row_text = normalize_text(row_text)

        if not row_text:
            continue

        pages.append({
            "page": table_record_index,
            "text": row_text,
        })
        table_record_index += 1

    return pages

def extract_text_file(path: Path):
    text = path.read_text(encoding="utf-8")
    text = normalize_text(text)

    if not text:
        return []

    return [{
        "page": 1,
        "text": text,
    }]

def extract_json_file(path: Path):
    raw = path.read_text(encoding="utf-8")
    data = json.loads(raw)

    pages = []

    # Case 1: already a list of records
    if isinstance(data, list):
        for i, item in enumerate(data, start=1):
            if isinstance(item, dict):
                text_parts = []

                for key in ["title", "heading", "section", "question", "answer", "content", "text", "body"]:
                    value = item.get(key)
                    if value:
                        text_parts.append(f"{key}: {value}")

                text = normalize_text("\n".join(text_parts))
                if text:
                    pages.append({
                        "page": i,
                        "text": text,
                    })

        return pages

    # Case 2: single JSON object
    if isinstance(data, dict):
        text_parts = []

        for key in ["title", "heading", "section", "question", "answer", "content", "text", "body"]:
            value = data.get(key)
            if value:
                text_parts.append(f"{key}: {value}")

        # fallback: stringify whole object if known fields are missing
        if not text_parts:
            text_parts.append(json.dumps(data, ensure_ascii=False, indent=2))

        text = normalize_text("\n".join(text_parts))
        if text:
            return [{
                "page": 1,
                "text": text,
            }]

    return []

def extract_file(path: Path):
    suffix = path.suffix.lower()

    if suffix == ".pdf":
        return extract_pdf(path)
    if suffix == ".md":
        return extract_markdown(path)
    if suffix == ".txt":
        return extract_text_file(path)
    if suffix == ".json":
        return extract_json_file(path)

    return []

def walk_documents():
    """
    Expected structure:
    data/
      <program>/
        specs/          # normative technical specifications
        policies/       # certification/compliance rules
        guides/         # step-by-step tool/process guides
        explanations/   # conceptual/how-it-works material
        faq/            # quick Q&A reference material
        glossary/       # terms and acronyms
        email/          # case files and thread analysis
        reports/        # generated analysis/report outputs
        memory/         # curated project memory and decisions
        reference/      # temporary legacy folder during migration
    """
    all_records = []

    for program_dir in DATA_DIR.iterdir():
        if not program_dir.is_dir():
            continue

        program = program_dir.name

        for doc_type_dir in program_dir.iterdir():
            if not doc_type_dir.is_dir():
                continue

            doc_type = doc_type_dir.name
            if doc_type not in VALID_DOC_TYPES:
                print(f"Skipping unknown doc type: {program}/{doc_type}")
                continue

            for file_path in doc_type_dir.rglob("*"):
                if not file_path.is_file():
                    continue
                if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
                    continue

                print(f"Processing: {program}/{doc_type}/{file_path.name}")
                pages = extract_file(file_path)

                for p in pages:
                    all_records.append({
                        "program": program,
                        "domain": program.lower(),
                        "doc_type": doc_type,
                        "source_type": "email_case" if doc_type == "email" else doc_type,
                        "doc_name": file_path.name,
                        "page": p["page"],
                        "text": p["text"],
                    })

    return all_records


def write_pages(records):
    ensure_directories()

    with PAGES_PATH.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"✅ Wrote {len(records)} pages to {PAGES_PATH}")


def main():
    records = walk_documents()

    if not records:
        print("No documents found.")
        return

    write_pages(records)


if __name__ == "__main__":
    main()