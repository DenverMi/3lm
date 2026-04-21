import re


EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
URL_RE = re.compile(r"https?://\S+|www\.\S+")
ID_RE = re.compile(r"\b[A-Z0-9][A-Z0-9._-]{5,}\b")


def redact_text(text: str) -> str:
    text = EMAIL_RE.sub("[EMAIL]", text)
    text = URL_RE.sub("[URL]", text)
    text = ID_RE.sub("[ID]", text)
    return text