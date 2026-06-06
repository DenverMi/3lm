import json
from pathlib import Path
from typing import Any, Dict, List

import ollama

THREADS_DIR = Path("data/bluetooth/email_threads")
OUT_DIR = Path("data/bluetooth/email_cases")
MODEL = "qwen3.6:27b"


def load_thread(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_thread_text(thread: Dict[str, Any], max_messages: int = 8) -> str:
    messages = thread.get("messages", [])
    messages = sorted(messages, key=lambda x: x.get("date", ""))[-max_messages:]

    parts: List[str] = []
    for i, msg in enumerate(messages, start=1):
        parts.append(
            f"[Message {i}]\n"
            f"Date: {msg.get('date', '')}\n"
            f"From: {msg.get('from', '')}\n"
            f"To: {msg.get('to', '')}\n"
            f"CC: {msg.get('cc', '')}\n"
            f"Subject: {msg.get('subject', '')}\n"
            f"Body:\n{msg.get('body', '').strip()}\n"
        )
    return "\n\n".join(parts)


def build_prompt(thread: Dict[str, Any], case_id: str) -> str:
    subject = thread.get("subject", "")
    thread_text = build_thread_text(thread)

    return f"""
You are extracting reusable Bluetooth consulting knowledge from an internal email thread.

Your task:
Read the thread and output ONE JSON object only.
Do not explain.
Do not add markdown fences.
Do not add commentary.
If a field is unknown, use an empty string.
If multiple possibilities exist, choose the most likely one from the thread.

Output JSON schema:
{{
  "case_id": "{case_id}",
  "iut_type": "",
  "customer_question": "",
  "actual_issue": "",
  "consultant_answer": "",
  "final_recommendation": "",
  "bluetooth_tags": [],
  "qualification_stage": "",
  "source_thread": "{thread.get("thread_id", "")}"
}}

Rules:
- customer_question: what the customer is explicitly asking for
- actual_issue: the real technical or qualification problem behind the question
- consultant_answer: the consultant's substantive answer or reasoning
- final_recommendation: the practical action the customer or team should take
- bluetooth_tags: short tags like qualification, QDID, EPL, RF, PTS, ICS, profile, LE Audio, listing, reuse, design change
- qualification_stage must be one of:
  "pre-sales", "planning", "implementation", "pre-test review", "testing", "test failure", "listing / declaration", "post-launch change"
- Prefer Bluetooth qualification meaning over generic business meaning
- Ignore greetings, signatures, and repeated quoted text
- Focus on reusable consultant knowledge
- Keep answers concise but concrete

Thread subject:
{subject}

Thread content:
{thread_text}
""".strip()


def parse_llm_json(text: str) -> Dict[str, Any]:
    text = text.strip()

    # try direct parse
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # try extracting first JSON object
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        candidate = text[start:end + 1]
        return json.loads(candidate)

    raise ValueError("No valid JSON found in model output")


def normalize_case(data: Dict[str, Any], case_id: str, source_thread: str) -> Dict[str, Any]:
    allowed_stages = {
        "pre-sales",
        "planning",
        "implementation",
        "pre-test review",
        "testing",
        "test failure",
        "listing / declaration",
        "post-launch change",
    }

    tags = data.get("bluetooth_tags", [])
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",") if t.strip()]
    elif not isinstance(tags, list):
        tags = []

    stage = (data.get("qualification_stage") or "").strip()
    if stage not in allowed_stages:
        stage = ""

    return {
        "case_id": case_id,
        "iut_type": (data.get("iut_type") or "").strip(),
        "customer_question": (data.get("customer_question") or "").strip(),
        "actual_issue": (data.get("actual_issue") or "").strip(),
        "consultant_answer": (data.get("consultant_answer") or "").strip(),
        "final_recommendation": (data.get("final_recommendation") or "").strip(),
        "bluetooth_tags": tags,
        "qualification_stage": stage,
        "source_thread": source_thread,
    }


def extract_case(thread_path: Path, index: int) -> Dict[str, Any]:
    thread = load_thread(thread_path)
    case_id = f"BT-{index:04d}"
    prompt = build_prompt(thread, case_id)

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        options={
            "temperature": 0.1,
        },
        format="json",
    )

    content = response["message"]["content"]
    parsed = parse_llm_json(content)
    return normalize_case(parsed, case_id, thread.get("thread_id", ""))


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    thread_files = sorted(THREADS_DIR.glob("thread_*.json"))
    if not thread_files:
        raise FileNotFoundError(f"No thread files found in {THREADS_DIR}")

    success = 0
    failed = 0

    for i, thread_path in enumerate(thread_files, start=1):
        try:
            case = extract_case(thread_path, i)
            out_path = OUT_DIR / f"case_{i:04d}.json"
            out_path.write_text(json.dumps(case, ensure_ascii=False, indent=2), encoding="utf-8")
            success += 1
            print(f"OK  {thread_path.name} -> {out_path.name}")
        except Exception as e:
            failed += 1
            print(f"FAIL {thread_path.name} -> {e}")

    print(f"\nDone. Success: {success}, Failed: {failed}, Output: {OUT_DIR}")


if __name__ == "__main__":
    main()