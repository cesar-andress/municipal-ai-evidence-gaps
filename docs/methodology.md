# Methodology

## Study design

This artifact supports a **comparative documentary analysis** of publicly accessible municipal AI governance materials in Europe.

The unit of analysis is the **public document** (or document bundle) made available through official municipal channels: AI strategies, algorithm registers, transparency pages, policy statements, and linked governance artefacts.

## Analytic focus

The study examines **Public-Document Observability** — what categories of governance-relevant information appear in public documentation — and **evidence gaps** — categories that are thin, absent, or inconsistently reported.

## Non-goals

This workflow explicitly maintains the canonical non-claims:

- no readiness scoring
- no municipal ranking
- no legal compliance determination
- no LocalGovBench validation
- no inference of internal governance quality

It also does not access non-public administrative records.

## Coding protocol

**Current version:** v0.1.1

| Document | Role |
|----------|------|
| [`coding_protocol.md`](coding_protocol.md) | Dimension sheets (D1–D5), evidence labels, coding-unit rules, document hierarchy |
| [`coding_decision_rules_v0_1_1.md`](coding_decision_rules_v0_1_1.md) | Decision trees, tie-breaking rules, escalation rules |
| [`study_protocol_v0_1.md`](study_protocol_v0_1.md) | Study-level inclusion, sampling, and workflow |
| [`outputs/reports/protocol_change_log_v0_1_1.md`](../outputs/reports/protocol_change_log_v0_1_1.md) | v0.1 → v0.1.1 change register |

Protocol v0.1.1 was promoted following a three-document pilot validation (`outputs/reports/pilot_coding_protocol_test.md`). Pilot timing benchmark: ~34 minutes per document (single coder).

### Coding conventions (v0.1.1)

- **Evidence hierarchy:** source document > annex > committee record > summary page
- **Algorithm registers:** default register-level coding; entry-level when URL or scope targets one system
- **Evidence status:** four labels unchanged since v0.1; boundaries clarified with worked examples
- **Quote language:** `quoted_evidence` in source language; gloss in `coder_notes`

## Pipeline overview

```
collect_sources.py
    → data/raw/source_manifest.csv
build_corpus_index.py
    → data/interim/corpus_index.csv
code_observability.py
    → data/processed/coded_corpus.csv
export_tables.py
    → outputs/tables/, outputs/reports/
```

## Reproducibility

Each script is idempotent where possible and writes structured logs alongside outputs. Retrieval dates and source URLs are preserved to support audit trails suitable for Zenodo archival release.

## Status

Research design and coding protocol v0.1.1 complete. Initial corpus manifest v0.1 registered (23 sources). Pilot coding protocol validation complete. Full-corpus D1–D5 coding not yet started.
