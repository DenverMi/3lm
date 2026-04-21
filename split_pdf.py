from pathlib import Path
from math import ceil
from pypdf import PdfReader, PdfWriter

src = Path("data/for_conversion/BT Core_v6.2.pdf")
outdir = Path("data/for_conversion_split")
outdir.mkdir(parents=True, exist_ok=True)

reader = PdfReader(str(src), strict=False)
total = len(reader.pages)
parts = 4
chunk_size = ceil(total / parts)

print(f"Total pages: {total}")

for i in range(parts):
    start = i * chunk_size
    end = min((i + 1) * chunk_size, total)
    if start >= total:
        break

    writer = PdfWriter()

    for p in range(start, end):
        writer.add_page(reader.pages[p])

    out = outdir / f"BT_Core_v6.2_part{i+1}.pdf"
    with open(out, "wb") as f:
        writer.write(f)

    print(f"Wrote {out} pages {start + 1}-{end}")