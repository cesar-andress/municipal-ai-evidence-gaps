# Pilot coding protocol test

**Test date:** 2026-06-08  
**Protocol version:** v0.1 (`docs/coding_protocol.md`)  
**Purpose:** Validate D1–D5 coding workflow on three manifest sources before full-corpus coding.  
**Non-claims:** No paper findings; no municipal comparison; no ranking; no governance-quality inference.

---

## Pilot design

| Parameter | Value |
|-----------|-------|
| Documents coded | 3 |
| Dimensions per document | 5 (D1–D5) |
| Coding decisions recorded | 15 |
| Evidence labels used | 4 (v0.1 taxonomy) |
| `non_claim_boundary` | `observability_only_v0_1` (not applied row-by-row in this test log) |

### Document selection

| Municipality | Selected source | `source_type` | Selection rationale |
|--------------|-----------------|---------------|---------------------|
| Amsterdam | [Amsterdam Algorithm Register](https://algoritmeregister.amsterdam.nl/) | algorithm register | Preferred types (AI strategy, AI policy, governance framework) are `bot_gated` in manifest v0.1. Register is the only `ok` substantive source; tests register-as-coding-unit rules. |
| Barcelona | [Protocol for incorporating artificial intelligence into all municipal services](https://ajuntament.barcelona.cat/digital/en/technology-accessible-everyone/ethical-use-artificial/ethical-use-artificial-intelligence/protocol) | governance framework | Matches preferred type; `ok` retrieval; tests governance-framework depth and procurement/lifecycle language. |
| Helsinki | [Helsingin kaupungin datan ja tekoälyn eettiset periaatteet](https://ai.hel.fi/eettiset-periaatteet/) | AI policy | Matches preferred type; `ok` retrieval; tests principles-only policy page. |

**Access note:** Barcelona pilot coding used the public summary page at the manifest URL. A linked full-protocol document (`See the complete protocol`) was not retrieved in this test tranche.

---

## Coding log — Amsterdam Algorithm Register

**Source ID (pilot):** `pilot-amsterdam-register`  
**Language:** NL  
**Coder time:** 52 minutes

| Dimension | `evidence_status` | Ambiguity notes | Coding difficulty | Missing guidance | Suggested protocol clarification |
|-----------|-------------------|-----------------|-------------------|------------------|----------------------------------|
| D1_programme_ownership | `partial_or_indirect_signal` | Each entry lists publisher "Gemeente Amsterdam" but no named programme owner, unit, or contact for AI governance. | Medium | Rule for when organisational publisher counts vs named role required. | Add register-specific rule: index-level publisher ≠ programme owner; code `partial_or_indirect_signal` unless entry-level responsible unit/contact is populated. |
| D2_human_oversight_and_review | `partial_or_indirect_signal` | "Impacttoetsen" fields reference DPIA, IAMA, Ethical Bijsluiter on some entries; many show "Veld niet ingevuld." Index page does not describe review workflow. | High | Whether impact-assessment labels on register cards count as oversight evidence. | Clarify that named assessment artefact types (DPIA, IAMA) at entry level = `observable_named_artifact` for D2 **when entry is coding unit**; index-only scan = `partial_or_indirect_signal`. |
| D3_prompt_log_and_data_governance | `partial_or_indirect_signal` | Privacy Quickscan / Privacyverklaring appear on some entries; no prompt, log, or retention detail on index view. | Medium | Whether privacy impact labels without linked policy text are sufficient. | Add rule: privacy-assessment label alone on register card = `partial_or_indirect_signal`; linked municipal policy with retention detail required for `observable_named_artifact`. |
| D4_procurement_and_vendor_stewardship | `not_observable_publicly` | No vendor, contract, or tender reference on register index entries reviewed. | Low | — | — |
| D5_incident_audit_and_lifecycle_accountability | `partial_or_indirect_signal` | Entry `Status` values (`In gebruik`, `Buiten gebruik`, `In ontwikkeling`) and `Laatst gewijzigd` timestamps are visible; protocol excludes `last_updated` alone as lifecycle accountability. | High | Boundary between lifecycle **status field** and prohibited `last_updated`-only coding. | Clarify: register status enum + decommissioning state = `partial_or_indirect_signal`; audit/incident procedure still required for `observable_named_artifact`. |

---

## Coding log — Barcelona AI implementation protocol (summary page)

**Source ID (pilot):** `pilot-barcelona-protocol`  
**Language:** EN  
**Coder time:** 28 minutes

| Dimension | `evidence_status` | Ambiguity notes | Coding difficulty | Missing guidance | Suggested protocol clarification |
|-----------|-------------------|-----------------|-------------------|------------------|----------------------------------|
| D1_programme_ownership | `observable_policy_commitment` | Text references "governance and supervision bodies" without naming office holders on this page. | Medium | Threshold for named artefact when bodies are referenced but not listed. | Add rule: unnamed governance bodies in official protocol summary = `observable_policy_commitment`; named board/role = `observable_named_artifact`. |
| D2_human_oversight_and_review | `observable_policy_commitment` | Protocol states systems must be used in a "supervised" way; high-risk systems require stricter guarantee mechanisms and algorithmic impact studies. | Medium | Whether "supervised" without workflow steps is commitment vs partial signal. | Clarify EU risk-tier procedural language maps to `observable_policy_commitment` unless step-by-step review workflow is documented. |
| D3_prompt_log_and_data_governance | `partial_or_indirect_signal` | References "City Council's data protection mechanisms" without AI-specific logging or prompt rules on summary page. | Low | — | Add guidance for summary-page vs full-document coding depth. |
| D4_procurement_and_vendor_stewardship | `observable_policy_commitment` | Explicitly combines "public procurement process" with implementation stages and tendering safeguards. | Low | — | Confirm procurement-stage language in governance protocols = `observable_policy_commitment` even without contract IDs. |
| D5_incident_audit_and_lifecycle_accountability | `partial_or_indirect_signal` | "Life cycle of an algorithmic system" and risk-tier guarantee mechanisms mentioned; no incident route or audit publication on summary page. | Medium | Whether lifecycle mention in protocol preamble counts as partial signal. | Clarify lifecycle **process reference** in protocol = `partial_or_indirect_signal`; published audit/incident artefact = `observable_named_artifact`. |

---

## Coding log — Helsinki ethical principles for data and AI

**Source ID (pilot):** `pilot-helsinki-policy`  
**Language:** FI  
**Coder time:** 22 minutes

| Dimension | `evidence_status` | Ambiguity notes | Coding difficulty | Missing guidance | Suggested protocol clarification |
|-----------|-------------------|-----------------|-------------------|------------------|----------------------------------|
| D1_programme_ownership | `observable_policy_commitment` | Principle "Vastuu ja luottamus" requires a responsible party (`vastuutaho`) for each AI-using service; no named municipal office on page. | Low | — | Add example: service-level accountable-party principle = `observable_policy_commitment`. |
| D2_human_oversight_and_review | `observable_policy_commitment` | Principle "Ihmisen kontrollissa" requires human monitoring and intervention capacity for high-risk situations. | Low | — | — |
| D3_prompt_log_and_data_governance | `observable_policy_commitment` | Principles cover transparency, privacy, security, explainability; no prompt templates or log-retention periods. | Medium | Boundary between ethical data principles and D3 technical governance. | Clarify D3 requires prompt/log/retention specificity; ethical privacy/security principles alone = `observable_policy_commitment`, not `observable_named_artifact`. |
| D4_procurement_and_vendor_stewardship | `not_observable_publicly` | No procurement, vendor, or contract language. | Low | — | — |
| D5_incident_audit_and_lifecycle_accountability | `not_observable_publicly` | No incident, audit, evaluation, or decommissioning procedure. | Low | — | — |

---

## Pilot timing summary

| Source ID | Document type | Coder time (minutes) | Mean difficulty (1–3)* |
|-----------|---------------|----------------------|------------------------|
| `pilot-amsterdam-register` | algorithm register | 52 | 2.4 |
| `pilot-barcelona-protocol` | governance framework | 28 | 1.8 |
| `pilot-helsinki-policy` | AI policy | 22 | 1.4 |
| **Pilot mean** | | **34** | **1.9** |

\*Difficulty scale used in pilot: 1 = low, 2 = medium, 3 = high.

### Full-corpus effort estimate

| Parameter | Estimate |
|-----------|----------|
| Manifest rows (v0.1) | 23 |
| Dimensions per row | 5 |
| Total coding decisions | 115 |
| Mean minutes per document (pilot) | 34 |
| Single-coder document time | ~13 hours (782 min) |
| Protocol notes + CSV entry overhead (+20%) | ~2.5 hours |
| **Single-coder total (estimated)** | **~15–16 hours** |
| Double-coding subset (3 docs × 2 coders, reconciliation) | +4–5 hours |
| **Full-corpus protocol validation to coding-ready** | **~19–21 hours** |

Estimates assume manifest URLs remain accessible; register and committee-record sources may take longer than policy pages.

---

## Protocol readiness recommendation

**Recommendation:** `protocol needs minor revision`

**Rationale:** The v0.1 framework is operable — all 15 pilot decisions mapped to valid dimensions and evidence statuses without protocol violations. Recurring ambiguities concern (1) algorithm-register coding unit (index vs entry), (2) summary page vs full document depth, and (3) boundaries between `observable_policy_commitment` and `partial_or_indirect_signal` for procedural references. No pilot decision required a new dimension or evidence label. Revisions should be clarifications and worked examples, not a structural redesign.

---

## Artefacts

| File | Role |
|------|------|
| `outputs/reports/pilot_coding_protocol_test.md` | This pilot log |
| `outputs/reports/coding_protocol_refinement_log.md` | Consolidated refinement recommendations |
