from pathlib import Path
import argparse
import subprocess


def main():
    parser = argparse.ArgumentParser(description="Convert HTML to Markdown using Pandoc.")
    parser.add_argument("html", help="Path to HTML file")
    parser.add_argument("-o", "--output", help="Optional output Markdown path")
    args = parser.parse_args()

    html_path = Path(args.html)
    output_path = Path(args.output) if args.output else html_path.with_suffix(".md")

    subprocess.run(
        [
            "pandoc",
            str(html_path),
            "-f",
            "html",
            "-t",
            "markdown",
            "-o",
            str(output_path),
        ],
        check=True,
    )

    print(f"Wrote: {output_path}")


if __name__ == "__main__":
    main()