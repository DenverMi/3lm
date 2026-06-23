Read the attached IoT cybersecurity requirement records and produce retrieval-optimized crosswalk records.

The attached input is the ONLY allowed source.
All comparisons, mappings, summaries, and conclusions must come from the FULL contents of the attached input.

Important:

* The input may contain requirement records from multiple IoT cybersecurity frameworks, schemes, laws, standards, guidelines, or labeling programs.
* Your job is to identify reusable overlaps, differences, evidence reuse opportunities, and consulting takeaways across frameworks.
* Do not invent framework mappings that are not supported by the input.
* Do not use outside knowledge.
* Output JSON only.

Your goal:

* Understand the full set of requirement records
* Identify common cybersecurity requirement topics across frameworks
* Compare how different frameworks treat the same topic
* Preserve important differences in scope, mandatory status, target market, product coverage, evidence, assessment method, and lifecycle stage
* Produce standalone RAG-friendly crosswalk records
* Help future consulting answers explain overlap, gap, prioritization, and evidence reuse
* Output JSON only

Rules:

1. Output valid JSON only.
2. Do not use markdown fences.
3. Do not explain anything outside the JSON.
4. Write all values in English unless an official Japanese, EU, or technical phrase is necessary for accuracy.
5. Do not invent requirements, mappings, evidence, legal obligations, deadlines, penalties, or equivalence claims not supported by the input.
6. Do not claim two frameworks are equivalent unless the input explicitly supports equivalence.
7. If frameworks are similar but not identical, describe them as overlapping, related, or partially aligned.
8. Preserve mandatory / voluntary / recommended / conditional / informational distinctions.
9. Preserve product scope and market scope differences.
10. Preserve lifecycle-stage differences, such as design, pre-market, post-market support, vulnerability handling, software update, documentation, or labeling.
11. Preserve evidence differences, such as technical documentation, test report, declaration, policy, SBOM, label, vulnerability process, or conformity assessment.
12. Prefer fewer high-quality crosswalk records over many shallow duplicates.
13. Keep each crosswalk record centered on one reusable topic area.
14. Do not merge unrelated requirement areas into one record.
15. Make each crosswalk independently understandable and independently retrievable without requiring the full input.
16. Use wording that helps both semantic search and keyword search.
17. Include both framework terminology and plain-English phrasing when strongly supported by the input.
18. If only one framework covers a topic in the input, do not force a crosswalk. Only create a crosswalk record when at least two frameworks have relevant comparable content.
19. If the input is too thin to support a reliable comparison, output an empty crosswalks array.
20. Keep wording concise, dense, and reusable.

Return this exact schema:

{
"source_type": "cybersecurity_crosswalk_set",
"program": "IoT Cybersecurity",
"crosswalks": [
{
"source_type": "cybersecurity_crosswalk",
"program": "IoT Cybersecurity",
"crosswalk_id": "",
"topic": "",
"requirement_area": "",
"frameworks_compared": [],
"common_requirement": "",
"framework_positions": [],
"key_differences": "",
"evidence_reuse_strategy": "",
"implementation_priority": "",
"consulting_takeaway": "",
"applicability_notes": {
"target_markets": [],
"product_scope": [],
"actor_scope": [],
"conditions": []
},
"program_tags": [],
"search_aliases": [],
"confidence": ""
}
]
}

Field rules:

* source_type:
  For the top-level object, always return "cybersecurity_crosswalk_set".
  For each crosswalk item, always return "cybersecurity_crosswalk".

* program:
  Always return "IoT Cybersecurity".

* crosswalk_id:
  Build a stable short ID.
  Format:
  "iot_cybersecurity_<requirement_area_slug>_<number>"
  Examples:
  "iot_cybersecurity_default_passwords_001"
  "iot_cybersecurity_vulnerability_handling_001"
  "iot_cybersecurity_security_updates_001"
  "iot_cybersecurity_technical_documentation_001"

* topic:
  Short human-readable topic.
  Examples:
  "Default passwords"
  "Vulnerability handling"
  "Security updates"
  "Technical documentation"
  "Secure configuration"
  "Conformity assessment"
  "Labeling"
  "SBOM"
  "Access control"
  "Data protection"

* requirement_area:
  Normalized requirement area used for retrieval.
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

* frameworks_compared:
  List only frameworks actually compared in this crosswalk record.
  Examples:
  "JC-STAR"
  "CRA"
  "EN 18031"
  "ETSI EN 303 645"
  "NISTIR 8425"
  "UK PSTI"
  "Singapore CLS"
  "IEC 62443"
  Do not include frameworks that are only generally mentioned elsewhere but not relevant to this topic.

* common_requirement:
  One concise paragraph describing what the compared frameworks have in common for this topic.
  Avoid claiming identical requirements unless the input explicitly supports that.

* framework_positions:
  List one object per compared framework using this structure:
  {
  "framework": "",
  "requirement_summary": "",
  "mandatory_status": "",
  "source_reference": "",
  "required_evidence": [],
  "lifecycle_stage": "",
  "notes": ""
  }

  Field rules for framework_positions:

  * framework:
    The framework name from the input.
  * requirement_summary:
    Concise statement of that framework's position on this topic.
  * mandatory_status:
    Use one of:
    "mandatory"
    "voluntary"
    "recommended"
    "conditional"
    "informational"
    "unclear"
  * source_reference:
    Clause, article, section, annex, table, level, requirement number, or source locator from the input if available.
  * required_evidence:
    Evidence artifacts stated or expected in the input for that framework.
  * lifecycle_stage:
    Lifecycle stage from the input if available.
  * notes:
    Short note preserving important conditions, limits, scope, or uncertainty.

* key_differences:
  Explain the most important differences between frameworks.
  Focus on:

  * target market
  * product scope
  * mandatory versus voluntary status
  * level / risk class / assurance level
  * assessment route
  * evidence requirement
  * lifecycle timing
  * manufacturer / importer / distributor role
  * labeling versus legal compliance
  * technical control details
    If differences are minor or unclear, say so.

* evidence_reuse_strategy:
  Explain how a company could reuse evidence across the compared frameworks, based only on the input.
  Good examples:

  * "A single vulnerability disclosure policy may support multiple frameworks, but framework-specific wording and evidence may still be needed."
  * "Technical documentation can be reused as a base, but EU market obligations may require additional conformity documentation."
  * "Test evidence may support both schemes if the requirement area and product scope match."
    If evidence reuse is not supported by the input, use "".

* implementation_priority:
  Explain the practical priority for a Japanese company preparing for overlapping IoT cybersecurity standards.
  Focus on the most reusable action first.
  Examples:

  * "Prepare a common baseline policy first, then map it to each target market."
  * "Implement the technical control once, but maintain framework-specific evidence."
  * "Confirm product scope and target markets before choosing the compliance path."
    If the input does not support a priority, use "".

* consulting_takeaway:
  State the most reusable consulting lesson for this crosswalk.
  This should help answer future customer questions about overlap, differences, and practical next steps.

* applicability_notes:
  target_markets:
  Markets or jurisdictions covered by this crosswalk.
  Examples: ["Japan"], ["EU"], ["UK"], ["Singapore"], ["US"]
  Use only values supported by the input.

  product_scope:
  Product types covered by this crosswalk.
  Examples: ["consumer IoT products"], ["radio equipment"], ["products with digital elements"], ["internet-connected devices"], ["smart home devices"]
  Use only values supported by the input.

  actor_scope:
  Actors covered by this crosswalk.
  Examples: ["manufacturer"], ["importer"], ["distributor"], ["authorized representative"], ["tester"], ["certification body"], ["vendor"]
  Use only values supported by the input.

  conditions:
  Specific conditions that affect applicability.
  Examples:
  "applies when the product is placed on the EU market"
  "applies when the product has internet connectivity"
  "applies when the device supports remote access"
  "applies when the framework level requires third-party assessment"
  Use only conditions supported by the input.

* program_tags:
  Use 3 to 8 concise tags only if strongly supported.
  Examples:
  "IoT cybersecurity", "JC-STAR", "CRA", "Cyber Resilience Act", "EN 18031", "ETSI EN 303 645", "NISTIR 8425", "PSTI", "CLS", "RED", "product security", "secure by default", "vulnerability handling", "security update", "software update", "password policy", "access control", "authentication", "encryption", "data protection", "privacy", "secure boot", "firmware integrity", "SBOM", "risk assessment", "threat model", "conformity assessment", "self-declaration", "third-party certification", "labeling", "technical documentation", "evidence reuse", "market access", "Japan", "EU", "UK", "Singapore"

* search_aliases:
  Provide 5 to 12 short retrieval-friendly phrases, acronyms, or near-synonyms that are strongly supported by the input.
  These are for search matching, not for prose.
  Examples:
  "IoT cybersecurity crosswalk"
  "JC-STAR CRA mapping"
  "CRA ETSI EN 303 645 overlap"
  "EN 18031 comparison"
  "NISTIR 8425 mapping"
  "default password comparison"
  "vulnerability disclosure mapping"
  "security update evidence reuse"
  "technical documentation reuse"
  "IoT security label comparison"
  "overlapping cybersecurity standards"
  "Japan EU IoT cybersecurity"
  Keep them short.
  Do not invent unsupported aliases.

* confidence:
  Must be one of:
  "high"
  "medium"
  "low"

  Use:

  * "high" when the overlap, differences, and evidence reuse are explicit or strongly supported by the input
  * "medium" when the overlap is clear but some comparison details require reasonable inference
  * "low" when the crosswalk is useful but the input only weakly supports the comparison

Crosswalk policy:

* Create a crosswalk record only when at least two frameworks have comparable content for the same requirement area.
* If one framework has a requirement and another only mentions a related topic with no requirement detail, compare cautiously and lower confidence.
* Do not create a crosswalk only because framework names appear together.
* Do not claim that satisfying one framework automatically satisfies another unless the input explicitly says so.
* If one framework is a voluntary label and another is a legal obligation, preserve that distinction clearly.
* If one framework is a technical standard and another is a law or regulation, preserve that distinction clearly.
* If one framework is market-specific, preserve target market limits clearly.
* If a requirement is similar but has different evidence, scope, or assessment requirements, emphasize that difference.
* When in doubt, use "overlap" or "partial overlap" rather than "equivalent".

Recommended topic grouping:

* Group crosswalks by reusable consulting topic, not by framework pair.
* Example: one crosswalk for "vulnerability handling" may compare JC-STAR, CRA, ETSI EN 303 645, and NISTIR 8425 if all are supported in the input.
* Do not create separate pairwise records unless the input demands it.
* Prefer topic-centered comparison because it helps answer customer questions like:
  "Can our CRA evidence also help with JC-STAR?"
  "Which cybersecurity controls should we implement first?"
  "What overlaps between Japanese and EU IoT cybersecurity requirements?"

Quality standard:

* A good output should be directly useful for:

  1. semantic retrieval
  2. keyword retrieval
  3. reranking
  4. grounded answer generation
  5. plain-English explanation to non-experts
  6. cybersecurity framework comparison
  7. consulting recommendation planning
  8. evidence reuse planning for Japanese companies entering global markets

Process the next input now:
