from pathlib import Path
import argparse
import pymupdf4llm


def main():
    parser = argparse.ArgumentParser(description="Convert PDF to Markdown using PyMuPDF4LLM.")
    parser.add_argument("pdf", help="Path to PDF file")
    args = parser.parse_args()

    pdf_path = Path(args.pdf)
    md_path = pdf_path.with_suffix(".md")

    md_text = pymupdf4llm.to_markdown(str(pdf_path))
    md_path.write_text(md_text, encoding="utf-8")

    print(f"Wrote: {md_path}")


if __name__ == "__main__":
    main()