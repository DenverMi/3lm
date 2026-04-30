Read the attached JSON file and extract retrieval-optimized reusable Bluetooth consulting cases from it.

The attached file contains one email thread in JSON format.
Use the attached file as the only source of truth.

Important:
- One thread may contain one or more distinct Bluetooth consulting cases.
- If the thread contains multiple clearly different reusable issues, output multiple cases.
- If the thread contains only one main reusable issue, output one case.
- If the thread contains no reusable Bluetooth consulting knowledge, output an empty cases array.

Your goal:
- Understand the thread
- Identify each distinct reusable Bluetooth qualification / technical / procedural issue
- Convert each issue into a standalone RAG-friendly case record
- Preserve consultant reasoning
- Preserve practical actionability
- Improve future retrieval by including alternate phrasings, plain-English explanation, and search aliases
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
8. If a field is unknown, use an empty string or an empty array, as appropriate.
9. Do not hallucinate details.
10. Only create separate cases when the issues are meaningfully distinct and reusable on their own.
11. Keep each case atomic. Do not mix unrelated issues into one case.
12. Prefer Bluetooth qualification meaning over generic business summarization.
13. Make each case independently understandable and independently retrievable without requiring the full thread.
14. Use wording that helps both semantic search and keyword search.
15. Include both technical terminology and plain-English phrasing when strongly supported by the thread.
16. Do not invent alternative phrasings that change the meaning of the case.
17. Do not invent risks, costs, timelines, or test counts unless explicitly supported by the thread or directly implied by the qualification outcome.
18. Keep wording concise, dense, and reusable.

Return this exact schema:

{
  "source_thread": "",
  "cases": [
    {
      "case_id": "",
      "iut_type": "",
      "customer_question": "",
      "question_variants": [],
      "actual_issue": "",
      "plain_english_explanation": "",
      "consultant_answer": "",
      "decision_logic": "",
      "final_recommendation": "",
      "risk_if_done_wrong": "",
      "bluetooth_tags": [],
      "search_aliases": [],
      "qualification_stage": "",
      "confidence": "",
      "source_type": "email_case"
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

- iut_type:
  The product / implementation under test if inferable.
  Examples: "controller", "lighting device", "headset", "module", "keyboard", "TV", "medical bed", "USB dongle"
  If unclear, use "".

- customer_question:
  The clearest direct version of what the customer or internal requester is asking.

- question_variants:
  Provide 3 to 6 alternate phrasings of the same issue, only if strongly supported by the thread.
  These should reflect how different people might ask the same question:
  - customer wording
  - sales/support wording
  - consultant wording
  - technical wording
  Keep them concise.
  Do not add variants that introduce new facts.

- actual_issue:
  The real Bluetooth qualification / technical / procedural problem behind the question.

- plain_english_explanation:
  Explain the issue in simple terms for a non-expert in 2 to 4 sentences.
  Make it easy for sales or customer-facing staff to understand.
  Do not use unnecessary jargon.
  Do not dumb it down so much that the technical meaning is lost.

- consultant_answer:
  The consultant’s substantive reasoning, interpretation, or explanation.
  This should preserve the expert logic, not just the conclusion.

- decision_logic:
  State the core reasoning that determines the correct outcome.
  Focus on the rule, dependency, mismatch, eligibility condition, or qualification principle that drives the answer.

- final_recommendation:
  The practical next action for that case.
  This must be action-oriented.

- risk_if_done_wrong:
  Explain the likely failure, delay, rework, rejection, unnecessary testing, or qualification risk if the issue is handled incorrectly.
  Include costs, schedules, test counts, or quotations only if explicitly supported by the thread.

- bluetooth_tags:
  Use 3 to 8 concise tags only if strongly supported.
  Examples:
  "qualification", "listing", "QDID", "EPL", "PTS", "ICS", "IXIT", "RF", "RF PHY", "profile", "GATT", "HCI", "controller", "host", "module", "reuse", "design change", "LE", "LE Audio", "Classic", "test report", "declaration", "IDL", "TCW", "AoA", "AoD", "consistency check"

- search_aliases:
  Provide 5 to 12 short retrieval-friendly phrases, acronyms, or near-synonyms that are strongly supported by the thread.
  These are for search matching, not for prose.
  Examples:
  "QDID combination invalid"
  "consistency check failed"
  "IDL error"
  "AoA mismatch"
  "RF PHY unsupported"
  "TCW not allowed"
  "subset design needed"
  Keep them short.
  Do not invent unsupported aliases.

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

- confidence:
  Must be one of:
  "high"
  "medium"
  "low"

  Use:
  - "high" when the issue, reasoning, and recommendation are explicit in the thread
  - "medium" when part of the case requires strong but reasonable inference
  - "low" when the case is reusable but some important fields are only weakly supported

- source_type:
  Always return "email_case"

Decision policy:
- If the thread is mostly about quotation / scheduling but still includes a real qualification decision, extract the qualification decision as a case.
- Only include iut_type, tags, aliases, and qualification_stage if they are explicitly supported by the thread or are very high-confidence inferences from the thread. Otherwise leave them empty.
- If a thread contains both administrative discussion and a real technical or qualification issue, keep only the reusable consulting issue as a case.
- If a thread contains no reusable Bluetooth consulting issue, return:
  {
    "source_thread": "<thread_id>",
    "cases": []
  }

Quality standard:
- A good output should be directly useful for:
  1. semantic retrieval
  2. keyword retrieval
  3. reranking
  4. grounded answer generation
  5. plain-English explanation to non-experts

Process the attached file now.