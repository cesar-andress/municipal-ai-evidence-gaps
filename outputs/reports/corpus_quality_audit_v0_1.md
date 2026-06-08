# Corpus quality audit v0.1

**Audit date:** 2026-06-08  
**Input:** [`data/processed/corpus_manifest_v0_1.csv`](../../data/processed/corpus_manifest_v0_1.csv)  
**Flags:** [`data/processed/corpus_manifest_quality_flags_v0_1.csv`](../../data/processed/corpus_manifest_quality_flags_v0_1.csv)  
**Prior inventory:** [`corpus_inventory_report.md`](corpus_inventory_report.md)

## Audit scope

Pre-coding quality review of corpus manifest v0.1. This audit checks manifest integrity, source suitability for municipal AI governance observability, and collection risks. It does **not** assign D1–D5 labels, evidence-status codes, governance-quality judgments, or municipal rankings.

---

## Executive summary

| Check | Result |
|-------|--------|
| Manifest rows audited | 23 |
| Exact duplicate URLs | 0 |
| Missing required fields | 0 |
| Inconsistent `municipality_id` values | 0 |
| Invalid `source_type` labels | 0 |
| Rows with `retrieval_status != ok` | 4 |
| Quality flags raised | 28 |
| Flags `critical` | 0 |
| Flags `moderate` | 12 |
| Flags `minor` | 16 |

**Overall assessment:** The manifest is structurally complete and uses a consistent identifier and source-type taxonomy. No critical integrity defects block a cautious move toward coding preparation. Moderate flags concentrate on (a) non-`ok` retrieval for four sources, (b) absence of procurement documents across all municipalities, (c) Tallinn's thin AI-specific coverage, and (d) several sources classified as broader than AI governance alone. The manifest should not be modified in this tranche; flagged items require manual verification or explicit coding-scope decisions before D1–D5 work begins.

---

## 1. Duplicate URLs

**Finding:** No exact URL duplicates detected across 23 rows.

**Related note (not URL duplication):** Several municipalities register multiple entries that point to the same policy artefact in different formats or languages (e.g. Helsinki ethical-principles page and decisions-portal record; Vienna KI strategy portal and English PDF; Barcelona Spanish and English strategy pages). These are recorded as separate manifest rows with distinct URLs. Content-overlap flags are issued where parallel editions or hub-and-document pairs may affect coding unit definition.

---

## 2. Missing required fields

**Required columns (v0.1 manifest):** `municipality_id`, `municipality_name`, `country`, `source_url`, `source_title`, `source_type`, `language`, `access_date`, `retrieval_status`, `notes`

| Field | Rows empty | Rows populated |
|-------|------------|----------------|
| All required fields | 0 | 23 |

**Finding:** No missing required fields.

---

## 3. `municipality_id` consistency

| `municipality_id` | `municipality_name` | `country` | Rows |
|-------------------|---------------------|-----------|------|
| mun-amsterdam | Amsterdam | NL | 3 |
| mun-barcelona | Barcelona | ES | 4 |
| mun-copenhagen | Copenhagen | DK | 2 |
| mun-helsinki | Helsinki | FI | 5 |
| mun-vienna | Vienna | AT | 6 |
| mun-tallinn | Tallinn | EE | 3 |

**Finding:** All rows follow the `mun-{city}` slug pattern. No cross-row mismatches between `municipality_id`, `municipality_name`, and `country`.

---

## 4. `source_type` label consistency

**Permitted labels (v0.1):** AI strategy · AI policy · algorithm register · governance framework · committee record · transparency portal · procurement document · other official document

| `source_type` | Count | Valid label |
|---------------|-------|-------------|
| AI strategy | 5 | yes |
| AI policy | 3 | yes |
| algorithm register | 3 | yes |
| governance framework | 7 | yes |
| committee record | 2 | yes |
| transparency portal | 3 | yes |
| procurement document | 0 | — |
| other official document | 0 | — |

**Finding:** All populated `source_type` values match the permitted taxonomy exactly. No spelling variants or alternate labels detected.

---

## 5. Sources potentially too generic for municipal AI governance

The following registered sources are official and municipal but primarily frame broader programmes (city strategy, digitalisation, innovation hubs, or informational portals) rather than standalone AI governance artefacts:

| Municipality | Source | Concern |
|--------------|--------|---------|
| Tallinn | Tallinn 2035 Strategy (`strateegia.tallinn.ee`) | City-wide development strategy portal; no AI-specific manifest entry with `ok` retrieval |
| Copenhagen | Digitaliseringsstrategi 2024-2027 | Municipal digitalisation strategy; AI referenced within broader digitalisation scope |
| Barcelona | Ethical use of artificial intelligence (hub) | Section landing page linking to substantive documents |
| Amsterdam | Algoritmes en AI | Innovation/digitalisation hub page |
| Helsinki | Get to know AI Register | Informational explainer for the register |
| Tallinn | Tallinn Digital Twin | Municipal data/digital-twin programme page; AI governance linkage indirect |

**Finding:** Six rows may be too generic as primary coding units for AI-specific governance dimensions unless scoped as context pages or cross-referenced to substantive policy documents in the same municipality.

---

## 6. `retrieval_status != ok`

| Municipality | Source | `retrieval_status` | Share of municipal rows |
|--------------|--------|-------------------|-------------------------|
| Amsterdam | Algoritmes en AI | `bot_gated` | 2/3 |
| Amsterdam | Amsterdamse Visie op AI | `bot_gated` | |
| Tallinn | BETTI trustworthy GenAI governance project | `bot_gated` | 2/3 |
| Tallinn | Tallinn Digital Twin | `bot_gated` | |

**Finding:** 4/23 rows (17.4%) are not directly retrievable via automated GET at access date. Amsterdam and Tallinn each depend partly on sources that were not machine-verified at collection. Both municipalities retain at least one `ok` source (Amsterdam algorithm register; Tallinn 2035 Strategy portal).

---

## 7. Document-count balance across municipalities

| Municipality | Documents | Deviation from mean (3.8) |
|--------------|-----------|---------------------------|
| Vienna | 6 | +2.2 |
| Helsinki | 5 | +1.2 |
| Barcelona | 4 | +0.2 |
| Amsterdam | 3 | −0.8 |
| Tallinn | 3 | −0.8 |
| Copenhagen | 2 | −1.8 |

**Finding:** Counts range from 2 to 6 (3:1 ratio). Copenhagen is the thinnest case (two committee/strategy records, no algorithm register or transparency portal). Vienna is the richest (portal, policy, strategy PDF, two governance-framework PDFs/page pairs). Imbalance is expected at manifest v0.1 but should be documented when interpreting cross-municipal document-type coverage later.

---

## 8. Source-type coverage gaps

### Corpus-wide

| `source_type` | Count | Gap |
|---------------|-------|-----|
| procurement document | 0 | **Absent** — no tender clauses, procurement guidelines, or contract templates registered |
| other official document | 0 | None registered |
| committee record | 2 | Only Copenhagen and Helsinki |
| algorithm register | 3 | No Barcelona register URL despite strategy commitment to a public register |
| transparency portal | 3 | Copenhagen has none |

### Per municipality

| Municipality | Missing or thin types |
|--------------|----------------------|
| Amsterdam | procurement document; AI strategy (only AI policy + register + hub) |
| Barcelona | procurement document; algorithm register (referenced in strategy, not manifest) |
| Copenhagen | algorithm register; transparency portal; procurement document; AI policy |
| Helsinki | procurement document; AI strategy document |
| Vienna | procurement document; algorithm register; committee record |
| Tallinn | AI strategy; AI policy; algorithm register; procurement document; committee record |

**Finding:** Procurement documents are entirely absent. This is the most uniform cross-corpus source-type gap and is directly relevant to D4 (procurement and vendor stewardship) observability.

---

## 9. Language coverage

| Municipality | Languages in manifest | Tier A screening languages | Gap |
|--------------|----------------------|----------------------------|-----|
| Amsterdam | NL | NL; EN | No English-language manifest row |
| Barcelona | ES; EN | CA; ES; EN | No Catalan (`CA`) manifest row |
| Copenhagen | DA | DA | Aligned |
| Helsinki | FI; EN | FI; EN | Aligned |
| Vienna | DE; EN | DE; EN | Aligned |
| Tallinn | ET; EN | ET; EN | Only one Estonian row; no standalone Estonian AI policy/strategy |

**Finding:** Language coverage is adequate for Finnish–English and German–English pairs. Gaps exist for Catalan (Barcelona) and for Amsterdam English material (vision page is `bot_gated`). Copenhagen and Tallinn corpora are single-language dominant for substantive governance text (DA; ET/EN mix with thin ET AI specificity).

---

## 10. Official-source provenance risks

| Risk | Affected rows | Description |
|------|---------------|-------------|
| Subdomain/off-portal hosting | `digitales.wien.gv.at` (3); `ai.hel.fi` (4); `algoritmeregister.amsterdam.nl` (1); `strateegia.tallinn.ee` (1) | Official municipal ecosystems but not the primary `wien.gv.at` / `hel.fi` / `amsterdam.nl` / `tallinn.ee` apex domains |
| Committee record without direct artefact URL | Copenhagen (2); Helsinki (1) | Manifest URLs point to meeting minutes pages; substantive PDFs are attachments (`bilag`) not separately registered |
| Bot-gated apex domain | Amsterdam (2); Tallinn (2) | `amsterdam.nl` and `tallinn.ee` pages not machine-confirmed at access date |
| Parallel edition pairs | Barcelona (ES/EN strategy); Vienna (portal/PDF); Helsinki (policy page/decision record) | Provenance is official but coding unit boundaries need explicit rules |

**Finding:** No non-municipal or consultancy domains detected. Provenance risks are procedural (attachment access, bot-gating, subdomain hosting) rather than authority-of-source risks.

---

## 11. Recommended pre-coding actions (summary)

| Action | Flag count | Purpose |
|--------|------------|---------|
| `keep` | 8 | Structurally sound primary sources |
| `verify_manually` | 10 | Bot-gated URLs, attachment-dependent records, language/procurement gaps |
| `retain_as_context_only` | 8 | Hub, explainer, or broad-strategy pages |
| `replace_source` | 2 | Prefer substantive artefact over portal landing where parallel exists |
| `exclude_from_coding` | 0 | None recommended at audit stage |

**Note:** `exclude_from_coding` was not applied in this audit tranche. Generic or context-only sources are flagged for scope decisions, not automatic removal.

---

## 12. Audit limitations

- Audit is manifest-metadata only; document bodies were not scraped or read.
- No new sources were collected; gaps are recorded, not filled.
- `corpus_manifest_v0_1.csv` was not modified.
- Flags do not constitute observability findings or governance assessments.

---

## Artefacts produced

| File | Description |
|------|-------------|
| `outputs/reports/corpus_quality_audit_v0_1.md` | This report |
| `data/processed/corpus_manifest_quality_flags_v0_1.csv` | Row-level quality flags (28 rows) |
