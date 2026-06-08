# Methodology

## Study design

This artifact supports a **comparative documentary analysis** of publicly accessible municipal AI governance materials in Europe.

The unit of analysis is the **public document** (or document bundle) made available through official municipal channels: AI strategies, algorithm registers, transparency pages, policy statements, and linked governance artefacts.

## Analytic focus

The study examines **observability** — what categories of governance-relevant information appear in public documentation — and **evidence gaps** — categories that are thin, absent, or inconsistently reported.

## Non-goals

This workflow explicitly does **not**:

- produce municipal readiness scores
- rank or league-table cities
- infer legal compliance or non-compliance
- access non-public administrative records

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

Protocol defined; corpus not yet collected.
