# Tier A verification protocol v0.1

**Purpose:** Screen proposed Tier A municipal sampling candidates against inclusion criteria **before** corpus collection, D1–D5 coding, or observability labelling.

**Aligned with:** [`municipal_sampling_strategy_v0_1.md`](municipal_sampling_strategy_v0_1.md) · [`study_protocol_v0_1.md`](study_protocol_v0_1.md)

**Status:** Initial screening complete (2026-06-08). **Not** a coded corpus. **Not** governance evidence collection.

---

## Scope

### In scope (screening only)

| Check | Description |
|-------|-------------|
| **a) Municipality status** | Confirm entity is a local/municipal government, not national or regional |
| **b) Official municipal domain** | Record canonical official web domain(s) |
| **c) Public AI documentation** | Confirm ≥1 publicly accessible municipal AI-governance-related page or document URL exists |
| **d) Language(s)** | Record primary publication language(s) |
| **e) Inclusion eligibility** | Apply inclusion/exclusion rules; no scoring or ranking |

### Out of scope

- D1–D5 observability coding
- Evidence-status labels
- Document download/archival (deferred to collection phase)
- Readiness or performance assessment
- Findings or cross-municipal comparison

---

## Inclusion tests (screening level)

A candidate passes screening when **all** are true:

1. European municipality in v0.1 geographic frame
2. Official municipal publisher (city government website or officially operated subdomain)
3. ≥1 URL referencing municipal AI governance, algorithms, or responsible AI use (strategy, register, protocol, code of conduct, ethics principles, or equivalent)
4. URL publicly reachable without authentication at verification (see bot-gating note below)
5. Language feasible per [`municipal_sampling_strategy_v0_1.md`](municipal_sampling_strategy_v0_1.md) §8

### Exclusions (screening)

- National/regional agency as primary publisher
- Media-only coverage without primary municipal document
- Vendor-only pages without official municipal adoption

---

## Verification procedure

```
1. Confirm municipality identity and country
2. Record official_domain
3. Search official domain for AI / algorithm / responsible AI governance pages
4. Record 1–3 primary URLs in notes (no content extraction)
5. HTTP accessibility check (GET, follow redirects)
6. Assign eligible yes/no with screening notes
7. Write row to tier_a_verification.csv
8. Summarise in tier_a_verification_report.md
```

**Bot-gating note:** Some official sites return HTTP 403 to automated clients while remaining publicly accessible in a standard browser. When this occurs, eligibility may be assigned `yes` if (i) an official subdomain returns HTTP 200, or (ii) an alternate official URL on the same domain is confirmed accessible, with the 403 URL flagged for browser re-check at collection.

---

## Outputs

| Output | Path |
|--------|------|
| Screening table | `data/processed/tier_a_verification.csv` |
| Screening report | `outputs/reports/tier_a_verification_report.md` |

---

## Candidates screened (this tranche)

Per verification task v0.1:

- Amsterdam (NL) — Tier A frame
- Barcelona (ES) — Tier A frame
- Copenhagen (DK) — Tier A frame
- Helsinki (FI) — Tier A frame
- Vienna (AT) — Tier A frame
- Tallinn (EE) — **Tier B in sampling frame**; included in this screening tranche by task specification

---

## Next steps (not executed)

1. Browser-confirmed re-check of bot-gated URLs at collection `access_date`
2. Register passing candidates in `corpus_manifest_template.csv`
3. Begin document manifest assembly (v0.2) — still no D1–D5 coding

---

## Document history

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-06-08 | Initial Tier A screening protocol and six-candidate verification |
