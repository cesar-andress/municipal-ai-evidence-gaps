# Coding decision log v0.1.1

**Protocol:** v0.1.1  
**Coding date:** 2026-06-08  
**Output:** [`data/processed/coding_results_v0_1_1.csv`](../../data/processed/coding_results_v0_1_1.csv)

This log records difficult coding decisions, tie-break applications, and protocol edge cases encountered during full-corpus coding. It does not contain findings, municipal comparisons, or governance-quality judgments.

---

## Summary

| Category | Count |
|----------|-------|
| Difficult cases logged | 12 |
| Tie-break applications | 3 |
| Formal escalations | 0 |
| Protocol edge cases | 8 |

All cases were resolved using [`coding_decision_rules_v0_1_1.md`](../../docs/coding_decision_rules_v0_1_1.md) without protocol modification.

---

## Difficult cases

### DC-01 — Amsterdam algorithm register (register-level unit)

| Field | Value |
|-------|-------|
| Source | `https://algoritmeregister.amsterdam.nl/` |
| Dimension | D2, D5 |
| Issue | Mixed populated/empty `Impacttoetsen` fields; status enum vs `last_updated` timestamps |
| Resolution | Register-level coding; D2/D5 → `partial_or_indirect_signal` per TB-5 |
| Rule | Algorithm register default (§ coding unit) |

### DC-02 — Barcelona protocol summary vs full document

| Field | Value |
|-------|-------|
| Source | Protocol summary URL |
| Issue | Linked "complete protocol" not separately manifest-registered |
| Resolution | Coded summary page; `coding_depth: summary` in notes |
| Rule | Document hierarchy — summary when full PDF not manifest row |

### DC-03 — Barcelona ES/EN strategy parallel editions

| Field | Value |
|-------|-------|
| Sources | ES and EN strategy pages |
| Issue | Near-duplicate content across language variants |
| Resolution | Independent coding rows per manifest URL; equivalent labels where text parallels |
| Rule | One manifest row = one coding unit |

### DC-04 — Copenhagen committee records without bilag retrieval

| Field | Value |
|-------|-------|
| Sources | AI kodeks; digitaliseringsstrategi committee pages |
| Issue | Substantive text in bilag 1 attachments not separately coded |
| Resolution | Coded minutes-page text only; `coding_depth: committee_record` |
| Rule | Hierarchy: committee record when annex not manifest-registered |

### DC-05 — Helsinki register index vs ethical principles

| Field | Value |
|-------|-------|
| Sources | `ai.hel.fi/en/ai-register/` vs `eettiset-periaatteet` |
| Issue | Same municipality, different observability profiles |
| Resolution | Register index → mostly `not_observable_publicly`; principles page → commitments D1–D3 |
| Rule | Source-type and coding-unit rules applied per URL |

### DC-06 — Helsinki paatokset decision vs principles page

| Field | Value |
|-------|-------|
| Sources | paatokset.hel.fi record vs ai.hel.fi principles |
| Issue | Decision adopts same eight principles; content overlap |
| Resolution | Both coded independently; equivalent D1–D3 labels on observable principle text |
| Rule | Parallel editions / committee record + policy page |

### DC-07 — Vienna KI strategy portal (TOC only)

| Field | Value |
|-------|-------|
| Source | `wien.gv.at/spezial/ki-strategie/` |
| Issue | Index page contains section titles only |
| Resolution | D2 `partial_or_indirect_signal` for section title; other dimensions `not_observable_publicly` |
| Rule | Summary-page depth; minimal codable content |

### DC-08 — Vienna strategy PDF vs kompass landing page

| Field | Value |
|-------|-------|
| Sources | Strategy PDF; kompass landing page |
| Issue | Landing page links PDF; both manifest-registered |
| Resolution | PDF coded `coding_depth: full`; landing page `coding_depth: summary` with PDF note |
| Rule | Hierarchy: prefer full document when both registered as separate rows |

### DC-09 — Vienna rahmenbedingungen D4 service-provider evaluation

| Field | Value |
|-------|-------|
| Source | `ki-rahmenbedingungen` |
| Dimension | D4 |
| Issue | CKT Phase 2 evaluates service providers — procurement-adjacent but no contract |
| Resolution | `partial_or_indirect_signal` |
| Rule | TB-1 conservative; vendor evaluation without contract ID |

### DC-10 — Tallinn 2035 strategy landing page

| Field | Value |
|-------|-------|
| Source | `strateegia.tallinn.ee` |
| Issue | Landing page lacks AI-specific governance text in accessible view |
| Resolution | All dimensions `not_observable_publicly` |
| Rule | No inference from city-strategy portal branding |

### DC-11 — Bot-gated sources (4 rows)

| Field | Value |
|-------|-------|
| Sources | Amsterdam (2); Tallinn (2) |
| Issue | HTTP 403 at collection; text unavailable at coding |
| Resolution | All dimensions `not_observable_publicly`; no inference |
| Rule | Code only observable evidence; silence ≠ internal absence |

### DC-12 — D3 cap on ethical principles (multiple sources)

| Field | Value |
|-------|-------|
| Sources | Helsinki principles; get-to-know; Barcelona strategy |
| Dimension | D3 |
| Issue | Privacy/security/transparency principles vs prompt/log specificity |
| Resolution | Maximum `observable_policy_commitment` |
| Rule | D3 boundary rule v0.1.1 |

---

## Tie-break applications

| ID | Source | Dimension | Labels considered | Applied | Rule |
|----|--------|-----------|-------------------|---------|------|
| TB-01 | Amsterdam register | D5 | `partial_or_indirect_signal` vs `not_observable_publicly` | `partial_or_indirect_signal` | TB-5: register index default |
| TB-02 | Barcelona hub | D4 | `partial_or_indirect_signal` vs `not_observable_publicly` | `partial_or_indirect_signal` | TB-4 avoided; indirect strategy reference present |
| TB-03 | Vienna rahmenbedingungen | D4 | `observable_policy_commitment` vs `partial_or_indirect_signal` | `partial_or_indirect_signal` | TB-1: conservative; no contract/stewardship terms |

---

## Escalations

No formal escalations were required. All decisions mapped to existing v0.1.1 rules. Cases DC-02 and DC-04 note **future manifest enrichment** (full protocol PDF; committee bilag URLs) as a collection concern, not a protocol gap.

---

## Protocol edge cases

| Edge case | Manifest examples | Handling |
|-----------|-------------------|----------|
| Register index URL | Amsterdam; Helsinki (EN/FI) | Register-level default |
| Summary page with linked PDF | Barcelona protocol; Vienna kompass | `coding_depth: summary`; note linked artefact |
| Committee record minutes only | Copenhagen (2); Helsinki paatokset | `coding_depth: committee_record` |
| Portal TOC without body text | Vienna KI strategie index | Minimal partial signals only |
| Language parallel editions | Barcelona ES/EN | Separate rows; no merging |
| Bot-gated official URL | Amsterdam; Tallinn | `not_observable_publicly` all dimensions |
| City-wide strategy portal | Tallinn 2035 | No AI-specific text → not observable |
| Named unit in legal notice | Vienna strategy PDF | `observable_named_artifact` D1 |

---

## Not performed

- Municipal comparison or ranking
- Pattern interpretation across corpus
- Readiness scoring or compliance determination
- Protocol modification
