#!/usr/bin/env python3
"""
convert_pdf.py — Convert PDF files to Markdown using Docling.

Usage:
    python convert_pdf.py path/to/file.pdf
    python convert_pdf.py path/to/folder/
"""

import argparse
import sys
from pathlib import Path

from docling.document_converter import DocumentConverter


def convert(input_path: Path) -> None:
    if input_path.is_file():
        pdf_files = [input_path]
    elif input_path.is_dir():
        pdf_files = sorted(input_path.rglob("*.pdf"))
    else:
        print(f"Error: {input_path} is not a file or directory.")
        sys.exit(1)

    if not pdf_files:
        print(f"No PDF files found in {input_path}")
        sys.exit(0)

    converter = DocumentConverter()

    for pdf_path in pdf_files:
        output_path = pdf_path.with_suffix(".md")

        print(f"Converting: {pdf_path.name} ...")

        try:
            result = converter.convert(str(pdf_path))
            markdown = result.document.export_to_markdown()
            output_path.write_text(markdown, encoding="utf-8")
            print(f"  → Saved: {output_path.name}")

        except Exception as e:
            print(f"  ✗ Failed: {pdf_path.name} — {e}")

    print("\nDone.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert PDF files to Markdown using Docling."
    )
    parser.add_argument(
        "input",
        help="Path to a PDF file or a folder containing PDF files.",
    )
    args = parser.parse_args()

    convert(Path(args.input))


if __name__ == "__main__":
    main()