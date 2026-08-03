# HPF Knowledge Export Contract — Core (knowledge-export-core-v1)

**Status: schema frozen 2026-08-03. Producer: `tools/hpf-engine/export.py` 0.3.0.
Contract tier: CORE — see "What the core deliberately omits".**

This document is the contract specification. The producer and the corpus remain
the source of truth for content; this document freezes the *shape* of the
contract, its invariants, and its change discipline.

## 1. Position in the architecture

```
                 HPF Research
                      |
               (single source of truth)
                      |
                      v
              Research Corpus
                      |
          Derived projection only
                      |
          Knowledge Export Contract   <- this document
                      |
          Derived projection only
                      |
              Knowledge Index
                      |
      +---------+---------+---------+
      v         v         v         v
 Publishing  Marketing  Website   API
      +---------+---------+---------+
              Read-only consumers
```

The export is a **derived projection** of the corpus. HPF never writes into the
export; consumers never write into HPF; the export and the index are disposable
and rebuildable; the corpus remains authoritative.

## 2. The two concerns, kept orthogonal

Every record carries three independent axes plus pipeline integrity. The axes
answer two questions that must never be conflated:

- **Where did this knowledge come from?** -> `origin`
- **What evidential status does it currently hold?** -> `authority` + `status`

`schema_validation` is a separate concern: it records whether the object passed
the corpus schema validator (pipeline integrity), not its evidential status.

| Field              | Values (fixed)                                          | Meaning                                    |
|--------------------|---------------------------------------------------------|--------------------------------------------|
| `origin`           | `hpf`, `nist`, `cert`, `rfc`, `academic`, `internal`    | Source of the knowledge                     |
| `authority`        | `hpf_experiment`, `external_curated`, `imported`, `unverified` | Who/what established it           |
| `status`           | `observed`, `replicated`, `provisional`, `retired`      | Lifecycle evidential status                 |
| `schema_validation`| `valid`, `invalid`                                      | Pipeline integrity gate (corpus validator)  |

Example discriminations publishing can make without inventing interpretation:

```
TLS Certificate Pinning      Retry Storm Isolation
origin:    rfc               origin:    hpf
authority: external_curated  authority: hpf_experiment
status:    observed          status:    replicated
```

## 3. Per-record shape (core)

```jsonc
{
  "id": "abstract-syntax-tree",
  "title": "Abstract Syntax Tree",
  "kind": "concept",                       // concept | pattern | principle | decision (as recorded)
  "domain": null,                          // as recorded in the object
  "research_cycle": null,                  // as recorded in the object (Cycle 015 objects: "015")
  "source": "domain/knowledge/abstract-syntax-tree.md",  // engine-relative provenance
  "origin": "hpf",
  "authority": "hpf_experiment",
  "status": "observed",
  "schema_validation": "valid",            // or "invalid"
  "errors": [],                            // invalid records carry their validator errors here
  "blocks": { "Claims": 5, ... },          // block counts, all sections
  "claims": [],                            // stable core, valid records only
  "relationships": [],
  "constraints": [],
  "recommendations": []
}
```

## 4. Invariants

1. **No new claims.** Exports reformat corpus content only; every record is a
   derived projection of a parsed knowledge object.
2. **Provenance.** Every record carries source file, object id, kind, domain,
   and research cycle where recorded in the object.
3. **Invalid objects export metadata only.** `schema_validation == "invalid"`
   records carry their errors and NO semantic content. Consumers must filter on
   `schema_validation == "valid"` before use. Downstream claims can never
   outpace evidence.
4. **Regenerable projection.** The export is never hand-edited; the corpus is
   the single source of truth.
5. **Stable core only.** Exported blocks: objects, relationships, claims,
   constraints, recommendations.
6. **Consumers are read-only.** No downstream system mutates the corpus or any
   research artifact. One-way flow: Corpus -> Export -> Index -> Consumers.
   No Publishing -> Corpus. No Marketing -> Index -> Corpus.

## 5. Compatibility guarantees

- `schema_version` is incremented **only** on breaking changes to the record
  shape or the fixed value sets (`axes`, `schema_validation_values`).
- Within a schema version, producers may add:
  - new **optional** fields under a clearly separated extension section
    (`metadata`-style), never inside the frozen core fields;
  - values only for axes marked provisional in this document.
- Adding a value to a fixed value set (`axes`) is a breaking change to that
  schema version -> new schema_version and a migration rule.
- Consumers may rely on the frozen core fields and the fixed value sets for
  the schema_version they consume.
- The `authority` field is frozen for the core schema; richer authority
  models, if required, will be introduced only through a future schema
  version.

## 6. Migration rules

1. Breaking changes require a new `schema_version` and a written migration
   rule in this document BEFORE release of the new producer.
2. Migration rule format: old field/value -> new field/value, transformation
   to apply, and whether old consumers keep working (deprecation window).
3. A migration never invents content: renames, splits, and moves of existing
   exported content are allowed; new claims are not.
4. The provisional extension namespace (methodology terms, motif candidates,
   decomposition metrics) is admitted only through the vocabulary
   admission/removal rules and appears under an extension section — never
   inside the frozen core.
5. The export file itself is regenerable; no migration is ever applied to a
   stored export by hand. Re-run the producer against the corpus.

## 7. What the core deliberately omits

The contract is named **core** because it does not yet include:

- methodology namespace (referent/boundary convergence terms, vocabulary)
- motif candidates and discoveries
- the full authority layer (per-object lifecycle assignment beyond the
  current uniform `origin=hpf / authority=hpf_experiment / status=observed`
  defaults; per-object `replicated`/`provisional`/`retired` assignment awaits
  the R1 mapping)

These are planned, not admitted. Downstream teams must not assume "core"
implies them.

## 8. Experimental status

Implemented 2026-08-03 as an experimental implementation. Architectural
promotion is a programme-governance decision pending R1 (research queue:
R1/Cycle 016 -> independent reviews -> replication evidence -> vocabulary
graduation). Until promotion, treat the producer as experimental; the schema
freeze above governs the JSON shape, not the programme status. The core is
frozen: it will be used, tested, and versioned only when demonstrated
insufficiency requires it — the same discipline applied to the ontology and
the protocol. Fields are not added pre-emptively. Subsystem declared closed
2026-08-03: only bug fixes, insufficiencies discovered by use, and versioned
evolution may touch it.
