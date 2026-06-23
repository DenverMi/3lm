Read the attached source document and extract retrieval-optimized IoT cybersecurity requirement records from it.

The attached source document is the ONLY allowed source.
All reasoning, extraction, summaries, and conclusions must come from the FULL contents of the attached source document.

Important:

* The source may be a law, regulation, standard, guideline, certification scheme, labeling program, technical specification, FAQ, guidance document, checklist, or official explanatory material.
* The source may contain one or more reusable cybersecurity requirements.
* If the source contains multiple clearly different reusable requirements, output multiple requirement records.
* If the source contains no reusable IoT cybersecurity requirement, output an empty requirements array.
* Do not treat general background, marketing language, or non-requirement explanations as requirements unless they define scope, obligation, evidence, conformity process, or implementation expectation.

Your goal:

* Understand the source document
* Identify each distinct reusable IoT cybersecurity requirement, obligation, control, scope rule, evidence requirement, conformity requirement, labeling requirement, testing requirement, or lifecycle requirement
* Convert each requirement into a standalone RAG-friendly record
* Preserve the official meaning
* Preserve practical actionability
* Improve future retrieval by including plain-English explanation, requirement area, evidence expectations, product scope, lifecycle stage, framework names, and search aliases
* Avoid legal overstatement
* Output JSON only

Rules:

1. Output valid JSON only.
2. Do not use markdown fences.
3. Do not explain anything outside the JSON.
4. Write all values in English unless an official Japanese, EU, or technical phrase is necessary for accuracy.
5. Do not invent requirements, deadlines, penalties, product categories, evidence, test methods, or legal obligations not present in the source.
6. Do not infer missing annexes, referenced standards, attachments, diagrams, or tables that are not visible in the source.
7. If a requirement is conditional, preserve the condition clearly.
8. If a requirement depends on product category, risk class, target market, function, connectivity, radio capability, data processing, manufacturer role, importer role, or lifecycle stage, preserve that dependency clearly.
9. If the source distinguishes mandatory requirements from recommendations, guidance, examples, or best practices, preserve that distinction.
10. If the source contains conflicting or staged requirements, prefer the latest or most specific official statement in the source.
11. Keep each requirement atomic. Do not mix unrelated requirements into one record.
12. Prefer fewer high-quality requirement records over many overlapping fragments.
13. Make each requirement independently understandable and independently retrievable without requiring the full source document.
14. Use wording that helps both semantic search and keyword search.
15. Include both official terminology and plain-English phrasing when strongly supported by the source.
16. Keep wording concise, dense, and reusable.
17. Do not add consulting advice unless it follows directly from the source requirement.
18. Do not state that something is legally required unless the source clearly frames it as a requirement, obligation, mandatory condition, or compliance criterion.
19. For Japanese government guidance or labeling schemes, distinguish between government guidance, voluntary labeling, certification, conformity assessment, procurement expectation, and legal obligation when the source supports that distinction.
20. For EU sources, distinguish between law/regulation text, harmonized standard requirements, presumption of conformity, technical documentation, manufacturer obligation, and notified body / third-party assessment when the source supports that distinction.

Output each requirement into the following file pattern:
/output/requirements/
<framework_slug>_requirement_001.json
<framework_slug>_requirement_002.json
<framework_slug>_requirement_003.json

Return this exact schema:

{
"source_type": "framework_requirement",
"program": "IoT Cybersecurity",
"framework": "",
"framework_full_name": "",
"source_document_title": "",
"source_reference": "",
"requirement_id": "",
"requirement_area": "",
"requirement_summary": "",
"plain_english_explanation": "",
"official_requirement_text": "",
"applicability": {
"target_market": [],
"product_scope": [],
"actor_scope": [],
"risk_or_level_scope": "",
"conditions": []
},
"required_evidence": [],
"implementation_expectations": [],
"testing_or_assessment_expectations": [],
"lifecycle_stage": "",
"mandatory_status": "",
"overlaps_with": [],
"program_tags": [],
"search_aliases": [],
"confidence": ""
}

Field rules:

* source_type:
  Always return "framework_requirement".

* program:
  Always return "IoT Cybersecurity".

* framework:
  Short framework name explicitly supported by the source.
  Examples:
  "JC-STAR"
  "CRA"
  "EN 18031"
  "ETSI EN 303 645"
  "NISTIR 8425"
  "UK PSTI"
  "Singapore CLS"
  "IEC 62443"
  If unclear, use "".

* framework_full_name:
  Full name of the framework, law, standard, guideline, or scheme if available in the source.
  Examples:
  "Cyber Resilience Act"
  "ETSI EN 303 645"
  "NISTIR 8425"
  "Security Requirements for Consumer IoT Products"
  If unclear, use "".

* source_document_title:
  Title of the source document if available.
  Copy or summarize it accurately.
  If unclear, use "".

* source_reference:
  Clause, section, article, annex, table, level, requirement number, checklist item, page, or other source locator if available.
  Examples:
  "Article 13"
  "Annex I"
  "Section 5.1"
  "Provision 5.1-1"
  "Level 1 requirement"
  "Table 2"
  If unclear, use "".

* requirement_id:
  Build a stable short ID when the source has no exact requirement ID.
  Format:
  "<framework>*<requirement_area_slug>*<number>"
  Examples:
  "JC-STAR_vulnerability_handling_001"
  "CRA_security_updates_001"
  "ETSI303645_default_passwords_001"
  If the source provides an official ID, use that official ID.

* requirement_area:
  The topic area of the requirement.
  Examples:
  "default passwords"
  "vulnerability handling"
  "security updates"
  "secure configuration"
  "access control"
  "authentication"
  "encryption"
  "data protection"
  "privacy"
  "secure boot"
  "firmware integrity"
  "SBOM"
  "logging"
  "incident response"
  "technical documentation"
  "conformity assessment"
  "labeling"
  "product scope"
  "market placement"
  "support period"

* requirement_summary:
  One concise sentence stating what the requirement requires, recommends, or defines.
  Preserve conditions and scope.

* plain_english_explanation:
  Explain the requirement in simple terms for a product manager, sales person, or customer-facing consultant in 2 to 4 sentences.
  Do not overstate beyond the source.

* official_requirement_text:
  Use a short source-grounded paraphrase of the official requirement.
  Do not copy long passages verbatim.
  Keep it concise.
  If exact wording is needed for accuracy, quote only a short phrase.

* applicability:
  target_market:
  Markets or jurisdictions explicitly supported by the source.
  Examples: ["Japan"], ["EU"], ["UK"], ["Singapore"], ["US"]
  If unclear, return [].

  product_scope:
  Product types explicitly covered or strongly supported by the source.
  Examples: ["consumer IoT products"], ["radio equipment"], ["products with digital elements"], ["internet-connected devices"], ["smart home devices"]
  If unclear, return [].

  actor_scope:
  Actors explicitly covered by the source.
  Examples: ["manufacturer"], ["importer"], ["distributor"], ["authorized representative"], ["tester"], ["certification body"], ["vendor"]
  If unclear, return [].

  risk_or_level_scope:
  Risk class, assurance level, label level, conformity level, product class, or security level if stated.
  Examples: "JC-STAR Level 1", "important product", "critical product", "Class I", "Class II"
  If unclear, use "".

  conditions:
  List specific conditions that trigger the requirement.
  Examples:
  "applies when the product has remote access"
  "applies to products placed on the EU market"
  "applies when personal data is processed"
  "applies to radio equipment capable of communicating over the internet"
  If unclear, return [].

* required_evidence:
  List documents, records, test results, declarations, labels, procedures, policies, or artifacts required or expected by the source.
  Examples:
  "technical documentation"
  "risk assessment"
  "vulnerability disclosure policy"
  "software update policy"
  "SBOM"
  "test report"
  "conformity declaration"
  "labeling record"
  "user instructions"
  If none are stated, return [].

* implementation_expectations:
  List practical implementation expectations stated or directly implied by the requirement.
  Examples:
  "do not use universal default passwords"
  "provide security updates during the support period"
  "protect stored credentials"
  "document vulnerability handling process"
  "provide secure configuration by default"
  If none are stated, return [].

* testing_or_assessment_expectations:
  List testing, assessment, review, certification, labeling, self-declaration, or third-party evaluation expectations stated by the source.
  Examples:
  "self-declaration"
  "third-party assessment"
  "conformity assessment"
  "test against published checklist"
  "submit evidence to certification body"
  "maintain technical documentation"
  If none are stated, return [].

* lifecycle_stage:
  Must be one of:
  "design"
  "implementation"
  "pre-market"
  "testing / assessment"
  "market placement"
  "post-market support"
  "vulnerability handling"
  "software update"
  "documentation"
  "labeling"
  "regulatory monitoring"

* mandatory_status:
  Must be one of:
  "mandatory"
  "voluntary"
  "recommended"
  "conditional"
  "informational"
  "unclear"

  Use:

  * "mandatory" only when the source clearly frames it as a legal obligation, requirement, mandatory criterion, or required condition.
  * "voluntary" when the source clearly frames the scheme or requirement as voluntary.
  * "recommended" when the source frames it as guidance, recommendation, or best practice.
  * "conditional" when it applies only under stated conditions.
  * "informational" for definitions, explanatory notes, or scope descriptions that are useful for RAG but not themselves obligations.
  * "unclear" when the source does not make the status clear.

* overlaps_with:
  List other frameworks or standards explicitly mentioned as related, mapped, harmonized, equivalent, referenced, or overlapping in the source.
  Examples:
  "ETSI EN 303 645"
  "NISTIR 8425"
  "CRA"
  "EN 18031"
  If none are stated, return [].
  Do not invent cross-framework mappings in this requirement extraction prompt.

* program_tags:
  Use 3 to 8 concise tags only if strongly supported.
  Examples:
  "IoT cybersecurity", "JC-STAR", "CRA", "EN 18031", "ETSI EN 303 645", "NISTIR 8425", "PSTI", "CLS", "RED", "product security", "secure by default", "vulnerability handling", "security update", "software update", "password policy", "access control", "authentication", "encryption", "data protection", "privacy", "secure boot", "firmware integrity", "SBOM", "risk assessment", "threat model", "conformity assessment", "self-declaration", "third-party certification", "labeling", "technical documentation", "evidence reuse", "market access", "Japan", "EU", "UK", "Singapore"

* search_aliases:
  Provide 5 to 12 short retrieval-friendly phrases, acronyms, or near-synonyms that are strongly supported by the source.
  These are for search matching, not for prose.
  Examples:
  "IoT cybersecurity requirement"
  "JC-STAR Level 1"
  "CRA requirement"
  "Cyber Resilience Act obligation"
  "EN 18031 cybersecurity"
  "ETSI EN 303 645 provision"
  "NISTIR 8425 baseline"
  "default password requirement"
  "vulnerability disclosure"
  "security update policy"
  "technical documentation"
  "conformity assessment"
  "IoT security label"
  "secure by default"
  Keep them short.
  Do not invent unsupported aliases.

* confidence:
  Must be one of:
  "high"
  "medium"
  "low"

  Use:

  * "high" when the requirement, scope, and status are explicit in the source
  * "medium" when the requirement is explicit but some scope or evidence detail requires strong but reasonable inference
  * "low" when the record is reusable but some important fields are only weakly supported

Extraction policy:

* Extract requirements at the level useful for consulting and RAG.
* Do not split every sentence into a separate record.
* Do not merge unrelated controls into one record.
* If a table row defines one requirement area, extract that row as one record.
* If a section defines several distinct obligations, extract each obligation separately.
* If the source describes framework scope, market applicability, or product applicability, extract it as a requirement record only if it will help answer future consulting questions.
* If the source only references another standard without explaining the requirement, record the reference but do not invent the referenced content.
* If a requirement is duplicated in multiple parts of the source, extract the clearest version and include the best source_reference.

Framework-specific guidance:

* JC-STAR:
  Distinguish voluntary labeling / scheme requirements from Japanese legal obligations unless the source clearly states otherwise.
  Preserve level names, label levels, product categories, and evidence expectations when stated.
  Capture overlap or harmonization references only if stated.

* CRA / EU Cyber Resilience Act:
  Distinguish manufacturer obligations, product scope, essential cybersecurity requirements, technical documentation, conformity assessment, vulnerability handling, and post-market obligations when stated.
  Avoid legal advice beyond the text.

* EN 18031:
  Treat it as a technical standard or conformity route when the source says so.
  Preserve which part or requirement area is discussed if available.

* ETSI EN 303 645 / NISTIR 8425:
  Preserve baseline consumer IoT security controls such as default passwords, vulnerability disclosure, software updates, secure configuration, data protection, and documentation when stated.

* UK PSTI / Singapore CLS / other labeling schemes:
  Preserve scheme status, label level, product category, evidence requirement, and target market when stated.

Quality standard:

* A good output should be directly useful for:

  1. semantic retrieval
  2. keyword retrieval
  3. reranking
  4. grounded answer generation
  5. plain-English explanation to non-experts
  6. cybersecurity framework comparison
  7. consulting recommendation planning

Process the next source document now:
