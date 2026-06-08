# Coding protocol v0.1.1

**Version:** 0.1.1 (promoted from v0.1 following pilot validation, 2026-06-08)  
**Change log:** [`outputs/reports/protocol_change_log_v0_1_1.md`](../outputs/reports/protocol_change_log_v0_1_1.md)  
**Decision rules:** [`coding_decision_rules_v0_1_1.md`](coding_decision_rules_v0_1_1.md)  
**Aligned with:** `docs/study_protocol_v0_1.md`  
**Implementation:** `src/evidence_gaps/schema.py`, `scripts/code_observability.py`

## Purpose

Code publicly accessible municipal AI documents for **Public-Document Observability** across five programme-level dimensions (D1–D5). Coding records what appears in public documentation. The canonical non-claims apply: no readiness scoring; no municipal ranking; no legal compliance determination; no LocalGovBench validation; no inference of internal governance quality.

---

## Evidence status labels

| Label | Definition |
|-------|------------|
| `observable_named_artifact` | Concrete named artefact (role, register field, policy document, audit, contract reference) with locatable detail |
| `observable_policy_commitment` | Explicit commitment, principle, or procedural obligation without sufficient programme-level specificity |
| `partial_or_indirect_signal` | Fragmentary, implied, or indirect mention; weak basis for independent assessment |
| `not_observable_publicly` | No relevant evidence found in the coded public source(s) for this dimension |

### Evidence-status boundaries (v0.1.1)

Use the following distinctions when assigning labels. See [`coding_decision_rules_v0_1_1.md`](coding_decision_rules_v0_1_1.md) for the full decision tree.

#### `observable_named_artifact`

**Assign when** the source names a concrete, locatable governance artefact tied to the dimension.

| Positive example | Dimension |
|------------------|-----------|
| "Chief Data Officer, Digital City Office" with AI remit in organigram | D1 |
| Register entry field: `Impacttoetsen: DPIA, IAMA` on a distinct entry page | D2 |
| Log retention schedule: "automated decision logs retained 24 months" in AI policy | D3 |
| Contract award notice: "Vendor X — municipal chatbot, ref. 2024/123" | D4 |
| Published audit summary: "Algorithmic impact review, System Y, Q2 2024" | D5 |

| Negative example | Why not `observable_named_artifact` |
|------------------|--------------------------------------|
| "Governance and supervision bodies will be established" (no names) | → `observable_policy_commitment` |
| Register index shows publisher "Municipality" only | → `partial_or_indirect_signal` |
| "We are committed to transparency" | → `observable_policy_commitment` or `partial_or_indirect_signal` |
| Privacy Quickscan label on card with no linked policy text | → `partial_or_indirect_signal` |

#### `observable_policy_commitment`

**Assign when** the source states an explicit obligation, principle, or procedural rule but lacks named roles, artefacts, or operational detail sufficient for independent verification.

| Positive example | Dimension |
|------------------|-----------|
| "Each AI-using service must have a designated responsible party" | D1 |
| "High-risk systems require algorithmic impact studies" (EU risk-tier language) | D2 |
| Eight ethical principles including privacy and security (no log/prompt detail) | D3 |
| "Public procurement process integrated with algorithmic implementation stages" | D4 |
| "Systems must be used in a supervised and proportionate way" | D2 |

| Negative example | Why not `observable_policy_commitment` |
|------------------|---------------------------------------|
| "Human-centric AI" slogan with no obligation | → `partial_or_indirect_signal` |
| Topic not mentioned at all | → `not_observable_publicly` |
| Named DPIA document linked from register entry | → `observable_named_artifact` |

#### `partial_or_indirect_signal`

**Assign when** the dimension is touched indirectly, incompletely, or through metadata stubs without substantive detail.

| Positive example | Dimension |
|------------------|-----------|
| Register index: organisational publisher only, no responsible unit | D1 |
| Register card: `Impacttoetsen: Veld niet ingevuld` (field empty) | D2 |
| "Data protection mechanisms" referenced without AI-specific logging rules | D3 |
| Vendor logo on innovation page, no contract | D4 |
| Register status enum (`In use` / `Decommissioned`) without audit procedure | D5 |
| `Last updated` timestamp alone on register entry | D5 |

| Negative example | Why not `partial_or_indirect_signal` |
|------------------|-------------------------------------|
| Dimension not mentioned | → `not_observable_publicly` |
| Explicit supervised-use obligation in protocol | → `observable_policy_commitment` |
| Named ethics board charter with scope and cadence | → `observable_named_artifact` |

#### `not_observable_publicly`

**Assign when** the dimension is absent from the coded source. Silence is not evidence of internal absence of controls.

---

## Unit of coding

One **coding decision** per:

```
municipality × source document × dimension (D1–D5)
```

Record the effective coding unit in `coder_notes` when it differs from the manifest row (e.g. register entry, annex PDF).

---

## Algorithm registers (v0.1.1)

Algorithm registers require an explicit coding-unit decision before D1–D5 coding begins.

### Default: register-level coding

**Use register-level coding when:**

- The manifest URL points to the register index or listing page
- The coding task is the manifest row as registered in `corpus_manifest_v0_1.csv`
- No single entry is the stated focus of the source row

**Procedure:** Scan all visible entries for recurring metadata fields. Code each dimension based on what the register **as a whole** makes observable (typically `partial_or_indirect_signal` for index-level scans).

**Register-level example (D1):** Index lists publisher "Gemeente Amsterdam" on each card but no named programme owner → `partial_or_indirect_signal`.

### Required: entry-level coding

**Use entry-level coding when:**

- The manifest URL points to a **distinct public detail page** for one system
- The research design requires per-system observability for that municipality
- A register entry contains populated governance fields (responsible unit, impact assessment type, status) that differ materially across entries

**Procedure:** One coding decision set per `municipality × entry × dimension`. Set `source_id` to `{manifest_source_id}-entry-{slug}`. Quote from the entry page.

**Entry-level example (D2):** Entry page shows `Impacttoetsen: DPIA, De Ethische Bijsluiter` → `observable_named_artifact`.

### Register-level vs entry-level — quick reference

| Situation | Coding unit | Typical D2/D5 result |
|-----------|-------------|----------------------|
| Index page, mixed empty/populated cards | Register-level | `partial_or_indirect_signal` |
| Single entry detail page with named assessments | Entry-level | `observable_named_artifact` (if field populated) |
| Index page, all entries show status enum | Register-level | D5: `partial_or_indirect_signal` (status only) |
| Entry with decommissioning status + audit report link | Entry-level | D5: `observable_named_artifact` |

**Do not** upgrade index-level publisher name to `observable_named_artifact` for D1 programme ownership.

---

## Document hierarchy and coding depth (v0.1.1)

When a manifest URL is not the substantive source document, follow the evidence hierarchy below before coding.

### Preference order

```
1. source document   (primary policy, protocol PDF, strategy text, register entry page)
2. annex             (bilag, attachment, linked PDF from official page)
3. committee record  (meeting minutes page referencing adopted document)
4. summary page      (landing page, overview, press-style summary on official domain)
```

**Rule:** Code the **highest available artefact** in this order. If only a summary page is accessible, code the summary page and record `coding_depth: summary` in `coder_notes`.

### Hierarchy examples

| Manifest URL type | Action | `coder_notes` |
|-------------------|--------|---------------|
| Protocol summary with "See complete protocol" link | Retrieve and code linked PDF if accessible | `coding_depth: full; coded artefact: [PDF URL]` |
| Committee record with strategy in bilag 1 | Code bilag attachment if accessible; else code minutes page | `coding_depth: committee_record` or `coding_depth: annex` |
| AI strategy summary page only | Code summary page | `coding_depth: summary` |
| Register index | Code at register level per rules above | `coding_unit: register_level` |

**Do not** treat a summary page as equivalent to a source document when the full document is publicly linked and retrievable.

---

## Reliability

A pilot subset was double-coded (see `outputs/reports/pilot_coding_protocol_test.md`). Disagreements are resolved through protocol clarification and documented rule updates — not by averaging into scores.

**Pilot timing benchmark:** ~34 minutes per document (single coder); register sources may require longer.

---

## Dimension sheets

---

### D1 — Programme ownership

**Coding question:** Does public documentation name who owns, leads, or is accountable for municipal AI programmes at programme level (not only generic digitalisation)?

**Examples of public evidence (`observable_named_artifact`):**

- Named Chief Data / AI / Digital officer with explicit AI remit
- Published organigram or terms of reference for an AI governance board
- Register entry listing a responsible unit and contact point per system

**Examples of policy commitment (`observable_policy_commitment`):**

- "Each AI-using service must have a designated responsible party" without naming the office
- "Governance and supervision bodies" referenced without member names

**Examples of weak/indirect evidence (`partial_or_indirect_signal`):**

- Register index publisher name only (e.g. "Municipality")
- Generic "the municipality is committed to responsible AI" without role holders
- Digital strategy mentioning AI without accountable office

**Exclusion notes:**

- National ministry ownership references unless tied to a municipal programme
- Personal names of front-line staff unless part of a governance role description
- Do not infer ownership from service branding alone

---

### D2 — Human oversight and review

**Coding question:** Does public documentation describe human oversight, review, approval, or escalation for municipal AI systems or automated decisions?

**Examples of public evidence (`observable_named_artifact`):**

- Documented human-in-the-loop workflow for defined system classes
- Ethics or review board charter with meeting cadence and scope
- Register entry field naming impact assessment type (DPIA, IAMA, ethics review) on the **entry page**

**Examples of policy commitment (`observable_policy_commitment`):**

- "Systems must be used in a supervised and proportionate way"
- EU AI Act risk-tier language requiring stricter guarantee mechanisms for high-risk systems
- "Human monitoring and intervention capacity required" (principle-level)

**Examples of weak/indirect evidence (`partial_or_indirect_signal`):**

- Register index: assessment field empty or inconsistently populated across cards
- High-level fairness principles without review mechanism
- "Human centric AI" slogans without process detail

**Worked examples (v0.1.1):**

| Source context | Evidence | Label | Rationale |
|----------------|----------|-------|-----------|
| Register entry page | `Impacttoetsen: DPIA, IAMA` | `observable_named_artifact` | Named assessment types on entry = locatable oversight artefact |
| Register index scan | Some cards show DPIA, many show empty field | `partial_or_indirect_signal` | Inconsistent index-level metadata; not entry-level artefact |
| Protocol summary | "Supervised use" + high-risk impact studies required | `observable_policy_commitment` | Procedural obligation without step-by-step workflow |
| Ethical principles page | "Human oversight" principle, no process | `observable_policy_commitment` | Explicit obligation, insufficient operational detail |

**Exclusion notes:**

- Generic civil-service accountability statements not specific to AI
- Oversight of non-AI IT systems unless explicitly linked to AI programme
- Do not assume judicial or regulatory oversight unless municipally documented

---

### D3 — Prompt, log, and data governance

**Coding question:** Does public documentation address prompt management, logging, retention, or training/sensitive data boundaries for municipal AI or automated systems?

**Examples of public evidence (`observable_named_artifact`):**

- Published log retention schedule for automated decision systems
- Data processing notice linked to a named AI tool with retention period
- Documented prompt template governance or prohibition on unsanctioned prompts

**Examples of policy commitment (`observable_policy_commitment`):**

- Ethical principles covering privacy, security, transparency, explainability (without log/prompt/retention periods)
- "Data processed in compliance with applicable legislation"

**Examples of weak/indirect evidence (`partial_or_indirect_signal`):**

- Register card: `Privacy Quickscan` label without linked policy text
- General GDPR privacy notice without AI-specific logging detail
- "Data protection mechanisms" referenced in protocol summary without detail

**Worked examples (v0.1.1):**

| Source context | Evidence | Label | Rationale |
|----------------|----------|-------|-----------|
| AI policy | Eight principles: privacy, security, transparency | `observable_policy_commitment` | Ethical data commitments present; no prompt/log specificity |
| AI policy | "Logs retained 24 months for system X" | `observable_named_artifact` | Locatable retention rule |
| Register index | `Privacyverklaring` on card, no link | `partial_or_indirect_signal` | Assessment label stub without accessible policy |
| Protocol summary | "Data protection mechanisms" mentioned | `partial_or_indirect_signal` | Indirect reference on summary page |

**Boundary rule:** Ethical privacy/security principles alone **cannot** exceed `observable_policy_commitment` for D3. Prompt, log, or retention specificity is required for `observable_named_artifact`.

**Exclusion notes:**

- Do not code from technical screenshots or unofficial demos
- Exclude personal data examples; record locator only if policy-level
- Cloud provider generic terms unless municipally adopted as policy

---

### D4 — Procurement and vendor stewardship

**Coding question:** Does public documentation show how vendors are selected, overseen, and held accountable for municipal AI systems?

**Examples of public evidence (`observable_named_artifact`):**

- Public contract award notice identifying AI system scope and vendor
- Vendor stewardship clause or SLA excerpt in official procurement file
- Register entry linking system to contract reference or vendor role

**Examples of policy commitment (`observable_policy_commitment`):**

- Protocol integrating "public procurement process" with implementation stages
- Tender clauses requiring rights-respecting intelligent systems (without contract ID)

**Examples of weak/indirect evidence (`partial_or_indirect_signal`):**

- Vendor logo on a municipal innovation page without contract context
- Partnership press release without stewardship terms

**Exclusion notes:**

- Vendor marketing sites
- Subcontractor chains not disclosed in public municipal documents
- Do not infer contract terms from product documentation

---

### D5 — Incident, audit, and lifecycle accountability

**Coding question:** Does public documentation address incidents, audits, evaluations, updates, decommissioning, or lifecycle changes for municipal AI systems?

**Examples of public evidence (`observable_named_artifact`):**

- Published audit or evaluation summary of a named system
- Incident reporting procedure specific to automated systems
- Decommissioning notice with audit reference on register entry page

**Examples of policy commitment (`observable_policy_commitment`):**

- Strategy commits to periodic algorithmic audits (future tense, no published audit)

**Examples of weak/indirect evidence (`partial_or_indirect_signal`):**

- Register status enum: `In use` / `Decommissioned` / `In development`
- Protocol references "life cycle of an algorithmic system" without incident route
- `Last updated` timestamp on register entry **alone**

**Worked examples (v0.1.1):**

| Source context | Evidence | Label | Rationale |
|----------------|----------|-------|-----------|
| Register index | Status `Buiten gebruik` (decommissioned) on entries | `partial_or_indirect_signal` | Lifecycle state visible; not audit/incident artefact |
| Register index | `Laatst gewijzigd: 2026-05-19` only | `partial_or_indirect_signal` | Date alone excluded per protocol |
| Register entry | Status + linked evaluation report | `observable_named_artifact` | Named evaluation artefact locatable |
| Protocol summary | "Lifecycle" and risk-tier mechanisms mentioned | `partial_or_indirect_signal` | Process reference without incident/audit publication |
| AI policy | No lifecycle language | `not_observable_publicly` | Dimension absent |

**Boundary rule:** Register status enums → `partial_or_indirect_signal`. `observable_named_artifact` requires a named audit, incident procedure, evaluation, or decommissioning **document** — not status metadata alone.

**Exclusion notes:**

- National regulator actions unless mirrored in municipal publication
- Media-reported incidents without official municipal documentation
- Do not treat document `last_updated` date alone as lifecycle accountability

---

## Quote language convention (v0.1.1)

Record `quoted_evidence` in the **source document language**. Add an English gloss in `coder_notes` when the coder works from protocol definitions in English. Do not translate quotes in the `quoted_evidence` field.

---

## Prohibited uses

- Do not convert status labels into readiness scoring
- Do not perform municipal ranking by count of `not_observable_publicly`
- Do not perform legal compliance determination from gaps
- Do not perform LocalGovBench validation

## CSV templates

- Manifest: `data/processed/corpus_manifest_template.csv`
- Coding: `data/processed/coding_template.csv`

## Non-claim boundary field

Set `non_claim_boundary` on every coding row to the v0.1 constant (`observability_only_v0_1`). See `docs/non_claims.md`.
