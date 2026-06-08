# Protocol change log v0.1.1

**From:** Coding protocol v0.1  
**To:** Coding protocol v0.1.1  
**Date:** 2026-06-08  
**Trigger:** Pilot coding protocol validation (`pilot_coding_protocol_test.md`, `coding_protocol_refinement_log.md`)  
**Scope:** Clarifications and decision rules only. No new dimensions, evidence labels, or schema changes.

---

## Summary

| Metric | Value |
|--------|-------|
| Pilot ambiguities addressed | 5 (A1–A5) |
| New sections in `coding_protocol.md` | 4 |
| New supporting document | `docs/coding_decision_rules_v0_1_1.md` |
| Schema changes | None |
| Dimensions added/removed | None |
| Evidence labels added/removed | None |

**Verdict at v0.1:** protocol needs minor revision → **resolved in v0.1.1**

---

## Change register

### C1 — Algorithm register coding unit

| Field | Detail |
|-------|--------|
| **Issue** | Pilot case A1/A2: unclear whether to code register index or individual entries; index-level publisher and impact fields produced inconsistent D1/D2/D5 labels. |
| **Resolution** | Added § Algorithm registers with default register-level coding, required entry-level conditions, and quick-reference table. |
| **Rationale** | Manifest rows often point to index URLs; defaulting to register-level avoids false precision. Entry-level coding required when URL or scope targets one system with populated fields. |

### C2 — Summary page vs source document depth

| Field | Detail |
|-------|--------|
| **Issue** | Pilot Barcelona protocol coded at summary-page depth; full protocol link not retrieved; D1–D5 depth ambiguous. |
| **Resolution** | Added § Document hierarchy and coding depth with preference order: source document > annex > committee record > summary page. Mandate `coding_depth` in `coder_notes`. |
| **Rationale** | Observability should reflect the richest publicly accessible artefact; summary pages under-state commitments available in linked PDFs. |

### C3 — Evidence-status boundaries

| Field | Detail |
|-------|--------|
| **Issue** | Five of fifteen pilot decisions required deliberation between `observable_policy_commitment` and `partial_or_indirect_signal`; boundary with `observable_named_artifact` unclear for register metadata. |
| **Resolution** | Added § Evidence-status boundaries with positive/negative examples per label. Created `coding_decision_rules_v0_1_1.md` with four-step decision tree and six tie-breaking rules. |
| **Rationale** | Reliability requires explicit discriminators; pilot showed v0.1 labels are sufficient but boundaries were under-specified. |

### C4 — D2 register impact-assessment fields

| Field | Detail |
|-------|--------|
| **Issue** | Pilot A1: DPIA/IAMA labels on register cards — oversight artefact or metadata stub? |
| **Resolution** | D2 worked examples: entry-page named assessment types → `observable_named_artifact`; index scan with empty/inconsistent fields → `partial_or_indirect_signal`. |
| **Rationale** | Named assessment type on a locatable entry page meets "concrete named artefact"; index-level stubs do not. |

### C5 — D3 ethical principles vs technical governance

| Field | Detail |
|-------|--------|
| **Issue** | Pilot A5: Helsinki privacy/security principles coded D3; unclear cap without log/prompt detail. |
| **Resolution** | D3 boundary rule: ethical principles alone cannot exceed `observable_policy_commitment`. Added worked examples table. |
| **Rationale** | D3 targets prompt/log/retention specificity; principles address adjacent but distinct governance concerns. |

### C6 — D5 lifecycle status vs audit artefacts

| Field | Detail |
|-------|--------|
| **Issue** | Pilot A2: register `Status` and `Last updated` vs protocol exclusion of date-only lifecycle evidence. |
| **Resolution** | D5 boundary rule: status enum → `partial_or_indirect_signal`; `observable_named_artifact` requires named audit/incident/evaluation document. Worked examples added. |
| **Rationale** | Status metadata signals lifecycle state but does not substitute for accountability artefacts required by D5 coding question. |

### C7 — D1 unnamed governance bodies

| Field | Detail |
|-------|--------|
| **Issue** | Pilot A3: Barcelona "governance and supervision bodies" without names. |
| **Resolution** | D1 examples: unnamed bodies → `observable_policy_commitment`; named board/role → `observable_named_artifact`. |
| **Rationale** | Explicit institutional commitment without locatable names fits policy-commitment tier. |

### C8 — D2 supervised-use language

| Field | Detail |
|-------|--------|
| **Issue** | Pilot A4: "supervised" + EU risk-tier language without workflow steps. |
| **Resolution** | D2 worked example: procedural obligation without steps → `observable_policy_commitment`. Tie-break TB-3 in decision rules. |
| **Rationale** | Explicit supervised-use obligation exceeds fragmentary signal but lacks named artefact detail. |

### C9 — D4 procurement in governance protocols

| Field | Detail |
|-------|--------|
| **Issue** | Pilot confirmed procurement-stage language mappable but threshold unclear. |
| **Resolution** | D4 example: protocol integrating procurement process → `observable_policy_commitment` without contract ID. |
| **Rationale** | Tender-stage procedural integration is an explicit municipal commitment observable in public text. |

### C10 — Quote language convention

| Field | Detail |
|-------|--------|
| **Issue** | Pilot coded Finnish source with English protocol definitions; quote field convention unspecified. |
| **Resolution** | Added § Quote language convention: `quoted_evidence` in source language; English gloss in `coder_notes`. |
| **Rationale** | Preserves audit trail fidelity while allowing coders to work from English protocol text. |

### C11 — Decision rules document

| Field | Detail |
|-------|--------|
| **Issue** | Pilot recommended standalone decision tree and escalation path. |
| **Resolution** | Created `docs/coding_decision_rules_v0_1_1.md` with decision trees (evidence status, coding unit, document depth), tie-breaking rules, escalation rules, and six worked examples. |
| **Rationale** | Separates operational rules from dimension sheets; supports double-coding reconciliation. |

---

## Files modified or created

| File | Action |
|------|--------|
| `docs/coding_protocol.md` | Updated v0.1 → v0.1.1 |
| `docs/coding_decision_rules_v0_1_1.md` | Created |
| `docs/methodology.md` | Updated protocol reference |
| `outputs/reports/protocol_change_log_v0_1_1.md` | Created (this file) |
| `README.md` | Coding protocol version: v0.1.1 |

## Not changed

- `src/evidence_gaps/schema.py` (enums unchanged)
- `corpus_manifest_v0_1.csv`
- `data/processed/coding_template.csv` columns
- `non_claim_boundary` constant (`observability_only_v0_1`)

---

## Pilot case resolution map

| Case ID | v0.1 ambiguity | v0.1.1 rule |
|---------|----------------|-------------|
| A1 | DPIA on register cards | C4 — entry vs index rule |
| A2 | Status + last updated | C6 — D5 boundary rule |
| A3 | Unnamed governance bodies | C7 — D1 commitment tier |
| A4 | Supervised use language | C8 — D2 commitment tier |
| A5 | Principles vs D3 technical | C5 — D3 cap rule |
