import argparse
import json
import re
from datetime import datetime
from pathlib import Path


HEADER_PATTERNS = [
    r"(?im)^from\s*:\s.*$",
    r"(?im)^sent\s*:\s.*$",
    r"(?im)^to\s*:\s.*$",
    r"(?im)^cc\s*:\s.*$",
    r"(?im)^subject\s*:\s.*$",
    r"(?im)^差出人\s*[:：]\s.*$",
    r"(?im)^送信日時\s*[:：]\s.*$",
    r"(?im)^宛先\s*[:：]\s.*$",
    r"(?im)^件名\s*[:：]\s.*$",
]

QUOTE_START_PATTERNS = [
    r"(?im)^from\s*:\s.*$",
    r"(?im)^差出人\s*[:：]\s.*$",
    r"(?im)^-----original message-----$",
    r"(?im)^.*wrote\s*:\s*$",
]

SIGNATURE_START_PATTERNS = [
    r"(?im)^↓\s*20\d{2}/\d{1,2}/\d{1,2}.*所属部署名.*$",
    r"(?im)^\*{5,}.*$",
    r"(?im)^\*?\+?\*?\+?\*?\+?\*?\+?\*?\+.*$",
    r"(?im)^= = = =.*$",
    r"(?im)^アリオン株式会社\s*$",
    r"(?im)^株式会社シマノ\s*$",
    r"(?im)^〒\s*\[ID\].*$",
    r"(?im)^tel\s*[：:].*$",
    r"(?im)^mobile\s*[：:].*$",
    r"(?im)^e-?mail\s*[：:].*$",
    r"(?im)^email\s*$",
    r"(?im)^\[EMAIL\]\s*$",
]


def display_name(value: str) -> str:
    if not value:
        return ""

    value = re.sub(r"<[^>]+>", "", value)
    value = value.replace("[EMAIL]", "")
    value = re.sub(r"\s+", " ", value)
    value = value.strip(" ,;")

    return value.strip()


def format_date(value: str) -> str:
    if not value:
        return "日付不明"

    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d %H:%M")
    except Exception:
        return value


def cut_quoted_chain(text: str) -> str:
    cut_positions = []

    for pattern in QUOTE_START_PATTERNS:
        match = re.search(pattern, text)
        if match:
            cut_positions.append(match.start())

    if cut_positions:
        text = text[: min(cut_positions)]

    return text


def cut_signature(text: str) -> str:
    cut_positions = []

    for pattern in SIGNATURE_START_PATTERNS:
        match = re.search(pattern, text)
        if match:
            cut_positions.append(match.start())

    if cut_positions:
        text = text[: min(cut_positions)]

    return text


def remove_header_lines(text: str) -> str:
    for pattern in HEADER_PATTERNS:
        text = re.sub(pattern, "", text)

    return text


def normalize_japanese_spacing(text: str) -> str:
    # Remove spaces inserted between Japanese characters.
    text = re.sub(
        r"(?<=[\u3040-\u30ff\u3400-\u9fff])\s+(?=[\u3040-\u30ff\u3400-\u9fff])",
        "",
        text,
    )

    # Clean spaces before Japanese punctuation.
    text = re.sub(r"\s+([。、，．！？：；）】』」])", r"\1", text)

    # Clean spaces after opening Japanese brackets.
    text = re.sub(r"([（【『「])\s+", r"\1", text)

    # Normalize English/number spacing but do not destroy technical terms.
    text = re.sub(r"[ \t]+", " ", text)

    return text


def clean_body_for_reading(body: str) -> str:
    text = body or ""

    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # For mbox-extracted messages, keep only the actual message, not the whole quoted history.
    text = cut_quoted_chain(text)

    # Remove duplicated email transport headers.
    text = remove_header_lines(text)

    # Remove signature/footer blocks.
    text = cut_signature(text)

    lines = []
    for line in text.splitlines():
        line = line.strip()

        if not line:
            lines.append("")
            continue

        # Drop useless redaction-only/contact-only lines.
        if line in {"[EMAIL]", "[ID]", "[URL]"}:
            continue

        if re.fullmatch(r"[\*\+\-=＿ー\s]{5,}", line):
            continue

        if re.fullmatch(r"(TEL|Tel|Mobile|Mail|Email|e-mail)\s*[：:]?.*", line, flags=re.I):
            continue

        lines.append(line)

    text = "\n".join(lines)
    text = normalize_japanese_spacing(text)

    # Collapse excessive blank lines.
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()

def scrub_final_markdown(md: str) -> str:
    """
    Final cleanup for generated readable Markdown.
    Removes CC blocks and all [EMAIL] placeholder text.
    """
    cc_start_re = re.compile(r"^\s*(?:Cc|CC|ＣＣ)\s*[:：]", re.IGNORECASE)

    next_header_re = re.compile(
        r"^\s*(?:"
        r"From\s*:|"
        r"Sent\s*:|"
        r"To\s*:|"
        r"Subject\s*:|"
        r"差出人\s*[:：]|"
        r"送信日時\s*[:：]|"
        r"宛先\s*[:：]|"
        r"件名\s*[:：]|"
        r"---$|"
        r"##\s+"
        r")",
        re.IGNORECASE,
    )

    cleaned_lines = []
    skipping_cc = False

    for raw_line in md.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()

        if cc_start_re.match(stripped):
            skipping_cc = True
            continue

        if skipping_cc:
            if next_header_re.match(stripped):
                skipping_cc = False
            elif stripped == "":
                skipping_cc = False
                cleaned_lines.append("")
                continue
            else:
                continue

        line = re.sub(r"<\s*\[\s*EMAIL\s*\]\s*>", "", line, flags=re.IGNORECASE)
        line = re.sub(r"\[\s*EMAIL\s*\]", "", line, flags=re.IGNORECASE)
        line = re.sub(r"<\s*>", "", line)

        line = re.sub(r"\s{2,}", " ", line).rstrip()
        stripped = line.strip()

        if stripped in {"<>", "< >", ";", "；", ","}:
            continue

        if re.match(r"^\s*(?:Cc|CC|ＣＣ)\s*[:：]", stripped, re.IGNORECASE):
            continue

        cleaned_lines.append(line)

    md = "\n".join(cleaned_lines)
    md = re.sub(r"\n{3,}", "\n\n", md)

    return md.strip() + "\n"

def json_to_markdown(json_path: Path, output_path: Path | None = None) -> Path:
    data = json.loads(json_path.read_text(encoding="utf-8"))

    thread_id = data.get("thread_id", json_path.stem)
    subject = data.get("subject", "")
    messages = data.get("messages", [])

    if output_path is None:
        output_path = json_path.with_suffix(".readable.md")

    parts = []
    parts.append(f"# {thread_id}: {subject}".strip())
    parts.append("")
    parts.append(f"- Message count: {len(messages)}")
    parts.append(f"- Source JSON: `{json_path.name}`")
    parts.append("")

    for index, msg in enumerate(messages, start=1):
        date = format_date(msg.get("date", ""))
        sender = display_name(msg.get("from", ""))
        recipient = display_name(msg.get("to", ""))

        body = clean_body_for_reading(msg.get("body", ""))

        if not body:
            continue

        parts.append("---")
        parts.append("")
        parts.append(f"## {index}. {date}")
        parts.append("")
        if sender:
            parts.append(f"**From:** {sender}")
        if recipient:
            parts.append(f"**To:** {recipient}")

        attachments = [
            a for a in msg.get("attachments", [])
            if not a.lower().startswith("image")
        ]
        if attachments:
            parts.append(f"**Attachments:** {', '.join(attachments)}")

        parts.append("")
        parts.append(body)
        parts.append("")

    md = "\n".join(parts).strip() + "\n"
    md = scrub_final_markdown(md)

    output_path.write_text(md, encoding="utf-8")
    return output_path


def iter_json_files(input_path: Path):
    if input_path.is_file() and input_path.suffix.lower() == ".json":
        yield input_path
        return

    if input_path.is_dir():
        for path in sorted(input_path.glob("thread_*.json")):
            yield path
        return

    raise ValueError(f"Unsupported input path: {input_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert extracted email thread JSON files into readable Japanese Markdown reference files."
    )
    parser.add_argument(
        "input",
        help="Path to one thread_XXXX.json file or a folder containing thread JSON files",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="Optional output folder. If omitted, saves beside each JSON file.",
    )

    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output) if args.output else None

    written = []

    for json_path in iter_json_files(input_path):
        if output_dir:
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = output_dir / json_path.with_suffix(".readable.md").name
        else:
            output_path = None

        written_path = json_to_markdown(json_path, output_path)
        written.append(written_path)

    print(f"Wrote {len(written)} readable Markdown files")
    for path in written:
        print(path)


if __name__ == "__main__":
    main()