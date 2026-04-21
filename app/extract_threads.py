import json
import mailbox
import re
from collections import defaultdict
from email.utils import parsedate_to_datetime
from pathlib import Path
from email.header import decode_header

from app.redact_email import redact_text

MBOX_PATH = Path("data/bluetooth/email/bqc.mbox")
OUT_DIR = Path("data/bluetooth/email_threads")

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
    html = re.sub(r"&nbsp;", " ", html)
    html = re.sub(r"&lt;", "<", html)
    html = re.sub(r"&gt;", ">", html)
    html = re.sub(r"&amp;", "&", html)
    html = re.sub(r"\r\n?", "\n", html)
    html = re.sub(r"[ \t]+", " ", html)
    html = re.sub(r"\n{3,}", "\n\n", html)
    return html.strip()


def clean_body_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Drop common confidentiality junk and long separators
    bad_patterns = [
        r"(?is)this e-mail.*?confidential.*",
        r"(?is)the information contained in this email.*",
        r"(?is)このメール.*?機密.*",
        r"(?is)本メール.*?無断.*",
        r"(?im)^[-_]{5,}$",
    ]
    for pattern in bad_patterns:
        text = re.sub(pattern, "", text)

    # Cut quoted reply chains
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

    # Remove leading quote markers
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


def get_body(msg) -> str:
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
        return clean_body_text("\n".join(text_parts))
    if html_parts:
        return clean_body_text(clean_html("\n".join(html_parts)))
    return ""


def get_thread_key(msg) -> str:
    # Best available threading signals first
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


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    mbox = mailbox.mbox(str(MBOX_PATH))
    threads = defaultdict(list)

    total = 0
    kept = 0

    for msg in mbox:
        total += 1

        subject = decode_mime_header(msg.get("Subject") or "")
        body = get_body(msg)
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
                    attachments.append(redact_text(filename))

        threads[thread_key].append(
            {
                "message_id": (msg.get("Message-ID") or "").strip(),
                "subject": redact_text(subject),
                "from": redact_text(msg.get("From") or ""),
                "to": redact_text(msg.get("To") or ""),
                "cc": redact_text(msg.get("Cc") or ""),
                "date": date_iso,
                "attachments": attachments,
                "body": body,
            }
        )
        kept += 1

    for i, (_, messages) in enumerate(threads.items(), start=1):
        messages.sort(key=lambda x: x["date"] or "")
        out = {
            "thread_id": f"thread_{i:04d}",
            "subject": messages[0]["subject"] if messages else "",
            "message_count": len(messages),
            "messages": messages,
        }
        out_path = OUT_DIR / f"thread_{i:04d}.json"
        out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Read {total} messages")
    print(f"Kept {kept} messages with readable body")
    print(f"Saved {len(threads)} threads to {OUT_DIR}")


if __name__ == "__main__":
    main()