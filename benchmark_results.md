# Bluetooth RAG Benchmark Raw Results

## 1. In Bluetooth, what do we need to prepare in the compliance folder?

- Elapsed: 23.48s
- Ollama total: 8.79s
- Ollama load: 0.34s
- Prompt eval: 2.53s
- Token eval: 5.91s

```text
🔍 Retrieving relevant evidence...

Top retrieved sources (debug):
- score=19.4164  BT Official FAQ_20260409.md (p.21)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00017  priority=5  kind=body
- score=5.6937  BT Official FAQ_20260409.md (p.3)  id=bluetooth:reference:BT Official FAQ_20260409.md:p00003  priority=6  kind=front_page
- score=3.6086  thread_0037_case_02.json (p.1)  id=bluetooth:email:thread_0037_case_02.json:p00001  priority=1  kind=front_page
- score=3.6037  thread_0116_case_05.json (p.1)  id=bluetooth:email:thread_0116_case_05.json:p00001  priority=1  kind=front_page
- score=2.2109  Allion Internal FAQ.md (p.34)  id=bluetooth:reference:Allion Internal FAQ.md:c00033  priority=5  kind=body
- score=1.1085  thread_analysis_0079.json (p.1)  id=bluetooth:email:thread_analysis_0079.json:p00001  priority=1  kind=front_page
- score=0.7893  thread_0138_analysis.json (p.1)  id=bluetooth:email:thread_0138_analysis.json:p00001  priority=1  kind=front_page
- score=0.4992  BT Qualification Program Reference Document_QPRD_v5.md (p.6)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00005  priority=1  kind=body
- score=0.4961  BT Qualification Program Reference Document_QPRD_v5.md (p.21)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00020  priority=1  kind=body
- score=0.3619  thread_0127_analysis.json (p.1)  id=bluetooth:email:thread_0127_analysis.json:c00000  priority=0  kind=body

Selected sources for model:
- score=0.4992  BT Qualification Program Reference Document_QPRD_v5.md (p.6)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00005  priority=1  kind=body
- score=0.4961  BT Qualification Program Reference Document_QPRD_v5.md (p.21)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00020  priority=1  kind=body
- score=5.6937  BT Official FAQ_20260409.md (p.3)  id=bluetooth:reference:BT Official FAQ_20260409.md:p00003  priority=6  kind=front_page
🧠 Building grounded prompt...
🤖 Generating answer with local model...
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-17T09:20:42.553198Z' done=True done_reason='stop' total_duration=8785953833 load_duration=340640250 prompt_eval_count=2514 prompt_eval_duration=2528945000 eval_count=281 eval_duration=5914573000 message=Message(role='assistant', content='For all Qualified Products, Members must maintain documentation listed in Table 3.3 in a single location, commonly referred to as the “Compliance Folder”. Documentation must be stored at the time the Member submits the Product to the Bluetooth Qualification Process and must be retained for no less than one year after the Member stops offering the Product for sale or distribution. The Member is also required to make this documentation available to the Bluetooth SIG for inspection if requested.\n\nThe specific requirements for the Compliance Folder are as follows:\n\n| Compliance Folder Requirements | Use a single existing Design (Section 3.2.1) | Create a new Design (Section 3.2.2) |\n| :--- | :--- | :--- |\n| Product details | Required | Required |\n| Design details | Required | Required |\n| Test declaration | N/A | Required if test plan is generated |\n| Test report(s) | N/A | Required if test plan is generated |\n| Test logs | N/A | Required if test plan is generated |\n| TCW | N/A | As required |\n\nCitations:\n- [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00020 | BT Qualification Program Reference Document_QPRD_v5.md (p.21)]', thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
DEBUG timing: generate=8.79s
✅ Done.


⏱ Total elapsed: 16.39s
=== ANSWER ===

For all Qualified Products, Members must maintain documentation listed in Table 3.3 in a single location, commonly referred to as the “Compliance Folder”. Documentation must be stored at the time the Member submits the Product to the Bluetooth Qualification Process and must be retained for no less than one year after the Member stops offering the Product for sale or distribution. The Member is also required to make this documentation available to the Bluetooth SIG for inspection if requested.

The specific requirements for the Compliance Folder are as follows:

| Compliance Folder Requirements | Use a single existing Design (Section 3.2.1) | Create a new Design (Section 3.2.2) |
|:--- |:--- |:--- |
| Product details | Required | Required |
| Design details | Required | Required |
| Test declaration | N/A | Required if test plan is generated |
| Test report(s) | N/A | Required if test plan is generated |
| Test logs | N/A | Required if test plan is generated |
| TCW | N/A | As required |

Citations:
- [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00020 | BT Qualification Program Reference Document_QPRD_v5.md (p.21)]

=== SOURCES ===

- BT Qualification Program Reference Document_QPRD_v5.md (p.21)  [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00020]  score=0.4961  priority=1
```

## 2. Customer asks: If they use a qualified Bluetooth module, do they still need a new qualification?

- Elapsed: 23.69s
- Ollama total: 8.84s
- Ollama load: 0.35s
- Prompt eval: 2.00s
- Token eval: 6.27s

```text
🔍 Retrieving relevant evidence...

Top retrieved sources (debug):
- score=5.6918  BT Official FAQ_20260409.md (p.3)  id=bluetooth:reference:BT Official FAQ_20260409.md:p00003  priority=6  kind=front_page
- score=3.6113  thread_0045_case_01.json (p.1)  id=bluetooth:email:thread_0045_case_01.json:p00001  priority=1  kind=front_page
- score=3.2964  thread_0034_case_01.json (p.1)  id=bluetooth:email:thread_0034_case_01.json:p00001  priority=1  kind=front_page
- score=2.2156  Allion Internal FAQ.md (p.6)  id=bluetooth:reference:Allion Internal FAQ.md:c00005  priority=5  kind=body
- score=2.2128  Allion Internal FAQ.md (p.16)  id=bluetooth:reference:Allion Internal FAQ.md:c00015  priority=5  kind=body
- score=1.0953  thread_analysis_0065.json (p.1)  id=bluetooth:email:thread_analysis_0065.json:p00001  priority=1  kind=front_page
- score=0.4912  BT Qualification Program Reference Document_QPRD_v5.md (p.7)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00006  priority=1  kind=body

Selected sources for model:
- score=0.4912  BT Qualification Program Reference Document_QPRD_v5.md (p.7)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00006  priority=1  kind=body
- score=5.6918  BT Official FAQ_20260409.md (p.3)  id=bluetooth:reference:BT Official FAQ_20260409.md:p00003  priority=6  kind=front_page
- score=2.2156  Allion Internal FAQ.md (p.6)  id=bluetooth:reference:Allion Internal FAQ.md:c00005  priority=5  kind=body
🧠 Building grounded prompt...
🤖 Generating answer with local model...
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-17T09:21:06.244992Z' done=True done_reason='stop' total_duration=8842758666 load_duration=352606083 prompt_eval_count=2241 prompt_eval_duration=1997033000 eval_count=299 eval_duration=6270941000 message=Message(role='assistant', content="Yes, you must complete the Bluetooth Qualification Process for your product yourself, as your supplier or other member companies cannot qualify your products on your behalf. You can only qualify your products under your member company's account by completing the Bluetooth Qualification Process. If you are a retailer or supplier selling or distributing another organization's qualified Bluetooth product, and you are not adding any logos, branding, or representing the product as your own, you do not need to complete the Qualification Process for that product.\n\nWhen reusing a qualified Bluetooth module, testing may depend on whether your product adds or changes specific elements. Because the module qualification covers only hardware and low-level functionality, if your product adds or changes profiles, firmware behavior, or host software, only those new or changed layers must be tested, as previously qualified layers are not retested.\n\nCitations:\n- [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00006 | BT Qualification Program Reference Document_QPRD_v5.md (p.7)]\n- [bluetooth:reference:BT Official FAQ_20260409.md:p00003 | BT Official FAQ_20260409.md (p.3)]\n- [bluetooth:reference:Allion Internal FAQ.md:c00005 | Allion Internal FAQ.md (p.6)]", thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
DEBUG timing: generate=8.85s
✅ Done.


⏱ Total elapsed: 16.20s
=== ANSWER ===

Yes, you must complete the Bluetooth Qualification Process for your product yourself, as your supplier or other member companies cannot qualify your products on your behalf. You can only qualify your products under your member company's account by completing the Bluetooth Qualification Process. If you are a retailer or supplier selling or distributing another organization's qualified Bluetooth product, and you are not adding any logos, branding, or representing the product as your own, you do not need to complete the Qualification Process for that product.

When reusing a qualified Bluetooth module, testing may depend on whether your product adds or changes specific elements. Because the module qualification covers only hardware and low-level functionality, if your product adds or changes profiles, firmware behavior, or host software, only those new or changed layers must be tested, as previously qualified layers are not retested.

Citations:
- [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00006 | BT Qualification Program Reference Document_QPRD_v5.md (p.7)]
- [bluetooth:reference:BT Official FAQ_20260409.md:p00003 | BT Official FAQ_20260409.md (p.3)]
- [bluetooth:reference:Allion Internal FAQ.md:c00005 | Allion Internal FAQ.md (p.6)]

=== SOURCES ===

- BT Qualification Program Reference Document_QPRD_v5.md (p.7)  [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00006]  score=0.4912  priority=1
- BT Official FAQ_20260409.md (p.3)  [bluetooth:reference:BT Official FAQ_20260409.md:p00003]  score=5.6918  priority=6
- Allion Internal FAQ.md (p.6)  [bluetooth:reference:Allion Internal FAQ.md:c00005]  score=2.2156  priority=5
```

## 3. @ In past Bluetooth cases, if a customer uses a qualified Bluetooth module, did they still need a new qualification?

- Elapsed: 17.08s
- Ollama total: 8.44s
- Ollama load: 0.35s
- Prompt eval: 4.86s
- Token eval: 3.21s

```text
📧 Email/case-only mode...

🔍 Retrieving relevant email/case evidence...

Selected sources for model:
- score=30.6296  thread_0038_case_01.json (p.1)  id=bluetooth:email:thread_0038_case_01.json:p00001  priority=1  kind=front_page
- score=30.0613  thread_0101_case_02.json (p.1)  id=bluetooth:email:thread_0101_case_02.json:p00001  priority=1  kind=front_page
- score=29.9286  thread_0005_case_01.json (p.1)  id=bluetooth:email:thread_0005_case_01.json:p00001  priority=1  kind=front_page
- score=29.7820  thread_0116_case_04.json (p.1)  id=bluetooth:email:thread_0116_case_04.json:p00001  priority=1  kind=front_page
- score=29.6757  thread_0078_case_02.json (p.1)  id=bluetooth:email:thread_0078_case_02.json:p00001  priority=1  kind=front_page
- score=29.3605  thread_0078_case_01.json (p.1)  id=bluetooth:email:thread_0078_case_01.json:p00001  priority=1  kind=front_page
🧠 Building email-grounded prompt...
🤖 Generating answer with local model...
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-17T09:21:23.385121Z' done=True done_reason='stop' total_duration=8439859042 load_duration=352633292 prompt_eval_count=3657 prompt_eval_duration=4861412000 eval_count=149 eval_duration=3205804000 message=Message(role='assistant', content='Case reference:\n\n1. Using a pre-qualified module without changes may allow for qualification reuse using existing module evidence instead of new testing [bluetooth:email:thread_0038_case_01.json:p00001 | thread_0038_case_01.json (p.1)].\n2. A product using an existing qualified module must still complete its own Bluetooth qualification process, especially if adding new functionality like HFP which requires correct declaration and testing [bluetooth:email:thread_0005_case_01.json:p00001 | thread_0005_case_01.json (p.1)].', thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
✅ Done.


⏱ Total elapsed: 10.19s
=== ANSWER ===

Case reference:

1. Using a pre-qualified module without changes may allow for qualification reuse using existing module evidence instead of new testing.
2. A product using an existing qualified module must still complete its own Bluetooth qualification process, especially if adding new functionality like HFP which requires correct declaration and testing.

Citations:
- [bluetooth:email:thread_0038_case_01.json:p00001 | thread_0038_case_01.json (p.1)]
- [bluetooth:email:thread_0005_case_01.json:p00001 | thread_0005_case_01.json (p.1)]

=== SOURCES ===

- thread_0038_case_01.json (p.1)  [bluetooth:email:thread_0038_case_01.json:p00001]  score=30.6296  priority=1
- thread_0005_case_01.json (p.1)  [bluetooth:email:thread_0005_case_01.json:p00001]  score=29.9286  priority=1
```

## 4. In Bluetooth, what is TCW?

- Elapsed: 20.63s
- Ollama total: 8.05s
- Ollama load: 0.34s
- Prompt eval: 3.01s
- Token eval: 4.46s

```text
🔍 Retrieving relevant evidence...

Top retrieved sources (debug):
- score=44.2934  glossary.md (p.20)  id=bluetooth:reference:glossary.md:c00019  priority=5  kind=body
- score=39.8364  BT Qualification Program Reference Document_QPRD_v5.md (p.5)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00004  priority=4  kind=glossary
- score=37.2964  BT Qualification Program Reference Document_QPRD_v5.md (p.24)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00023  priority=1  kind=body
- score=9.2769  thread_0035_case_03.json (p.1)  id=bluetooth:email:thread_0035_case_03.json:c00000  priority=0  kind=body
- score=7.8493  BT Official FAQ_20260409.md (p.34)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00030  priority=8  kind=glossary

Selected sources for model:
- score=44.2934  glossary.md (p.20)  id=bluetooth:reference:glossary.md:c00019  priority=5  kind=body
- score=39.8364  BT Qualification Program Reference Document_QPRD_v5.md (p.5)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00004  priority=4  kind=glossary

Selected sources after definition fast path:
- score=44.2934  glossary.md (p.20)  id=bluetooth:reference:glossary.md:c00019  priority=5  kind=body
- score=39.8364  BT Qualification Program Reference Document_QPRD_v5.md (p.5)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00004  priority=4  kind=glossary
- score=7.8493  BT Official FAQ_20260409.md (p.34)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00030  priority=8  kind=glossary
🧠 Building grounded prompt...
🤖 Generating answer with local model...
DEBUG glossary definitions: []
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-17T09:21:43.916609Z' done=True done_reason='stop' total_duration=8050254208 load_duration=339048666 prompt_eval_count=2660 prompt_eval_duration=3011543000 eval_count=212 eval_duration=4457362000 message=Message(role='assistant', content='TCW stands for Test Coverage Waiver, which is a waiver granted by Bluetooth SIG allowing specific qualification requirements or test cases to be waived under defined conditions [bluetooth:reference:glossary.md:c00019 | glossary.md (p.20)]. If a test case has an approved TCW, the verdict is recorded as Waived, and the TCW shall be referenced in the Evidence Notes column [bluetooth:reference:BT Official FAQ_20260409.md:c00030 | BT Official FAQ_20260409.md (p.34)].\n\nCitations:\n[bluetooth:reference:glossary.md:c00019 | glossary.md (p.20)]\n[bluetooth:reference:BT Official FAQ_20260409.md:c00030 | BT Official FAQ_20260409.md (p.34)]', thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
DEBUG timing: generate=8.06s
✅ Done.


⏱ Total elapsed: 13.93s
=== ANSWER ===

TCW stands for Test Coverage Waiver, which is a waiver granted by Bluetooth SIG allowing specific qualification requirements or test cases to be waived under defined conditions. If a test case has an approved TCW, the verdict is recorded as Waived, and the TCW shall be referenced in the Evidence Notes column.

Citations:
- [bluetooth:reference:glossary.md:c00019 | glossary.md (p.20)]
- [bluetooth:reference:BT Official FAQ_20260409.md:c00030 | BT Official FAQ_20260409.md (p.34)]

=== SOURCES ===

- glossary.md (p.20)  [bluetooth:reference:glossary.md:c00019]  score=44.2934  priority=5
- BT Official FAQ_20260409.md (p.34)  [bluetooth:reference:BT Official FAQ_20260409.md:c00030]  score=7.8493  priority=8
```

## 5. In Bluetooth, what is the difference between ICS and IXIT?

- Elapsed: 23.73s
- Ollama total: 9.51s
- Ollama load: 0.35s
- Prompt eval: 3.54s
- Token eval: 5.50s

```text
🔍 Retrieving relevant evidence...

Top retrieved sources (debug):
- score=37.3192  glossary.md (p.15)  id=bluetooth:reference:glossary.md:c00014  priority=8  kind=glossary
- score=37.0564  glossary.md (p.13)  id=bluetooth:reference:glossary.md:c00012  priority=8  kind=glossary
- score=36.6964  Allion Internal FAQ.md (p.5)  id=bluetooth:reference:Allion Internal FAQ.md:p00005  priority=6  kind=front_page
- score=35.9164  Allion Internal FAQ.md (p.28)  id=bluetooth:reference:Allion Internal FAQ.md:c00027  priority=5  kind=body
- score=33.0864  BT Qualification Program Reference Document_QPRD_v5.md (p.5)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00004  priority=4  kind=glossary

Selected sources for model:
- score=33.0864  BT Qualification Program Reference Document_QPRD_v5.md (p.5)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00004  priority=4  kind=glossary
- score=37.3192  glossary.md (p.15)  id=bluetooth:reference:glossary.md:c00014  priority=8  kind=glossary
- score=37.0564  glossary.md (p.13)  id=bluetooth:reference:glossary.md:c00012  priority=8  kind=glossary
- score=36.6964  Allion Internal FAQ.md (p.5)  id=bluetooth:reference:Allion Internal FAQ.md:p00005  priority=6  kind=front_page
- score=37.2964  BT Qualification Program Reference Document_QPRD_v5.md (p.24)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00023  priority=1  kind=body

Selected sources after definition fast path:
- score=33.0864  BT Qualification Program Reference Document_QPRD_v5.md (p.5)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00004  priority=4  kind=glossary
- score=37.3192  glossary.md (p.15)  id=bluetooth:reference:glossary.md:c00014  priority=8  kind=glossary
- score=37.0564  glossary.md (p.13)  id=bluetooth:reference:glossary.md:c00012  priority=8  kind=glossary
- score=36.6964  Allion Internal FAQ.md (p.5)  id=bluetooth:reference:Allion Internal FAQ.md:p00005  priority=6  kind=front_page
- score=37.2964  BT Qualification Program Reference Document_QPRD_v5.md (p.24)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00023  priority=1  kind=body
🧠 Building grounded prompt...
🤖 Generating answer with local model...
DEBUG glossary definitions: ['ICS: Implementation Conformance Statement']
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-17T09:22:07.72344Z' done=True done_reason='stop' total_duration=9505281250 load_duration=349633916 prompt_eval_count=3033 prompt_eval_duration=3539321000 eval_count=260 eval_duration=5500648000 message=Message(role='assistant', content='Implementation Conformance Statement (ICS) is a document produced by the Bluetooth SIG for each Bluetooth Specification that identifies the features of that specification [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00004 | BT Qualification Program Reference Document_QPRD_v5.md (p.5), bluetooth:reference:glossary.md:c00012 | glossary.md (p.13)]. In contrast, IXIT (Implementation eXtra Information for Testing) is a form completed by a Member providing additional configuration details to facilitate testing beyond the ICS [bluetooth:reference:glossary.md:c00014 | glossary.md (p.15)].\n\nCitations:\n[bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00004 | BT Qualification Program Reference Document_QPRD_v5.md (p.5)]\n[bluetooth:reference:glossary.md:c00012 | glossary.md (p.13)]\n[bluetooth:reference:glossary.md:c00014 | glossary.md (p.15)]', thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
DEBUG timing: generate=9.52s
✅ Done.


⏱ Total elapsed: 16.82s
=== ANSWER ===

Implementation Conformance Statement (ICS) is a document produced by the Bluetooth SIG for each Bluetooth Specification that identifies the features of that specification. In contrast, IXIT (Implementation eXtra Information for Testing) is a form completed by a Member providing additional configuration details to facilitate testing beyond the ICS.

Citations:
- [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00004 | BT Qualification Program Reference Document_QPRD_v5.md (p.5)]
- [bluetooth:reference:glossary.md:c00014 | glossary.md (p.15)]
- [bluetooth:reference:glossary.md:c00012 | glossary.md (p.13)]

=== SOURCES ===

- BT Qualification Program Reference Document_QPRD_v5.md (p.5)  [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00004]  score=33.0864  priority=4
- glossary.md (p.15)  [bluetooth:reference:glossary.md:c00014]  score=37.3192  priority=8
- glossary.md (p.13)  [bluetooth:reference:glossary.md:c00012]  score=37.0564  priority=8
```

## 6. In Bluetooth, what is Option 2b?

- Elapsed: 20.25s
- Ollama total: 7.27s
- Ollama load: 0.36s
- Prompt eval: 2.88s
- Token eval: 3.69s

```text
🔍 Retrieving relevant evidence...

Top retrieved sources (debug):
- score=28.6964  BT Qualification Program Reference Document_QPRD_v5.md (p.13)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00012  priority=1  kind=body
- score=21.8164  BT Official FAQ_20260409.md (p.18)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00014  priority=5  kind=body
- score=21.8164  BT Official FAQ_20260409.md (p.28)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00024  priority=5  kind=body
- score=19.6964  BT Qualification Program Reference Document_QPRD_v5.md (p.1)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00000  priority=1  kind=body
- score=15.4687  Bluetooth Core Specification_v6.2.md (p.100254)  id=bluetooth:specs:Bluetooth Core Specification_v6.2.md:t100254  priority=4  kind=definition

Selected sources for model:
- score=28.6964  BT Qualification Program Reference Document_QPRD_v5.md (p.13)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00012  priority=1  kind=body
- score=21.8164  BT Official FAQ_20260409.md (p.18)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00014  priority=5  kind=body
- score=21.8164  BT Official FAQ_20260409.md (p.28)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00024  priority=5  kind=body

Selected sources after definition fast path:
- score=28.6964  BT Qualification Program Reference Document_QPRD_v5.md (p.13)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00012  priority=1  kind=body
- score=21.8164  BT Official FAQ_20260409.md (p.18)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00014  priority=5  kind=body
- score=21.8164  BT Official FAQ_20260409.md (p.28)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00024  priority=5  kind=body
🧠 Building grounded prompt...
🤖 Generating answer with local model...
DEBUG glossary definitions: ['Option 2b: Allowed if unmodified']
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-17T09:22:27.963782Z' done=True done_reason='stop' total_duration=7265912750 load_duration=356601917 prompt_eval_count=2624 prompt_eval_duration=2884068000 eval_count=175 eval_duration=3685344000 message=Message(role='assistant', content='Option 2b refers to creating any other new Design, which is allowed when using deprecated specifications from an included Design if they are unmodified. When using this option, a Member must provide the DN(s) or QDID(s) for any Design(s) included in the new Design, an active TCRL Package version, and an ICS Form.\n\nCitations:\n- [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00012 | BT Qualification Program Reference Document_QPRD_v5.md (p.13)]\n- [bluetooth:reference:BT Official FAQ_20260409.md:c00014 | BT Official FAQ_20260409.md (p.18)]', thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
DEBUG timing: generate=7.28s
✅ Done.


⏱ Total elapsed: 12.85s
=== ANSWER ===

Option 2b refers to creating any other new Design, which is allowed when using deprecated specifications from an included Design if they are unmodified. When using this option, a Member must provide the DN(s) or QDID(s) for any Design(s) included in the new Design, an active TCRL Package version, and an ICS Form.

Citations:
- [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00012 | BT Qualification Program Reference Document_QPRD_v5.md (p.13)]
- [bluetooth:reference:BT Official FAQ_20260409.md:c00014 | BT Official FAQ_20260409.md (p.18)]

=== SOURCES ===

- BT Qualification Program Reference Document_QPRD_v5.md (p.13)  [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00012]  score=28.6964  priority=1
- BT Official FAQ_20260409.md (p.18)  [bluetooth:reference:BT Official FAQ_20260409.md:c00014]  score=21.8164  priority=5
```

## 7. In Bluetooth, what is the difference between Option 2a and Option 2b?

- Elapsed: 23.94s
- Ollama total: 9.61s
- Ollama load: 0.36s
- Prompt eval: 3.77s
- Token eval: 5.24s

```text
🔍 Retrieving relevant evidence...

Top retrieved sources (debug):
- score=36.6964  Allion Internal FAQ.md (p.5)  id=bluetooth:reference:Allion Internal FAQ.md:p00005  priority=6  kind=front_page
- score=35.9164  Allion Internal FAQ.md (p.28)  id=bluetooth:reference:Allion Internal FAQ.md:c00027  priority=5  kind=body
- score=23.6964  BT Qualification Program Reference Document_QPRD_v5.md (p.12)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00011  priority=1  kind=body
- score=23.6964  BT Qualification Program Reference Document_QPRD_v5.md (p.13)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00012  priority=1  kind=body
- score=22.4164  BT Official FAQ_20260409.md (p.27)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00023  priority=5  kind=body

Selected sources for model:
- score=23.6964  BT Qualification Program Reference Document_QPRD_v5.md (p.13)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00012  priority=1  kind=body
- score=23.6964  BT Qualification Program Reference Document_QPRD_v5.md (p.12)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00011  priority=1  kind=body
- score=36.6964  Allion Internal FAQ.md (p.5)  id=bluetooth:reference:Allion Internal FAQ.md:p00005  priority=6  kind=front_page
- score=35.9164  Allion Internal FAQ.md (p.28)  id=bluetooth:reference:Allion Internal FAQ.md:c00027  priority=5  kind=body
- score=46.8538  glossary.md (p.5)  id=bluetooth:reference:glossary.md:c00004  priority=8  kind=glossary

Selected sources after definition fast path:
- score=23.6964  BT Qualification Program Reference Document_QPRD_v5.md (p.13)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00012  priority=1  kind=body
- score=23.6964  BT Qualification Program Reference Document_QPRD_v5.md (p.12)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00011  priority=1  kind=body
- score=36.6964  Allion Internal FAQ.md (p.5)  id=bluetooth:reference:Allion Internal FAQ.md:p00005  priority=6  kind=front_page
- score=35.9164  Allion Internal FAQ.md (p.28)  id=bluetooth:reference:Allion Internal FAQ.md:c00027  priority=5  kind=body
- score=46.8538  glossary.md (p.5)  id=bluetooth:reference:glossary.md:c00004  priority=8  kind=glossary
🧠 Building grounded prompt...
🤖 Generating answer with local model...
DEBUG glossary definitions: []
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-17T09:22:51.877243Z' done=True done_reason='stop' total_duration=9610807459 load_duration=355667334 prompt_eval_count=3127 prompt_eval_duration=3767711000 eval_count=247 eval_duration=5241211000 message=Message(role='assistant', content='Option 2a involves creating a new Design by combining two or more unmodified Designs that have DNs or QDIDs into one of the permitted combinations listed in Table 3.1, requiring the provision of DNs or QDIDs for included Designs, the desired Core Configuration (if applicable), and the active TCRL Package version used for checking the Core Configuration and evaluating test requirements. In contrast, Option 2b involves creating any other new Design, which requires a Member to provide DN(s) or QDID(s) for any included Designs, an active TCRL Package version, and an ICS Form that is filled out for each new Layer implemented in the new Design or for each modified Layer based on an included Design.\n\nCitations:\n[bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00011 | BT Qualification Program Reference Document_QPRD_v5.md (p.12)]\n[bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00012 | BT Qualification Program Reference Document_QPRD_v5.md (p.13)]', thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
DEBUG timing: generate=9.63s
✅ Done.


⏱ Total elapsed: 17.10s
=== ANSWER ===

Option 2a involves creating a new Design by combining two or more unmodified Designs that have DNs or QDIDs into one of the permitted combinations listed in Table 3.1, requiring the provision of DNs or QDIDs for included Designs, the desired Core Configuration (if applicable), and the active TCRL Package version used for checking the Core Configuration and evaluating test requirements. In contrast, Option 2b involves creating any other new Design, which requires a Member to provide DN(s) or QDID(s) for any included Designs, an active TCRL Package version, and an ICS Form that is filled out for each new Layer implemented in the new Design or for each modified Layer based on an included Design.

Citations:
- [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00012 | BT Qualification Program Reference Document_QPRD_v5.md (p.13)]
- [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00011 | BT Qualification Program Reference Document_QPRD_v5.md (p.12)]

=== SOURCES ===

- BT Qualification Program Reference Document_QPRD_v5.md (p.13)  [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00012]  score=23.6964  priority=1
- BT Qualification Program Reference Document_QPRD_v5.md (p.12)  [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00011]  score=23.6964  priority=1
```

## 8. BluetoothのQualificationで、Compliance Folderには何を入れる必要がありますか？

- Elapsed: 22.22s
- Ollama total: 9.06s
- Ollama load: 0.35s
- Prompt eval: 2.27s
- Token eval: 6.22s

```text
🔍 Retrieving relevant evidence...

Top retrieved sources (debug):
- score=42.9625  BT Qualification Program Reference Document_QPRD_v5.md (p.21)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00020  priority=1  kind=body
- score=42.1964  BT Qualification Program Reference Document_QPRD_v5.md (p.7)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00006  priority=1  kind=body
- score=35.9164  Allion Internal FAQ.md (p.20)  id=bluetooth:reference:Allion Internal FAQ.md:c00019  priority=5  kind=body
- score=35.9164  Allion Internal FAQ.md (p.34)  id=bluetooth:reference:Allion Internal FAQ.md:c00033  priority=5  kind=body
- score=35.9164  BT Official FAQ_20260409.md (p.11)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00007  priority=5  kind=body

Selected sources for model:
- score=42.9625  BT Qualification Program Reference Document_QPRD_v5.md (p.21)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00020  priority=1  kind=body
- score=42.1964  BT Qualification Program Reference Document_QPRD_v5.md (p.7)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00006  priority=1  kind=body
- score=35.9164  Allion Internal FAQ.md (p.20)  id=bluetooth:reference:Allion Internal FAQ.md:c00019  priority=5  kind=body
🧠 Building grounded prompt...
🤖 Generating answer with local model...
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-17T09:23:14.095835Z' done=True done_reason='stop' total_duration=9057977667 load_duration=347347458 prompt_eval_count=2305 prompt_eval_duration=2266877000 eval_count=296 eval_duration=6222361000 message=Message(role='assistant', content='すべてのQualified Productsにおいて、MembersはTable 3.3に記載されたドキュメントを単一の場所（一般的に「Compliance Folder」と呼ばれます）で維持する必要があります。ドキュケーションは、MemberがProductをBluetooth Qualification Processに提出する時点で保存されていなければならず、また、MemberがProductの販売または配布を停止した後も少なくとも1年間保持しなければなりません。また、MemberはBluetooth SIGからの要請があった場合、検査のためにドキュメントを利用可能な状態にしておく必要があります。\n\nCompliance Folderの要件は以下の通りです。\n\n| Compliance Folder Requirements | Use a single existing Design (Section 3.2.1) | Create a new Design (Section 3.2.2) |\n| :--- | :--- | :--- |\n| Product details | Required | Required |\n| Design details | Required | Required |\n| Test declaration | N/A | Required if test plan is generated |\n| Test report(s) | N/A | Required if test plan is generated |\n| Test logs | N/A | Required if test plan is generated |\n| TCW | N/A | As required |\n\nCitations:\n- [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00020 | BT Qualification Program Reference Document_QPRD_v5.md (p.21)]', thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
DEBUG timing: generate=9.07s
✅ Done.


⏱ Total elapsed: 15.37s
=== ANSWER ===

すべてのQualified Productsにおいて、MembersはTable 3.3に記載されたドキュメントを単一の場所（一般的に「Compliance Folder」と呼ばれます）で維持する必要があります。ドキュケーションは、MemberがProductをBluetooth Qualification Processに提出する時点で保存されていなければならず、また、MemberがProductの販売または配布を停止した後も少なくとも1年間保持しなければなりません。また、MemberはBluetooth SIGからの要請があった場合、検査のためにドキュメントを利用可能な状態にしておく必要があります。

Compliance Folderの要件は以下の通りです。

| Compliance Folder Requirements | Use a single existing Design (Section 3.2.1) | Create a new Design (Section 3.2.2) |
|:--- |:--- |:--- |
| Product details | Required | Required |
| Design details | Required | Required |
| Test declaration | N/A | Required if test plan is generated |
| Test report(s) | N/A | Required if test plan is generated |
| Test logs | N/A | Required if test plan is generated |
| TCW | N/A | As required |

Citations:
- [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00020 | BT Qualification Program Reference Document_QPRD_v5.md (p.21)]

=== SOURCES ===

- BT Qualification Program Reference Document_QPRD_v5.md (p.21)  [bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00020]  score=42.9625  priority=1
```

## 9. Bluetoothで認証済みモジュールを使う場合、新しい認証は必要ですか？

- Elapsed: 24.73s
- Ollama total: 9.29s
- Ollama load: 0.35s
- Prompt eval: 2.38s
- Token eval: 6.54s

```text
🔍 Retrieving relevant evidence...

Top retrieved sources (debug):
- score=19.7150  BT Official FAQ_20260409.md (p.21)  id=bluetooth:reference:BT Official FAQ_20260409.md:c00017  priority=5  kind=body
- score=5.6937  BT Official FAQ_20260409.md (p.3)  id=bluetooth:reference:BT Official FAQ_20260409.md:p00003  priority=6  kind=front_page
- score=3.5996  thread_0045_case_01.json (p.1)  id=bluetooth:email:thread_0045_case_01.json:p00001  priority=1  kind=front_page
- score=3.2964  thread_0080_case_02.json (p.1)  id=bluetooth:email:thread_0080_case_02.json:p00001  priority=1  kind=front_page
- score=2.3416  glossary.md (p.10)  id=bluetooth:reference:glossary.md:c00009  priority=8  kind=glossary
- score=1.7949  glossary.md (p.11)  id=bluetooth:reference:glossary.md:c00010  priority=5  kind=body
- score=1.3259  Bluetooth チャンネル・サウンディング_技術概要.md (p.1)  id=bluetooth:reference:Bluetooth チャンネル・サウンディング_技術概要.md:c00008  priority=2  kind=body
- score=1.3256  Bluetooth チャンネル・サウンディング_技術概要.md (p.1)  id=bluetooth:reference:Bluetooth チャンネル・サウンディング_技術概要.md:c00002  priority=2  kind=body
- score=1.3225  Bluetooth Channel Sounding_Technical overview.md (p.1)  id=bluetooth:reference:Bluetooth Channel Sounding_Technical overview.md:c00003  priority=2  kind=body
- score=1.3209  Bluetooth Channel Sounding_Technical overview.md (p.1)  id=bluetooth:reference:Bluetooth Channel Sounding_Technical overview.md:c00013  priority=2  kind=body

Selected sources for model:
- score=5.6937  BT Official FAQ_20260409.md (p.3)  id=bluetooth:reference:BT Official FAQ_20260409.md:p00003  priority=6  kind=front_page
- score=3.5996  thread_0045_case_01.json (p.1)  id=bluetooth:email:thread_0045_case_01.json:p00001  priority=1  kind=front_page
- score=3.2964  thread_0080_case_02.json (p.1)  id=bluetooth:email:thread_0080_case_02.json:p00001  priority=1  kind=front_page
🧠 Building grounded prompt...
🤖 Generating answer with local model...
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-17T09:23:38.793385Z' done=True done_reason='stop' total_duration=9293896125 load_duration=351335375 prompt_eval_count=2475 prompt_eval_duration=2381065000 eval_count=311 eval_duration=6536082000 message=Message(role='assistant', content='はい、認証済みBluetoothモジュールを使用している場合でも、最終製品のBluetooth Qualification Process（Bluetooth認証プロセス）を自社で完了させる必要があります。サプライヤーや他の加盟企業が、お客様に代わって製品の認証を行うことはできません。製品の販売または配布を開始する日までに、自社の加盟企業アカウントを使用して認証を完了させておく必要があります。\n\nすでに認証済みのBluetoothモジュールを使用しているからといって、最終製品の認証が自動的に完了することはありません。最終製品を販売する企業は、依然として独自のBluetooth SIG認証ステップを完了し、正しいBluetooth SIG加盟企業アカウントの下で製品を申請する必要があります。不必要な再試験を避けて認証を承認させるためには、適切なドキュメンテーションや含まれる設計リファレンスを準備しておく必要があります。\n\n参考事例:\n既存の認証済みBluetoothモジュールを使用した製品のBluetooth SIG認証について、正しい加盟企業アカウントの所有権、ドキュメンテーションパッケージ、および宣言ワークフローを使用しながら、エンド製品としての認証を完了させる必要があるケースがあります。\n\nCitations:\n[bluetooth:reference:BT Official FAQ_20260409.md:p00003 | BT Official FAQ_20260409.md (p.3)]\n[bluetooth:email:thread_0045_case_01.json:p00001 | thread_0045_case_01.json (p.1)]', thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
DEBUG timing: generate=9.30s
✅ Done.


⏱ Total elapsed: 17.27s
=== ANSWER ===

はい、認証済みBluetoothモジュールを使用している場合でも、最終製品のBluetooth Qualification Process（Bluetooth認証プロセス）を自社で完了させる必要があります。サプライヤーや他の加盟企業が、お客様に代わって製品の認証を行うことはできません。製品の販売または配布を開始する日までに、自社の加盟企業アカウントを使用して認証を完了させておく必要があります。

すでに認証済みのBluetoothモジュールを使用しているからといって、最終製品の認証が自動的に完了することはありません。最終製品を販売する企業は、依然として独自のBluetooth SIG認証ステップを完了し、正しいBluetooth SIG加盟企業アカウントの下で製品を申請する必要があります。不必要な再試験を避けて認証を承認させるためには、適切なドキュメンテーションや含まれる設計リファレンスを準備しておく必要があります。

参考事例:
既存の認証済みBluetoothモジュールを使用した製品のBluetooth SIG認証について、正しい加盟企業アカウントの所有権、ドキュメンテーションパッケージ、および宣言ワークフローを使用しながら、エンド製品としての認証を完了させる必要があるケースがあります。

Citations:
- [bluetooth:reference:BT Official FAQ_20260409.md:p00003 | BT Official FAQ_20260409.md (p.3)]
- [bluetooth:email:thread_0045_case_01.json:p00001 | thread_0045_case_01.json (p.1)]

=== SOURCES ===

- BT Official FAQ_20260409.md (p.3)  [bluetooth:reference:BT Official FAQ_20260409.md:p00003]  score=5.6937  priority=6
- thread_0045_case_01.json (p.1)  [bluetooth:email:thread_0045_case_01.json:p00001]  score=3.5996  priority=1
```

## 10. BluetoothでTCWとは何ですか？

- Elapsed: 17.41s
- Ollama total: 4.31s
- Ollama load: 0.35s
- Prompt eval: 2.30s
- Token eval: 1.46s

```text
🔍 Retrieving relevant evidence...

Top retrieved sources (debug):
- score=41.0164  glossary.md (p.20)  id=bluetooth:reference:glossary.md:c00019  priority=5  kind=body
- score=36.8364  BT Qualification Program Reference Document_QPRD_v5.md (p.5)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00004  priority=4  kind=glossary
- score=34.2964  BT Qualification Program Reference Document_QPRD_v5.md (p.24)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00023  priority=1  kind=body
- score=5.4981  glossary.md (p.1)  id=bluetooth:reference:glossary.md:c00000  priority=8  kind=glossary
- score=3.6225  Bluetooth Core Specification_v6.2.md (pp.440-443)  id=bluetooth:specs:Bluetooth Core Specification_v6.2.md:c00148  priority=2  kind=body

Selected sources for model:
- score=36.8364  BT Qualification Program Reference Document_QPRD_v5.md (p.5)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00004  priority=4  kind=glossary
- score=5.4981  glossary.md (p.1)  id=bluetooth:reference:glossary.md:c00000  priority=8  kind=glossary

Selected sources after definition fast path:
- score=41.0164  glossary.md (p.20)  id=bluetooth:reference:glossary.md:c00019  priority=5  kind=body
- score=36.8364  BT Qualification Program Reference Document_QPRD_v5.md (p.5)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00004  priority=4  kind=glossary
🧠 Building grounded prompt...
🤖 Generating answer with local model...
DEBUG glossary definitions: []
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-17T09:23:56.260065Z' done=True done_reason='stop' total_duration=4307177208 load_duration=354857625 prompt_eval_count=2309 prompt_eval_duration=2299305000 eval_count=70 eval_duration=1460828000 message=Message(role='assistant', content='TCW（Test Coverage Waiver）とは、定義された条件下において、特定の適合要件またはテストケースの免除を許可するためにBluetooth SIGによって付与されるウェイバー（免除）のことです。\n\n[bluetooth:reference:glossary.md:c00019 | glossary.md (p.20)]', thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
DEBUG timing: generate=4.32s
✅ Done.


⏱ Total elapsed: 10.29s
=== ANSWER ===

TCW（Test Coverage Waiver）とは、定義された条件下において、特定の適合要件またはテストケースの免除を許可するためにBluetooth SIGによって付与されるウェイバー（免除）のことです。

Citations:
- [bluetooth:reference:glossary.md:c00019 | glossary.md (p.20)]

=== SOURCES ===

- glossary.md (p.20)  [bluetooth:reference:glossary.md:c00019]  score=41.0164  priority=5
```

## 11. BluetoothでICSとは何ですか？

- Elapsed: 16.69s
- Ollama total: 3.40s
- Ollama load: 0.35s
- Prompt eval: 1.90s
- Token eval: 1.13s

```text
🔍 Retrieving relevant evidence...

Top retrieved sources (debug):
- score=43.5564  glossary.md (p.13)  id=bluetooth:reference:glossary.md:c00012  priority=8  kind=glossary
- score=36.8364  BT Qualification Program Reference Document_QPRD_v5.md (p.5)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00004  priority=4  kind=glossary
- score=36.5764  Host Controller Interface_TS.md (pp.3-6)  id=bluetooth:specs:Host Controller Interface_TS.md:c00026  priority=2  kind=body
- score=36.5764  Host Controller Interface_TS.md (pp.6-10)  id=bluetooth:specs:Host Controller Interface_TS.md:c00027  priority=2  kind=body
- score=34.2964  BT Qualification Program Reference Document_QPRD_v5.md (p.24)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00023  priority=1  kind=body

Selected sources for model:
- score=43.5564  glossary.md (p.13)  id=bluetooth:reference:glossary.md:c00012  priority=8  kind=glossary
- score=36.8364  BT Qualification Program Reference Document_QPRD_v5.md (p.5)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00004  priority=4  kind=glossary

Selected sources after definition fast path:
- score=43.5564  glossary.md (p.13)  id=bluetooth:reference:glossary.md:c00012  priority=8  kind=glossary
- score=36.8364  BT Qualification Program Reference Document_QPRD_v5.md (p.5)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00004  priority=4  kind=glossary
🧠 Building grounded prompt...
🤖 Generating answer with local model...
DEBUG glossary definitions: []
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-17T09:24:12.917276Z' done=True done_reason='stop' total_duration=3397156250 load_duration=345665958 prompt_eval_count=2311 prompt_eval_duration=1904552000 eval_count=55 eval_duration=1133559000 message=Message(role='assistant', content='ICS — Implementation Conformance Statementとは、各Bluetooth Specificationにおいて、その仕様の機能を特定するためにBluetooth SIGによって作成される文書です。\n\n[bluetooth:reference:glossary.md:c00012 | glossary.md (p.13)]', thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
DEBUG timing: generate=3.41s
✅ Done.


⏱ Total elapsed: 9.51s
=== ANSWER ===

ICS — Implementation Conformance Statementとは、各Bluetooth Specificationにおいて、その仕様の機能を特定するためにBluetooth SIGによって作成される文書です。

Citations:
- [bluetooth:reference:glossary.md:c00012 | glossary.md (p.13)]

=== SOURCES ===

- glossary.md (p.13)  [bluetooth:reference:glossary.md:c00012]  score=43.5564  priority=8
```

## 12. BluetoothでIXITとは何ですか？

- Elapsed: 16.97s
- Ollama total: 3.94s
- Ollama load: 0.35s
- Prompt eval: 2.27s
- Token eval: 1.29s

```text
🔍 Retrieving relevant evidence...

Top retrieved sources (debug):
- score=43.5564  glossary.md (p.15)  id=bluetooth:reference:glossary.md:c00014  priority=8  kind=glossary
- score=36.8364  BT Qualification Program Reference Document_QPRD_v5.md (p.5)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00004  priority=4  kind=glossary
- score=36.5764  Baseband_TS.md (pp.4-11)  id=bluetooth:specs:Baseband_TS.md:c00011  priority=2  kind=body
- score=36.5764  Security_Manager_TS.md (pp.4-11)  id=bluetooth:specs:Security_Manager_TS.md:c00007  priority=2  kind=body
- score=34.2964  BT Qualification Program Reference Document_QPRD_v5.md (p.24)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00023  priority=1  kind=body

Selected sources for model:
- score=43.5564  glossary.md (p.15)  id=bluetooth:reference:glossary.md:c00014  priority=8  kind=glossary
- score=36.8364  BT Qualification Program Reference Document_QPRD_v5.md (p.5)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00004  priority=4  kind=glossary

Selected sources after definition fast path:
- score=43.5564  glossary.md (p.15)  id=bluetooth:reference:glossary.md:c00014  priority=8  kind=glossary
- score=36.8364  BT Qualification Program Reference Document_QPRD_v5.md (p.5)  id=bluetooth:policies:BT Qualification Program Reference Document_QPRD_v5.md:c00004  priority=4  kind=glossary
🧠 Building grounded prompt...
🤖 Generating answer with local model...
DEBUG glossary definitions: []
RAW OLLAMA RESPONSE:
model='gemma4:26b' created_at='2026-06-17T09:24:29.921187Z' done=True done_reason='stop' total_duration=3935709041 load_duration=354800333 prompt_eval_count=2314 prompt_eval_duration=2271684000 eval_count=62 eval_duration=1294097000 message=Message(role='assistant', content='IXIT（Implementation eXtra Information for Testing）とは、ICSを超えたテストを容易にするために、追加の構成詳細を提供するMemberによって記入されるフォームです。\n\n[bluetooth:reference:glossary.md:c00014 | glossary.md (p.15)]', thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None
DEBUG timing: generate=3.95s
✅ Done.


⏱ Total elapsed: 9.83s
=== ANSWER ===

IXIT（Implementation eXtra Information for Testing）とは、ICSを超えたテストを容易にするために、追加の構成詳細を提供するMemberによって記入されるフォームです。

Citations:
- [bluetooth:reference:glossary.md:c00014 | glossary.md (p.15)]

=== SOURCES ===

- glossary.md (p.15)  [bluetooth:reference:glossary.md:c00014]  score=43.5564  priority=8
```
