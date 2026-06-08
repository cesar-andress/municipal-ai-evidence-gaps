# Coding protocol refinement log

**Derived from:** [`pilot_coding_protocol_test.md`](pilot_coding_protocol_test.md)  
**Protocol version audited:** v0.1  
**Date:** 2026-06-08  
**Scope:** Protocol validation only. No municipal findings. No cross-city comparison.

---

## Protocol readiness verdict

| Verdict | Selected |
|---------|----------|
| protocol ready | |
| **protocol needs minor revision** | **yes** |
| protocol needs major revision | |

---

## What worked well

1. **Five-dimension structure is codable.** All 15 pilot decisions (3 documents × 5 dimensions) were completed without dimension gaps or label invalidity.
2. **Four evidence-status labels are sufficient** for initial discrimination between named artefacts, commitments, weak signals, and non-observability within a single source.
3. **Non-claim boundary is clear in practice.** Pilot coding stayed at public-text observability without drifting into compliance or quality judgment.
4. **Source-type diversity tested key edge cases:** algorithm register (Amsterdam), governance framework summary (Barcelona), and principles-based AI policy (Helsinki) each surfaced distinct protocol questions.
5. **Dimension sheets D4 and D5** produced low ambiguity on principles-only and register-index sources (`not_observable_publicly` was straightforward).
6. **CSV/schema alignment** (`src/evidence_gaps/schema.py`) matches coding protocol enums; no schema change required for pilot.

---

## Ambiguous cases

| Case ID | Source (pilot) | Dimension | Status assigned | Ambiguity |
|---------|----------------|-----------|-----------------|-----------|
| A1 | Amsterdam register | D2 | `partial_or_indirect_signal` | DPIA/IAMA labels on cards — oversight artefact or metadata stub? |
| A2 | Amsterdam register | D5 | `partial_or_indirect_signal` | `Status` + `Laatst gewijzigd` vs protocol exclusion of date-only lifecycle evidence |
| A3 | Barcelona protocol summary | D1 | `observable_policy_commitment` | "Governance and supervision bodies" unnamed |
| A4 | Barcelona protocol summary | D2 | `observable_policy_commitment` | "Supervised" + risk-tier language without workflow steps |
| A5 | Helsinki ethical principles | D3 | `observable_policy_commitment` | Privacy/security principles vs prompt/log specificity |

---

## Dimensions requiring clarification

| Dimension | Priority | Issue | Proposed clarification |
|-----------|----------|-------|--------------------------|
| D1 | Medium | Register publisher ≠ programme owner | Index-level org name → `partial_or_indirect_signal`; named unit/role/contact → `observable_named_artifact` |
| D2 | **High** | Register impact-assessment fields | Entry-level named assessment type (DPIA, ethics review) → `observable_named_artifact` when entry is unit; index scan → `partial_or_indirect_signal` |
| D3 | Medium | Ethical principles vs technical governance | Principles without log/prompt/retention detail → `observable_policy_commitment` max |
| D4 | Low | Procurement language in protocols | Tender-stage/process reference without contract ID → `observable_policy_commitment` |
| D5 | **High** | Lifecycle status fields in registers | Status enum (in use / decommissioned / in development) → `partial_or_indirect_signal`; incident/audit artefact still needed for `observable_named_artifact` |

---

## Evidence-status issues

| Issue | Frequency in pilot | Recommendation |
|-------|-------------------|----------------|
| `observable_policy_commitment` vs `partial_or_indirect_signal` boundary | 5/15 decisions required deliberation | Add decision tree: named role/artefact → named_artifact; explicit procedural commitment → policy_commitment; vague or incomplete reference → partial |
| `partial_or_indirect_signal` vs `not_observable_publicly` | 2/15 required deliberation | Reinforce: topic mentioned without locatable detail = partial; topic absent = not_observable |
| Register metadata as artefact | 3 Amsterdam dimensions | Add appendix example row for algorithm-register entry coding |
| Summary page depth | 2 Barcelona dimensions | Require manifest note `coding_depth: summary` vs `full` or mandate attachment retrieval before coding |

---

## Recommended revisions (v0.1.1 draft scope)

### Priority 1 — before full-corpus coding

1. **Coding unit rule for algorithm registers**
   - Default: one manifest row = register index (all entries scanned for recurring fields).
   - Optional: per-entry coding when entry has distinct public detail page; record in `coder_notes`.
2. **Document depth rule**
   - If manifest URL is a landing/summary page, coder must follow primary linked artefact or record `coding_depth: summary` in notes.
3. **D2/D5 worked examples for register fields**
   - Add two annotated examples to `docs/coding_protocol.md` appendix.

### Priority 2 — improve reliability

4. **Decision tree for evidence-status selection** (one page, flowchart or table).
5. **Language handling note:** pilot coded Helsinki FI source with protocol definitions in EN; add rule for quote language in `quoted_evidence` field.
6. **Timing benchmark:** use pilot mean 34 min/document for workload planning (see pilot report).

### Not recommended

- Adding dimensions or evidence-status labels (pilot did not exhaust v0.1 taxonomy).
- Municipal weighting or scoring rules (violates non-claims).

---

## Revision tracking

| Item | Target doc | Status |
|------|------------|--------|
| Register coding unit rule | `docs/coding_protocol.md` | Proposed |
| Summary vs full document rule | `docs/coding_protocol.md` | Proposed |
| D2/D5 register examples | `docs/coding_protocol.md` | Proposed |
| Evidence-status decision tree | `docs/coding_protocol.md` | Proposed |
| Quote language convention | `docs/study_protocol_v0_1.md` | Proposed |

No protocol files were modified in this pilot tranche.
