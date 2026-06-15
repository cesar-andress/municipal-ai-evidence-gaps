# Second-coder protocol — IRR subsample v1

**Protocol version:** v0.1.1 (frozen — do not modify)  
**Primary documents:** [`coding_protocol.md`](coding_protocol.md), [`coding_decision_rules_v0_1_1.md`](coding_decision_rules_v0_1_1.md)  
**Subsample design:** [`irr_study_design_v1.md`](irr_study_design_v1.md)

---

## 1. Purpose and boundaries

You will independently assign **evidence-status labels** to **40 document–dimension assessments** (8 documents × 5 dimensions) drawn from the municipal AI evidence corpus.

**You are measuring:** what publicly accessible official text makes observable under uniform rules.

**You are not measuring:** municipal governance quality, legal compliance, or performance.

**Do not:** compare cities, rank municipalities, or infer internal practices from public silence.

---

## 2. Before you start (required reading)

1. Read [`coding_protocol.md`](coding_protocol.md) §Evidence-status labels and §Non-claims (30 min).
2. Read [`coding_decision_rules_v0_1_1.md`](coding_decision_rules_v0_1_1.md) §1–§6 decision trees and tie-breaks (45 min).
3. Review six worked examples in decision rules §6 (15 min).
4. Confirm you have **not** seen Coder 1's labels for your assigned documents.

**Briefing checkpoint:** Coder 1 confirms you can explain Steps 1–4 and when register-level vs entry-level coding applies.

---

## 3. Assigned documents (8 sources; 40 cells)

Code **only** these manifest URLs. Use the **access date in the manifest**; retrieve current public text. If a URL now returns HTTP 403, code all five dimensions `not_observable_publicly` and note `retrieval_status: blocked_at_irr_date` in `coder_notes` — do **not** substitute another URL.

| ID | Municipality | Source type | URL |
|----|--------------|-------------|-----|
| IRR-01 | Amsterdam | algorithm register | `https://algoritmeregister.amsterdam.nl/` |
| IRR-02 | Barcelona | governance framework | `https://ajuntament.barcelona.cat/digital/en/technology-accessible-everyone/ethical-use-artificial/ethical-use-artificial-intelligence/protocol` |
| IRR-03 | Barcelona | transparency portal | `https://ajuntament.barcelona.cat/digital/en/technology-accessible-everyone/ethical-use-artificial` |
| IRR-04 | Copenhagen | committee record | `https://www.kk.dk/dagsordener-og-referater/Økonomiudvalget/møde-18022020/referat/punkt-6` |
| IRR-05 | Helsinki | algorithm register | `https://ai.hel.fi/en/ai-register/` |
| IRR-06 | Helsinki | AI policy | `https://ai.hel.fi/eettiset-periaatteet/` |
| IRR-07 | Vienna | AI strategy | `https://digitales.wien.gv.at/wp-content/uploads/sites/47/2025/09/1065373-2025_MD-OS_PIKT_KI-Strategie_Sanjath_EN_korr-bf.pdf` |
| IRR-08 | Vienna | governance framework | `https://digitales.wien.gv.at/ki-rahmenbedingungen/` |

---

## 4. Coding procedure (per document)

For each document, complete **five rows** (D1–D5):

1. **Select coding unit** — apply register decision tree (R1–R2) if source is an algorithm register; default register-level for index URLs.
2. **Select coding depth** — apply document-depth tree (D1–D4); follow hierarchy source > annex > committee record > summary.
3. **For each dimension D1–D5**, walk evidence-status Steps 1–4.
4. **Apply tie-breaks** TB-1–TB-6 when ambiguous; record `tie_break: TB-n` in notes.
5. **Record fields:**
   - `evidence_status` (required)
   - `quoted_evidence` (source language; short verbatim or field label)
   - `page_or_section` (heading, register field, or PDF page)
   - `coder_notes` (coding_unit, coding_depth, tie_break as needed)

**Dimension labels (use exactly):**

- `D1_programme_ownership`
- `D2_human_oversight_and_review`
- `D3_prompt_log_and_data_governance`
- `D4_procurement_and_vendor_stewardship`
- `D5_incident_audit_and_lifecycle_accountability`

**Evidence-status labels (use exactly):**

- `observable_named_artifact`
- `observable_policy_commitment`
- `partial_or_indirect_signal`
- `not_observable_publicly`

---

## 5. Independence rules

- Code **before** any reconciliation meeting.
- Do **not** discuss specific documents with Coder 1 until all 40 cells are submitted.
- Questions about **protocol rules** (not document content) may be logged; Coder 1 answers generically without revealing their labels.

---

## 6. Disagreement resolution (after independent coding)

1. Coder 1 runs agreement script (see workflow doc).
2. Both coders review **disagreements only** (expect ~15–25% raw disagreement on partial/commitment boundaries).
3. Apply published tie-break rules in order TB-1–TB-6.
4. If still tied after tie-breaks, Coder 1 documents escalation in `irr_reconciliation_log_v1.md` and retains Coder 1 label for main corpus; **both labels preserved** in IRR file for κ calculation (pre-reconciliation κ reported).

**Report two κ values:**

- **κ~initial~** — independent codes only (primary for manuscript)
- **κ~reconciled~** — optional supplementary after adjudication

---

## 7. Deliverables from Coder 2

1. Completed worksheet: `data/processed/irr_coding_coder2_v1.csv`
2. Time log (optional): minutes per document
3. Protocol ambiguity log: any rule gaps discovered

**Deadline target:** one working week after briefing (4–5 hours coding time).

---

## 8. Quality checklist (self-audit before submit)

- [ ] Exactly 40 rows (8 URLs × 5 dimensions)
- [ ] No duplicate dimension per URL
- [ ] All four evidence-status values used where appropriate
- [ ] Register sources have `coding_unit` in notes
- [ ] No governance-quality language in notes
- [ ] File validates against worksheet template columns

---

**Contact:** Coder 1 / corresponding author for protocol-only questions.
