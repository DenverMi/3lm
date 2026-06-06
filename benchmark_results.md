# Bluetooth RAG Benchmark Raw Results

## 1. In Bluetooth, what do we need to prepare in the compliance folder?

- Elapsed: 25.12s

```text
🔍 Retrieving relevant evidence...

Top retrieved sources (debug):
- score=19.4164  BT Official FAQ_20260409.md (p.21)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00017  priority=5  kind=body
- score=5.6932  BT Official FAQ_20260409.md (p.3)  id=bluetooth:reference:BT Official FAQ_20260409.md:p00003  priority=6  kind=front_page
- score=3.6110  thread_0037_case_02.json (p.1)  id=bluetooth:email:thread_0037_case_02.json:p00001  priority=1  kind=front_page
- score=3.6056  thread_0072_case_04.json (p.1)  id=bluetooth:email:thread_0072_case_04.json:p00001  priority=1  kind=front_page
- score=2.2109  Allion Internal FAQ.md (p.34)  id=bluetooth:reference:Allion Internal FAQ.md:c00033  priority=5  kind=body
- score=1.1088  thread_analysis_0079.json (p.1)  id=bluetooth:email:thread_analysis_0079.json:p00001  priority=1  kind=front_page
- score=0.4638  BT Qualification Program Reference Document_QPRD_v5.md (p.18)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00017  priority=1  kind=body

Selected sources for model:
- score=0.4638  BT Qualification Program Reference Document_QPRD_v5.md (p.18)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00017  priority=1  kind=body
- score=5.6932  BT Official FAQ_20260409.md (p.3)  id=bluetooth:reference:BT Official FAQ_20260409.md:p00003  priority=6  kind=front_page
- score=2.2109  Allion Internal FAQ.md (p.34)  id=bluetooth:reference:Allion Internal FAQ.md:c00033  priority=5  kind=body
🧠 Building grounded prompt...
🤖 Generating answer with local model...
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-06T16:15:10.269382Z' done=True done_reason='stop' total_duration=10492767417 load_duration=326489792 prompt_eval_count=2069 prompt_eval_duration=1818704000 eval_count=379 eval_duration=8316384000 message=Message(role='assistant', content='A Compliance Folder is a mandatory archive containing qualification evidence that must be retained after product shipment ends. For all Qualified Products, Members must maintain the documentation listed in Table 3.3 in a single location. This documentation must be stored at the time the Member submits the Product to the Bluetooth Qualification Process and must be retained for no less than one year after the Member stops offering the Product for sale or distribution. The Member must also make this documentation available to the Bluetooth SIG for inspection if requested.\n\nThe specific requirements for the Compliance Folder depend on whether a Member uses an existing Design or creates a new Design:\n\n*   **Product details**: Required for both using an existing Design and creating a new Design.\n*   **Design details**: Required for both using an existing Design and creating a new Design.\n*   **Test declaration**: Not applicable (N/A) when using an existing Design; required if a test plan is generated when creating a new Design.\n*   **Test report(s)**: Not applicable (N/A) when using an existing Design; required if a test plan is generated when creating a new Design.\n*   **Test logs**: Not applicable (N/A) when using an existing Design; required if a test plan is generated when creating a new Design.\n*   **TCW**: Not applicable (N/A) when using an existing Design; required as necessary when creating a new Design.\n\nCitations:\n- [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00017 | BT Qualification Program Reference Document_QPRD_v5.md (p.18)]\n- [bluetooth:reference:Allion Internal FAQ.md:c00033 | Allion Internal FAQ.md (p.34)]', thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
DEBUG timing: generate=10.50s
✅ Done.


⏱ Total elapsed: 17.99s
=== ANSWER ===

A Compliance Folder is a mandatory archive containing qualification evidence that must be retained after product shipment ends. For all Qualified Products, Members must maintain the documentation listed in Table 3.3 in a single location. This documentation must be stored at the time the Member submits the Product to the Bluetooth Qualification Process and must be retained for no less than one year after the Member stops offering the Product for sale or distribution. The Member must also make this documentation available to the Bluetooth SIG for inspection if requested.

The specific requirements for the Compliance Folder depend on whether a Member uses an existing Design or creates a new Design:

* **Product details**: Required for both using an existing Design and creating a new Design.
* **Design details**: Required for both using an existing Design and creating a new Design.
* **Test declaration**: Not applicable (N/A) when using an existing Design; required if a test plan is generated when creating a new Design.
* **Test report(s)**: Not applicable (N/A) when using an existing Design; required if a test plan is generated when creating a new Design.
* **Test logs**: Not applicable (N/A) when using an existing Design; required if a test plan is generated when creating a new Design.
* **TCW**: Not applicable (N/A) when using an existing Design; required as necessary when creating a new Design.

Citations:
- [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00017 | BT Qualification Program Reference Document_QPRD_v5.md (p.18)]
- [bluetooth:reference:Allion Internal FAQ.md:c00033 | Allion Internal FAQ.md (p.34)]

=== SOURCES ===

- BT Qualification Program Reference Document_QPRD_v5.md (p.18)  [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00017]  score=0.4638  priority=1
- BT Official FAQ_20260409.md (p.3)  [bluetooth:reference:BT Official FAQ_20260409.md:p00003]  score=5.6932  priority=6
- Allion Internal FAQ.md (p.34)  [bluetooth:reference:Allion Internal FAQ.md:c00033]  score=2.2109  priority=5
```

## 2. Customer asks: If they use a qualified Bluetooth module, do they still need a new qualification?

- Elapsed: 19.21s

```text
🔍 Retrieving relevant evidence...

Top retrieved sources (debug):
- score=5.6912  BT Official FAQ_20260409.md (p.3)  id=bluetooth:reference:BT Official FAQ_20260409.md:p00003  priority=6  kind=front_page
- score=3.6117  thread_0045_case_01.json (p.1)  id=bluetooth:email:thread_0045_case_01.json:p00001  priority=1  kind=front_page
- score=3.6025  thread_0026_case_01.json (p.1)  id=bluetooth:email:thread_0026_case_01.json:p00001  priority=1  kind=front_page
- score=2.2156  Allion Internal FAQ.md (p.6)  id=bluetooth:reference:Allion Internal FAQ.md:c00005  priority=5  kind=body
- score=2.2131  Allion Internal FAQ.md (p.16)  id=bluetooth:reference:Allion Internal FAQ.md:c00015  priority=5  kind=body
- score=1.2636  BT Qualification Program Reference Document_QPRD_v5.md (p.1)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:p00001  priority=2  kind=front_page
- score=1.1020  thread_analysis_0032.json (p.1)  id=bluetooth:email:thread_analysis_0032.json:p00001  priority=1  kind=front_page

Selected sources for model:
- score=5.6912  BT Official FAQ_20260409.md (p.3)  id=bluetooth:reference:BT Official FAQ_20260409.md:p00003  priority=6  kind=front_page
- score=2.2156  Allion Internal FAQ.md (p.6)  id=bluetooth:reference:Allion Internal FAQ.md:c00005  priority=5  kind=body
- score=2.2131  Allion Internal FAQ.md (p.16)  id=bluetooth:reference:Allion Internal FAQ.md:c00015  priority=5  kind=body
🧠 Building grounded prompt...
🤖 Generating answer with local model...
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-06T16:15:29.481141Z' done=True done_reason='stop' total_duration=5902594750 load_duration=300048334 prompt_eval_count=1896 prompt_eval_duration=1453182000 eval_count=178 eval_duration=3765481000 message=Message(role='assistant', content='Yes, you must complete the Bluetooth Qualification Process for your product yourself, as suppliers or other member companies cannot qualify products on your behalf. While using a qualified Bluetooth module may mean that certain layers do not need retesting, testing is still required because the module qualification covers only hardware and low-level functionality. If your product adds or changes profiles, firmware behavior, or host software, then those new or changed layers must be tested, although previously qualified layers are not retested.\n\nCitations:\n[bluetooth:reference:BT Official FAQ_20260409.md:p00003 | BT Official FAQ_20260409.md (p.3)]\n[bluetooth:reference:Allion Internal FAQ.md:c00005 | Allion Internal FAQ.md (p.6)]', thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
DEBUG timing: generate=5.91s
✅ Done.


⏱ Total elapsed: 12.84s
=== ANSWER ===

Yes, you must complete the Bluetooth Qualification Process for your product yourself, as suppliers or other member companies cannot qualify products on your behalf. While using a qualified Bluetooth module may mean that certain layers do not need retesting, testing is still required because the module qualification covers only hardware and low-level functionality. If your product adds or changes profiles, firmware behavior, or host software, then those new or changed layers must be tested, although previously qualified layers are not retested.

Citations:
- [bluetooth:reference:BT Official FAQ_20260409.md:p00003 | BT Official FAQ_20260409.md (p.3)]
- [bluetooth:reference:Allion Internal FAQ.md:c00005 | Allion Internal FAQ.md (p.6)]

=== SOURCES ===

- BT Official FAQ_20260409.md (p.3)  [bluetooth:reference:BT Official FAQ_20260409.md:p00003]  score=5.6912  priority=6
- Allion Internal FAQ.md (p.6)  [bluetooth:reference:Allion Internal FAQ.md:c00005]  score=2.2156  priority=5
- Allion Internal FAQ.md (p.16)  [bluetooth:reference:Allion Internal FAQ.md:c00015]  score=2.2131  priority=5
```

## 3. @ In past Bluetooth cases, if a customer uses a qualified Bluetooth module, did they still need a new qualification?

- Elapsed: 23.26s

```text
📧 Email/case-only mode...

🔍 Retrieving relevant email/case evidence...
🧠 Building email-grounded prompt...
🤖 Generating answer with local model...
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-06T16:15:52.750047Z' done=True done_reason='stop' total_duration=8586298625 load_duration=308015875 prompt_eval_count=2179 prompt_eval_duration=2147929000 eval_count=256 eval_duration=6116218000 message=Message(role='assistant', content="In past cases, using a pre-qualified Bluetooth module does not automatically qualify the final product, and the company selling the final product still needs to complete its own Bluetooth SIG qualification steps and submit the product under the correct Bluetooth SIG member account [bluetooth:email:thread_0045_case_01.json:p00001 | thread_0045_case_01.json (p.1)]. The finished-product brand owner must independently become a Bluetooth SIG member and complete qualification under its own company name, even if manufacturing and payment are handled by an OEM or factory partner [bluetooth:email:thread_analysis_0032.json:p00001 | thread_analysis_0032.json (p.1)]. However, in a specific scenario where a product changed from one supplier's Bluetooth module to another already-qualified module while continuing to use the same Bluetooth version and no new Bluetooth features were being added, no additional Bluetooth qualification procedures were needed [bluetooth:email:thread_0026_case_01.json:p00001 | thread_0026_case_01.json (p.1)].", thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
✅ Done.


⏱ Total elapsed: 16.88s
=== ANSWER ===

In past cases, using a pre-qualified Bluetooth module does not automatically qualify the final product, and the company selling the final product still needs to complete its own Bluetooth SIG qualification steps and submit the product under the correct Bluetooth SIG member account. The finished-product brand owner must independently become a Bluetooth SIG member and complete qualification under its own company name, even if manufacturing and payment are handled by an OEM or factory partner. However, in a specific scenario where a product changed from one supplier's Bluetooth module to another already-qualified module while continuing to use the same Bluetooth version and no new Bluetooth features were being added, no additional Bluetooth qualification procedures were needed.

Citations:
- [bluetooth:email:thread_0045_case_01.json:p00001 | thread_0045_case_01.json (p.1)]
- [bluetooth:email:thread_0026_case_01.json:p00001 | thread_0026_case_01.json (p.1)]
- [bluetooth:email:thread_analysis_0032.json:p00001 | thread_analysis_0032.json (p.1)]

=== SOURCES ===

- thread_0045_case_01.json (p.1)  [bluetooth:email:thread_0045_case_01.json:p00001]  score=3.6056  priority=1
- thread_0026_case_01.json (p.1)  [bluetooth:email:thread_0026_case_01.json:p00001]  score=3.5952  priority=1
- thread_analysis_0032.json (p.1)  [bluetooth:email:thread_analysis_0032.json:p00001]  score=1.1030  priority=1
```

## 4. In Bluetooth, what is TCW?

- Elapsed: 17.20s

```text
🔍 Retrieving relevant evidence...

Top retrieved sources (debug):
- score=44.2934  glossary.md (p.20)  id=bluetooth:reference:glossary.md:c00019  priority=5  kind=body
- score=37.2964  BT Qualification Program Reference Document_QPRD_v5.md (p.4)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00003  priority=1  kind=body
- score=37.2964  BT Qualification Program Reference Document_QPRD_v5.md (p.19)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00018  priority=1  kind=body
- score=9.2762  thread_0035_case_03.json (p.1)  id=bluetooth:email:thread_0035_case_03.json:c00000  priority=0  kind=body
- score=5.3104  BT Official FAQ_20260409.md (p.34)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00030  priority=5  kind=body

Selected sources for model:
- score=44.2934  glossary.md (p.20)  id=bluetooth:reference:glossary.md:c00019  priority=5  kind=body
- score=37.2964  BT Qualification Program Reference Document_QPRD_v5.md (p.19)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00018  priority=1  kind=body
🧠 Building grounded prompt...
🤖 Generating answer with local model...
DEBUG glossary definitions: []
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-06T16:16:09.922635Z' done=True done_reason='stop' total_duration=4913735292 load_duration=320170542 prompt_eval_count=2014 prompt_eval_duration=1704041000 eval_count=132 eval_duration=2866639000 message=Message(role='assistant', content='TCW — Test Coverage Waiver is a waiver granted by Bluetooth SIG allowing specific qualification requirements or test cases to be waived under defined conditions. A valid and approved TCW may be provided by a Member to address inconsistencies identified during the consistency check of an ICS Form.\n\nCitations:\n[bluetooth:reference:glossary.md:c00019 | glossary.md (p.20)]\n[bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00018 | BT Qualification Program Reference Document_QPRD_v5.md (p.19)]', thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
DEBUG timing: generate=4.93s
✅ Done.


⏱ Total elapsed: 10.78s
=== ANSWER ===

TCW — Test Coverage Waiver is a waiver granted by Bluetooth SIG allowing specific qualification requirements or test cases to be waived under defined conditions. A valid and approved TCW may be provided by a Member to address inconsistencies identified during the consistency check of an ICS Form.

Citations:
- [bluetooth:reference:glossary.md:c00019 | glossary.md (p.20)]
- [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00018 | BT Qualification Program Reference Document_QPRD_v5.md (p.19)]

=== SOURCES ===

- glossary.md (p.20)  [bluetooth:reference:glossary.md:c00019]  score=44.2934  priority=5
- BT Qualification Program Reference Document_QPRD_v5.md (p.19)  [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00018]  score=37.2964  priority=1
```

## 5. In Bluetooth, what is the difference between ICS and IXIT?

- Elapsed: 16.81s

```text
🔍 Retrieving relevant evidence...

Top retrieved sources (debug):
- score=36.7787  glossary.md (p.15)  id=bluetooth:reference:glossary.md:c00014  priority=5  kind=body
- score=36.6964  Allion Internal FAQ.md (p.5)  id=bluetooth:reference:Allion Internal FAQ.md:p00005  priority=6  kind=front_page
- score=36.5164  glossary.md (p.13)  id=bluetooth:reference:glossary.md:c00012  priority=5  kind=body
- score=35.9164  Allion Internal FAQ.md (p.28)  id=bluetooth:reference:Allion Internal FAQ.md:c00027  priority=5  kind=body
- score=32.9764  BT Qualification Program Reference Document_QPRD_v5.md (p.4)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:p00004  priority=2  kind=front_page

Selected sources for model:
- score=32.9764  BT Qualification Program Reference Document_QPRD_v5.md (p.4)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:p00004  priority=2  kind=front_page
- score=36.7787  glossary.md (p.15)  id=bluetooth:reference:glossary.md:c00014  priority=5  kind=body
- score=36.6964  Allion Internal FAQ.md (p.5)  id=bluetooth:reference:Allion Internal FAQ.md:p00005  priority=6  kind=front_page
- score=36.5164  glossary.md (p.13)  id=bluetooth:reference:glossary.md:c00012  priority=5  kind=body
- score=37.2964  BT Qualification Program Reference Document_QPRD_v5.md (p.4)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00003  priority=1  kind=body
🧠 Building grounded prompt...
🤖 Generating answer with local model...
DEBUG glossary definitions: []
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-06T16:16:26.776279Z' done=True done_reason='stop' total_duration=3182398334 load_duration=321526209 prompt_eval_count=2873 prompt_eval_duration=137519000 eval_count=116 eval_duration=2474518000 message=Message(role='assistant', content='ICS (Implementation Conformance Statement) is a document produced by the Bluetooth SIG for each Bluetooth Specification that identifies the features of that specification, whereas IXIT (Implementation eXtra Information for Testing) is a form completed by a Member providing additional configuration details to facilitate testing beyond the ICS.\n\nCitations:\n[bluetooth:reference:glossary.md:c00012 | glossary.md (p.13)]\n[bluetooth:reference:glossary.md:c00014 | glossary.md (p.15)]', thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
DEBUG timing: generate=3.19s
✅ Done.


⏱ Total elapsed: 10.43s
=== ANSWER ===

ICS (Implementation Conformance Statement) is a document produced by the Bluetooth SIG for each Bluetooth Specification that identifies the features of that specification, whereas IXIT (Implementation eXtra Information for Testing) is a form completed by a Member providing additional configuration details to facilitate testing beyond the ICS.

Citations:
- [bluetooth:reference:glossary.md:c00014 | glossary.md (p.15)]
- [bluetooth:reference:glossary.md:c00012 | glossary.md (p.13)]

=== SOURCES ===

- BT Qualification Program Reference Document_QPRD_v5.md (p.4)  [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:p00004]  score=32.9764  priority=2
- glossary.md (p.15)  [bluetooth:reference:glossary.md:c00014]  score=36.7787  priority=5
- Allion Internal FAQ.md (p.5)  [bluetooth:reference:Allion Internal FAQ.md:p00005]  score=36.6964  priority=6
- glossary.md (p.13)  [bluetooth:reference:glossary.md:c00012]  score=36.5164  priority=5
- BT Qualification Program Reference Document_QPRD_v5.md (p.4)  [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00003]  score=37.2964  priority=1
```

## 6. In Bluetooth, what is Option 2b?

- Elapsed: 15.22s

```text
🔍 Retrieving relevant evidence...

Top retrieved sources (debug):
- score=28.6964  BT Qualification Program Reference Document_QPRD_v5.md (p.10)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00009  priority=1  kind=body
- score=21.8164  BT Official FAQ_20260409.md (p.18)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00014  priority=5  kind=body
- score=21.8164  BT Official FAQ_20260409.md (p.28)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00024  priority=5  kind=body
- score=19.6964  BT Qualification Program Reference Document_QPRD_v5.md (p.11)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00010  priority=1  kind=body
- score=15.4685  Bluetooth Core Specification_v6.2.md (p.100254)  id=bluetooth:specs:Bluetooth Core Specification_v6.2.md:t100254  priority=4  kind=definition

Selected sources for model:
- score=28.6964  BT Qualification Program Reference Document_QPRD_v5.md (p.10)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00009  priority=1  kind=body
- score=21.8164  BT Official FAQ_20260409.md (p.18)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00014  priority=5  kind=body
- score=21.8164  BT Official FAQ_20260409.md (p.28)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00024  priority=5  kind=body
🧠 Building grounded prompt...
🤖 Generating answer with local model...
DEBUG glossary definitions: []
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-06T16:16:41.877279Z' done=True done_reason='stop' total_duration=3836178292 load_duration=316858250 prompt_eval_count=2394 prompt_eval_duration=176377000 eval_count=140 eval_duration=2967259000 message=Message(role='assistant', content='Option 2b is a process used to create any other new Design. Under this option, using active specifications is allowed, using deprecated specifications is allowed from an included Design, and using withdrawn specifications is not allowed.\n\n[bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00009 | BT Qualification Program Reference Document_QPRD_v5.md (p.10)]\n[bluetooth:reference:BT Official FAQ_20260409.md:c00014 | BT Official FAQ_20260409.md (p.18)]', thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
DEBUG timing: generate=3.84s
✅ Done.


⏱ Total elapsed: 8.95s
=== ANSWER ===

Option 2b is a process used to create any other new Design. Under this option, using active specifications is allowed, using deprecated specifications is allowed from an included Design, and using withdrawn specifications is not allowed.

Citations:
- [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00009 | BT Qualification Program Reference Document_QPRD_v5.md (p.10)]
- [bluetooth:reference:BT Official FAQ_20260409.md:c00014 | BT Official FAQ_20260409.md (p.18)]

=== SOURCES ===

- BT Qualification Program Reference Document_QPRD_v5.md (p.10)  [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00009]  score=28.6964  priority=1
- BT Official FAQ_20260409.md (p.18)  [bluetooth:reference:BT Official FAQ_20260409.md:c00014]  score=21.8164  priority=5
- BT Official FAQ_20260409.md (p.28)  [bluetooth:reference:BT Official FAQ_20260409.md:c00024]  score=21.8164  priority=5
```

## 7. In Bluetooth, what is the difference between Option 2a and Option 2b?

- Elapsed: 19.99s

```text
🔍 Retrieving relevant evidence...

Top retrieved sources (debug):
- score=36.6964  Allion Internal FAQ.md (p.5)  id=bluetooth:reference:Allion Internal FAQ.md:p00005  priority=6  kind=front_page
- score=35.9164  Allion Internal FAQ.md (p.28)  id=bluetooth:reference:Allion Internal FAQ.md:c00027  priority=5  kind=body
- score=23.6964  BT Qualification Program Reference Document_QPRD_v5.md (p.9)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00008  priority=1  kind=body
- score=23.6964  BT Qualification Program Reference Document_QPRD_v5.md (p.10)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00009  priority=1  kind=body
- score=22.4164  BT Official FAQ_20260409.md (p.27)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00023  priority=5  kind=body

Selected sources for model:
- score=23.6964  BT Qualification Program Reference Document_QPRD_v5.md (p.10)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00009  priority=1  kind=body
- score=23.6964  BT Qualification Program Reference Document_QPRD_v5.md (p.9)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00008  priority=1  kind=body
- score=36.6964  Allion Internal FAQ.md (p.5)  id=bluetooth:reference:Allion Internal FAQ.md:p00005  priority=6  kind=front_page
- score=35.9164  Allion Internal FAQ.md (p.28)  id=bluetooth:reference:Allion Internal FAQ.md:c00027  priority=5  kind=body
- score=44.3140  glossary.md (p.5)  id=bluetooth:reference:glossary.md:c00004  priority=5  kind=body
🧠 Building grounded prompt...
🤖 Generating answer with local model...
DEBUG glossary definitions: []
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-06T16:17:01.994696Z' done=True done_reason='stop' total_duration=6348675667 load_duration=327441584 prompt_eval_count=2968 prompt_eval_duration=674566000 eval_count=236 eval_duration=5053179000 message=Message(role='assistant', content='Option 2a involves creating a new Design by combining two or more unmodified Designs that have DNs or QDIDs into one of the permitted combinations, requiring the Member to provide the DNs or QDIDs for included Designs, the desired Core Configuration, and the active TCRL Package version used for checking the applicable Core Configuration and evaluating test requirements. In contrast, Option 2b involves creating any other new Design, which requires a Member to provide the DN(s) or QDID(s) for any included Designs, an active TCRL Package version, and an ICS Form for each new Layer implemented in the new Design or for each modified Layer based on an included Design.\n\nCitations:\n[bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00008 | BT Qualification Program Reference Document_QPRD_v5.md (p.9)]\n[bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00009 | BT Qualification Program Reference Document_QPRD_v5.md (p.10)]', thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
DEBUG timing: generate=6.36s
✅ Done.


⏱ Total elapsed: 13.63s
=== ANSWER ===

Option 2a involves creating a new Design by combining two or more unmodified Designs that have DNs or QDIDs into one of the permitted combinations, requiring the Member to provide the DNs or QDIDs for included Designs, the desired Core Configuration, and the active TCRL Package version used for checking the applicable Core Configuration and evaluating test requirements. In contrast, Option 2b involves creating any other new Design, which requires a Member to provide the DN(s) or QDID(s) for any included Designs, an active TCRL Package version, and an ICS Form for each new Layer implemented in the new Design or for each modified Layer based on an included Design.

Citations:
- [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00009 | BT Qualification Program Reference Document_QPRD_v5.md (p.10)]
- [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00008 | BT Qualification Program Reference Document_QPRD_v5.md (p.9)]

=== SOURCES ===

- BT Qualification Program Reference Document_QPRD_v5.md (p.10)  [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00009]  score=23.6964  priority=1
- BT Qualification Program Reference Document_QPRD_v5.md (p.9)  [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00008]  score=23.6964  priority=1
- Allion Internal FAQ.md (p.5)  [bluetooth:reference:Allion Internal FAQ.md:p00005]  score=36.6964  priority=6
- Allion Internal FAQ.md (p.28)  [bluetooth:reference:Allion Internal FAQ.md:c00027]  score=35.9164  priority=5
- glossary.md (p.5)  [bluetooth:reference:glossary.md:c00004]  score=44.3140  priority=5
```

## 8. BluetoothのQualificationで、Compliance Folderには何を入れる必要がありますか？

- Elapsed: 19.74s

```text
🔍 Retrieving relevant evidence...

Top retrieved sources (debug):
- score=42.9613  BT Qualification Program Reference Document_QPRD_v5.md (p.18)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00017  priority=1  kind=body
- score=35.9164  Allion Internal FAQ.md (p.20)  id=bluetooth:reference:Allion Internal FAQ.md:c00019  priority=5  kind=body
- score=35.9164  Allion Internal FAQ.md (p.33)  id=bluetooth:reference:Allion Internal FAQ.md:c00032  priority=5  kind=body
- score=35.9164  BT Official FAQ_20260409.md (p.11)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00007  priority=5  kind=body
- score=34.9624  glossary.md (p.1)  id=bluetooth:reference:glossary.md:p00001  priority=6  kind=front_page

Selected sources for model:
- score=42.9613  BT Qualification Program Reference Document_QPRD_v5.md (p.18)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00017  priority=1  kind=body
- score=35.9164  Allion Internal FAQ.md (p.20)  id=bluetooth:reference:Allion Internal FAQ.md:c00019  priority=5  kind=body
- score=35.9164  Allion Internal FAQ.md (p.33)  id=bluetooth:reference:Allion Internal FAQ.md:c00032  priority=5  kind=body
🧠 Building grounded prompt...
🤖 Generating answer with local model...
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-06T16:17:21.727299Z' done=True done_reason='stop' total_duration=7290606917 load_duration=476522584 prompt_eval_count=1953 prompt_eval_duration=161073000 eval_count=296 eval_duration=6350156000 message=Message(role='assistant', content='すべてのQualified Productsにおいて、MembersはTable 3.3に記載されたドキュメントを単一の場所（一般的に「Compliance Folder」と呼ばれます）で維持する必要があります。ドキュケーションは、MemberがProductをBluetooth Qualification Processに提出する時点で保存されている必要があり、また、MemberがProductの販売または配布を停止した後、少なくとも1年間保持しなければなりません。また、MemberはBluetooth SIGからの要請があった場合、検査のためにドキュメントを利用可能な状態にしておく必要があります。Compliance Folderに必要な内容は以下の通りです。\n\n| Compliance Folder | Use a single existing Design | Create a new Design |\n| :--- | :--- | :--- |\n| Requirements | (Section 3.2.1) | (Section 3.2.2) |\n| Product details | Required | Required |\n| Design details | Required | Required |\n| Test declaration | N/A | Required if test plan is generated |\n| Test report(s) | N/A | Required if test plan is generated |\n| Test logs | N/A | Required if test plan is generated |\n| TCW | N/A | As required |\n\nCitations:\n- [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00017 | BT Qualification Program Reference Document_QPRD_v5.md (p.18)]', thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
DEBUG timing: generate=7.30s
✅ Done.


⏱ Total elapsed: 13.42s
=== ANSWER ===

すべてのQualified Productsにおいて、MembersはTable 3.3に記載されたドキュメントを単一の場所（一般的に「Compliance Folder」と呼ばれます）で維持する必要があります。ドキュケーションは、MemberがProductをBluetooth Qualification Processに提出する時点で保存されている必要があり、また、MemberがProductの販売または配布を停止した後、少なくとも1年間保持しなければなりません。また、MemberはBluetooth SIGからの要請があった場合、検査のためにドキュメントを利用可能な状態にしておく必要があります。Compliance Folderに必要な内容は以下の通りです。

| Compliance Folder | Use a single existing Design | Create a new Design |
|:--- |:--- |:--- |
| Requirements | (Section 3.2.1) | (Section 3.2.2) |
| Product details | Required | Required |
| Design details | Required | Required |
| Test declaration | N/A | Required if test plan is generated |
| Test report(s) | N/A | Required if test plan is generated |
| Test logs | N/A | Required if test plan is generated |
| TCW | N/A | As required |

Citations:
- [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00017 | BT Qualification Program Reference Document_QPRD_v5.md (p.18)]

=== SOURCES ===

- BT Qualification Program Reference Document_QPRD_v5.md (p.18)  [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00017]  score=42.9613  priority=1
- Allion Internal FAQ.md (p.20)  [bluetooth:reference:Allion Internal FAQ.md:c00019]  score=35.9164  priority=5
- Allion Internal FAQ.md (p.33)  [bluetooth:reference:Allion Internal FAQ.md:c00032]  score=35.9164  priority=5
```

## 9. Bluetoothで認証済みモジュールを使う場合、新しい認証は必要ですか？

- Elapsed: 20.49s

```text
🔍 Retrieving relevant evidence...

Top retrieved sources (debug):
- score=19.7148  BT Official FAQ_20260409.md (p.21)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00017  priority=5  kind=body
- score=5.6930  BT Official FAQ_20260409.md (p.3)  id=bluetooth:reference:BT Official FAQ_20260409.md:p00003  priority=6  kind=front_page
- score=3.5996  thread_0045_case_01.json (p.1)  id=bluetooth:email:thread_0045_case_01.json:p00001  priority=1  kind=front_page
- score=3.2964  thread_0080_case_02.json (p.1)  id=bluetooth:email:thread_0080_case_02.json:p00001  priority=1  kind=front_page
- score=1.8011  glossary.md (p.10)  id=bluetooth:reference:glossary.md:c00009  priority=5  kind=body
- score=1.7951  glossary.md (p.11)  id=bluetooth:reference:glossary.md:c00010  priority=5  kind=body
- score=1.7522  Bluetooth チャンネル・サウンディング_技術概要.md (p.1)  id=bluetooth:reference:Bluetooth チャンネル・サウンディング_技術概要.md:p00001  priority=3  kind=front_page
- score=1.3259  Bluetooth チャンネル・サウンディング_技術概要.md (p.1)  id=bluetooth:reference:Bluetooth チャンネル・サウンディング_技術概要.md:c00008  priority=2  kind=body
- score=1.3225  Bluetooth Channel Sounding_Technical overview.md (p.1)  id=bluetooth:reference:Bluetooth Channel Sounding_Technical overview.md:c00003  priority=2  kind=body
- score=1.3210  Bluetooth Channel Sounding_Technical overview.md (p.1)  id=bluetooth:reference:Bluetooth Channel Sounding_Technical overview.md:c00013  priority=2  kind=body

Selected sources for model:
- score=5.6930  BT Official FAQ_20260409.md (p.3)  id=bluetooth:reference:BT Official FAQ_20260409.md:p00003  priority=6  kind=front_page
- score=3.5996  thread_0045_case_01.json (p.1)  id=bluetooth:email:thread_0045_case_01.json:p00001  priority=1  kind=front_page
🧠 Building grounded prompt...
🤖 Generating answer with local model...
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-06T16:17:42.218105Z' done=True done_reason='stop' total_duration=6787567333 load_duration=306406541 prompt_eval_count=1915 prompt_eval_duration=1856064000 eval_count=206 eval_duration=4413982000 message=Message(role='assistant', content='はい、新しい認証が必要です。認証済みのBluetoothモジュールを使用している場合でも、最終製品のBluetooth SIG認証は自動的には完了しません。最終製品を販売または配布する企業は、自社でBluetooth Qualification Processを完了させる必要があります。この際、適切なBluetooth SIGメンバーアカウントの下で製品を申請し、不必要な再試験を避けるために、適切なドキュメントや設計リファレンスを準備する必要があります。なお、サプライヤーや他の加盟企業が、あなたの代わりに製品の認証を行うことはできません。\n\nCitations:\n- [bluetooth:reference:BT Official FAQ_20260409.md:p00003 | BT Official FAQ_20260409.md (p.3)]\n- [bluetooth:email:thread_0045_case_01.json:p00001 | thread_0045_case_01.json (p.1)]', thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
DEBUG timing: generate=6.79s
✅ Done.


⏱ Total elapsed: 14.07s
=== ANSWER ===

はい、新しい認証が必要です。認証済みのBluetoothモジュールを使用している場合でも、最終製品のBluetooth SIG認証は自動的には完了しません。最終製品を販売または配布する企業は、自社でBluetooth Qualification Processを完了させる必要があります。この際、適切なBluetooth SIGメンバーアカウントの下で製品を申請し、不必要な再試験を避けるために、適切なドキュメントや設計リファレンスを準備する必要があります。なお、サプライヤーや他の加盟企業が、あなたの代わりに製品の認証を行うことはできません。

Citations:
- [bluetooth:reference:BT Official FAQ_20260409.md:p00003 | BT Official FAQ_20260409.md (p.3)]
- [bluetooth:email:thread_0045_case_01.json:p00001 | thread_0045_case_01.json (p.1)]

=== SOURCES ===

- BT Official FAQ_20260409.md (p.3)  [bluetooth:reference:BT Official FAQ_20260409.md:p00003]  score=5.6930  priority=6
- thread_0045_case_01.json (p.1)  [bluetooth:email:thread_0045_case_01.json:p00001]  score=3.5996  priority=1
```

## 10. BluetoothでTCWとは何ですか？

- Elapsed: 15.70s

```text
🔍 Retrieving relevant evidence...

Top retrieved sources (debug):
- score=41.0164  glossary.md (p.20)  id=bluetooth:reference:glossary.md:c00019  priority=5  kind=body
- score=34.2964  BT Qualification Program Reference Document_QPRD_v5.md (p.4)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00003  priority=1  kind=body
- score=34.2964  BT Qualification Program Reference Document_QPRD_v5.md (p.19)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00018  priority=1  kind=body
- score=2.5592  BT Official FAQ_20260409.md (p.1)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00000  priority=5  kind=body
- score=2.3103  BT Official FAQ_20260409.md (p.25)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00021  priority=5  kind=body

Selected sources for model:
- score=41.0164  glossary.md (p.20)  id=bluetooth:reference:glossary.md:c00019  priority=5  kind=body
- score=2.5592  BT Official FAQ_20260409.md (p.1)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00000  priority=5  kind=body
🧠 Building grounded prompt...
🤖 Generating answer with local model...
DEBUG glossary definitions: []
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-06T16:17:57.856068Z' done=True done_reason='stop' total_duration=3280718917 load_duration=618719292 prompt_eval_count=1611 prompt_eval_duration=1210508000 eval_count=68 eval_duration=1427929000 message=Message(role='assistant', content='TCW（Test Coverage Waiver）とは、定義された条件下において、特定の適合性要件またはテストケースの免除を認めるBluetooth SIGによるウェイバー（免除）のことです。\n\n[bluetooth:reference:glossary.md:c00019 | glossary.md (p.20)]', thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
DEBUG timing: generate=3.29s
✅ Done.


⏱ Total elapsed: 9.21s
=== ANSWER ===

TCW（Test Coverage Waiver）とは、定義された条件下において、特定の適合性要件またはテストケースの免除を認めるBluetooth SIGによるウェイバー（免除）のことです。

Citations:
- [bluetooth:reference:glossary.md:c00019 | glossary.md (p.20)]

=== SOURCES ===

- glossary.md (p.20)  [bluetooth:reference:glossary.md:c00019]  score=41.0164  priority=5
- BT Official FAQ_20260409.md (p.1)  [bluetooth:reference:BT Official FAQ_20260409.md:c00000]  score=2.5592  priority=5
```

## 11. BluetoothでICSとは何ですか？

- Elapsed: 16.09s

```text
🔍 Retrieving relevant evidence...

Top retrieved sources (debug):
- score=41.0164  glossary.md (p.13)  id=bluetooth:reference:glossary.md:c00012  priority=5  kind=body
- score=36.5764  Host Controller Interface_TS.md (pp.3-6)  id=bluetooth:specs:Host Controller Interface_TS.md:c00025  priority=2  kind=body
- score=36.5764  Host Controller Interface_TS.md (pp.6-10)  id=bluetooth:specs:Host Controller Interface_TS.md:c00026  priority=2  kind=body
- score=34.2964  BT Qualification Program Reference Document_QPRD_v5.md (p.4)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00003  priority=1  kind=body
- score=34.2964  BT Qualification Program Reference Document_QPRD_v5.md (p.19)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00018  priority=1  kind=body

Selected sources for model:
- score=41.0164  glossary.md (p.13)  id=bluetooth:reference:glossary.md:c00012  priority=5  kind=body
- score=34.2964  BT Qualification Program Reference Document_QPRD_v5.md (p.19)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00018  priority=1  kind=body
🧠 Building grounded prompt...
🤖 Generating answer with local model...
DEBUG glossary definitions: []
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-06T16:18:14.00984Z' done=True done_reason='stop' total_duration=3952666958 load_duration=618628750 prompt_eval_count=2016 prompt_eval_duration=2152500000 eval_count=55 eval_duration=1167244000 message=Message(role='assistant', content='ICS — Implementation Conformance Statementとは、各Bluetooth Specificationの機能を示すためにBluetooth SIGによって作成される文書です。\n\nCitations:\n[bluetooth:reference:glossary.md:c00012 | glossary.md (p.13)]', thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
DEBUG timing: generate=3.96s
✅ Done.


⏱ Total elapsed: 9.80s
=== ANSWER ===

ICS — Implementation Conformance Statementとは、各Bluetooth Specificationの機能を示すためにBluetooth SIGによって作成される文書です。

Citations:
- [bluetooth:reference:glossary.md:c00012 | glossary.md (p.13)]

=== SOURCES ===

- glossary.md (p.13)  [bluetooth:reference:glossary.md:c00012]  score=41.0164  priority=5
- BT Qualification Program Reference Document_QPRD_v5.md (p.19)  [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00018]  score=34.2964  priority=1
```

## 12. BluetoothでIXITとは何ですか？

- Elapsed: 16.12s

```text
🔍 Retrieving relevant evidence...

Top retrieved sources (debug):
- score=41.0164  glossary.md (p.15)  id=bluetooth:reference:glossary.md:c00014  priority=5  kind=body
- score=36.5764  Baseband_TS.md (pp.5-13)  id=bluetooth:specs:Baseband_TS.md:c00011  priority=2  kind=body
- score=36.5764  Security_Manager_TS.md (pp.7-15)  id=bluetooth:specs:Security_Manager_TS.md:c00007  priority=2  kind=body
- score=34.2964  BT Qualification Program Reference Document_QPRD_v5.md (p.4)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00003  priority=1  kind=body
- score=34.2964  BT Qualification Program Reference Document_QPRD_v5.md (p.19)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00018  priority=1  kind=body

Selected sources for model:
- score=41.0164  glossary.md (p.15)  id=bluetooth:reference:glossary.md:c00014  priority=5  kind=body
- score=36.5764  Baseband_TS.md (pp.5-13)  id=bluetooth:specs:Baseband_TS.md:c00011  priority=2  kind=body
🧠 Building grounded prompt...
🤖 Generating answer with local model...
DEBUG glossary definitions: []
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-06T16:18:30.130767Z' done=True done_reason='stop' total_duration=4217829959 load_duration=610109125 prompt_eval_count=2163 prompt_eval_duration=2182335000 eval_count=67 eval_duration=1405420000 message=Message(role='assistant', content='IXIT（Implementation eXtra Information for Testing）とは、ICSを超えたテストを容易にするために、追加の構成詳細を提供するMemberによって記入されるフォームのことです。\n\nCitations:\n[bluetooth:reference:glossary.md:c00014 | glossary.md (p.15)]', thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
DEBUG timing: generate=4.22s
✅ Done.


⏱ Total elapsed: 10.03s
=== ANSWER ===

IXIT（Implementation eXtra Information for Testing）とは、ICSを超えたテストを容易にするために、追加の構成詳細を提供するMemberによって記入されるフォームのことです。

Citations:
- [bluetooth:reference:glossary.md:c00014 | glossary.md (p.15)]

=== SOURCES ===

- glossary.md (p.15)  [bluetooth:reference:glossary.md:c00014]  score=41.0164  priority=5
- Baseband_TS.md (pp.5-13)  [bluetooth:specs:Baseband_TS.md:c00011]  score=36.5764  priority=2
```
