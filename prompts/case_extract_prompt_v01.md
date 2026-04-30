Read the attached JSON file and extract reusable Bluetooth consulting knowledge from it.

The attached file contains one email thread in JSON format. Use the file itself as the only source of truth.

Important:
- One thread may contain one or more distinct Bluetooth consulting cases.
- If the thread contains multiple clearly different issues, output multiple cases.
- If the thread contains only one main issue, output one case.
- If the thread contains no reusable Bluetooth consulting knowledge, output an empty cases array.

Your job:
- Understand the thread
- Identify each distinct reusable Bluetooth qualification / technical / procedural issue
- Summarize the consultant’s reasoning for each issue
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
  Read the value directly from the attached JSON file's "thread_id" field.
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
  The consultant’s substantive reasoning, interpretation, or explanation.

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

Process the attached file now.

