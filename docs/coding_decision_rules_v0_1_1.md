# Coding decision rules v0.1.1

**Protocol:** [`coding_protocol.md`](coding_protocol.md) v0.1.1  
**Derived from:** Pilot validation (`outputs/reports/pilot_coding_protocol_test.md`, `outputs/reports/coding_protocol_refinement_log.md`)  
**Date:** 2026-06-08

This document operationalises evidence-status assignment, coding-unit selection, and disagreement resolution. It does not authorise municipal comparison, ranking, or governance-quality inference.

---

## 1. Decision tree — evidence status

Start at **Step 1** for each `municipality × source × dimension` decision.

```
STEP 1: Is the dimension mentioned or addressed in the coded artefact?
│
├─ NO  → not_observable_publicly
│
└─ YES → STEP 2

STEP 2: Does the source name a concrete, locatable artefact for this dimension?
        (named role, assessment type on entry page, contract ID, audit report,
         retention period, incident procedure document)
│
├─ YES → observable_named_artifact
│
└─ NO  → STEP 3

STEP 3: Does the source state an explicit obligation, principle, or procedural rule?
        (supervised use, responsible party per service, procurement-stage safeguards,
         ethical principles with clear requirements)
│
├─ YES → observable_policy_commitment
│
└─ NO  → STEP 4

STEP 4: Is there a fragmentary, implied, or metadata-only reference?
        (publisher name only, empty register field, status enum, date alone,
         "data protection mechanisms" without detail, vendor logo)
│
├─ YES → partial_or_indirect_signal
│
└─ NO  → not_observable_publicly
        (dimension nominally present but no codable public content)
```

### Decision tree — quick examples

| Evidence snippet | Step reached | Label |
|------------------|--------------|-------|
| No mention of procurement | 1 | `not_observable_publicly` |
| `Impacttoetsen: DPIA` on register **entry page** | 2 | `observable_named_artifact` |
| "Each service must have a responsible party" | 3 | `observable_policy_commitment` |
| Register index: publisher "Municipality" only | 4 | `partial_or_indirect_signal` |
| `Status: Decommissioned` on register card | 4 | `partial_or_indirect_signal` |

---

## 2. Decision tree — coding unit (algorithm registers)

```
STEP R1: Does the manifest URL point to a single system's detail page?
│
├─ YES → ENTRY-LEVEL coding (one entry × five dimensions)
│
└─ NO  → STEP R2

STEP R2: Is the manifest row explicitly scoped to one named entry in coder_notes
         or source_title?
│
├─ YES → ENTRY-LEVEL coding
│
└─ NO  → REGISTER-LEVEL coding (scan all visible entries; note in coder_notes)
```

**Register-level default** applies to index/listing URLs unless R1 or R2 applies.

---

## 3. Decision tree — document depth

```
STEP D1: Is the manifest URL a source document (PDF, full protocol, policy page,
         register entry)?
│
├─ YES → Code that URL. coding_depth: full
│
└─ NO  → STEP D2

STEP D2: Is a linked annex or attachment publicly accessible?
         (bilag, "complete protocol" PDF, strategy attachment)
│
├─ YES → Code annex/attachment. Record URL in coder_notes. coding_depth: annex
│
└─ NO  → STEP D3

STEP D3: Is the URL a committee record referencing an adopted document?
│
├─ YES → Code minutes page; note missing annex if inaccessible.
│         coding_depth: committee_record
│
└─ NO  → STEP D4

STEP D4: Is the URL a summary/landing page only?
│
├─ YES → Code summary page. coding_depth: summary
│
└─ NO  → Code available text; record ambiguity in coder_notes.
```

**Hierarchy reminder:** source document > annex > committee record > summary page.

---

## 4. Tie-breaking rules

Apply in order when two labels appear equally defensible.

| Priority | Rule | Example |
|----------|------|---------|
| TB-1 | **Prefer the more conservative label** (less specific) when evidence is ambiguous | Named artefact vs commitment → choose commitment |
| TB-2 | **Prefer `partial_or_indirect_signal` over `observable_policy_commitment`** when obligation language is vague | "Human-centric AI" → partial, not commitment |
| TB-3 | **Prefer `observable_policy_commitment` over `partial_or_indirect_signal`** when an explicit obligation is stated | "Supervised use required" → commitment, not partial |
| TB-4 | **Prefer `not_observable_publicly` over `partial_or_indirect_signal`** when the dimension is not addressed | Principles page with no procurement text → not_observable for D4 |
| TB-5 | **Register index scans default to `partial_or_indirect_signal`** for D1/D2/D5 unless entry-level coding applies | Index-level DPIA mention on some cards only |
| TB-6 | **D3 ethical principles cap at `observable_policy_commitment`** unless log/prompt/retention detail is present | Helsinki-style principles page |

Document tie-break application in `coder_notes` (e.g. `tie_break: TB-3`).

---

## 5. Escalation rules

| Trigger | Action | Record in |
|---------|--------|-----------|
| Two coders disagree on evidence status | Reviewer applies tie-breaking rules; if still tied, convene protocol clarification | `coder_notes`; log in refinement doc if rule gap found |
| Manifest URL is summary but full document is linked and retrievable | Coder must retrieve full document before finalising; if blocked, flag `verify_manually` | `coder_notes`: `coding_depth: summary; retrieval blocked` |
| Register entry vs register-level unclear | Default register-level; escalate if manifest row title names one system | `coder_notes`: `coding_unit: register_level` |
| Evidence spans manifest row + linked annex | Code highest artefact per hierarchy; one coding row set per effective unit | `coder_notes`: `coded artefact: [URL]` |
| New source type not covered by protocol | Do not code; escalate to protocol maintainer | Issue tracker / refinement log |
| Label would imply compliance or quality judgment | Re-code using observability definition only; escalate if recurrent | `non_claim_boundary` check |

**Escalation outcome:** Update [`coding_protocol.md`](coding_protocol.md) or this document — not ad hoc coder discretion.

---

## 6. Worked decision examples (pilot-derived)

### Example 1 — Register index, D2

- **Source:** Algorithm register index (multiple cards)
- **Evidence:** Some cards show `DPIA`; many show empty impact field
- **Coding unit:** Register-level
- **Tree:** Step 1 YES → Step 2 NO (inconsistent index metadata, not entry artefact) → Step 3 NO → Step 4 YES
- **Label:** `partial_or_indirect_signal`
- **Tie-break:** TB-5

### Example 2 — Register entry page, D2

- **Source:** Single algorithm detail page
- **Evidence:** `Impacttoetsen: DPIA, De Ethische Bijsluiter`
- **Coding unit:** Entry-level
- **Tree:** Step 1 YES → Step 2 YES
- **Label:** `observable_named_artifact`

### Example 3 — Protocol summary, D4

- **Source:** Governance framework summary page
- **Evidence:** "Combines public procurement process with implementation stages"
- **Coding depth:** summary (unless full PDF retrieved)
- **Tree:** Step 1 YES → Step 2 NO → Step 3 YES
- **Label:** `observable_policy_commitment`

### Example 4 — Ethical principles, D3

- **Source:** AI policy (principles page)
- **Evidence:** Privacy, security, transparency principles; no log retention
- **Tree:** Step 1 YES → Step 2 NO → Step 3 YES
- **Label:** `observable_policy_commitment`
- **Cap rule:** D3 principles cannot exceed commitment without log/prompt detail

### Example 5 — Register index, D5

- **Source:** Algorithm register index
- **Evidence:** Status `In use` / `Decommissioned`; last-modified dates
- **Tree:** Step 1 YES → Step 2 NO → Step 3 NO → Step 4 YES
- **Label:** `partial_or_indirect_signal`
- **Note:** Status enum ≠ audit artefact; date alone excluded

### Example 6 — AI policy, D5

- **Source:** Ethical principles page
- **Evidence:** No incident, audit, or lifecycle language
- **Tree:** Step 1 NO
- **Label:** `not_observable_publicly`

---

## 7. Field conventions

| Field | Convention |
|-------|------------|
| `quoted_evidence` | Source language; short verbatim or field label |
| `page_or_section` | Section heading, register field name, or PDF page |
| `coder_notes` | `coding_unit`, `coding_depth`, `tie_break`, `coded artefact` as needed |
| `non_claim_boundary` | Always `observability_only_v0_1` |

---

## Version history

| Version | Date | Change |
|---------|------|--------|
| v0.1.1 | 2026-06-08 | Initial decision rules; pilot-derived trees and tie-breaks |
