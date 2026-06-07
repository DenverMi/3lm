import subprocess
import time
import re
from pathlib import Path

QUESTIONS = [
    "In Bluetooth, what do we need to prepare in the compliance folder?",
    "Customer asks: If they use a qualified Bluetooth module, do they still need a new qualification?",
    "@ In past Bluetooth cases, if a customer uses a qualified Bluetooth module, did they still need a new qualification?",
    "In Bluetooth, what is TCW?",
    "In Bluetooth, what is the difference between ICS and IXIT?",
    "In Bluetooth, what is Option 2b?",
    "In Bluetooth, what is the difference between Option 2a and Option 2b?",
    "BluetoothのQualificationで、Compliance Folderには何を入れる必要がありますか？",
    "Bluetoothで認証済みモジュールを使う場合、新しい認証は必要ですか？",
    "BluetoothでTCWとは何ですか？",
    "BluetoothでICSとは何ですか？",
    "BluetoothでIXITとは何ですか？",
]

RESULTS_PATH = Path("benchmark_results.md")
SCOREBOARD_PATH = Path("benchmark_scoreboard.md")

TIMING_FIELDS = [
    "total_duration",
    "load_duration",
    "prompt_eval_duration",
    "eval_duration",
]

def ns_to_seconds(value: str) -> float:
    try:
        return int(value) / 1_000_000_000
    except Exception:
        return 0.0


def extract_ollama_timings(output: str) -> dict[str, float]:
    timings = {field: 0.0 for field in TIMING_FIELDS}

    for field in TIMING_FIELDS:
        match = re.search(rf"(?<![A-Za-z_]){field}=(\d+)", output)
        if not match:
            continue

        timings[field] = ns_to_seconds(match.group(1))

    return timings

def run_question(question: str) -> tuple[float, str]:
    command = [
        "python",
        "-m",
        "app.answer",
        "--program",
        "bluetooth",
        "--debug",
        question,
    ]

    start = time.perf_counter()
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
    )
    elapsed = time.perf_counter() - start

    output = result.stdout.strip()

    if result.stderr.strip():
        output += "\n\nSTDERR:\n" + result.stderr.strip()

    return elapsed, output


def guess_source_quality(output: str) -> str:
    if "matter:" in output or "aliro:" in output:
        return "FAIL - cross-program source"

    citation_count = output.count("- [bluetooth:")

    if citation_count == 0:
        return "FAIL - no citations"
    if citation_count <= 3:
        return "Good"
    if citation_count <= 5:
        return "Noisy"

    return "Too noisy"


def guess_grade(output: str) -> str:
    fail_markers = [
        "do not contain",
        "not enough information",
        "provided documents do not contain",
        "general knowledge",
    ]

    lowered = output.lower()

    if any(marker in lowered for marker in fail_markers):
        return "REVIEW"

    if "matter:" in output or "aliro:" in output:
        return "FAIL"

    return "TODO"

def main() -> None:
    raw_lines = ["# Bluetooth RAG Benchmark Raw Results", ""]
    board_lines = [
        "# Bluetooth RAG Benchmark Scoreboard",
        "",
        "| # | Question | Time | Ollama | Load | Prompt eval | Token eval | Grade | Source quality | Notes |",
        "|---:|---|---:|---:|---:|---:|---:|---|---|---|",
    ]

    for index, question in enumerate(QUESTIONS, start=1):
        print(f"[{index}/{len(QUESTIONS)}] {question}")

        elapsed, output = run_question(question)
        timings = extract_ollama_timings(output)

        raw_lines.extend(
            [
                f"## {index}. {question}",
                "",
                f"- Elapsed: {elapsed:.2f}s",
                f"- Ollama total: {timings['total_duration']:.2f}s",
                f"- Ollama load: {timings['load_duration']:.2f}s",
                f"- Prompt eval: {timings['prompt_eval_duration']:.2f}s",
                f"- Token eval: {timings['eval_duration']:.2f}s",
                "",
                "```text",
                output,
                "```",
                "",
            ]
        )

        safe_question = question.replace("|", "\\|")
        grade = guess_grade(output)
        source_quality = guess_source_quality(output)

        board_lines.append(
            f"| {index} | {safe_question} | {elapsed:.2f}s | "
            f"{timings['total_duration']:.2f}s | "
            f"{timings['load_duration']:.2f}s | "
            f"{timings['prompt_eval_duration']:.2f}s | "
            f"{timings['eval_duration']:.2f}s | "
            f"{grade} | {source_quality} | TODO |"
        )

        RESULTS_PATH.write_text("\n".join(raw_lines), encoding="utf-8")
        SCOREBOARD_PATH.write_text("\n".join(board_lines), encoding="utf-8")

        print(f"Done: {elapsed:.2f}s")

    print(f"\nSaved raw results to: {RESULTS_PATH}")
    print(f"Saved scoreboard to: {SCOREBOARD_PATH}")


if __name__ == "__main__":
    main()