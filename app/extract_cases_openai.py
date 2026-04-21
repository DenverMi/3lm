import json
import time
from pathlib import Path
from typing import Any, Dict, List

from openai import OpenAI

client = OpenAI()

THREADS_DIR = Path("data/bluetooth/email_threads")
OUT_DIR = Path("data/bluetooth/email_cases_openai")

MODEL = "gpt-5.4-mini"
SLEEP_BETWEEN_CALLS = 1.0
OVERWRITE = False


PROMPT_TEMPLATE = """
Read the JSON email thread provided below and extract reusable Bluetooth consulting knowledge from it.

The JSON email thread below is the only allowed source.
Do not use information from earlier messages or any outside context.
If any detail is not supported by the JSON thread, do not invent it.

Important:
- One thread may contain one or more distinct Bluetooth consulting cases.
- If the thread contains multiple clearly different issues, output multiple cases.
- If the thread contains only one main issue, output one case.
- If the thread contains no reusable Bluetooth consulting knowledge, output an empty cases array.

Your job:
- Understand the thread
- Identify each distinct reusable Bluetooth qualification / technical / procedural issue
- Summarize the consultant's reasoning for each issue
- Extract the practical recommendation for each issue
- Remove customer-specific details
- Output JSON only

Rules:
1. Output valid JSON only.
2. Do not use markdown fences.
3. Do not explain anything outside the JSON.
4. Write all values in English unless a Japanese technical phrase is necessary for accuracy.
5. Redact sensitive details:
   - person names -> [PERSON]
   - company names -> [COMPANY]
   - email addresses -> [EMAIL]
   - URLs -> [URL]
   - product IDs / quote numbers / project codes -> [ID]
6. Ignore greetings, signatures, disclaimers, and repeated quoted history unless they affect the decision.
7. If the consultant answer is spread across multiple messages, combine it into one coherent answer.
8. If a field is unknown, use an empty string.
9. Do not hallucinate details.
10. Only create separate cases when the issues are meaningfully distinct and reusable on their own.
11. Keep each case atomic. Do not mix unrelated issues into one case.
12. Prefer Bluetooth qualification meaning over generic business summarization.

Return this exact schema:

{
  "source_thread": "",
  "cases": [
    {
      "case_id": "",
      "iut_type": "",
      "customer_question": "",
      "actual_issue": "",
      "consultant_answer": "",
      "final_recommendation": "",
      "bluetooth_tags": [],
      "qualification_stage": ""
    }
  ]
}

Field rules:
- source_thread:
  Read the value directly from the JSON thread's "thread_id" field.
  Copy it exactly as-is.
  Do not infer it from the filename.
  Do not change it.
  Do not renumber it.
  Example:
  if thread_id is "thread_0004", then source_thread must be "thread_0004".

- case_id:
  Build case_id strictly from source_thread using this format:
  "<source_thread>_case_01"
  "<source_thread>_case_02"
  "<source_thread>_case_03"
  and so on.

  Rules:
  1. Use the exact source_thread value.
  2. Number cases in the order they appear in the output.
  3. Use two digits: 01, 02, 03...
  4. Never use any other thread number.
  5. Never infer case_id from the filename.
  6. If source_thread is "thread_0004", valid case_ids are:
     "thread_0004_case_01"
     "thread_0004_case_02"
     etc.

- iut_type:
  The product / implementation under test if inferable.
  Examples: "controller", "lighting device", "headset", "module", "keyboard", "TV", "medical bed", "USB dongle"
  If unclear, use "".

- customer_question:
  What the customer or internal requester is explicitly asking for that case.

- actual_issue:
  The real Bluetooth qualification / technical / procedural problem behind the question.

- consultant_answer:
  The consultant's substantive reasoning, interpretation, or explanation.

- final_recommendation:
  The practical next action for that case.
  This must be action-oriented.

- bluetooth_tags:
  Use 3 to 8 concise tags only if strongly supported.
  Examples:
  "qualification", "listing", "QDID", "EPL", "PTS", "ICS", "IXIT", "RF", "RF PHY", "profile", "GATT", "HCI", "controller", "host", "module", "reuse", "design change", "LE", "LE Audio", "Classic", "test report", "declaration"

- qualification_stage:
  Must be one of:
  "pre-sales"
  "planning"
  "implementation"
  "pre-test review"
  "testing"
  "test failure"
  "listing / declaration"
  "post-launch change"

Decision policy:
- If the thread is mostly about quotation / scheduling but still includes a real qualification decision, extract the qualification decision as a case.
- Only include iut_type, tags, and qualification_stage if they are explicitly supported by the thread or are a very high-confidence inference from the thread. Otherwise leave them empty.
- If a thread contains both administrative discussion and a real technical or qualification issue, keep only the reusable consulting issue as a case.
- If the thread contains no reusable Bluetooth consulting issue, return:
  {
    "source_thread": "<thread_id>",
    "cases": []
  }

Before writing the final JSON:
- verify that output source_thread exactly matches the thread_id in the JSON input
- verify that every case_id begins with "<source_thread>_case_"
- if not, correct it before returning

Thread JSON:
__THREAD_JSON__
""".strip()


ALLOWED_STAGES = {
    "pre-sales",
    "planning",
    "implementation",
    "pre-test review",
    "testing",
    "test failure",
    "listing / declaration",
    "post-launch change",
}


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_json_response(text: str) -> Dict[str, Any]:
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end != -1 and end > start:
            return json.loads(text[start:end + 1])
        raise


def normalize_case(case: Dict[str, Any], source_thread: str, idx: int) -> Dict[str, Any]:
    case_id = f"{source_thread}_case_{idx:02d}"

    tags = case.get("bluetooth_tags", [])
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",") if t.strip()]
    elif not isinstance(tags, list):
        tags = []

    clean_tags: List[str] = []
    for tag in tags:
        if isinstance(tag, str):
            t = tag.strip()
            if t and t not in clean_tags:
                clean_tags.append(t)

    stage = str(case.get("qualification_stage", "") or "").strip()
    if stage not in ALLOWED_STAGES:
        stage = ""

    return {
        "case_id": case_id,
        "source_thread": source_thread,
        "iut_type": str(case.get("iut_type", "") or "").strip(),
        "customer_question": str(case.get("customer_question", "") or "").strip(),
        "actual_issue": str(case.get("actual_issue", "") or "").strip(),
        "consultant_answer": str(case.get("consultant_answer", "") or "").strip(),
        "final_recommendation": str(case.get("final_recommendation", "") or "").strip(),
        "bluetooth_tags": clean_tags,
        "qualification_stage": stage,
    }


def extract_cases_from_thread(thread: Dict[str, Any]) -> Dict[str, Any]:
    prompt = PROMPT_TEMPLATE.replace(
    "__THREAD_JSON__",
    json.dumps(thread, ensure_ascii=False, indent=2)
)

    response = client.responses.create(
        model=MODEL,
        input=prompt,
    )

    raw = response.output_text
    data = parse_json_response(raw)

    source_thread = str(data.get("source_thread") or thread.get("thread_id") or "").strip()
    if not source_thread:
        raise ValueError("Missing source_thread")

    if source_thread != thread.get("thread_id"):
        source_thread = str(thread.get("thread_id"))

    raw_cases = data.get("cases", [])
    if not isinstance(raw_cases, list):
        raw_cases = []

    normalized_cases = [
        normalize_case(case, source_thread, idx)
        for idx, case in enumerate(raw_cases, start=1)
    ]

    return {
        "source_thread": source_thread,
        "cases": normalized_cases,
        "raw_response": raw,
    }


def save_cases(result: Dict[str, Any]) -> int:
    source_thread = result["source_thread"]
    cases = result["cases"]

    saved = 0
    for case in cases:
        out_path = OUT_DIR / f"{case['case_id']}.json"
        if out_path.exists() and not OVERWRITE:
            continue
        out_path.write_text(
            json.dumps(case, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        saved += 1

    audit_path = OUT_DIR / f"{source_thread}_cases.json"
    if OVERWRITE or not audit_path.exists():
        audit_payload = {
            "source_thread": source_thread,
            "cases": cases,
        }
        audit_path.write_text(
            json.dumps(audit_payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    return saved


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    thread_files = sorted(THREADS_DIR.glob("thread_0011.json"))
    if not thread_files:
        raise FileNotFoundError(f"No thread files found in {THREADS_DIR}")

    total_threads = 0
    total_cases = 0
    failed = 0

    for thread_path in thread_files:
        thread = load_json(thread_path)
        source_thread = str(thread.get("thread_id") or thread_path.stem)

        audit_path = OUT_DIR / f"{source_thread}_cases.json"
        if audit_path.exists() and not OVERWRITE:
            print(f"SKIP {thread_path.name} -> already extracted")
            continue

        try:
            result = extract_cases_from_thread(thread)
            saved = save_cases(result)
            total_threads += 1
            total_cases += len(result["cases"])
            print(f"OK   {thread_path.name} -> {len(result['cases'])} case(s), saved {saved}")
        except Exception as e:
            failed += 1
            print(f"FAIL {thread_path.name} -> {e}")

        time.sleep(SLEEP_BETWEEN_CALLS)

    print(f"\nDone. Threads processed: {total_threads}, Cases extracted: {total_cases}, Failed: {failed}")


if __name__ == "__main__":
    main()