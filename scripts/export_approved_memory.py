from pathlib import Path


REVIEW_DIR = Path("storage/memory_review")
DATA_DIR = Path("data")

PROGRAMS = {"bluetooth", "aliro", "matter"}


def parse_review_file(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    sections = text.split("\n## ")

    records = []

    for section in sections[1:]:
        section = "## " + section

        lines = section.splitlines()

        record_id = ""
        record_type = ""
        status = ""
        program = ""
        memory_lines = []
        in_memory_text = False

        for line in lines:
            stripped = line.strip()

            if stripped.startswith("- id:"):
                record_id = stripped.removeprefix("- id:").strip()

            elif stripped.startswith("- type:"):
                record_type = stripped.removeprefix("- type:").strip()

            elif stripped.startswith("- status:"):
                status = stripped.removeprefix("- status:").strip().lower()

            elif stripped.startswith("- program:"):
                program = stripped.removeprefix("- program:").strip().lower()

            elif stripped == "### Proposed memory text":
                in_memory_text = True
                memory_lines = []

            elif stripped == "---":
                in_memory_text = False

            elif in_memory_text:
                memory_lines.append(line)

        memory_text = "\n".join(memory_lines).strip()

        if status == "approved" and program in PROGRAMS and memory_text:
            records.append(
                {
                    "id": record_id,
                    "type": record_type,
                    "program": program,
                    "memory_text": memory_text,
                }
            )

    return records

def collect_existing_source_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()

    existing_ids = set()

    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()

        if stripped.startswith("- source_id:"):
            source_id = stripped.removeprefix("- source_id:").strip()
            if source_id:
                existing_ids.add(source_id)

    return existing_ids

def main() -> None:
    if not REVIEW_DIR.exists():
        print(f"Review folder not found: {REVIEW_DIR}")
        return

    records_by_program: dict[str, list[dict]] = {
        program: [] for program in PROGRAMS
    }

    for path in sorted(REVIEW_DIR.glob("*_review.md")):
        records = parse_review_file(path)

        for record in records:
            records_by_program[record["program"]].append(record)

    for program, records in sorted(records_by_program.items()):
        if not records:
            continue

        output_dir = DATA_DIR / program / "memory"
        output_path = output_dir / "approved_memory.md"

        output_dir.mkdir(parents=True, exist_ok=True)

        existing_ids = collect_existing_source_ids(output_path)

        new_records = [
            record for record in records
            if record.get("id") and record.get("id") not in existing_ids
        ]

        if not new_records:
            print(f"No new approved memory for {program}")
            continue

        lines = []

        if not output_path.exists():
            lines.append(f"# Approved Memory: {program}")
            lines.append("")
            lines.append("These entries were manually reviewed and approved for RAG retrieval.")
            lines.append("")

        existing_count = len(existing_ids)

        for i, record in enumerate(new_records, start=existing_count + 1):
            lines.append(f"## Memory {i}")
            lines.append("")
            lines.append(f"- source_id: {record['id']}")
            lines.append(f"- type: {record['type']}")
            lines.append(f"- program: {program}")
            lines.append("")
            lines.append(record["memory_text"])
            lines.append("")

        if output_path.exists():
            with output_path.open("a", encoding="utf-8") as f:
                f.write("\n")
                f.write("\n".join(lines))

            print(f"Appended {len(new_records)} approved memory item(s) to {output_path}")
        else:
            output_path.write_text("\n".join(lines), encoding="utf-8")
            print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()