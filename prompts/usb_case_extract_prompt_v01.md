Read the attached MD file and extract retrieval-optimized reusable USB consulting cases from it.

The attached MD file contains one email thread.
The attached MD file is the ONLY allowed source.
All reasoning, extraction, and conclusions must come from the FULL contents of the attached MD thread.

Important:

* One thread may contain one or more distinct USB consulting cases.
* If the thread contains multiple clearly different reusable issues, output multiple cases.
* If the thread contains only one main reusable issue, output one case.
* If the thread contains no reusable USB consulting knowledge, output an empty cases array.

Your goal:

* Understand the thread
* Identify each distinct reusable USB certification / compliance / testing / technical / procedural issue
* Convert each issue into a standalone RAG-friendly case record
* Preserve consultant reasoning
* Preserve practical actionability
* Improve future retrieval by including alternate phrasings, plain-English explanation, and search aliases
* Remove customer-specific details
* Resolve conflicting intermediate conclusions into the final authoritative outcome
* Output JSON only

Rules:

1. Output valid JSON only.
2. Do not use markdown fences.
3. Do not explain anything outside the JSON.
4. Write all values in English unless a Japanese technical phrase is necessary for accuracy.
5. Redact sensitive details:

   * person names -> [PERSON]
   * company names -> [COMPANY]
   * email addresses -> [EMAIL]
   * URLs -> [URL]
   * product IDs / quote numbers / project codes -> [ID]
6. Ignore greetings, signatures, disclaimers, and duplicated quoted history only after confirming they do not contain additional decision logic, corrections, customer confirmations, or final outcomes.
7. If the consultant answer is spread across multiple messages, combine it into one coherent answer.
8. If a field is unknown, use an empty string or an empty array, as appropriate.
9. Do not infer missing emails, attachments, screenshots, test reports, certificates, or technical evidence that are not explicitly visible in the thread.
10. Only create separate cases when the issues are meaningfully distinct and reusable on their own. Prefer fewer high-quality atomic cases over many overlapping cases extracted from the same discussion.
11. Keep each case atomic. Do not mix unrelated issues into one case.
12. Prefer USB certification, compliance, test, and implementation meaning over generic business summarization.
13. Make each case independently understandable and independently retrievable without requiring the full thread.
14. Use wording that helps both semantic search and keyword search.
15. Include both technical terminology and plain-English phrasing when strongly supported by the thread.
16. Do not invent alternative phrasings that change the meaning of the case.
17. Do not invent risks, costs, timelines, or test counts unless explicitly supported by the thread or directly implied by the certification or testing outcome.
18. Later messages override earlier assumptions, drafts, tentative conclusions, or superseded internal discussions.
19. Keep wording concise, dense, and reusable.
20. Do not infer thread structure, outcomes, or case boundaries from snippets, previews, or partial retrieval context. Analyze the complete thread before extracting cases.

Output each case into the following file pattern:
/output/cases/
<source_thread>_case_01.json
<source_thread>_case_02.json
<source_thread>_case_03.json

Return this exact schema:

{
"source_thread": "",
"case_id": "",
"source_type": "email_case",
"program": "USB",
"iut_type": "",
"customer_question": "",
"question_variants": [],
"actual_issue": "",
"plain_english_explanation": "",
"consultant_answer": "",
"decision_logic": "",
"final_recommendation": "",
"risk_if_done_wrong": "",
"program_tags": [],
"search_aliases": [],
"qualification_stage": "",
"confidence": ""
}

Field rules:

* source_thread:
  Read the value directly from the attached MD file's "thread_id" field.
  Copy it exactly as-is.
  Do not infer it from the filename.
  Do not change it.
  Do not renumber it.

* case_id:
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

* source_type:
  Always return "email_case".

* program:
  Always return "USB".

* iut_type:
  The product / implementation under test if inferable.
  Examples: "USB device", "USB host", "USB hub", "USB-C cable", "USB-C adapter", "USB PD charger", "dock", "monitor", "laptop", "peripheral", "embedded device", "USB dongle".
  If unclear, use "".

* customer_question:
  The clearest direct version of what the customer or internal requester is asking.

* question_variants:
  Provide 3 to 6 alternate phrasings of the same issue, only if strongly supported by the thread.
  These should reflect how different people might ask the same question:

  * customer wording
  * sales/support wording
  * consultant wording
  * technical wording
    Keep them concise.
    Do not add variants that introduce new facts.

* actual_issue:
  The real USB certification / compliance / testing / technical / procedural problem behind the question.

* plain_english_explanation:
  Explain the issue in simple terms for a non-expert in 2 to 4 sentences.
  Make it easy for sales or customer-facing staff to understand.
  Do not use unnecessary jargon.
  Do not dumb it down so much that the technical meaning is lost.

* consultant_answer:
  The consultant’s substantive reasoning, interpretation, or explanation.
  This should preserve the expert logic, not just the conclusion.

* decision_logic:
  State the core reasoning that determines the correct outcome.
  Focus on the rule, dependency, mismatch, eligibility condition, test requirement, evidence requirement, certification principle, or procedural condition that drives the answer.

* final_recommendation:
  The practical next action for that case.
  This must be action-oriented.

* risk_if_done_wrong:
  Explain the likely failure, delay, rework, rejection, unnecessary testing, certification risk, compliance risk, or customer-facing risk if the issue is handled incorrectly.
  Include costs, schedules, test counts, or quotations only if explicitly supported by the thread.

* program_tags:
  Use 3 to 8 concise tags only if strongly supported.
  Examples:
  "USB", "USB-IF", "USB-C", "USB Type-C", "USB PD", "PD controller", "hub", "host", "device", "dock", "charger", "cable", "connector", "logo usage", "certification", "compliance testing", "test report", "test log", "interoperability", "TID", "XID", "VID", "PID", "e-marker", "alternate mode", "DisplayPort Alt Mode", "power delivery", "electrical test", "protocol test", "compliance checklist"

* search_aliases:
  Provide 5 to 12 short retrieval-friendly phrases, acronyms, or near-synonyms that are strongly supported by the thread.
  These are for search matching, not for prose.
  Examples:
  "USB certification issue"
  "USB-IF compliance question"
  "USB-C test failure"
  "USB PD test report"
  "Type-C connector compliance"
  "USB logo usage"
  "USB test evidence"
  "USB hub certification"
  "USB PD controller issue"
  "VID PID question"
  "TID reuse"
  "USB retest needed"
  Keep them short.
  Do not invent unsupported aliases.

* qualification_stage:
  Must be one of:
  "pre-sales"
  "planning"
  "implementation"
  "pre-test review"
  "testing"
  "test failure"
  "certification / listing"
  "post-launch change"

* confidence:
  Must be one of:
  "high"
  "medium"
  "low"

  Use:

  * "high" when the issue, reasoning, and recommendation are explicit in the thread
  * "medium" when part of the case requires strong but reasonable inference
  * "low" when the case is reusable but some important fields are only weakly supported

Decision policy:

* If the thread is mostly about quotation / scheduling but still includes a real USB certification, compliance, testing, or implementation decision, extract that decision as a case.
* Only include iut_type, tags, aliases, and qualification_stage if they are explicitly supported by the thread or are very high-confidence inferences from the thread. Otherwise leave them empty.
* If a thread contains both administrative discussion and a real technical, certification, compliance, or testing issue, keep only the reusable consulting issue as a case.
* If a thread contains no reusable USB consulting issue, return:
  {
  "source_thread": "<thread_id>",
  "cases": []
  }

Thread completeness requirements:

* Read and process the FULL attached MD thread before generating output.
* Do not rely only on preview snippets, truncated excerpts, search snippets, or partial context windows.
* Parse the entire messages array in the attached MD file.
* Review all messages before deciding how many cases exist.
* Cases may depend on information spread across multiple emails.
* Do not generate output until the entire thread has been analyzed.
* If only a partial thread is visible, continue reading the file until the full thread is available.
* Output is invalid if source_thread or case reasoning is derived from filename, preview text, or partial snippets instead of the full JSON content.

Final-state resolution policy:

* When determining the final recommendation or final issue state:

  1. Prefer explicit customer confirmation
  2. Then explicit consultant conclusion
  3. Then latest corrected internal decision
  4. Ignore superseded earlier assumptions or draft conclusions
* If the thread contains conflicting intermediate conclusions, extract the final resolved outcome.

Quality standard:

* A good output should be directly useful for:

  1. semantic retrieval
  2. keyword retrieval
  3. reranking
  4. grounded answer generation
  5. plain-English explanation to non-experts

Process the next file now:
