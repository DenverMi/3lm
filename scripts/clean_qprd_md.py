from pathlib import Path
import re

INPUT = Path("data/bluetooth/policies/QPRD.md")
OUTPUT = Path("data/bluetooth/policies/BT Qualification Program Reference Document_QPRD_v5.md")


def clean_line(line: str) -> str:
    line = line.strip()

    # Remove Pandoc attribute blocks
    line = re.sub(r"\{#[^}]+\}", "", line)
    line = re.sub(r"\{\.[^}]+\}", "", line)
    line = re.sub(r"\{[^}]*class=[^}]*\}", "", line)
    line = re.sub(r"\{[^}]*target=[^}]*\}", "", line)
    line = re.sub(r"\{[^}]*rel=[^}]*\}", "", line)

    # Convert markdown links to visible text only
    line = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)

    # Clean citation links like [[[4]](#id3930)] -> [4]
    line = re.sub(r"\[\[\[([0-9]+)\]\]\(#?[A-Za-z0-9_.-]+\)\]", r"[\1]", line)
    line = re.sub(r"\[\[([0-9]+)\]\]", r"[\1]", line)

    # Remove leftover link/citation classes
    line = line.replace("{.xref", "")
    line = line.replace(".linktype-component}", "")
    line = line.replace("{.link", "")
    line = line.replace("{.citation}", "")

    # Remove weird Pandoc literals
    line = line.replace("::: literallayout", "")
    line = line.replace(":::", "")
    line = line.replace("\\", "")

    # Fix headings like ### [1.1][.] [Definitions]
    line = re.sub(r"^(#{1,6})\s+\[([^\]]+)\]\[\.\]\s+\[([^\]]+)\]", r"\1 \2. \3", line)
    line = re.sub(r"^(#{1,6})\s+\[\*?([^\]]+?)\*?\]", r"\1 \2", line)

    # Normalize Bluetooth markdown artifact
    line = line.replace("Bluetooth[*^®^*]", "Bluetooth®")
    line = line.replace("Bluetooth^®^", "Bluetooth®")

    # Normalize spaces
    line = re.sub(r"[ \t]+", " ", line)

    return line.strip()


def should_skip(line: str) -> bool:
    stripped = line.strip()
    low = stripped.lower()

    if not stripped:
        return False

    # Skip wrapper fences and web layout junk
    if re.fullmatch(r":{3,}.*", stripped):
        return True

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
        "role=",
        "style=",
        "aria-hidden",
        "target=\"_blank\"",
        "rel=\"noopener\"",
    ]

    if any(p in low for p in junk_patterns):
        return True

    # Skip image lines
    if stripped.startswith("!["):
        return True

    # Skip pure table border lines
    if re.fullmatch(r"[+\-:=| ]{8,}", stripped):
        return True

    # Skip lonely markers
    if stripped in {"\\", ":::","::::", ":::::"}:
        return True

    return False


def remove_toc_block(lines):
    """
    Remove only the early table-of-contents block before Version metadata.
    Do not remove UUID/link-looking lines later in the real document.
    """
    cleaned = []
    in_early_toc = False
    before_version = True

    for line in lines:
        if line.startswith("- [Version:") or line.startswith("- Version:"):
            before_version = False
            in_early_toc = False
            cleaned.append(line)
            continue

        # Only detect TOC before the first Version block
        if before_version and re.search(r"\]\(#UUID-", line):
            in_early_toc = True
            continue

        if in_early_toc:
            continue

        cleaned.append(line)

    return cleaned


def remove_duplicate_tail(lines):
    # Keep all content for now.
    # The previous duplicate-removal logic was too aggressive.
    return lines


def main():
    raw = INPUT.read_text(encoding="utf-8", errors="ignore")
    raw_lines = raw.splitlines()

    stage1 = []
    started = False

    for line in raw_lines:
        if "Qualification Program Reference Document" in line or line.strip() == "Abstract":
            started = True

        if not started:
            continue

        if should_skip(line):
            continue

        cleaned = clean_line(line)

        if cleaned:
            stage1.append(cleaned)
        else:
            stage1.append("")

    stage1 = remove_toc_block(stage1)
    stage1 = remove_duplicate_tail(stage1)

    text = "\n".join(stage1)

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

    text = "\n".join(final_lines).strip() + "\n"

    OUTPUT.write_text(text, encoding="utf-8")
    print(f"Wrote cleaned Markdown to: {OUTPUT}")


if __name__ == "__main__":
    main()