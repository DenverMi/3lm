from pathlib import Path
import sys
from markitdown import MarkItDown


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/convert_to_md.py <input-file>")
        sys.exit(1)

    src = Path(sys.argv[1]).expanduser().resolve()

    if not src.exists():
        raise FileNotFoundError(src)

    out = src.with_suffix(".md")

    result = MarkItDown().convert(str(src))
    out.write_text(result.text_content, encoding="utf-8")

    print(f"Converted: {src}")
    print(f"Saved to:   {out}")
    print(f"Chars:      {len(result.text_content):,}")


if __name__ == "__main__":
    main()