# Repository Writing Style (SMPTE‑Aligned)

This repository captures an audiovisual workflow intended for publication as a SMPTE Engineering Guideline (EG). Our house style aligns with SMPTE Administrative Guidelines and provides a clear “EG‑mode” (informative) path while preserving “Normative‑mode” guidance for internal drafts that may later migrate to a Standard (ST) or Recommended Practice (RP).

Primary sources we follow:
- SMPTE AG‑16 — Standards Style Guide: https://doc.smpte-doc.org/ag-16/main/
- SMPTE AG‑04 — Engineering Document Templates: https://doc.smpte-doc.org/ag-04/main/
- SMPTE AG‑02 — Document Naming and Packaging: https://doc.smpte-doc.org/ag-02/4b17ef0f1d612ab8c7b8b060784e07f38a6bb374/
- SMPTE AG‑03 — Permitted Normative References: https://doc.smpte-doc.org/ag-03/main/
- MXF UL Style Guidelines (if relevant): https://doc.smpte-doc.org/ag-24/main/

Additional style references (informative):
- IETF RFC 7322 — RFC Style Guide: https://www.rfc-editor.org/rfc/rfc7322
- ETSI Drafting Rules (EDR): https://www.etsi.org/standards/etsi-drafting-rules
- IEEE SA — Standards Style resources: https://standards.ieee.org (Author resources)
- W3C Manual of Style (editorial): https://www.w3.org/2001/06/manual/

Secondary references (when AG‑16 is silent):
- ISO/IEC Directives, Part 2 (drafting and structure)
- RFC 2119 and RFC 8174 (interpretation only; SMPTE uses lower‑case forms)
- NIST SP 811 and BIPM SI Brochure (SI units)

## Document Modes
- EG‑mode (informative, default): conforms to SMPTE’s definition of Engineering Guidelines. EGs are tutorial/guidance documents and shall not include Conformance Language, Normative Text, or Normative References.
- Normative‑mode (ST/RP‑aligned): used only if a section is being drafted with requirements. This mode uses conformance language per AG‑16. Do not mix modes within a single document.

When in doubt, author in EG‑mode.

## Structure (EG‑mode — default)
- Foreword (unnumbered; informative context)
- 1 Scope (what the guideline covers; non‑requirements wording)
- 2 References (informative only; no normative references)
- 3 Terms and definitions (informative glossary)
- 4 Overview (system/roles/inputs/outputs)
- 5 Procedure (preconditions, steps, validation)
- 6 Data formats and exchange (file formats, color spaces, naming, metadata)
- 7 Operational considerations (performance, reproducibility, provenance, risks)
- Annexes (informative; lettered and titled)
- Bibliography (informative only)

Templates
- EG‑mode template (informative only): `docs/templates/eg-informative-template.md`
  - Note: A Normative‑mode template is intentionally omitted from this repo for now. Request one if/when requirements drafting is needed.

## Structure (Normative‑mode — internal drafts only)
- Foreword (unnumbered)
- 1 Scope
- 2 Conformance
- 3 Normative references (limited by AG‑03)
- 4 Terms and definitions
- 5+ Body clauses (requirements, procedure, data formats)
- Annexes (clearly labeled normative or informative)
- Bibliography (informative only)

## Language Rules
- EG‑mode:
  - Avoid conformance language. Do not use lower‑case italicized conformance terms as requirements: _shall_, _shall not_, _should_, _should not_, _may_.
  - Prefer neutral guidance forms: “This guideline recommends…”, “Operators typically…”, “Preferred practice is…”, “Implementations can…”.
  - Title Clause 2 as “References” and treat all citations as informative.
- Normative‑mode (AG‑16):
  - Use lower‑case, italicized verbal forms:
    - _shall_, _shall not_ — requirement, no deviation permitted
    - _should_, _should not_ — strong recommendation
    - _may_ — permission
  - “Note” and “informative” prose is non‑normative.
  - Do not use upper‑case IETF style (e.g., MUST/SHALL/SHOULD).

## References and Citations
- EG‑mode: all references are informative; place in Clause 2 or in the Bibliography. Do not include a “Normative references” clause.
- Normative‑mode: separate normative references (Clause 3) from the Bibliography; only include sources permitted by AG‑03. Cite by designator (e.g., “see SMPTE AG‑16, 7.12.2”).

## Terms, Symbols, Numbers
- Define specialized terms in Clause 3 or 4; avoid redefining common terms.
- Units: use SI. Spell out on first use with symbol in parentheses (e.g., “seconds (s)”).
- Numbers: follow AG‑16 7.12 (engineering notation where appropriate) and 7.13 for hex.
- Dates/times: ISO 8601 forms. Frame rates as `24 fps`, `23.976 fps`.

## Figures, Tables, Listings
- Caption and number sequentially per type: “Figure 1 — …”, “Table 1 — …”.
- Refer in text by number (“see Figure 2”).
- Use monospace for code, CLI, JSON/YAML, and Nuke knob names.

## Lists (bulleted and numbered)
- Choose list type by intent:
  - Numbered lists — ordered procedures or checklists where sequence matters.
  - Bulleted lists — unordered sets (options, considerations, examples).
- Provide a clear lead‑in sentence ending with a colon that states the organizing idea of the list.
- Enforce parallel structure across items:
  - Procedures — start each item with an imperative verb (“Align…”, “Train…”, “Validate…”), followed by an expected outcome where useful (em dash).
  - Descriptive sets — use consistent noun phrases (“Color reference”, “Spatial reference”).
- Keep one idea per bullet; avoid mixed content (action + example + caveat). Split into separate bullets or sub‑sections if needed.
- Prefer concise items (ideally one line). For long lists, group into 4–6 item blocks or convert to a table.
- Punctuation and case:
  - Fragments — start with a capital letter, no terminal period.
  - Full sentences — start with a capital letter and end with a period.
- Avoid deep nesting. If sub‑steps are essential, limit to one sub‑level or use sub‑headings/tables instead.
- Cross‑reference figures/tables by number inside list items when relevant (e.g., “see Figure 1”).

## Procedural Content
- Write stepwise procedures with clear preconditions and expected outcomes.
- Use consistent, concise instructions; avoid ambiguous verbs.
- In EG‑mode, express guidance as preferred practices and examples, not conformance requirements.

Recommended step pattern (EG‑mode):
- Preconditions — data, tools, and environment expectations.
- Steps — ordered imperatives with brief expected outcomes (use an em dash).
- Validation — objective checks or acceptance criteria.

## Naming and Packaging (repo conventions)
- File names: lower‑case with hyphens; concise and scoped (e.g., `chroma-recovery.md`).
- Images: store in `docs/images/`; reference and number as figures.
- Paths: keep repository‑relative; never hard‑code absolute paths.

## Accessibility and Inclusive Language
- Follow AG‑16 section 8; avoid exclusionary terms.
- Prefer active, clear, testable language. Apply Plain Language principles.

## Language and Locale
- Use English (US) spelling and punctuation (for example, “color”, “center”).
- Use the Oxford (serial) comma in lists of three or more items.
- Use en dash (–) for numeric ranges (for example, “3–4 pairs”) and em dash (—) for parenthetical emphasis; surround the em dash with spaces in running text.
- Avoid idioms, slang, and culturally specific metaphors.
- Define acronyms and initialisms at first use: full term (acronym). Use the acronym thereafter if it improves clarity (for example, convolutional neural network (CNN)).
- Prefer descriptive link text over “here”; keep URLs out of running text.

## Exemplars to Emulate (EGs)
- EG 2098‑3 — Immersive Audio Renderer Expectations and Testing Recommendations (procedural/QC sections)
- EG 2046‑3 — Safe Areas for Television (clear figures and annexes)
- EG 2111‑1/‑2/‑3 — SDI Standards Roadmap (concise scope/cross‑references)
- EG 2074 — SMPTE Metadata Naming Guidelines (naming discipline)

## Checklist Before Merging (EG‑mode)
- Structure follows EG‑mode template; no Clause 2 “Conformance”.
- No conformance language (_shall/should/may_) used as requirements.
- References are informative; no “Normative references” clause.
- Figures/tables are numbered and referenced in text.
- Units are SI; dates/times are ISO 8601.
- All paths are repository‑relative.

List hygiene (manual):
- Lead‑in sentence states the organizing idea.
- List type matches intent (numbered for steps; bullets for sets).
- Items are parallel and concise; one idea per item.
- Punctuation/case follow the rules above.

Manual checks (optional):
- Scan for conformance terms: `rg -n "\\bshall|\\bshould|\\bmay|Conformance|Normative references" docs/`
- Verify headings order: `rg -n "^##? (Foreword|1 Scope|2 References|3 Terms|4 Overview|5 Procedure)" docs/`

## Editorial Review
We do not require automated prose linting. Authors and reviewers _shall_ apply this guide during review. For EG‑mode specifically:
- Keep the document informative; avoid requirements language.
- Ensure the structure matches the EG‑mode template.
- Separate general references from the Bibliography; do not add normative references.
- Number and reference figures/tables consistently.
- Use SI units and ISO 8601 dates/times.

Before merging, maintainers _should_ scan new or edited docs against the EG‑mode checklist and the templates in `docs/templates/`.
