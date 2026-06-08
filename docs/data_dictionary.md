# Data dictionary

Field definitions for planned corpus files. No data rows are populated in the initial scaffold.

## `source_manifest.csv` (raw)

| Field | Type | Description |
|-------|------|-------------|
| `source_id` | string | Stable identifier for a municipal source entry |
| `municipality` | string | Municipality name |
| `country` | string | ISO 3166-1 alpha-2 country code |
| `document_type` | string | Strategy, register, transparency page, policy, other |
| `url` | string | Public URL at time of retrieval |
| `retrieved_at` | date | ISO 8601 retrieval date |
| `language` | string | Primary document language (ISO 639-1) |
| `notes` | string | Collector notes (optional) |

## `corpus_index.csv` (interim)

| Field | Type | Description |
|-------|------|-------------|
| `document_id` | string | Stable identifier for a coded document unit |
| `source_id` | string | Foreign key to `source_manifest` |
| `title` | string | Document title as published |
| `publication_year` | integer | Year visible on document or page (nullable) |
| `file_format` | string | html, pdf, docx, other |
| `inclusion_status` | string | included, excluded, pending |

## `coded_corpus.csv` (processed)

| Field | Type | Description |
|-------|------|-------------|
| `document_id` | string | Foreign key to `corpus_index` |
| `category` | string | Governance evidence category (see coding protocol) |
| `observability` | string | present, partial, absent, not_applicable |
| `coder` | string | Coder identifier |
| `coded_at` | date | ISO 8601 coding date |
| `evidence_excerpt` | string | Short supporting quote or locator (optional) |
| `notes` | string | Analytic notes (optional) |

## Governance evidence categories

Categories are defined in `coding_protocol.md` and implemented in `src/evidence_gaps/schema.py`.
