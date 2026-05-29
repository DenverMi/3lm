import argparse
import json
import mailbox
import re
from collections import defaultdict
from email import policy
from email.header import decode_header
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
from pathlib import Path

from app.redact_email import redact_text


def decode_mime_header(value: str) -> str:
    if not value:
        return ""

    parts = []
    for text, enc in decode_header(value):
        if isinstance(text, bytes):
            charset = enc or "utf-8"
            try:
                parts.append(text.decode(charset, errors="ignore"))
            except LookupError:
                parts.append(text.decode("utf-8", errors="ignore"))
        else:
            parts.append(text)

    return "".join(parts).strip()


def clean_html(html: str) -> str:
    html = re.sub(r"(?is)<(script|style).*?>.*?</\1>", " ", html)
    html = re.sub(r"(?i)<br\s*/?>", "\n", html)
    html = re.sub(r"(?i)</p\s*>", "\n", html)
    html = re.sub(r"(?i)</div\s*>", "\n", html)
    html = re.sub(r"(?i)</li\s*>", "\n", html)
    html = re.sub(r"(?i)<li\s*>", "- ", html)
    html = re.sub(r"<[^>]+>", " ", html)
    html = html.replace("&nbsp;", " ")
    html = html.replace("&lt;", "<")
    html = html.replace("&gt;", ">")
    html = html.replace("&amp;", "&")
    html = re.sub(r"\r\n?", "\n", html)
    html = re.sub(r"[ \t]+", " ", html)
    html = re.sub(r"\n{3,}", "\n\n", html)
    return html.strip()


def clean_thread_body(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Remove embedded forwarded/reply headers now stored in JSON fields
    header_patterns = [
        r"(?im)^from:\s.*$",
        r"(?im)^sent:\s.*$",
        r"(?im)^to:\s.*$",
        r"(?im)^cc:\s.*$",
        r"(?im)^subject:\s.*$",
        r"(?im)^差出人:\s.*$",
        r"(?im)^送信日時:\s.*$",
        r"(?im)^宛先:\s.*$",
        r"(?im)^件名:\s.*$",
    ]
    for pattern in header_patterns:
        text = re.sub(pattern, "", text)

    # Remove common signature/footer junk, but keep real content
    footer_start_patterns = [
        r"(?im)^= = = = =.*$",
        r"(?im)^\*{5,}.*$",
        r"(?im)^-{10,}.*$",
        r"(?im)^e-mail:\s*\[EMAIL\].*$",
        r"(?im)^mail:\s*\[EMAIL\].*$",
        r"(?im)^tel[:：].*$",
        r"(?im)^mobile[:：].*$",
        r"(?im)^〒\[ID\].*$",
    ]
    for pattern in footer_start_patterns:
        text = re.sub(pattern, "", text)

    # Remove standalone contact/org lines that repeat constantly
    noisy_lines = [
        r"株式会社ソアー",
        r"アリオン株式会社",
        r"事業統括本部",
        r"技術開発本部",
        r"ビジネスソリューション事業部",
        r"営業統括部",
        r"EMS/ODM開発部",
        r"技術二課",
        r"\[ID\]",
        r"\[EMAIL\]",
    ]

    cleaned_lines = []
    for line in text.splitlines():
        stripped = line.strip()

        if not stripped:
            cleaned_lines.append("")
            continue

        if any(re.fullmatch(pattern, stripped) for pattern in noisy_lines):
            continue

        cleaned_lines.append(stripped)

    text = "\n".join(cleaned_lines)

    # Normalize excessive blank lines
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def clean_body_text(text: str, cut_quotes: bool = True) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    bad_patterns = [
        r"(?is)this e-mail.*?confidential.*",
        r"(?is)the information contained in this email.*",
        r"(?is)このメール.*?機密.*",
        r"(?is)本メール.*?無断.*",
        r"(?im)^[-_]{5,}$",
    ]

    for pattern in bad_patterns:
        text = re.sub(pattern, "", text)

    if cut_quotes:
        split_markers = [
            r"(?im)^from:\s.*$",
            r"(?im)^sent:\s.*$",
            r"(?im)^subject:\s.*$",
            r"(?im)^on .* wrote:$",
            r"(?im)^-----original message-----$",
            r"(?im)^差出人:\s.*$",
            r"(?im)^送信日時:\s.*$",
            r"(?im)^件名:\s.*$",
            r"(?im)^宛先:\s.*$",
            r"(?im)^.*wrote:\s*$",
        ]

        cut_positions = []
        for marker in split_markers:
            m = re.search(marker, text)
            if m:
                cut_positions.append(m.start())

        if cut_positions:
            text = text[: min(cut_positions)]

    text = re.sub(r"(?m)^\s*>+\s?", "", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def decode_payload(payload: bytes, charset: str | None) -> str:
    candidates = [charset, "utf-8", "cp932", "iso-2022-jp", "shift_jis", "latin-1"]

    for enc in candidates:
        if not enc:
            continue
        try:
            return payload.decode(enc, errors="ignore")
        except LookupError:
            continue

    return payload.decode("utf-8", errors="ignore")


def get_body(msg, cut_quotes: bool = True) -> str:
    text_parts = []
    html_parts = []

    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            disposition = str(part.get("Content-Disposition") or "").lower()

            if "attachment" in disposition:
                continue

            payload = part.get_payload(decode=True)
            if not payload:
                continue

            decoded = decode_payload(payload, part.get_content_charset())

            if content_type == "text/plain":
                text_parts.append(decoded)
            elif content_type == "text/html":
                html_parts.append(decoded)
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            decoded = decode_payload(payload, msg.get_content_charset())

            if msg.get_content_type() == "text/plain":
                text_parts.append(decoded)
            elif msg.get_content_type() == "text/html":
                html_parts.append(decoded)

    if text_parts:
        return clean_body_text("\n".join(text_parts), cut_quotes=cut_quotes)

    if html_parts:
        return clean_body_text(clean_html("\n".join(html_parts)), cut_quotes=cut_quotes)

    return ""


def get_thread_key(msg) -> str:
    thread_index = (msg.get("Thread-Index") or "").strip()
    if thread_index:
        return f"thread-index:{thread_index[:22]}"

    references = (msg.get("References") or "").strip()
    if references:
        first_ref = references.split()[0]
        return f"ref:{first_ref}"

    in_reply_to = (msg.get("In-Reply-To") or "").strip()
    if in_reply_to:
        return f"reply:{in_reply_to}"

    subject = decode_mime_header(msg.get("Subject") or "")
    subject = re.sub(r"^(re|fw|fwd)\s*:\s*", "", subject, flags=re.IGNORECASE)
    subject = re.sub(r"\s+", " ", subject).strip().lower()

    return f"subject:{subject}"


def load_messages(input_path: Path):
    if input_path.is_file() and input_path.suffix.lower() == ".mbox":
        mbox = mailbox.mbox(str(input_path))
        for msg in mbox:
            yield msg
        return

    if input_path.is_file() and input_path.suffix.lower() == ".eml":
        with input_path.open("rb") as f:
            yield BytesParser(policy=policy.default).parse(f)
        return

    if input_path.is_dir():
        for eml_path in sorted(input_path.rglob("*.eml")):
            with eml_path.open("rb") as f:
                yield BytesParser(policy=policy.default).parse(f)
        return

    raise ValueError(f"Unsupported input path: {input_path}")


def should_cut_quotes(input_path: Path) -> bool:
    return input_path.is_file() and input_path.suffix.lower() == ".mbox"


def should_split_inline(input_path: Path) -> bool:
    return input_path.is_file() and input_path.suffix.lower() == ".eml"


def split_inline_email_chain(body: str):
    header_pattern = re.compile(r"(?im)^(差出人:|From:)\s+.+$")

    matches = list(header_pattern.finditer(body))

    if not matches:
        return [body]

    parts = []

    first_body = body[: matches[0].start()].strip()
    if first_body:
        parts.append(first_body)

    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        part = body[start:end].strip()

        if part:
            parts.append(part)

    return parts


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract email threads from .mbox or .eml files."
    )
    parser.add_argument(
        "input",
        help="Path to .mbox file, .eml file, or folder containing .eml files",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="Optional output folder for extracted thread JSON files",
    )
    args = parser.parse_args()

    input_path = Path(args.input)

    if args.output:
        out_dir = Path(args.output)
    else:
        out_dir = input_path.parent if input_path.is_file() else input_path

    out_dir.mkdir(parents=True, exist_ok=True)

    threads = defaultdict(list)

    total = 0
    kept = 0

    cut_quotes = should_cut_quotes(input_path)
    split_inline = should_split_inline(input_path)

    for msg in load_messages(input_path):
        total += 1

        subject = decode_mime_header(msg.get("Subject") or "")
        body = get_body(msg, cut_quotes=cut_quotes)
        body = redact_text(body)

        if not body:
            continue

        date_raw = msg.get("Date")
        try:
            dt = parsedate_to_datetime(date_raw) if date_raw else None
            date_iso = dt.isoformat() if dt else ""
        except Exception:
            date_iso = ""

        thread_key = get_thread_key(msg)

        attachments = []
        if msg.is_multipart():
            for part in msg.walk():
                filename = part.get_filename()
                if filename:
                    clean_name = redact_text(filename)

                    # Ignore useless inline images for RAG
                    if clean_name.lower().startswith("image"):
                        continue

                    attachments.append(clean_name)

        body_parts = split_inline_email_chain(body) if split_inline else [body]

        for part_index, part_body in enumerate(body_parts, start=1):
            part_body = clean_thread_body(part_body)

            if not part_body:
                continue

            threads[thread_key].append(
                {
                    "message_id": (msg.get("Message-ID") or "").strip(),
                    "part_index": part_index,
                    "subject": redact_text(subject),
                    "from": redact_text(msg.get("From") or ""),
                    "to": redact_text(msg.get("To") or ""),
                    "cc": redact_text(msg.get("Cc") or ""),
                    "date": date_iso,
                    "attachments": attachments if part_index == 1 else [],
                    "body": part_body,
                }
            )
            kept += 1

    for i, (_, messages) in enumerate(threads.items(), start=1):
        messages.sort(key=lambda x: x.get("date") or "")

        out = {
            "thread_id": f"thread_{i:04d}",
            "subject": messages[0]["subject"] if messages else "",
            "message_count": len(messages),
            "messages": messages,
        }

        out_path = out_dir / f"thread_{i:04d}.json"
        out_path.write_text(
            json.dumps(out, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    print(f"Read {total} messages")
    print(f"Kept {kept} messages with readable body")
    print(f"Saved {len(threads)} threads to {out_dir}")


if __name__ == "__main__":
    main()