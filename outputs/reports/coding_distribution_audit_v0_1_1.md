# Coding distribution audit v0.1.1

**Audit date:** 2026-06-08  
**Input:** [`data/processed/coding_results_v0_1_1.csv`](../../data/processed/coding_results_v0_1_1.csv)  
**Corpus metadata:** [`data/processed/corpus_manifest_v0_1.csv`](../../data/processed/corpus_manifest_v0_1.csv)  
**Protocol:** v0.1.1

Pre-RQ analysis distribution audit. This report describes coded observation frequencies only. It does not answer RQ1–RQ3, compare municipalities substantively, or generate paper findings.

---

## Corpus scope

| Metric | Value |
|--------|-------|
| Coding rows | 115 |
| Manifest sources | 23 |
| Municipalities | 6 |
| Source types (manifest) | 7 |

---

## 1. Distribution by `evidence_status`

| `evidence_status` | Count | Share |
|-------------------|-------|-------|
| `not_observable_publicly` | 50 | 43.5% |
| `observable_policy_commitment` | 37 | 32.2% |
| `partial_or_indirect_signal` | 25 | 21.7% |
| `observable_named_artifact` | 3 | 2.6% |
| **Total** | **115** | **100%** |

---

## 2. Distribution by dimension (D1–D5)

| Dimension | `observable_named_artifact` | `observable_policy_commitment` | `partial_or_indirect_signal` | `not_observable_publicly` | Total |
|-----------|----------------------------|-------------------------------|-----------------------------|--------------------------|-------|
| D1_programme_ownership | 3 | 7 | 7 | 6 | 23 |
| D2_human_oversight_and_review | 0 | 10 | 8 | 5 | 23 |
| D3_prompt_log_and_data_governance | 0 | 11 | 4 | 8 | 23 |
| D4_procurement_and_vendor_stewardship | 0 | 3 | 2 | 18 | 23 |
| D5_incident_audit_and_lifecycle_accountability | 0 | 6 | 4 | 13 | 23 |

### Dimension-level modal status

| Dimension | Modal `evidence_status` | Share of dimension rows |
|-----------|-------------------------|-------------------------|
| D1 | Mixed (no single status >60%) | — |
| D2 | `observable_policy_commitment` | 43.5% |
| D3 | `observable_policy_commitment` | 47.8% |
| D4 | **`not_observable_publicly`** | **78.3%** |
| D5 | `not_observable_publicly` | 56.5% |

**Dimension dominated by a single status (>60%):** D4 only (`not_observable_publicly`, 78.3%).

---

## 3. Distribution by municipality

| `municipality_id` | `observable_named_artifact` | `observable_policy_commitment` | `partial_or_indirect_signal` | `not_observable_publicly` | Non-`not_observable` rows |
|-------------------|----------------------------|-------------------------------|-----------------------------|--------------------------|---------------------------|
| mun-amsterdam | 0 | 0 | 4 | 11 | 4 / 15 |
| mun-barcelona | 0 | 11 | 8 | 1 | 19 / 20 |
| mun-copenhagen | 0 | 4 | 4 | 2 | 8 / 10 |
| mun-helsinki | 0 | 9 | 4 | 12 | 13 / 25 |
| mun-vienna | 3 | 13 | 5 | 9 | 21 / 30 |
| mun-tallinn | 0 | 0 | 0 | 15 | 0 / 15 |

**Note:** Row counts differ by municipality because manifest source counts differ (Amsterdam 3; Barcelona 4; Copenhagen 2; Helsinki 5; Vienna 6; Tallinn 3).

### Municipalities with unusually sparse observability

| Municipality | Indicator | Detail |
|--------------|-----------|--------|
| mun-tallinn | **Zero non-`not_observable` rows** | 15/15 `not_observable_publicly`; 10 rows from bot-gated sources; 5 from strategy landing with no AI-specific text coded |
| mun-amsterdam | **Low non-`not_observable` rate** | 4/15 (26.7%); 10 rows from bot-gated sources; 4 partial signals from register index only |
| mun-helsinki | **High `not_observable` count** | 12/25 (52.2%); driven by register index pages (10 rows) |

These patterns reflect manifest composition and retrieval status, not coding-label invalidity.

---

## 4. Distribution by `source_type`

| `source_type` | `observable_named_artifact` | `observable_policy_commitment` | `partial_or_indirect_signal` | `not_observable_publicly` | Total rows |
|---------------|----------------------------|-------------------------------|-----------------------------|--------------------------|------------|
| AI strategy | 1 | 11 | 7 | 6 | 25 |
| AI policy | 0 | 4 | 2 | 9 | 15 |
| algorithm register | 0 | 0 | 8 | 7 | 15 |
| committee record | 0 | 5 | 2 | 3 | 10 |
| governance framework | 2 | 12 | 4 | 12 | 30 |
| transparency portal | 0 | 5 | 2 | 13 | 20 |

**Manifest types with zero corpus rows:** `procurement document`; `other official document` (absent from manifest v0.1).

### Source types and `observable_named_artifact`

| `source_type` | `observable_named_artifact` count | Share of all named-artifact rows |
|---------------|-----------------------------------|----------------------------------|
| governance framework | 2 | 66.7% |
| AI strategy | 1 | 33.3% |
| All other types | 0 | 0% |

**Finding:** All three `observable_named_artifact` rows originate from Vienna `governance framework` (2) and `AI strategy` PDF (1). No other source type produced this label.

---

## 5. Category health flags

### Empty categories (dimension × status cells with count = 0)

| Cell | Count |
|------|-------|
| D2 × `observable_named_artifact` | 0 |
| D3 × `observable_named_artifact` | 0 |
| D4 × `observable_named_artifact` | 0 |
| D5 × `observable_named_artifact` | 0 |

### Near-empty categories (count ≤ 2)

| Cell | Count |
|------|-------|
| D4 × `partial_or_indirect_signal` | 2 |
| Corpus-wide × `observable_named_artifact` | 3 |

### Structural empty categories (manifest-level)

| Category | Status |
|----------|--------|
| `procurement document` | No manifest sources → no coding rows |
| `other official document` | No manifest sources → no coding rows |

---

## 6. Investigation: `observable_named_artifact`

### Count

| Metric | Value |
|--------|-------|
| Total rows | 3 |
| Share of corpus | 2.6% |
| Dimensions represented | D1 only |
| Municipalities represented | mun-vienna only |

### Detail table

| # | Municipality | Dimension | `source_type` | Source URL |
|---|--------------|-----------|---------------|------------|
| 1 | mun-vienna | D1_programme_ownership | AI strategy | `https://digitales.wien.gv.at/wp-content/uploads/sites/47/2025/09/1065373-2025_MD-OS_PIKT_KI-Strategie_Sanjath_EN_korr-bf.pdf` |
| 2 | mun-vienna | D1_programme_ownership | governance framework | `https://digitales.wien.gv.at/ki-kompass-fuer-bedienstete-der-stadt-wien/` |
| 3 | mun-vienna | D1_programme_ownership | governance framework | `https://digitales.wien.gv.at/wp-content/uploads/sites/47/2025/07/20250407_AI-Compass_engl.pdf` |

### Quoted evidence (locators)

| # | `quoted_evidence` | `page_or_section` |
|---|-------------------|-------------------|
| 1 | ICT Strategy and Process Management Group (MD-OS/PIKT) | Legal notice |
| 2 | AI-Kompetenznetzwerk, bestehend aus Vertreter*innen der Magistratsdirektion | Entstehungsgeschichte |
| 3 | AI Competence Network (headed by the Executive Group for Organisation and Security (MD-OS)) | Document header |

---

## 7. Assessment: plausibly rare vs under-assigned

### Evidence that `observable_named_artifact` is plausibly rare

| Factor | Audit reading |
|--------|---------------|
| Protocol v0.1.1 register default | Amsterdam and Helsinki registers coded at index level → caps D1–D5 below named-artifact threshold |
| D3 ethical-principles cap | Principles pages cannot exceed `observable_policy_commitment` for D3 |
| D4 manifest gap | No procurement documents in corpus → D4 named-artifact structurally unlikely |
| Conservative tie-breaks | TB-1/TB-5 applied in register and procurement-adjacent cases |
| Full-document concentration | Named units appear only where legal notice / competence network names exist (Vienna PDFs) |

### Evidence of possible under-assignment (interpretation risk)

| Factor | Audit reading |
|--------|---------------|
| Register entry pages not coded | Amsterdam register contains populated `Impacttoetsen` fields on some entries; index-level rule may suppress D2 named-artifact opportunities |
| Committee bilag not coded | Copenhagen kodeks and strategy attachments not separately manifest-registered |
| Barcelona protocol full PDF not coded | Summary page coded; may lack locatable artefacts available in linked full protocol |
| Bot-gated sources | 4 sources (20 rows) coded entirely `not_observable_publicly` — corpus retrieval constraint, not label error |

### Audit conclusion on `observable_named_artifact`

**Predominantly plausibly rare** for this manifest under v0.1.1 rules. **Localized under-assignment risk** exists for D1/D2 on algorithm-register entry pages and annex-level documents, but does not invalidate the current coding set for descriptive pre-RQ distribution review.

---

## 8. Audit limitations

- No re-coding performed
- No municipal ranking or RQ answers
- `source_type` joined from manifest v0.1 at audit time
- Municipality row totals reflect manifest source counts, not equal sampling weights
