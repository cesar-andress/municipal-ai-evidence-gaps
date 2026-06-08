# Coding protocol v0.1

**Aligned with:** `docs/study_protocol_v0_1.md`  
**Implementation:** `src/evidence_gaps/schema.py`, `scripts/code_observability.py`

## Purpose

Code publicly accessible municipal AI documents for **Public-Document Observability** across five programme-level dimensions (D1–D5). Coding records what appears in public documentation. The canonical non-claims apply: no readiness scoring; no municipal ranking; no legal compliance determination; no LocalGovBench validation; no inference of internal governance quality.

## Evidence status labels

| Label | Definition |
|-------|------------|
| `observable_named_artifact` | Concrete named artefact (role, register, policy document, audit, contract reference) with locatable detail |
| `observable_policy_commitment` | Explicit commitment or principle without sufficient programme-level specificity |
| `partial_or_indirect_signal` | Fragmentary, implied, or indirect mention; weak basis for independent assessment |
| `not_observable_publicly` | No relevant evidence found in the coded public source(s) for this dimension |

## Unit of coding

One **coding decision** per:

```
municipality × source document × dimension (D1–D5)
```

Multi-page transparency hubs may be coded as one source if internally cross-linked; split register entries may be coded per entry when each entry is a distinct public artefact (noted in `coder_notes`).

## Reliability

A pilot subset will be double-coded. Disagreements are resolved through protocol clarification and documented rule updates — not by averaging into scores.

## Dimension sheets

---

### D1 — Programme ownership

**Coding question:** Does public documentation name who owns, leads, or is accountable for municipal AI programmes at programme level (not only generic digitalisation)?

**Examples of public evidence (`observable_named_artifact`):**

- Named Chief Data / AI / Digital officer with explicit AI remit
- Published organigram or terms of reference for an AI governance board
- Register metadata listing a responsible unit and contact point per system

**Examples of weak/indirect evidence (`partial_or_indirect_signal` / `observable_policy_commitment`):**

- Generic "the municipality is committed to responsible AI" without role holders
- Digital strategy mentioning AI without accountable office
- Vendor name present without municipal owner

**Exclusion notes:**

- National ministry ownership references unless tied to a municipal programme
- Personal names of front-line staff unless part of a governance role description
- Do not infer ownership from service branding alone

**Relationship to programme-level governance readiness:**

Programme ownership is necessary for independent external assessment of who can answer questions, implement changes, and account for decisions. Public naming of roles and units is observable evidence; aspirational commitments alone leave ownership **unobservable** for assessment purposes. This dimension does **not** score readiness — it records whether ownership evidence is publicly available.

---

### D2 — Human oversight and review

**Coding question:** Does public documentation describe human oversight, review, approval, or escalation for municipal AI systems or automated decisions?

**Examples of public evidence (`observable_named_artifact`):**

- Documented human-in-the-loop workflow for defined system classes
- Ethics or review board charter with meeting cadence and scope
- Algorithm register field for human review requirement per system

**Examples of weak/indirect evidence:**

- High-level fairness principles without review mechanism
- "Human centric AI" slogans without process detail
- Oversight mentioned only for future systems

**Exclusion notes:**

- Generic civil-service accountability statements not specific to AI
- Oversight of non-AI IT systems unless explicitly linked to AI programme
- Do not assume judicial or regulatory oversight unless municipally documented

**Relationship to programme-level governance readiness:**

Independent assessors need to know whether humans review outputs, escalate edge cases, and update controls. Observable review routines support assessment; policy commitments without process detail signal an **evidence gap**, not necessarily weak internal practice.

---

### D3 — Prompt, log, and data governance

**Coding question:** Does public documentation address prompt management, logging, retention, or training/sensitive data boundaries for municipal AI or automated systems?

**Examples of public evidence (`observable_named_artifact`):**

- Published log retention schedule for automated decision systems
- Data processing notice linked to a named AI tool with retention period
- Documented prompt template governance or prohibition on unsanctioned prompts

**Examples of weak/indirect evidence:**

- General GDPR privacy notice without AI-specific logging detail
- Open-data policy without linkage to model training or prompts
- Security policy mentioning logs generically

**Exclusion notes:**

- Do not code from technical screenshots or unofficial demos
- Exclude personal data examples; record locator only if policy-level
- Cloud provider generic terms unless municipally adopted as policy

**Relationship to programme-level governance readiness:**

Programme-level assessment requires traceability: what is logged, how long, who accesses logs, and how data/prompt boundaries are set. Public silence on these topics is `not_observable_publicly` — not evidence of absence of internal controls.

---

### D4 — Procurement and vendor stewardship

**Coding question:** Does public documentation show how vendors are selected, overseen, and held accountable for municipal AI systems?

**Examples of public evidence (`observable_named_artifact`):**

- Public contract award notice identifying AI system scope and vendor
- Vendor stewardship clause or SLA excerpt in official procurement file
- Register entry linking system to contract reference or vendor role

**Examples of weak/indirect evidence:**

- Vendor logo on a municipal innovation page without contract context
- Partnership press release without stewardship terms
- "We work with leading providers" language

**Exclusion notes:**

- Vendor marketing sites
- Subcontractor chains not disclosed in public municipal documents
- Do not infer contract terms from product documentation

**Relationship to programme-level governance readiness:**

Municipal AI often depends on vendors. Assessors need public evidence of procurement scope, stewardship, and accountability chains. Thin procurement disclosure creates observability gaps; it is not a ranking of vendor maturity.

---

### D5 — Incident, audit, and lifecycle accountability

**Coding question:** Does public documentation address incidents, audits, evaluations, updates, decommissioning, or lifecycle changes for municipal AI systems?

**Examples of public evidence (`observable_named_artifact`):**

- Published audit or evaluation summary of a named system
- Incident reporting procedure specific to automated systems
- Decommissioning notice or major version change log in register

**Examples of weak/indirect evidence:**

- Generic transparency commitment without incident route
- Annual digital report mentioning AI without lifecycle events
- Future audit promise in strategy document

**Exclusion notes:**

- National regulator actions unless mirrored in municipal publication
- Media-reported incidents without official municipal documentation
- Do not treat document `last_updated` date alone as lifecycle accountability

**Relationship to programme-level governance readiness:**

Sustained governance requires observable lifecycle accountability — what happens after deployment. Public documentation often emphasises launch and principles; this dimension captures whether post-deployment evidence is observable.

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
