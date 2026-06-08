# Global editorial style guide v0.1

**Authority:** Repository editor-in-chief  
**Scope:** All `.md` and `.tex` files in `municipal-ai-evidence-gaps/` and `paper/`  
**Date:** 2026-06-08

This guide is the **single editorial authority** for terminology, research questions, non-claims, and capitalization across the GIQ manuscript and public artifact.

**Audit log:** [`editorial_consistency_audit.md`](editorial_consistency_audit.md)

---

## 1. Canonical terminology

Always use these terms (British **programme** spelling):

| Canonical term | Meaning | Notes |
|----------------|---------|-------|
| **municipal AI programme** | Municipal systems, vendors, workflows, and governance arrangements | Context only; not directly observed |
| **Programme-Level Governance Readiness** | Whether documented structures would allow external programme-level assessment | **Not measured** by this study |
| **Public-Document Observability** | Degree to which governance evidence is identifiable in **public documentation** | Hyphenate when naming the construct |
| **evidence gap** | Thin, partial, or absent programme-level evidence in public documentation | Plural: evidence gaps |
| **observable evidence** | Locatable governance information in public documentation | Not a readiness proxy |
| **accountability limitation** | Constraint on external oversight via the public record | Plural: accountability limitations |
| **public documentation** | Official publicly accessible municipal AI governance materials (collective) | Preferred over *public documents* for the phenomenon |
| **public document** | One retrievable source unit in the corpus | Use when counting or citing a single URL/PDF |

### Avoid (unless quoting external sources)

| Do not use | Use instead |
|------------|-------------|
| program-level | programme-level |
| governance maturity | programme-level governance evidence (or omit) |
| governance capability | programme-level governance evidence (or omit) |
| benchmark score | (omit; see non-claims) |
| readiness score / readiness index | no readiness scoring (non-claim) |
| transparency score | Public-Document Observability / evidence status labels |
| maturity score | (omit) |
| league table / city ranking | no municipal ranking (non-claim) |

---

## 2. Canonical research questions

Use **verbatim** everywhere (README, protocols, manuscript, storyline). No paraphrase.

**RQ1.** What governance evidence is publicly observable in municipal AI documentation?

**RQ2.** Which governance dimensions are systematically under-observable?

**RQ3.** What patterns of transparency and evidence gaps emerge across municipalities and document types?

### Discussion implication (not an RQ)

> What are the implications of these evidence gaps for independent governance assessment based on public documentation alone?

---

## 3. Canonical non-claims

Use this block verbatim in protocols, README, Method, and Limitations unless context requires a single-item reference:

- **no readiness scoring**
- **no municipal ranking**
- **no legal compliance determination**
- **no LocalGovBench validation**
- **no inference of internal governance quality**

### Extended non-claims (supporting detail)

May elaborate but must not contradict the five canonical items. See [`non_claims.md`](non_claims.md).

---

## 4. Canonical capitalization

| Term | Capitalization |
|------|----------------|
| Government Information Quarterly | Full journal name; abbreviate **GIQ** after first use |
| LocalGovBench | CamelCase |
| Programme-Level Governance Readiness | Title case when naming the concept |
| Public-Document Observability | Title case when naming the construct |
| municipal AI programme | Lower case (common noun) |
| evidence gap / observable evidence / accountability limitation | Lower case |
| public documentation | Lower case |

---

## 5. Spelling and locale

- **British English:** programme, organisation, behaviour, centre (unless proper name dictates otherwise)
- **Em dash:** use spaced en dash or unspaced em dash consistently within a document; prefer `---` in LaTeX, `—` in Markdown

---

## 6. Repository roles

| Repository | Role |
|------------|------|
| `municipal-ai-evidence-gaps/` | Public artifact; **authoritative** for protocols, schema, editorial guide |
| `paper/` | Private GIQ manuscript; must align with this guide |

Manuscript authors update `paper/` after protocol changes in the public artifact.

---

## 7. Document history

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-06-08 | Initial global editorial style guide |
