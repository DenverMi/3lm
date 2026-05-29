from pathlib import Path
import argparse
import re


def clean_line(line: str) -> str:
    line = line.rstrip()

    # Remove Markdown image links, including base64 image blobs
    line = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", line)

    # Remove common Pandoc / HTML attribute blocks
    line = re.sub(r"\s*\{#[^}]+\}", "", line)
    line = re.sub(r"\s*\{\.[^}]+\}", "", line)
    line = re.sub(r"\s*\{[^}]*class=[^}]*\}", "", line)
    line = re.sub(r"\s*\{[^}]*target=[^}]*\}", "", line)
    line = re.sub(r"\s*\{[^}]*rel=[^}]*\}", "", line)
    line = re.sub(r"\s*\{[^}]*style=[^}]*\}", "", line)

    # Keep visible text from Markdown links
    line = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)

    # Clean citation links like [[[4]](#id3930)] -> [4]
    line = re.sub(r"\[\[\[([0-9]+)\]\]\(#?[A-Za-z0-9_.-]+\)\]", r"[\1]", line)
    line = re.sub(r"\[\[([0-9]+)\]\]", r"[\1]", line)

    # Remove common leftover class fragments
    leftovers = [
        "{.xref",
        ".linktype-component}",
        "{.link",
        "{.citation}",
        "{.bold}",
        "{.emphasis}",
    ]
    for token in leftovers:
        line = line.replace(token, "")

    # Remove Pandoc div/literal markers but preserve line content
    line = line.replace("::: literallayout", "")
    line = line.replace(":::", "")

    # Normalize common artifacts
    line = line.replace("Bluetooth[*^®^*]", "Bluetooth®")
    line = line.replace("Bluetooth^®^", "Bluetooth®")

    # Fix headings like ### [1.1][.] [Definitions]
    line = re.sub(r"^(#{1,6})\s+\[([^\]]+)\]\[\.\]\s+\[([^\]]+)\]", r"\1 \2. \3", line)
    line = re.sub(r"^(#{1,6})\s+\[\*?([^\]]+?)\*?\]", r"\1 \2", line)

    # Normalize whitespace
    line = re.sub(r"[ \t]+", " ", line)

    return line.strip()


def should_skip_line(line: str) -> bool:
    stripped = line.strip()
    low = stripped.lower()

    if not stripped:
        return False

    # Pure Pandoc div fences / wrapper lines
    if re.fullmatch(r":{3,}.*", stripped):
        return True

    # Pure table border lines from grid tables
    if re.fullmatch(r"[+\-:=| ]{8,}", stripped):
        return True
    
    if stripped.startswith("<img") or stripped.startswith("<figure") or stripped.startswith("</figure"):
        return True

    # Obvious website/layout junk
    junk_patterns = [
        "wp-block",
        "kadence",
        "kt-row",
        "kb-row",
        "content-wrapper",
        "inner-wrap",
        "entry-content",
        "site-main",
        "toc-wrapper",
        "toc-placeholder",
        "footer-content",
        "additional-links",
        "spec-embed",
        "connector",
        "glyphicon",
        "aria-hidden",
        "role=",
        "style=",
        "target=\"_blank\"",
        "rel=\"noopener\"",
    ]

    return any(p in low for p in junk_patterns)


def clean_markdown(text: str) -> str:
    cleaned = []

    for raw_line in text.splitlines():
        if should_skip_line(raw_line):
            continue

        line = clean_line(raw_line)
        cleaned.append(line)

    text = "\n".join(cleaned)

    # Remove excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove repeated adjacent non-empty lines
    final_lines = []
    prev = None

    for line in text.splitlines():
        if line.strip() and line == prev:
            continue
        final_lines.append(line)
        prev = line

    return "\n".join(final_lines).strip() + "\n"


def main():
    parser = argparse.ArgumentParser(description="Conservatively clean Markdown for RAG ingestion.")
    parser.add_argument("input", help="Input Markdown file or folder")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite original .md files")
    args = parser.parse_args()

    input_path = Path(args.input)

    if input_path.is_file():
        md_files = [input_path]
    else:
        md_files = sorted(input_path.rglob("*.md"))

    for md_path in md_files:
        if md_path.name.endswith("_clean.md"):
            continue

        raw = md_path.read_text(encoding="utf-8", errors="ignore")
        cleaned = clean_markdown(raw)

        if args.overwrite:
            output_path = md_path
        else:
            output_path = md_path.with_name(md_path.stem + "_clean.md")

        output_path.write_text(cleaned, encoding="utf-8")
        print(f"Wrote cleaned Markdown to: {output_path}")


if __name__ == "__main__":
    main()