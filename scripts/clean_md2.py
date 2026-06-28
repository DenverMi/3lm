from pathlib import Path
import argparse
import re


def clean_line(line: str) -> str:
    line = line.rstrip()

    # Remove Markdown image links, including base64 image blobs
    line = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", line)

    # Remove Docling image placeholder comments
    line = re.sub(r"<!--\s*image\s*-->", "", line, flags=re.IGNORECASE)

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

    # Replace <br> tags with a space (inline in table cells etc.)
    line = re.sub(r"<br\s*/?>", " ", line, flags=re.IGNORECASE)

    # Remove soft hyphens (Docling PDF hyphenation artifacts: "disclo ­ sure" -> "disclosure")
    line = re.sub(r"\s*\u00ad\s*", "", line)

    # Normalize whitespace
    line = re.sub(r"[ \t]+", " ", line)

    # Remove HTML span tags (keep text content)
    line = re.sub(r"<span[^>]*>", "", line)
    line = re.sub(r"</span>", "", line)

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

    # Picture placeholder lines
    if re.match(r"^\*\*==> picture \[\d+ x \d+\] intentionally omitted <==\*\*$", stripped):
        return True

    # Picture text block markers
    if re.match(r"^\*\*----- (Start|End) of picture text -----\*\*(<br>)?$", stripped):
        return True

    # Repeated document header lines (Bluetooth TS style)
    if re.match(r"^\*\*[A-Z][A-Za-z0-9 ()/_-]+\*\* / \*\*[A-Za-z ]+\*\*$", stripped):
        return True
    if re.match(r"^\*\*[A-Z][A-Za-z0-9 ()/_-]+ \*\*/ [A-Za-z ]+$", stripped):
        return True

    # Plain TOC dot-leader lines (non-table)
    if re.search(r"\.[ .]{10,}", stripped):
        return True

    # Orphaned lone page numbers (single digit or small number on its own line)
    if re.fullmatch(r"\d{1,4}", stripped):
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


def strip_boilerplate_sections(text: str) -> str:
    """
    Strip boilerplate sections that appear in every spec and add no RAG value:
    - Table of Contents
    - Copyright / Notice of Use and Disclosure
    - Participants / Contributors
    - Top-level Revision History (not numbered ones like 11.1.1. Revision History)
    - Bluetooth acknowledgment sections (contributor lists, not protocol content)

    Safe rule: only strip headings that match exactly (case-insensitive, ignoring
    markdown bold markers). Numbered headings like "11.1.1. Revision History" are
    kept because they are real spec content.
    """

    # Headings to strip (exact match, no number prefix allowed)
    # These are matched after stripping markdown bold markers (**) and whitespace.
    STRIP_HEADINGS = {
        "table of contents",
        "list of tables",
        "list of figures",
        "list of abbreviations",
        "document history",
        "consolidated table of contents",
        "the bluetooth core specification consolidated table of contents",
        "copyright notice, license and disclaimer",
        "notice of use and disclosure",
        "disclaimer and copyright notice",
        "participants",
        "contributors",
        "revision history",
        "version history and acknowledgments",
        "acknowledgments",
    }

    # Bluetooth version-specific acknowledgment headings
    # e.g. "ACKNOWLEDGMENTS FOR V5.2", "ACKNOWLEDGMENTS (UP TO V5.1)"
    BT_ACK_PATTERN = re.compile(
        r"^acknowledgments?\s*(for\s+v[\d.]+|\(up to v[\d.]+\))?$",
        re.IGNORECASE,
    )

    def heading_level(line: str) -> int:
        m = re.match(r"^(#{1,6})\s", line)
        return len(m.group(1)) if m else 0

    def heading_text(line: str) -> str:
        # Strip markdown heading markers and bold markers
        text = re.sub(r"^#{1,6}\s+", "", line)
        text = re.sub(r"\*+", "", text)
        text = text.strip().lower()
        # Remove trailing punctuation
        text = text.rstrip(".:,")
        return text

    def is_numbered_heading(line: str) -> bool:
        # e.g. "## 11.1.1. Revision History" or "## **11.1.1. Revision History**"
        text = re.sub(r"^#{1,6}\s+", "", line)
        text = re.sub(r"\*+", "", text).strip()
        return bool(re.match(r"^\d+[\d.]*\s+", text))

    def should_strip_heading(line: str) -> bool:
        if not line.startswith("#"):
            return False
        if is_numbered_heading(line):
            return False
        ht = heading_text(line)
        if ht in STRIP_HEADINGS:
            return True
        if BT_ACK_PATTERN.match(ht):
            return True
        return False

    lines = text.splitlines()
    output = []
    skip_until_level = None

    for line in lines:
        level = heading_level(line)

        # If we're in a skip block, check if we've hit a sibling or parent heading
        if skip_until_level is not None:
            if level > 0 and level <= skip_until_level:
                skip_until_level = None
            else:
                continue  # still inside the boilerplate section

        if should_strip_heading(line):
            skip_until_level = level
            continue  # skip the heading itself too

        output.append(line)

    return "\n".join(output)


def strip_matter_page_breaks(text: str) -> str:
    """
    Remove Matter spec PDF page break artifacts.
    """
    # Variant 1: copyright line first (MarkItDown/PyMuPDF style)
    text = re.sub(
        r"\n+Copyright © Connectivity Standards Alliance, Inc\. All rights reserved\."
        r"\n+Page \d+"
        r"\n+Matter Specification [^\n]+"
        r"\n+Connectivity Standards Alliance Document [^\n]+"
        r"\n+",
        "\n\n",
        text,
    )

    # Variant 2: page number first (Docling sometimes reverses order)
    text = re.sub(
        r"\n+Page \d+ Copyright © Connectivity Standards Alliance, Inc\. All rights reserved\."
        r"\n+Matter Specification [^\n]+"
        r"\n+Connectivity Standards Alliance Document [^\n]+"
        r"\n+",
        "\n\n",
        text,
    )

    # Variant 3: single combined line (Docling collapses some page breaks)
    text = re.sub(
        r"\n+Matter Specification [^\n]+ Connectivity Standards Alliance Document [^\n]+"
        r"\n+",
        "\n\n",
        text,
    )

    return text


def strip_bluetooth_page_breaks(text: str) -> str:
    """
    Remove Bluetooth Core Spec PDF page break artifacts.
    """
    # Full form: Proprietary + Version Date + Spec title + Page
    text = re.sub(
        r"\n+Bluetooth SIG Proprietary"
        r"\n+Version Date: [^\n]+"
        r"\n+BLUETOOTH [^\n]+"
        r"\n+Page \d+"
        r"\n+",
        "\n\n",
        text,
    )

    # Short form without Version Date line
    text = re.sub(
        r"\n+Bluetooth SIG Proprietary"
        r"\n+BLUETOOTH [^\n]+"
        r"\n+Page \d+"
        r"\n+",
        "\n\n",
        text,
    )

    # Standalone "Bluetooth SIG Proprietary" line
    text = re.sub(
        r"\n+Bluetooth SIG Proprietary\n+",
        "\n\n",
        text,
    )

    return text


def strip_bluetooth_ts_page_breaks(text: str) -> str:
    """
    Remove Bluetooth Test Suite PDF page break artifacts.
    """
    text = re.sub(
        r"\n+Bluetooth SIG Proprietary"
        r"\n+Page \*\*\d+ of \d+\*\*"
        r"\n+",
        "\n\n",
        text,
    )

    text = re.sub(
        r"\n+Page \*\*\d+ of \d+\*\*\n+",
        "\n\n",
        text,
    )

    return text


def strip_picture_toc_blocks(text: str) -> str:
    """
    Remove TOC dot-leader table rows from Docling and MarkItDown outputs.
    """
    def is_toc_row(line: str) -> bool:
        if not line.startswith("|"):
            return False
        cells = [c.strip() for c in line.split("|") if c.strip()]
        if not cells:
            return False
        # Any cell that is only dots, spaces, and digits = TOC row
        for cell in cells:
            if re.fullmatch(r"[.\s\d]+", cell) and "." in cell:
                return True
        # First cell ends with dot leaders
        if re.search(r"\.\s*\.\s*\.\s*$", cells[0]):
            return True
        # Page break leaked into table row
        if any(
            re.search(r"Specification R\d+\.\d+|Alliance Document \d{2}-\d+", cell)
            for cell in cells
        ):
            return True
        return False

    cleaned = []
    for line in text.splitlines():
        if is_toc_row(line):
            continue
        cleaned.append(line)

    text = "\n".join(cleaned)

    # Pure dot leader lines (not in tables)
    text = re.sub(
        r"^[ \t]*(?:\.[ \t]*){5,}\d*\s*$",
        "",
        text,
        flags=re.MULTILINE,
    )

    return text


def clean_markdown(text: str) -> str:
    cleaned = []

    for raw_line in text.splitlines():
        if should_skip_line(raw_line):
            continue

        line = clean_line(raw_line)
        cleaned.append(line)

    text = "\n".join(cleaned)

    # Strip page break artifacts (order matters: most specific first)
    text = strip_matter_page_breaks(text)
    text = strip_bluetooth_ts_page_breaks(text)
    text = strip_bluetooth_page_breaks(text)
    text = strip_picture_toc_blocks(text)

    # Strip boilerplate sections
    text = strip_boilerplate_sections(text)

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