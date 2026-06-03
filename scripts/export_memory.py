import json
from pathlib import Path


CORRECTIONS_PATH = Path("storage/corrections.jsonl")
NOTES_PATH = Path("storage/notes.jsonl")
OUTPUT_DIR = Path("storage/memory_review")


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []

    records = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        records.append(json.loads(line))

    return records

def normalize_program(value: str | None) -> str:
    value = (value or "unknown").strip().lower()
    return value or "unknown"

def collect_existing_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()

    existing_ids = set()

    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("- id:"):
            record_id = stripped.removeprefix("- id:").strip()
            if record_id:
                existing_ids.add(record_id)

    return existing_ids

def write_section(lines: list[str], title: str, records: list[dict], record_type: str) -> None:
    lines.append(f"# {title}")
    lines.append("")

    if not records:
        lines.append("_No records found._")
        lines.append("")
        return

    for i, record in enumerate(records, start=1):
        record_id = record.get("correction_id") or record.get("note_id") or ""
        program = record.get("program", "")
        conversation_title = record.get("conversation_title", "")
        previous_user_question = record.get("previous_user_question", "")
        previous_assistant_answer = record.get("previous_assistant_answer", "")

        if record_type == "correction":
            raw_text = record.get("correction", "")
        else:
            raw_text = record.get("note", "")

        lines.append(f"## {record_type.upper()} {i}")
        lines.append("")
        lines.append(f"- id: {record_id}")
        lines.append(f"- type: {record_type}")
        lines.append(f"- status: unreviewed")
        lines.append(f"- program: {program}")
        lines.append(f"- conversation_title: {conversation_title}")
        lines.append("")

        if previous_user_question:
            lines.append("### Previous user question")
            lines.append("")
            lines.append(previous_user_question)
            lines.append("")

        if previous_assistant_answer:
            lines.append("### Previous assistant answer")
            lines.append("")
            lines.append(previous_assistant_answer)
            lines.append("")

        lines.append("### Proposed memory text")

        lines.append("")
        lines.append(raw_text)
        lines.append("")
        lines.append("---")
        lines.append("")


def main() -> None:
    corrections = load_jsonl(CORRECTIONS_PATH)
    notes = load_jsonl(NOTES_PATH)

    programs = sorted(
        {
            normalize_program(record.get("program"))
            for record in corrections + notes
        }
    )


    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for program in programs:
        program_corrections = [
            record for record in corrections
            if normalize_program(record.get("program")) == program
        ]
        program_notes = [
            record for record in notes
            if normalize_program(record.get("program")) == program
        ]

        lines = []
        lines.append(f"# Memory Review: {program}")
        lines.append("")
        lines.append("Edit this file manually. Change `status: unreviewed` to `status: approved` only when the memory text is correct.")
        lines.append("")

        write_section(lines, "Corrections", program_corrections, "correction")
        write_section(lines, "Notes", program_notes, "note")

        output_path = OUTPUT_DIR / f"{program}_review.md"

        existing_ids = collect_existing_ids(output_path)

        new_lines = []
        write_section(new_lines, "Corrections", [
            record for record in program_corrections
            if (record.get("correction_id") or "") not in existing_ids
        ], "correction")

        write_section(new_lines, "Notes", [
            record for record in program_notes
            if (record.get("note_id") or "") not in existing_ids
        ], "note")

        if output_path.exists():
            if not new_lines or all("_No records found._" in line for line in new_lines):
                print(f"No new records for {program}")
                continue

            with output_path.open("a", encoding="utf-8") as f:
                f.write("\n\n")
                f.write("\n".join(new_lines))

            print(f"Appended new records to {output_path}")
        else:
            output_path.write_text("\n".join(lines), encoding="utf-8")
            print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()