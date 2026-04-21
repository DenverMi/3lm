import json
import re
from pathlib import Path

from pypdf import PdfReader

from app.config import DATA_DIR, PAGES_PATH, SUPPORTED_EXTENSIONS, ensure_directories

VALID_DOC_TYPES = {"email", "specs", "policies", "reports", "reference"}


def normalize_text(text: str) -> str:
    text = text.replace("\\(", "(").replace("\\)", ")")
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)
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
    text = path.read_text(encoding="utf-8")
    text = normalize_text(text)

    if not text:
        return []

    return [{
        "page": 1,
        "text": text,
    }]


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
    text = path.read_text(encoding="utf-8")
    text = normalize_text(text)

    if not text:
        return []

    return [{
        "page": 1,
        "text": text,
    }]

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
      aliro/
        email/
        policies/
        reference/
        reports/
        specs/
      wifi/
      hdmi/
      matter/
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

            for file_path in doc_type_dir.iterdir():
                if not file_path.is_file():
                    continue
                if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
                    continue

                print(f"Processing: {program}/{doc_type}/{file_path.name}")
                pages = extract_file(file_path)

                for p in pages:
                    all_records.append({
                        "program": program,
                        "doc_type": doc_type,
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