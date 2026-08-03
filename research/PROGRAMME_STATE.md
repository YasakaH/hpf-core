# HPF Research Programme — Programme State

## Document Purpose

This document records **what the project is trying to prove** and **how each cycle contributes to that proof**.

It does not duplicate cycle summaries. The dossier for each cycle records *what happened*. This document records the *research design* — the hypotheses, invariants, architecture laws, and evidence accumulation strategy that make individual cycles cohere into a cumulative research programme.

Any researcher — human or AI — should be able to resume work from this document and the most recent cycle summary without reconstructing months of context.

---

## Research Status

The project is no longer in architecture design.

It is in **architecture validation**.

---

## Architecture Freeze Protocol

The following components are frozen during validation:

- Parser
- Validator
- Analyzer
- Atomic evidence schema

Changes are permitted only when all of the following hold:

1. Recurring representation friction exists.
2. It appears across multiple independent cycles.
3. It cannot be resolved through tooling or modelling conventions.
4. The change preserves backwards compatibility.

Every research cycle tests whether the frozen components remain sufficient without modification.

---

## Protocol Version and Stability Principle

The protocol (research design, not the architecture) is versioned and now presumed stable:

| Version | Contents |
|---|---|
| v1.0 | Original protocol — cycles 001–011 |
| v1.1 | Cycle 012 closeout controls — internal adversarial review, strengthened Phase 5, motif maturity gate |
| v1.2 | Cycle 013 round 1 — amendments A1–A5 (external-frame review, sealed probes, scorecard, Programme B gates, motif promotion gate) |
| **v1.3** | **Cycle 013 round 2 — amendments B1–B8 (judgment independence: frozen rubrics, objective verdict conditions, scorecard split, A/B probe comparison, epistemic-discontinuity gate G7, counterexample search strategy, randomized frame rotation, Protocol Stability Principle)** |
| **v1.3.1** | **2026-08-01 — defect corrections A-1, A-2, A-4 (verdict-condition applicability, frame-draw procedure, internal-review adjudication) + administration hardening (A-3, document control — reclassified to Category B at ratification); no amendments — see `research/protocol/adversarial-review-01.md`** |

> **Protocol Stability Principle (B8):** the protocol is presumed stable as of v1.3. Future amendments require a demonstrated deficiency exposed by a completed cycle under the current protocol (an experiment-validated deficiency) — not a theoretical improvement. Amendments are rare, explicitly justified against this bar, and versioned. A success under a frozen protocol is stronger than a success under an evolving one; the freeze is what makes later successes persuasive.

**Standing documentation rule (adopted at the Cycle 014 architecture review, 2026-08-03):** new governance documents are created only when they (a) introduce a genuinely new measurement instrument or (b) record an irreversible research event; otherwise the content belongs as a section in an existing document.

**Research-question note (Cycle 014 architecture review, 2026-08-03):** the programme's operative question moves from sufficiency testing ("Does engineering knowledge require more evidence primitives or complexity destinations?") to boundary-mapping ("What are the epistemic limits of evidence-based representation?"). H₁'s falsification criteria remain in force; the shift is in the programme's self-understanding and is recorded deliberately.

**Prioritised open items (Cycle 014 architecture review, programme-owner ordering, 2026-08-03):** (1) `HPF_VALIDATION_ARGUMENT.md` — **DONE 2026-08-03**: the programme's evidence statement without the chronological narrative, basis for external publication (v1.0, written after Cycle 014 closeout and its architecture review; **updated to v1.1 after Cycle 015 closeout and the post-closeout adjudicator-level audit (2026-08-03)**: cycle table extended through 015, F1 replication recorded, decomposition-convergence result + R1 priority + vocabulary appendix terms added; evidence-status conventions throughout: DEMONSTRATED / OBSERVED / PROGRAMME-LEVEL DECISION / OPEN; carries the arm-(c) disposition in §4.1/§6.1/§7); (2) kill review — **RATIFIED 2026-08-03** with four refinements (falsification-probability mission, unrestricted attack surfaces, verdicts K1–K4, mandatory single-experiment answer); instrument frozen at `research/KILL_REVIEW_INSTRUMENT.md`; scheduled as the final negative gate before Programme B, not run now; (3) object-identity experiment — **RATIFIED 2026-08-03** as **Cycle 015's primary experiment**: renamed **independent decomposition convergence**; primary endpoint: independent authors' decompositions of the same source material converge sufficiently to support stable representation; scoring pre-registered before authoring (exact match / semantic match / split / merge / missing / novel); hostile-domain re-test + v1.3.2 validation = secondary outcomes. **F1 disposition: UNRESOLVED — arm (c) deferral (2026-08-03): neither arm ratified; F1 recorded as an unresolved architectural tension; protocol not amended (v1.3.2 stays a draft); Cycle 015 replication criterion decides the arms.** **UPDATE 2026-08-03 (Cycle 015 closeout): F1 REPLICATION CONFIRMED** — the ontology-first frame (drawn at Phase 0, independently of 014) returned ESCAPED on all five R-conditions, all semantic-class (formal-ontology machinery); two independent observations now exist; per the pre-registered criterion the programme may now ratify arm (a) (semantics in scope) or arm (b) (Scope-and-remit clause, v1.3.2) **on evidence — the arm decision is the programme owner's ratification point**; the architecture review's retained recommendation remains arm (b). The Cycle 015 primary endpoint was met independently of the frame outcome (Band B — convergence up to equivalence).

The freeze stands at **v1.3.1** (2026-08-01): the pre-Cycle-014 full-stack adversarial review found 3 Category A integrity defects, corrected as narrowly-scoped defect corrections (A-1, A-2, A-4) under the review discipline — not amendments. A fourth finding (A-3, document control) was reclassified to Category B at ratification — governance/protocol administration — with its fix retained as administration hardening. Category B findings (11) are carried in the review report and revisited at Cycle 014 closeout. Documentation-only clarifications adopted at ratification (decision-table classification, reproducibility in the review objective, terminology) are recorded in the review report and dossier; they did not create a protocol version. The protocol is frozen at v1.3.1; Cycle 014 pre-registration proceeds under it.

The architecture freeze (above) and the protocol stability principle are distinct: architecture changes require recurring representation friction; protocol changes now require a demonstrated experimental deficiency. Both bars are deliberately high.

## Release Checklist (pre-snapshot gate)

*Adopted 2026-08-03. A checklist, not a protocol: before claiming "HPF Research Snapshot vX.Y" (or any release-level summary of programme state), verify each item and record the outcome. Process metric, not scientific result — the checklist certifies that the documentation reflects the records; the validation argument carries the evidence.*

- [ ] Ontology frozen (no schema / primitive / kind changes since Cycle 002)
- [ ] Protocol frozen (v1.3.1; unratified drafts listed explicitly, e.g. v1.3.2)
- [ ] Adjudicator-level audit complete for the cycle(s) claimed
- [ ] Synchronization manifest complete for the research set
- [ ] Validation argument current (version recorded)
- [ ] Chronicle current (latest entry recorded)
- [ ] Owner decisions recorded (open ratification items listed, not silently omitted)
- [ ] Implementation debt empty, or explicitly listed

Each item is verified at snapshot time; an unchecked or outstanding item must be listed explicitly in the snapshot, not silently passed.

**Snapshot convention (future recommendation, not adopted):** at the next major milestone (e.g., R1 completion), consider a tagged, **immutable** research snapshot ("HPF Research Snapshot vX.Y") capturing the frozen protocol version, the ontology version, the validation argument version, the implementation audit, the synchronization manifest, and the release checklist status. Snapshots are archival checkpoints, not living documents: later corrections belong to a subsequent snapshot or to an explicit errata document — never retroactive edits to a released snapshot.

**Knowledge Export Contract (experimental implementation 2026-08-03; architectural status NOT adopted — promotion is a governance decision pending R1):** a provenance-preserving, validation-aware export contract exposing validated HPF knowledge to downstream consumers (publishing, marketing, documentation, website, sales, API) — consumers depend only on the contract, never on HPF internals (dossiers, programme state, validator). Implementation: `tools/hpf-engine/export.py` (producer 0.3.0, schema 1.2, contract `knowledge-export-core-v1`; run `python export.py --out export/latest.json`; output `tools/hpf-engine/export/latest.json`), specification: `tools/hpf-engine/EXPORT_CONTRACT.md` (schema frozen 2026-08-03; invariants; compatibility guarantees; migration rules). The engine already existed and was verified: 175 corpus objects parsed, 158 valid / 17 invalid (29 errors), matching the documented closeout exactly; the audit gap was that the previous handoff (`pipeline.py`) exported no validation state, no provenance, and only 11 hand-picked concepts. Two concerns are kept orthogonal per record — `origin` (hpf/nist/cert/rfc/academic/internal) and `authority` (hpf_experiment/external_curated/imported/unverified) + `status` (observed/replicated/provisional/retired) — never conflated with each other or with `schema_validation` (pipeline integrity: valid/invalid). Invalid records export metadata and errors only, never content. Stable core exported (objects, relationships, claims, constraints, recommendations); the provisional extension namespace (methodology terms, motif candidates, decomposition metrics, authority layer) is NOT exported until admitted by the vocabulary admission/removal rules. The contract and the knowledge index are derived projections of the corpus — the corpus remains the single source of truth; consumers are READ-ONLY (no downstream system ever mutates the corpus or research artifacts). Still future: the knowledge index, consumer adapters, and any productization engine — nothing before the contract is ratified at R1. **Subsystem closed 2026-08-03:** no new export fields, contract ideas, governance, or invariants; only bug fixes, insufficiencies discovered by use, and versioned evolution (per `EXPORT_CONTRACT.md` §8). Deferred observation (not adopted): split conformance checking into shape (`check_contract.py`) and content statistics (`check_export.py`) if use demonstrates the need. **Consumer side deliberately absent before R1 (architectural boundary, 2026-08-03):** producer subsystem accepted as complete — corpus, parser/validator, `knowledge-export-core-v1`, conformance check. No knowledge index, adapter interface, or consumer code before R1; only bug fixes. **OWNER OVERRIDE 2026-08-03:** the programme owner directed implementation of the consumer side ahead of R1. Built as experimental: knowledge index (`tools/hpf-engine/index.py`, derived projection of the export), contract-only consumers (`tools/hpf-engine/consumers/render_markdown.py` publishing, `factsheet.py` marketing), and the Research Workbench (`website-hpf/`, internal-only at `hpf.versatilesparks.qzz.io`, behind Cloudflare Access as the single authentication boundary, itself a contract-only consumer of `knowledge-export-core-v1`). The contract freeze discipline is unchanged: schema evolution still requires demonstrated recurring insufficiency. Consumer findings (Sufficiency / Leakage / Pressure) now flow from actual use and feed the R1 evidence review. Consumers will be treated as contract pressure-tests (Phase C: can independent consumers operate using ONLY the export?): if a consumer needs HPF internals (dossiers, programme state, validator), that is a failure of the contract, not a reason to widen it. First consumer after R1 to be the smallest possible (e.g. `render_markdown.py` producing a Markdown report from the contract alone) before any blog, website, or marketing tooling. **Final architecture sign-off (principal review, 2026-08-03):** architecture approved; HPF research subsystem, export subsystem, and governance model internally consistent and appropriately bounded. Governing principle: *if a consumer requires HPF internals, the contract has failed — not the consumer.* HPF's four responsibilities: knowledge creation (research), knowledge validation (protocol + replication), knowledge representation (ontology + export contract), knowledge distribution (future consumers). No further architecture reviews scheduled; future evolution driven solely by demonstrated insufficiencies. Next review is an evidence review after R1: did R1 expose an insufficiency? did the contract survive independent use? did the first consumer require HPF internals? did any governance rule fail in practice? **First consumer = contract validation experiment, not a publishing tool (observed 2026-08-03):** the governing principle is its acceptance criterion — can an independent subsystem perform useful work using only the exported contract? Evaluate against three criteria: (1) Sufficiency — task completable from the export alone; (2) Leakage — required HPF internal artifacts or assumptions; (3) Pressure — information genuinely needed that the contract did not expose. Pressure identifies candidate insufficiencies; only a demonstrated, recurring insufficiency justifies versioning — the same recurrence rule applied to the ontology and protocol. Sufficiency and Leakage are success/failure criteria; the first consumer is the first test of the contract, not of integration mechanics. **Designated candidate first consumer (recorded 2026-08-03): the Research Workbench** — a private, authenticated UI (separate subdomain; never part of the public site) exposing corpus, objects, search, relationships, validation, export, diagnostics, and research cycle views. The UI is itself a consumer of `knowledge-export-core-v1` and must never bypass the contract to read engine internals — if it needs internals, that is contract pressure evidence. Rationale: daily real use makes it the strongest contract validation experiment, replacing the earlier `render_markdown.py` placeholder as the candidate first consumer. Still gated on R1 evidence; consumer subsystem remains absent until then. Workbench is not a productization engine and does not precede the contract.

**Release and deployment governance (adopted 2026-08-03):** the workbench deploys only on explicit, owner-triggered release (`workflow_dispatch` on "Release HPF Workbench") - never from a push; a push only ever produces commits and tests. The deployed dataset is always the committed release: exports are versioned, committed artifacts (`exports/YYYY-MM-DD.json` + `.index.json`, plus `latest.json`/`latest.index.json` pointers); generation is an owner-driven release step, and CI verifies the committed artifact (`check_contract.py` gate) rather than regenerating it, so the deployed dataset is reproducible from git alone. Authentication is a single boundary: Cloudflare Access at the edge is the only authentication layer; the client-side in-app login gate was removed (2026-08-03) because anything shipped to the client is visible to an authenticated user and adds no security - the application assumes edge-authenticated users. `versatilesparks-hpf.pages.dev` is a deployment endpoint, not a public address; `hpf.versatilesparks.qzz.io` is the only entry point. **Git policy (adopted 2026-08-03):** automated agents may create commits and open pull requests, but may not rewrite history or force-push `main`; only the programme owner merges to `main` and triggers releases. The single history reconciliation of 2026-08-03 (superseding the pre-existing stale engine snapshot after the remote force-push) was a one-time repair and does not set precedent. **Operational rule (adopted 2026-08-03):** agents may diagnose and propose fixes automatically, but infrastructure mutations - secrets, workflows, deployments, access policy, domain configuration - happen only after explicit owner approval; the 2026-08-03 session (secret provisioning, workflow re-registration repair, first release dispatch) was owner-directed and does not set precedent for autonomous mutation.

---

## Emergent Methodology Vocabulary

*Status: research-methodology vocabulary, not protocol. Recorded 2026-08-03 following the Cycle 015 adjudicator-level audit. These terms name measurements the protocol's instruments already independently tracked before they were explicitly named; they introduce no new measurement instrument and are descriptive, not normative.*

- **Referent convergence** — agreement on the existence and identity of the engineering entities identified by independent analysts (Cycle 015: 30/51 canonical objects = 58.8%).
- **Boundary convergence** — agreement on how those entities are partitioned into knowledge objects (Cycle 015: 5 split/merge events = 9.8%; maximal disagreements E1, E5).

Cycle 015 demonstrates that these variables can diverge and should therefore be analysed independently.

### Stable Methodology Vocabulary

| Term | Meaning |
|---|---|
| Referent convergence | Agreement on the entities identified. |
| Boundary convergence | Agreement on partitioning those entities. |
| Canonical alignment | Adjudicated semantic reconciliation prior to scoring. |
| Maximal disagreement | A decomposition conflict not resolvable by semantic equivalence. |
| Structure correspondence | Referent set tracks document organization without implying causation. |

These are methodological terms that describe the experiment, not evidence primitives that describe the ontology.

**Admission rule (adopted 2026-08-03):** methodology vocabulary is admitted only *after* the experiment that gives rise to it — never anticipated — and only when the concept has been observed across multiple experiments. High admission bar, deliberately: this list stays small and descriptive and does not become a second framework. **Removal criterion:** a term is retired if later experiments fail to reproduce the pattern it names — the vocabulary is falsifiable, not cumulative.

---

## Research Priorities

**Highest-priority replication target — R1 (external validity):** Cycle 015 established internal validity for the decomposition-convergence instrument. The principal remaining limitation is external validity arising from curated source material. Replication on unedited third-party incident reports is therefore the highest-priority validation experiment, pre-committed to the two-level test (does structure predict the referent set but not boundary placement?). Status: research priority, not a protocol amendment.

---

## Hypotheses

### H₀ (Null)

Engineering domains require domain-specific evidence structures that cannot be represented by a single stable atomic schema.

### H₁ (Empirical)

Engineering knowledge appears to be representable using a stable set of evidence primitives regardless of technical domain.

Every research cycle attempts to reject H₀.

---

## Current Evidence

### Completed Validation Cycles

| Cycle | Experimental Target | Subject | Result |
|-------|-------------------|---------|--------|
| 001   | Deterministic (pilot) | Browser State | Pass |
| 002   | Deterministic | Browser Memory / Profiles | Pass |
| 003   | Deterministic | Browser Perception / Detection | Pass |
| 004   | Deterministic | Browser Architecture / Protocols | Pass |
| 005   | Deterministic Infrastructure | Networking (TCP/TLS/HTTP/Proxy) | Pass |
| 006   | Systemic | Distributed Systems | Pass |
| 007   | Probabilistic | Security Engineering | Pass |
| 008   | Probabilistic + Adaptive | Machine Learning | Pass |
| 009   | Transformational | Compilers / Static Analysis | Pass |
| 010   | Data Semantics | Databases | Pass |
| 011   | Temporal Guarantees | Real-Time Systems | Pass |
| 012   | Cyber-Physical | Robotics / Autonomous Systems | Pass |

### Accumulated Metrics

| Metric | 001 | 002 | 003 | 004 | 005 | 006 | 007 | 008 | 009 | 010 | 011 | 012 |
|--------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Schema changes | — | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Parser changes | — | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Validator changes | — | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Schema friction | — | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Passing objects | — | 1 | 4 | 6 | 10 | 26 | 41 | 57 | 73 | 89 | 105 | 121 |
| Total corpus | — | 21 | 21 | 23 | 27 | 43 | 58 | 74 | 90 | 106 | 122 | 138 |
| Object kinds (cumulative) | — | 1 | 1 | 1 | 1 | 3 | 4 | 4 | 4 | 4 | 4 | 4 |

### Secondary Metrics

The primary falsification signal is vocabulary growth (new evidence primitives). Two secondary signals are tracked to prevent complexity from escaping the schema by migrating elsewhere:

#### Object Kind Stability

The identity layer (object taxonomy) is separate from the evidence vocabulary. Both are measured:

| Metric | Purpose |
|---|---|
| New evidence primitives | Primary falsification signal |
| New object kinds | Secondary abstraction pressure |
| New relationship patterns | Normal graph growth |

Cumulative object kinds in the HPF-format corpus: `concept` (002), `+principle` (006), `+pattern` (006), `+decision` (007). The failure mode to watch: every new domain creating a new object kind (threat-model, consensus-model, training-model...) — that would recreate domain-specific schemas indirectly and triggers architecture review even though primitive stability would remain technically unfalsified.

#### Complexity Migration Matrix

The emerging theory is about *where* complexity moves. Each knowledge category is expected to migrate complexity into a different graph dimension while the vocabulary stays constant:

| Cycle(s) | Domain | Knowledge category | Complexity moved into |
|---|---|---|---|
| 001–004 | Browser automation | Deterministic | Graph composition |
| 005 | Networking | Deterministic infrastructure | Graph composition |
| 006 | Distributed Systems | Systemic | Relationships |
| 007 | Security | Probabilistic | Evidence qualification |
| 008 | Machine Learning | Probabilistic + adaptive | Validity conditions + feedback relationships |
| 009 | Compilers / Static Analysis | Transformational | Constraint-carrying relationships + qualification (observation-model scoping) + decision structure |
| 010 | Databases / Data Semantics | Data semantics | Constraints + validity conditions (unification n=3) + decision structure + cross-domain relationships |
| 011 | Real-Time Systems | Temporal guarantees | Constraints (time as validity condition) + qualification (WCET as observation) + decision structure (posture) + motif topology (arbitration candidate) |
| 012 | Robotics / Autonomous Systems | Cyber-physical (epistemic separation) | Constraints (dynamics as constraint relationships) + qualification (belief at distance 2–3, Epistemic Distance gradient 1→3+) + verification (stability, safety-case — candidate n=6) + decision structure (autonomy, arbitration re-test) + motif topology (Epistemic Chain → Closed Epistemic Loop watch) |

Cycle 008 answered the migration question: adaptation is not a separate complexity class. It resolved as validity conditions (constraints) + feedback relationships + qualification — a composition of existing destinations, not a new one. Outcome space result: fits qualification complexity (outcome 1) and new graph pattern (outcome 2) both occurred; vocabulary expansion (outcome 3) did not.

Cycle 009 answered the transformation question: transformation is not a separate complexity class either. It resolved as constraint-carrying relationships (the preserve/verify pair — operates_on + preserves + verified_by) + qualification (correctness claims scoped by stated observation models) + decision structure (Tier 4). Five candidate primitive families rejected by composition: representation, transformation, proof, formal rule, equivalence. Outcome space: outcome A (composition) dominant, outcome B (new motif: preserve/verify pair) occurred, outcome C (vocabulary expansion) did not. Two consecutive "not a separate class" results (008 adaptive, 009 transformational) support the working theory that across tested engineering categories, increasing complexity has so far migrated through composition, relationships, qualification, and decision structure rather than requiring vocabulary expansion.

Cycle 010 answered the data semantics question: data semantics is not a separate epistemic mode either. It decomposed into existing destinations — constraints (normal forms as structural constraints, anomaly taxonomy as constraint structure, consistency models as constraint contracts, RPO/RTO as recovery constraints), validity conditions (schema validity = derivation, joining knowledge validity 008, enabling conditions 009, artifact validity 009 — the unification hypothesis at n=3), decision structure (isolation levels, query planning, index selection, data governance — all exactly 4 Decision Factors), and cross-domain relationships (6 links to the 006/008/009 corpora). The strongest pre-registered temptation — the relational model's entities/relationships/keys mapping directly onto HPF's entities/relationships/constraints — was treated as evidence (coincidence-as-evidence), not accident. Outcome space: outcome A dominant, outcome B (cross-domain recognition motif: analogous_to) occurred, outcome C absent. Three consecutive "not a separate class" results (008 adaptive, 009 transformational, 010 data semantics), with the unification hypothesis now at n=3 — three domains agree that every validity claim in engineering is bound by stated conditions, and the conditions are constraints.

Cycle 011 answered the temporal question: hard temporal guarantees are not a separate epistemic mode either. Time as a correctness condition itself resolved through composition — deadline as validity condition on completion (the fifth temporal defusal, unification hypothesis at n=5), WCET as observation with confidence (prediction-object structure), scheduling as decision + pattern, priority inversion as failure mode + mitigation pattern, overload as bounded-response constraints. The pre-registered danger object (priority-inversion) was resolved without a concurrency-failure primitive. Outcome space: outcome A dominant, outcome B occurred (arbitration motif candidate), outcome C absent. Four consecutive "not a separate class" results (008 adaptive, 009 transformational, 010 data semantics, 011 temporal guarantees). The temporal-constraint-density observation dimension discriminated cleanly: 100% of constraints time-bounded in all tiers vs 40–45% of edges — temporal pressure concentrates in guarantee structure and dilutes in decision content. The guarantee-object motif reached n=4 (type-safety, data-integrity, atomicity, real-time-guarantee).

Cycle 012 answered the cyber-physical question: knowledge whose truth is never directly observable — only inferred through layered models — is not a separate epistemic mode either. Epistemic separation resolved through composition: reality → observation → qualified observation → claim → decision. The danger object (belief-state) resolved as composition ("belief is composition, not ontology" — the POMDP belief as constraint + qualification), the safety case as claim + evidence + argument artifact (P3 — "an artifact of evidence, exactly as a proof is"; verification family candidate n=6), stability as verification pattern (P4 — "stability is demonstrated, not claimed"), autonomy as decision under an incomplete world model (P6 — 4 Decision Factors, 13th decision object), arbitration re-tested at n=4 and not promoted. P1–P9 all held; 0 primitives, 0 new kinds; the guarantee motif reached n=5 (closed-loop-guarantee); the prediction-object family reached n=4 (state-estimation). New programme-wide observation dimension validated: **Epistemic Distance** measured the full gradient 1 → 3+ (sensing 1, belief 2–3, safety-case 3+ — the corpus maximum) without schema change, separating distance (structural) from confidence (qualificational). Temporal Constraint Density discriminated within the category: model tier 25%/15%, junction tier 37.5%/20%, belief/decision tiers 0%/5% (the 011 T2/T4 dilution pattern reproduced). Outcome space: outcome A dominant, outcome B elements (the Epistemic Chain → Closed Epistemic Loop named as a watch), outcome C absent. Five consecutive "not a separate class" results (008 adaptive, 009 transformational, 010 data semantics, 011 temporal guarantees, 012 cyber-physical).

**Cycle 012 closeout review (research lead):** the review identified a new experimental-design risk — *destination bias*: the research is beginning to optimize itself (predictions becoming extremely precise — exact factor counts, exact motif growth, exact pattern resolutions — creates the unconscious pressure to "find the destination" rather than "discover whether one exists"). Pre-registration and frozen ontology control hindsight bias and primitive inflation but not this. The review's prescription, adopted as protocol below: an adversarial-review control (appointed at every cycle closeout, whose only task is to argue HPF is wrong — prove the ontology insufficient, not improve the object), a strengthened Phase 5 criterion (record how hard the cycle tried to prove there was *no* destination, not merely that no destination appeared), and a maturity gate for motifs: **engineering must not mature engineering motifs** — the verification family (and any candidate) requires at least one genuinely different epistemology (e.g., mathematical proof, clinical evidence, legal burden of proof) before maturity. Engineering cycles continue (one or two hostile domains per the review), then Programme B (biology → economics → social).

#### Evidence Graph Motifs (catalogue v0.1)

Cycles 007–011 revealed that complexity does not only migrate into graph dimensions — it also organizes into **recurring graph structures** that repeat across domains without becoming vocabulary. These are tracked as a provisional catalogue, **not** as a finalized architectural component. The catalogue remains empirical; candidate motifs must satisfy the acceptance criteria and survive further cycles.

**Distinction**: a *primitive* changes the representation language; a *motif* changes how existing primitives are composed. Motifs are measured at the edge level only — block-level ratios are disciplined into uniformity by authoring conventions and reveal nothing.

**Motif acceptance criteria** — a candidate motif must satisfy all of:

1. Appears independently in multiple objects.
2. Appears across multiple cycles or domains.
3. Explains composition rather than vocabulary.
4. Improves understanding without changing representation.
5. Is optional — never required — for valid modelling.

**Anti-primitive rule**: every motif must always be expressible as an optional composition of existing primitives. A motif that becomes mandatory for valid modelling is a hidden primitive and triggers architecture review. (Transformation Chain, for example, must never become "transformation = required motif".)

**Motifs vs graph properties**: motifs are reusable structures; graph properties are measurements of topology. The two abstraction levels are kept separate below.

**Motifs**:

| Motif | Appeared | Representative objects |
|---|---|---|
| Guarantee Object | 009, 010, 011, 012 | type-safety, data-integrity, atomicity, real-time-guarantee, closed-loop-guarantee — scoped claim + invariants + failure modes (n=5) |
| Transformation Chain | 009, 010 | compiler-optimization, query-optimization — before-state + action + after-state + correctness constraint (n=2, cross-domain) |
| Validity Derivation | 008, 009, 010 | training-data, build-systems, schema-migration, backup-recovery — validity as derivation under stated conditions (n=3, unification hypothesis) |
| Feedback Loop | 008 | model-monitoring → retraining-decisions — observation → recommendation → action → new observation |
| Failure-Recovery Loop | 006, 010 | retry-pattern/circuit-breaker, transaction-failures, backup-recovery — failure mode + mitigation link + recovery discipline |
| Decision Tradeoff | 007, 009, 010, 011, 012 | risk-acceptance, optimization-tradeoffs, isolation-levels, query-planning, index-selection, data-governance, scheduling-policy, hard-vs-soft-real-time, real-time-throughput-tradeoff, autonomy-decision, resource-arbitration — decision object with exactly 4 Decision Factors |

**Graph properties** (measurements, not motifs):

| Property | Cycles | Measurement |
|---|---|---|
| Guarantee Hub | 009, 010, 011 | Guarantee-family edge share clusters around guarantee objects (010: 32.9%, 009: 39.8%, 007: 4.5%) — topology, not a construct |
| Cross-domain recognition | 010, 011, 012 | analogous_to links binding the corpus into a single graph (010: 4; 011: 8; 012: 37 cross-domain links total — every prior corpus 006–011 links in) |
| Temporal Constraint Density | 011, 012 | 011: constraints 100% time-bounded all tiers, edges 40–45%; 012: model tier 25%/15%, junction tier 37.5%/20%, belief/decision tiers 0%/5% — temporal pressure concentrates in guarantee structure; discriminates within a category, not only between categories |
| Epistemic Distance | 012 | Inferential layers between a claim and directly observable reality: full gradient 1 → 3+ measured (sensing 1, state 1–2, belief/estimation 2–3, autonomy-decision 3, safety-case 3+); distance structural, confidence qualificational — programme-wide metric |

**Motif candidates** (observed, not yet catalogue entries — must survive further cycles and satisfy all acceptance criteria): **Arbitration** (012 arbitration, 011 scheduling, 006 consensus, 010 locking — contenders + selection rule + allocation + guarantee; resolved as graph topology, not a construct; re-tested at n=4 in 012 and NOT promoted), **Isolation** (006 strong-consistency, 010 isolation-levels, 011 temporal-isolation — guarantee separation across 3 domains), **Prediction-object** (012 state-estimation and belief-state, 008 benchmarks, 010 query plans, 011 WCET — model of the world as evidence source feeding a decision; tracked with comparison metrics), **Verification family** (012 stability + safety-case, 009 equivalence-checking + formal-verification, 008 benchmark-validity, 011 schedulability-analysis — claim + evidence + constraints, where verification does not become ontology; candidate at n=6).

**Motif maturity gate (Cycle 012 closeout review):** engineering must not mature engineering motifs. No candidate — including the verification family at n=6 — may be treated as mature until it has survived at least one genuinely different epistemology that justifies truth differently (e.g., mathematical proof, clinical evidence, legal burden of proof). Maturity is deferred to Programme B at the earliest; the candidate status is a claim about engineering categories only.

Current explanatory hypothesis: **across the engineering categories tested so far, new knowledge has consistently increased graph organization rather than evidence vocabulary. Recurring graph motifs are the current explanatory hypothesis for that organization.** This is an emerging theory, not a finalized component — it must survive several more orthogonal cycles before it earns architectural status.

#### Adaptation Complexity (Cycle 008 observation dimension)

ML introduces the first post-deployment change: the system itself evolves after deployment. Tracked without schema changes as observation metrics:

| Metric | Question |
|---|---|
| Adaptation events | How often does knowledge depend on system evolution? |
| Feedback relationships | Are learning loops expressible as relationships? |
| Drift representation | Does changing behaviour require new modelling constructs? |

Expected outcome under H₁: adaptation complexity becomes another graph pattern (observation → recommendation → action → new observation), not a new primitive.

### Hypothesis Hierarchy

| Level | Hypothesis | Status |
|-------|-----------|--------|
| L1 | Browser automation knowledge is representable | Strongly supported (4 cycles) |
| L2 | Orthogonal infrastructure domains are representable | Supported (Networking, cycle 005) |
| L3 | Any abstraction level is representable | **Supported** (Distributed Systems, cycle 006; Security, cycle 007; Machine Learning, cycle 008; Compilers, cycle 009; Databases, cycle 010; Real-Time, cycle 011; Robotics, cycle 012) |
| L4 | Domain-independent for all engineering | Untested |

Claim discipline: status statements are limited to tested categories. The correct formulation is **"HPF has remained domain-independent across tested engineering categories"** — not "HPF is domain-independent." Tested: deterministic (browser automation, networking), systemic (distributed systems), probabilistic (security), adaptive (machine learning), transformational (compilers/static analysis), data semantics (databases), temporal guarantees (real-time systems), cyber-physical (robotics — epistemic separation). Untested: biological systems, economics, social systems, non-engineering knowledge, and (per the Cycle 012 closeout review) the deliberately hostile engineering categories that remain (distributed AI agent ecosystems, adversarial cyber operations, multi-agent coordination, human-in-the-loop safety-critical systems).

---

## Central Invariant

> **Knowledge diversity increases while the evidence vocabulary remains constant.**

Passing validation counts are a secondary metric. The primary research result is the absence of schema evolution under increasing domain diversity.

The vocabulary is binary: either the evidence primitives changed, or they did not. This is a stronger invariant than "representational complexity" because vocabulary change is objectively measurable.

---

## Architecture Laws

### Ontological Sufficiency Principle

**The schema models the underlying entities, relationships, constraints, and evidence — not the way humans choose to visualize or explain them.**

Consequence: workflow, timeline, sequence, flowchart, and state diagram blocks are not needed. Those are presentation layers over existing ontology.

Design filter for any proposed new block:

> Does this represent a new kind of knowledge, or merely a new way of viewing existing knowledge?

### Representation Minimality Principle

**If existing primitives faithfully represent the ontology, introduce no additional primitive. Express richer views through composition instead of expansion.**

Consequence: retry storms become relationships among objects. TCP handshake becomes claims and constraints. Failure cascades become connected objects. Composition is the mechanism for complexity, not schema growth.

### Primitive-Motif Distinction Principle

**A primitive changes the representation language; a motif changes how existing primitives are composed.**

New recurring patterns must be captured as motifs — provisional, optional compositions of existing primitives — never promoted to primitives while expressible through composition. A motif that becomes mandatory for valid modelling is a hidden primitive and triggers architecture review. Primitive governance asks "does this require a new evidence type?"; motif governance asks "does this composition pattern remain optional?"

---

## Outcome Classification

Every cycle observation is classified into one of three categories:

| Type | Meaning |
|------|---------|
| Failure | Required schema evolution or new evidence primitive |
| Discovery | New modelling insight, no schema change |
| Confirmation | Expected behaviour observed without friction |

---

## Research Method

### Controlled Variables (Instrumentation)

- Parser
- Validator
- Analyzer
- Atomic evidence schema (9 primitives: claims, relationships, constraints, observations, trade-offs, failures, heuristics, recommendations, decision factors)

### Independent Variable

- Knowledge category / experimental subject

### Measured Variables

- **Representation failure**: Could a concept not be faithfully represented using existing evidence primitives?
- **Research discovery**: Did the domain reveal a new modelling pattern while remaining representable?
- **Authoring friction**: Was the schema difficult to use for a given domain?
- **Granularity stability**: Were object boundaries obvious or contested?
- **Pressure point observations**: Recorded per cycle across four categories:
  1. Structural (multi-layer representations)
  2. Systemic (emergent behaviour)
  3. Temporal (sequences, ordering)
  4. Granularity (splitting / merging decisions)

### Pressure Point Policy

Only recurring representation failure across multiple independent cycles justifies considering architecture evolution. Non-recurring authoring friction is recorded but does not trigger architecture review.

### Adversarial Review (destination-bias control — Cycle 012 closeout review)

**Motivation.** The programme controls ontology drift, vocabulary drift, primitive inflation, hindsight bias, and prediction leakage. It does not control *destination bias*: the researcher's natural pressure to map every new pressure onto an existing complexity destination ("find the destination" rather than "discover whether one exists"). As predictions become extremely precise (exact factor counts, exact motif growth, exact pattern resolutions), the experiment risks optimizing itself instead of testing the ontology.

**The control (internal).** After every cycle, an appointed adversarial reviewer argues the case that **HPF is wrong in this domain** — that a pressure escapes the existing destinations, that a resolution is a forced fit, that the ontology is insufficient. The reviewer's task is explicitly not to improve objects. At least one negative claim per cycle must be recorded with the reasoning and the counter-evidence; a cycle with no attempted negative claim does not close.

**External-frame adversarial review (Amendment A1, Cycle 013).** The internal review argues from inside HPF's own framework. Every object-authoring cycle (from Cycle 014) must additionally include at least one external-frame adversarial review — written entirely in a competing philosophy's own terms, standards, and vocabulary. Frames are selected by seeded pseudo-random draw (B7): all four frames appear within every four object-authoring cycles; no frame twice in succession; seed and selection recorded at cycle start.

| Frame | Standard it argues from | Typical negative claim |
|---|---|---|
| Ontology-first (BFO/DOLCE-style upper ontology) | Rich category distinctions: kinds, roles, dispositions, boundaries, processes | "HPF's primitives conflate categories — 'pattern' mixes process with disposition; 'decision' is a role, not a kind; a boundary cannot be expressed." |
| Category-theoretic (categorical semantics) | Compositional laws: identity, associativity, functoriality, universal constructions | "Graph composition without categorical laws is ad hoc — there is no defined identity/associativity, so 'composition' is not a well-defined operation." |
| Formal-methods / model-theoretic | Truth conditions, formal semantics, proof obligations | "Claims have no formal truth conditions — an evidence block is not a semantics; verification claims cannot be discharged." |
| MBSE / systems engineering | Executability, standard conformance (SysML/UML), integration | "A representation that cannot execute or integrate with engineering tooling adds nothing over SysML; it is a private notation." |

**Independent evaluation rubric (Amendment B1, Cycle 013 round 2).** The review pipeline: frame appointed (randomized) → **rubric frozen** (the frame's evaluation rubric is pre-registered and versioned *before* the argument exists, in the frame's own vocabulary, with no reference to HPF outcomes — so it cannot be tuned to the result) → argument (citing the specific rubric conditions HPF allegedly fails) → response (counter-evidence, cited to corpus content) → **verdict** (mechanical application of the frozen rubric + B2 conditions; the research lead's only role is factual verification that cited corpus content exists). A second researcher can re-derive the verdict from the record.

Frozen rubric templates (condition sets, checkable): **Ontology-first** — R1 kind/role distinction; R2 disposition vs process; R3 boundary/continuant; R4 dependence; R5 entity references resolve to defined universals. **Category-theoretic** — C1 identity morphisms and laws; C2 associativity; C3 functoriality; C4 universal constructions (products/pullbacks); C5 evidence kinds form a category with well-defined morphisms. **Formal-methods** — F1 truth conditions per claim; F2 defined grammar; F3 proof obligations discharge; F4 semantics defined; F5 consistency checkable. **MBSE** — M1 executability; M2 SysML/UML conformance; M3 tooling/serialization; M4 requirements→design→verification traceability; M5 lifecycle span.

**Objective verdict conditions (Amendment B2, Cycle 013 round 2).** Verdicts are mechanical, not judgment calls. **ESCAPED** if ANY of: (1) the response cannot answer using the current ontology (no composition of existing objects/relationships/primitives addresses the cited deficiency); (2) the response requires an undocumented assumption; (3) the response requires a new primitive or new object kind; (4) the response requires scope narrowing (narrowing recorded as a forced-fit incident; narrowing that changes the claim's meaning = ESCAPED); (5) the response contradicts a previously recorded cycle result or claim. Otherwise **CONTAINED** (counter-evidence satisfies the cited rubric conditions). Otherwise **DISMISSED** (the negative claim fails on its own terms — the cited condition is misapplied or absent from the frozen rubric). An ESCAPED outcome triggers architecture review.

**The strengthened Phase 5 criterion.** The falsification question is not only "is there no destination?" but **"how hard did we try to prove there wasn't one?"** — recorded per cycle as an attempted-falsification intensity statement. The researcher's posture is to break HPF, not to fit it. Confidence increases for the right reason: the ontology survives hostile pressure, not because each new cycle continues to fit.

**Maturity gate.** Engineering must not mature engineering motifs. Candidates (verification family, arbitration, isolation, prediction-object, guarantee) are claims about engineering categories only; maturity requires survival across a genuinely different epistemology (mathematical proof, clinical evidence, legal burden of proof) at Programme B. A cycle may promote a candidate to catalogue entry only if the adversarial review could not produce a counter-instance against it.

### Prediction Specificity Control (Amendment A2, Cycle 013)

**Motivation.** Fine-grained predictions (exact factor counts, exact motif counts, exact resolutions) make the researcher's destination visible during authoring — the more specific the prediction, the easier to unconsciously steer the object toward it.

**The control.** Predictions split into two tiers in every tier addendum:

1. **Coarse expectations (H-level)** — falsifiable direction claims (new primitive / no new primitive; maps to a destination / maps to none). These guide authoring and are checked at tier close.
2. **Fine-grained predictions (F-probes)** — specific counts, exact resolutions, exact factor sets. Recorded in the addendum marked **sealed**; not consulted during authoring; checked only at tier close. An F-probe that fails is recorded as an **overfitting signal**, not a falsification event; an F-probe that succeeds adds weak confirmation only.
3. **Counter-probes** — each addendum records at least one explicit counter-probe: the specific way the tier would falsify its central expectation. Counter-probes force the author to predict the tier's failure modes, opposing destination bias.

**Forced-fit audit (Amendment B4, Cycle 013 round 2 — A/B probe comparison).** Introspection is replaced by a recorded comparison. Sealed-authoring is the **blind condition (Version A)**. At tier close the probes are revealed (**Version B**) and a probe-outcome diff is recorded: every F-probe and every decoy gets MATCH / MISMATCH / NOT-APPLICABLE. **Decoy probes**: one plausible-but-wrong fine-grained prediction per tier, included in the sealed set. Interpretation: outcomes tracking true probes but not decoys = seal working; tracking both = contamination; a strong MATCH on a true probe where the domain plausibly permits an alternative resolution = destination-bias flag (counted as a forced-fit incident). The audit's counterfactual question is asked of the recorded diff and its documented alternatives — not of memory. Every confirmed fine-grained prediction is also reviewed for post-hoc rationalization.

### Cycle Scorecard (Amendments A3 + B3, Cycle 013)

**Motivation.** "0 primitives" is necessary but not sufficient — a cycle can pass while quietly forcing every pressure into a destination. The scorecard is the quality measure. It has **two sections, never aggregated** (B3): objective and subjective variables are not commensurable.

**Objective metrics** (counts, verifiable):

| Dimension | Definition | Threshold |
|---|---|---|
| Forced-fit incidents | Straining resolutions flagged by the probe-outcome diff (A/B comparison), the adversarial reviews, and the verdicts (analogy force, convenient scoping, contorted claims, scope narrowing), counted per cycle | ≤ 1 per hostile cycle |
| Unresolved pressures | Pressures in the dossier's Residual Pressures entries left deferred/latent (resolved pressures are not failures; disposition recorded) | ≤ 1 per hostile cycle, with disposition |
| Vocabulary additions | New evidence primitives (9 fixed), new object kinds (4 fixed), new relationship verbs, new analogy targets required | primitives/kinds 0; verbs: explanation simplicity ≥ 3 (0 new verbs = 5; 1 = 4; 2 = 3; 3 = 2; 4+ = 1) |
| Escaped reviews | External-frame verdicts of ESCAPED | 0 per hostile cycle |

**Descriptive metrics** (recorded, not scored — commentary only):

| Dimension | Definition |
|---|---|
| Adversarial challenge strength | Strongest negative claim of the cycle: 1 trivial / 2 standard-internal / 3 standard-external / 4 severe (survived counter-evidence attempt) / 5 falsification-adjacent (escaped temporarily, resolved only by narrowing the claim) |
| Research-lead confidence | Justified assessment of the cycle's resolutions |

Scored prospectively from Cycle 014 (Cycle 012 is not retro-scored — the dimensions were not measured during the cycle, and retrospective calibration is itself a hindsight-bias risk; the hostile-domain cycles establish the baseline). A cycle with degraded objective metrics is recorded as a *low-confidence pass*, which gates Programme B transition (A4, G4) and motif promotion (A5). The v1.2 composite scorecard is withdrawn.

**Residual Pressures entry** (dossier requirement): every tier records pressures that did not fully resolve, with disposition — RESOLVED / DEFERRED / LATENT. The objective metrics count deferred/latent only. Interaction guard: a cycle claiming 0 forced-fit incidents and 0 unresolved pressures must show the probe-outcome diff and audit ran and came back clean — an *empty* record is not a *clean* record.

### Programme B Entry Gates (Amendment A4, Cycle 013)

**Motivation.** "Programme B after engineering" was narrative; transition criteria must be objective.

**The gates.** The programme may transition to Programme B (biology → economics → social, each isolating one epistemic shift: design, optimization, consensus) only when **all** of:

- **G1** — Two hostile-domain engineering cycles passed (Cycle 014 + Cycle 015, or successors): 0 primitives, 0 new object kinds, 0 ESCAPED reviews.
- **G2** — Two independent external-frame adversarial reviews completed from two distinct frames (A1), neither producing an ESCAPED outcome.
- **G3** — No recurring escape pressure: any adversarial-flagged escaping pressure must not recur in a later cycle; recurrence without resolution blocks the transition.
- **G4** — Scorecard discipline: forced-fit incidents ≤ 1 per hostile cycle; unresolved pressures ≤ 1 per hostile cycle with recorded disposition; explanation simplicity ≥ 3 each cycle.
- **G5** — Every promoted motif has a non-empty attempted-counterexample register (A5).
- **G6** — The decision-factor anomaly search ran in at least one hostile cycle: a documented search for a decision object requiring ≠ 4 factors, finding none.
- **G7 — Epistemic discontinuity pilot (Amendment B5, Cycle 013 round 2)** — before full Programme B: a pilot cycle (4 objects, one tier) in a domain whose justification structure differs categorically from engineering (medicine — clinical evidence as the justification mode; or biology — evolved, non-designed knowledge), run under the full protocol (external-frame review, sealed probes + decoys, split scorecard, residual pressures), passing with 0 primitives and objective metrics within thresholds. Engineering stress (G1) does not substitute: biology does not merely increase complexity, it changes the epistemology. If medicine is chosen, the pilot doubles as the verification-family epistemology test (Cycle 012 maturity gate). The pilot's residual pressures become the Programme B agenda.

### Motif Promotion Gate and Attempted-Counterexample Register (Amendment A5, Cycle 013)

**Motivation.** n=5/n=6 appearances are encouraging, but appearance count alone is weak evidence — motifs must show recurrence, independence, discriminative power, and survive a deliberate search for counter-instances.

**The gate.** A motif candidate may be promoted to catalogue entry only when **all** of:

1. The five acceptance criteria hold (multi-object, multi-cycle/domain, explains composition, improves understanding, optional).
2. **Recurrence** — ≥ 5 independent appearances across ≥ 3 distinct domains (appearances within one domain's sub-tiers count as one; e.g., robotics T1–T4 = one domain).
3. **Independence** — the appearances' domains do not share a sub-domain lineage (arbitration's four appearances span consensus/locking/scheduling/arbitration = four domains; verification's six span four domains).
4. **Discriminative power** — a documented ablation argument: what the motif explains that a generic alternative (plain relationships, generic pattern label) does not; removing the motif's structure from a representative object must materially degrade it.
5. **Failed counterexample search** — the candidate has an **attempted-counterexample register**: a documented, pre-registered search for counter-instances (a decision object with ≠ 4 factors; a guarantee object without stated scope; a verification artifact that is not claim + evidence + constraints). **Search strategy required (Amendment B6, Cycle 013 round 2)**: the register records (a) the search space (instances examined — e.g., all decision objects, all guarantee objects, hostile-cycle instances); (b) inclusion criteria (which instances count as candidates); (c) the stopping criterion (exhaustive, or n consecutive candidates without a counter-instance, or domain-exhaustive — stated in advance); (d) justification (why the search space suffices for the claim). An empty register, or a register without a stated strategy, is a block — not a pass.
6. **No ESCAPED external review** dismissing it as a frame artifact.

Promotion (catalogue entry) is distinct from maturity: **maturity** (architectural status) still requires the Programme B epistemology gate (math/medicine/law), per the Cycle 012 maturity gate. A promoted motif can be demoted by a later counter-instance.

---

## Experimental Unit

A research cycle is complete only when:

1. Knowledge objects have been authored (object-authoring cycles) — or, for a protocol cycle, the protocol amendments are adopted and recorded (Cycle 013 precedent).
2. Validation passes.
3. Pressure points are evaluated.
4. Outcome classification is recorded.
5. H₀/H₁ status is updated if appropriate.
6. The end-of-cycle questions are answered.
7. **The adversarial review is conducted** (destination-bias control — a recorded, reasoned attempt to prove the ontology insufficient in this domain; a cycle with no attempted negative claim does not close). Object-authoring cycles also conduct the external-frame review (A1).
8. **The cycle scorecard is recorded** (B3 — objective metrics: forced-fit incidents, unresolved pressures, vocabulary additions, escaped reviews; descriptive metrics: challenge strength, confidence — never aggregated) and the dossier's Residual Pressures entries are complete.

---

## Falsification Criteria

H₁ would be considered falsified if:

- a recurring engineering concept cannot be represented using existing evidence primitives
- multiple independent cycles require the same additional primitive
- the deficiency cannot be addressed through composition
- architecture evolution becomes necessary
- **the adversarial review produces pressure that escapes the existing complexity destinations, and the escape survives the counter-evidence** (the strengthened Phase 5 criterion: the attractor state is "no primitive, but no destination either"; attempted-falsification intensity is recorded every cycle)
- **an external-frame review (A1) returns ESCAPED and the escape survives the counter-evidence** (a competing philosophy demonstrating in its own terms that the representation is insufficient)

Passing a cycle requires 0 primitives (primary endpoint). The cycle scorecard (A3) is the quality measure — a pass with a degraded scorecard (systematic forced fits, unresolved pressures without disposition, an empty forced-fit audit) is recorded as a *low-confidence pass*, which gates Programme B transition (A4, G4) and motif promotion (A5).

---

## Assumptions

The research programme depends on the following assumptions. If any are invalidated, the methodology must be reconsidered:

- Engineering knowledge is decomposable into independent knowledge objects
- Objects communicate through explicit, typed relationships
- Evidence primitives are domain-independent unless disproven
- Presentation formats are not ontology

---

## Evidence Primitives (The 9 Blocks)

The atomic evidence schema defines nine primitives that compose every knowledge object:

| Primitive | Purpose |
|-----------|---------|
| Claims | Self-contained, verifiable factual statements |
| Relationships | Typed, directional links between objects |
| Constraints | Boundaries, limits, preconditions, invariants |
| Observations | Empirical findings, measurements, behavioural notes |
| Trade-offs | Explicit sacrifice dimensions when comparing alternatives |
| Failures | Failure modes, conditions, observable evidence |
| Heuristics | Rules of thumb, experience-based patterns |
| Recommendations | Prescriptive guidance traceable to evidence |
| Decision Factors | Criteria that influence choice under uncertainty |

---

## Knowledge Axes (Orthogonal Dimensions)

Research coverage must span two independent axes:

| Axis | Values |
|------|--------|
| Knowledge type | Deterministic → Systemic → Probabilistic |
| Abstraction level | Mechanism → Protocol → Architecture → Operations → Decision |

Examples of coverage targets:

| Topic | Type | Abstraction |
|-------|------|-------------|
| TCP handshake | Deterministic | Mechanism |
| HTTP | Deterministic | Protocol |
| Raft | Systemic | Protocol / Algorithm |
| CAP theorem | Systemic | Architecture |
| Threat modelling | Probabilistic | Decision |
| Model evaluation | Probabilistic | Operations |

---

## Research Roadmap (Hypothesis-Driven)

Future cycles are named by experimental target, not domain.

| Cycle | Experimental Target | Candidate Subject | Status |
|-------|-------------------|-------------------|--------|
| 006 | Systemic Knowledge Test | Distributed Systems | **Complete** |
| 007 | Probabilistic Knowledge Test | Security | **Complete** |
| 008 | Probabilistic + Adaptive Knowledge Test | Machine Learning | **Complete** |
| 009 | Transformational Knowledge Test | Compilers / Static Analysis | **Complete** |
| 010 | Data Semantics Knowledge Test | Databases | **Complete** |
| 011 | Temporal Guarantees Knowledge Test | Real-Time Systems | **Complete** |
| 012 | Cyber-Physical Knowledge Test | Robotics / Autonomous Systems | **Complete** |
| 013 | Protocol Hardening | Research protocol amendments A1–A5 + B1–B8 (external-frame review with frozen rubrics, objective verdicts, sealed probes + decoys, split scorecard, Programme B gates incl. G7, motif promotion gate, Protocol Stability Principle) — **protocol version v1.3** | **Complete** |
| 014 | Hostile-Domain Falsification Experiment #1 | Adversarial Artifact Analysis (reverse engineering / obfuscated binaries / firmware analysis / forensic reconstruction as instances — the modeler's own knowledge becomes inferential; selected at the pre-Cycle-014 review under the assumption-violation criterion; deception rejected: already expressible via Cycle 007 blinds/distorts) — test question: "Can HPF faithfully represent engineering knowledge whose ground truth is intentionally inaccessible and must be reconstructed through iterative inference?" — frame draw executed at pre-registration: **Formal-methods / model-theoretic** — 16 objects authored across T1–T4 (0 primitives, 0 kinds, 0 verbs; H1–H9 held at object level; Closed Epistemic Loop named as motif candidate; G6 first-pass done) | **FAILED-EXTERNAL-REVIEW** — object-level composition clean (16 PASS 0/0, all probes MATCHed, no decoys); external review returned **ESCAPED on F1 (terminal)** — the first genuine, non-overridable ESCAPED in programme history (F2–F5 CONTAINED); F1 semantics pressure maps onto no existing complexity destination — **attractor-state falsification signal recorded** (outcome class C); **architecture review triggered** (§6.4) — semantics-destination question / B8 amendment eligibility, scheduled closeout follow-up / Cycle 015 pre-work; G1 not met by 014 alone; Cycle 015 re-tests under frozen v1.3.1 — **frozen 2026-08-03**: pre-registered blind framework reconstruction test complete — fresh-context reader given only the 16 purified objects reconstructed HPF's scheme (all block/field sets MATCH; purpose MATCH; no ABSENT features; only DIVERGENT item: `concepts` mechanism); engineering evaluation: conditional acceptance ("sound guardrails… a specialist would endorse the discipline") — emergence supported; divergence record + freeze-era corrections (concepts/Relationships drift in 2 objects fixed, 3 pass-3 metric-language residuals fixed, certainty/confidence wording harmonized — all revalidated PASS 0/0, no review-cited text altered) in dossier item 5–6 and `blind-reconstruction-014.md`; open items: architecture review (F1 semantics disposition / B8 eligibility / evidence-chain aggregation question / validator referential-rule gap) — **architecture review conducted 2026-08-03** (`research/adversarial-artifact-analysis/architecture-review-014.md`): four-question scope — no primitive deficiency; no destination deficiency demonstrated (**F1 pressure best interpreted as a remit-boundary signal, not an eleventh destination — a programme-level decision recommended by the review, not an experimentally demonstrated fact**; B8 amendment v1.3.2 Scope-and-remit clause drafted, failure-elicited by design under B8 and carrying no independent evidence value — ratification pending; H₁ not falsified under the recommended disposition); no ontology deficiency by F1, but **object-identity assumption elevated to the programme's deepest open problem** (no convergence experiment exists; candidate Cycle 015 domain criterion / G7 pilot); no verdict-pipeline protocol defect, one scope deficiency (unstated epistemic remit) exposed → **B8 amendment path used for the first time**; **Discovery B recorded as B1 + B2** (B1: representation language reconstructible from the corpus alone; B2: **authoring process leaves statistical fingerprints independent of the schema — first-class finding**; **authoring-variation discipline adopted**; count measurements must control authoring-channel confounds); research-question shift made explicit (sufficiency testing → boundary-mapping); Phase-6 semantic-validator item queued; kill-review instrument proposed (final negative gate before Programme B); cycle records immutable — **owner dispositions 2026-08-03 (architecture-review-014 §7)**: **F1 = arm (c) deferral** — neither arm ratified; F1 recorded as an **unresolved architectural tension**; protocol **not amended** (v1.3.2 Scope-and-remit clause remains a draft, unratified); H1 not falsified and not yet narrowed; **Cycle 015 replication criterion pre-registered** — F1 pressure replicating under an independently drawn hostile frame justifies the arm (a)/(b) choice on two independent observations; non-replication makes F1 a frame-specific pressure (arm (b) ratifiable then with stronger justification); **kill review ratified** with four refinements (falsification-probability mission, unrestricted attack surfaces, verdicts K1–K4, mandatory single-experiment answer; instrument frozen — `research/KILL_REVIEW_INSTRUMENT.md`; placement: final negative gate before Programme B); **Cycle 015 ratified as independent decomposition convergence** (renamed from contested-decomposition) — primary endpoint: independent authors decompose the same source material and their object boundaries and relationships converge sufficiently to support stable representation; convergence scoring pre-registered before authoring (exact match / semantic match / split / merge / missing / novel); hostile-domain re-test and v1.3.2 validation are secondary outcomes |
| 015 | Hostile-Domain Falsification Experiment #2 | **Ratified 2026-08-03 as independent decomposition convergence** (primary endpoint: do independent authors' decompositions of the same engineering source converge sufficiently for stable representation; scoring pre-registered before authoring) — **pre-registration ratified 2026-08-03** (`research/decomposition-convergence/CYCLE_015_PREREGISTRATION.md`, v1.1): **domain = APT campaign-level threat analysis**; four frozen instruments (convergence bands ratified as drafted with lexicographic hard gates, independence protocol, blind reconciliation stage as the measurement foundation, interpretation table); "canonical" defined precisely; F1-replication criterion operationalized (semantic-class ESCAPED under an independently drawn frame; frame drawn at pre-registration from the remaining rotation: ontology-first / category-theoretic / MBSE; formal-methods excluded to keep the draw independent); hostile re-test + v1.3.2 evidence = secondary observations | **COMPLETE 2026-08-03 — primary endpoint met: Band B (convergence up to equivalence)** — 58.8% canonical (30/51), 5 split/merge events (9.8%), maximal disagreement at the Hammer boundary (H1 engaged, Band A unreachable), 0 unresolvable; P1 failed (campaign boundary held across all three authors), P2/P3/P4 confirmed; interpretation: object identity is an equivalence structure with recorded tolerance, not a unique partition (owner's predicted outcome); **Phase 3 authored 21 objects** (adjudicated union, all PASS 0/0; corpus 154 → 175); **Phase 4: external-frame review (ontology-first, R1–R5) ESCAPED on all five conditions — semantic-class — F1 REPLICATION CONFIRMED (two independent observations; arm (a)/(b) ratifiable on evidence — arm decision is the owner's ratification point; review retains arm (b) recommendation)**; scorecard: escaped reviews 1 (threshold 0, violated on this instrument); probes T1–T4 all MATCH, decoys D1–D2 not realized; closeout in `research/decomposition-convergence/CYCLE_015_DOSSIER.md`; **post-closeout adjudicator-level audit (2026-08-03): verdict re-confirmed from raw pair files — the band is not an artifact of counting choices; errata corrections recorded in the dossier (exact-only rate corrected to 18/51 = 35.3% across six referents, second maximal disagreement E5 in pair 2v3, R3 restated as structure correspondence); corrections affect numerical accuracy and interpretive precision only — Band B and the primary conclusion unchanged**; post-015 queued: third-party-report replication (R1), dual adjudicators, semantic validator (Phase 6), kill review before Programme B | Closed |
| 016 | External-Validity Replication (R1) | **Highest-priority replication (elevated 2026-08-03)** — decomposition convergence on an unedited third-party incident report (CERT/vendor postmortem; no research-lead involvement in source material); Cycle 015 established internal validity; the principal remaining limitation is external validity from curated source material; two-level test pre-committed: does source-document structure predict the referent set but not boundary placement?; R1 also carries the methodology-terminology hypothesis (do referent/boundary convergence reproduce as measurable phenomena?) — separable outcomes; elevation is a research priority, not a protocol amendment | Not started — queued |

Cycle 008 framing (proposed; pre-registration in the dossier at cycle start): the test question is not "Can ML be represented?" but "Does machine intelligence introduce a new epistemic mode that cannot be decomposed into existing evidence structures?" Proposed tier structure by epistemic pressure: Tier 1 — model uncertainty (confidence calibration, probabilistic outputs, hallucination, uncertainty estimation); Tier 2 — learning systems (training data, generalization, overfitting, distribution shift); Tier 3 — evaluation (benchmark validity, metric selection, human evaluation, alignment); Tier 4 — operational ML (monitoring, drift, retraining decisions, deployment risk).

Cycle 009 framing (proposed; pre-registration in the dossier at cycle start): the test question is "Does transformational knowledge require a new evidence primitive for representing systems that change form while preserving properties?" Compilers attack the biggest remaining untested engineering abstraction: transformation + correctness. A weak schema would invent transformation, proof, algorithm, and rule blocks; HPF must demonstrate composition suffices. Candidate primitive temptations per tier: representation (Tier 1 — AST/IR/semantics stack), transformation (Tier 2 — before/after), proof and equivalence (Tier 3 — correctness), decision complexity (Tier 4 — optimization reality). Pre-registered outcome space: A — composition (constraint preservation + relationship change + observation); B — discovery (transformation as its own reusable relationship motif); C — falsification (vocabulary expansion). Where transformation complexity moves is the migration question: the interesting result is not whether the cycle passes, but where the complexity goes.

Cycle 010 framing (proposed; pre-registration in the dossier at cycle start): the test question is "Does data semantics — the schema as a model of the world, and the guarantees held over it — introduce a new epistemic mode that cannot be decomposed into existing evidence structures?" Databases were selected at the Phase 5 checkpoint for falsification value, not novelty: data is the only untested universal (every prior category consumes data), and the domain re-tests two established resolutions at higher n (transformation via query optimization, validity conditions via schema migration — the unification hypothesis n=3 test). Candidate primitive temptations per tier: data/entity (Tier 1), transaction/atomicity/consistency (Tier 2), query/index (Tier 3), migration/replication/recovery (Tier 4). Attractor-state failure criterion sharpened: the falsification signal is not "a primitive was needed" but "the pressure mapped onto no existing destination" (composition, qualification, constraints, decision structure).

Cycle 010 result: **Pass.** All 19 addendum predictions held; outcome classification 0 Failure / 5 Discovery / 11 Confirmation. The unification hypothesis survived n=3 (schema validity = derivation, joining knowledge validity 008, enabling conditions 009, artifact validity 009). The corpus is now a single cross-domain graph: 6 `analogous_to` links bind databases to the 006/008/009 corpora, and the relational model's direct mapping onto HPF vocabulary (entities/relationships/keys → entities/relationships/constraints) was recorded as coincidence-as-evidence. Cycle 010 answered the pre-registered question in the negative — data semantics is not a new epistemic mode — and left 8 open questions, including whether the unification hypothesis has a boundary and whether the decision-factor count stabilizes at 4. Phase 5 analysis suggested the programme now accumulate L4-relevant evidence only if it leaves engineering; otherwise the next cycle should be selected by falsification value (unmappable-pressure search), not novelty.

Cycle 011 framing (pre-registered in the dossier at cycle start): the test question is "Do hard temporal guarantees — deadlines, schedulability, worst-case execution time — introduce a new epistemic mode that cannot be decomposed into existing evidence structures?" Real-time systems were selected for falsification value, not novelty: the programme has defused temporal temptations four times (005 sequence, 008 drift, 009 ordering, 010 transaction — "constraints bind outcome validity, not duration"), and real-time is the strongest remaining form of the pressure — time as a correctness condition itself, not a qualifier. If deadline/schedulability/WCET resolve through composition, the temporal-trap chain reaches its fifth defusal and the "time is just another constraint dimension" hypothesis strengthens; if the pressure maps onto no existing destination, that is the attractor-state falsification signal. Candidate primitive temptations per tier: time/deadline (Tier 1), scheduling policy (Tier 2), schedulability guarantee (Tier 3), overload/isolation (Tier 4).

Cycle 011 result: **Pass.** All 19 addendum predictions held; outcome classification 0 Failure / 3 Discovery / 13 Confirmation. The fifth temporal defusal completed the theory: deadline = validity condition on completion, and the unification hypothesis reached n=5 (knowledge validity 008, enabling conditions 009, artifact validity 009, schema validity 010, completion validity 011). WCET resolved as observation with confidence ("the strongest guarantee in real-time rests on an estimate"); priority-inversion — the pre-registered danger object — resolved as failure mode + priority-ordering invariant + mitigation pattern, no concurrency-failure primitive. The temporal-constraint-density observation dimension discriminated cleanly (constraints 100% time-bounded all tiers; edges 40–45%), and the guarantee-object motif reached n=4. Outcome space: outcome A dominant, outcome B occurred (arbitration motif candidate), outcome C absent. Cycle 011 left 8 open questions, including whether the unification hypothesis has a boundary, whether the decision-factor count at 4 stabilizes, and whether the three motif candidates (arbitration, isolation, prediction-object) survive to catalogue entry.

Cycle 012 framing (pre-registered in the dossier at cycle start): the test question is "Do engineering systems whose knowledge depends on continuous interaction with an external physical world require additional evidence structures beyond those already observed?" — sharpened to "Can HPF represent knowledge whose truth is never directly observable, but only inferred through layered models?" Robotics was selected at the Cycle 012 review as the compound stress test: it combines nearly every validated pressure (temporal 011, uncertainty 007/008, arbitration 006/010/011, bounded response 006, guarantees 009/010/011) and adds two never-tested pressures — continuous dynamics and epistemic separation (the system's knowledge is never directly observable: World → Sensors → Noise → Estimator → Belief → Decision → Actuation). The central hypothesis: the real novelty is not continuity but **indirect knowledge of reality**. Estimation is pre-registered as the highest-risk pressure (observation about a model's best belief, not about reality — no estimate primitive); safety case as the fifth verification-family member (joining equivalence-checking, formal-verification, benchmark-validity, schedulability-analysis); stability as verification pattern (demonstrated, not claimed); autonomy as decision under an incomplete world model (generating options, not choosing predefined ones). P5 (pre-registered by the research lead): the greatest pressure is epistemic separation, not continuous mathematics — expected resolution Reality → Observation → Qualified observation → Claim → Decision, no new primitive. New programme-wide observation metric: **Epistemic Distance** (inferential layers between a claim and directly observable reality; generalizes to ML/economics/medicine). Candidate primitive temptations per tier: state/signal (T1), perception/estimation (T2), control/stability (T3), safety-case/argument and autonomous-decision (T4).

Cycle 012 result: **Pass.** 16/16 objects PASS 0/0; 0 failures, 3 discoveries (P5 at maximum depth; Epistemic Distance gradient 1→3+ measured without schema change; the Epistemic Chain closing into the Closed Epistemic Loop watch); 13 confirmations; all 20 addendum predictions held. The verification family candidate reached n=6, the guarantee motif n=5, the prediction-object family n=4; the arbitration candidate re-tested at n=4 and not promoted; decision-factor count held at 13 × 4. Primary Endpoint reached: epistemic separation maps onto existing destinations (outcome A) with outcome B elements (loop watch); outcome C absent. Temporal Constraint Density discriminated within the category (model 25%/15%, junction 37.5%/20%, belief/decision 0%/5%) — the 011 dilution pattern reproduced. Cycle 012 left 8 open questions, led by the closeout review's finding: **destination bias** — the research beginning to optimize itself. The closeout review adopted three protocol changes: the adversarial-review control (cycle-closeout requirement), the strengthened Phase 5 criterion (attempted-falsification intensity recorded), and the motif maturity gate (engineering must not mature engineering motifs; a genuinely different epistemology — mathematical proof, clinical evidence, legal burden — is required before maturity).

Cycle 013 framing (adopted at the Cycle 012 closeout follow-up review; dossier in `research/protocol-hardening/`): the research-lead review identified five methodological issues — (1) adversarial review still internal (a reviewer inside the HPF framework cannot escape HPF's assumptions); (2) destination bias reduced, not eliminated (specific predictions make the destination visible during authoring); (3) cycle success remains binary ("0 primitives" without quality measures); (4) Programme B transition criteria implicit; (5) motif candidates lack statistical discipline (appearance counts without recurrence/independence/discriminative-power/counterexample-search requirements). Cycle 013 authors no objects; it adopts amendments A1–A5: the external-frame adversarial review (rotating competing philosophies — ontology-first, category-theoretic, formal-methods, MBSE — with CONTAINED/DISMISSED/ESCAPED outcomes), the prediction specificity control (coarse H-level expectations vs sealed F-probes + counter-probes + forced-fit audit), the non-binary cycle scorecard (forced-fit incidents, unresolved pressures, adversarial challenge strength, explanation simplicity; prospective from Cycle 014 — Cycle 012 is not retro-scored on hindsight-bias grounds), the explicit Programme B entry gates (G1–G6: two hostile domains, two distinct-frame reviews, no recurring escape pressure, scorecard thresholds, counterexample registers, decision-factor anomaly search), and the motif promotion gate (recurrence ≥ 5 across ≥ 3 independent domains, discriminative power, failed counterexample search, no ESCAPED review; maturity still deferred to the Programme B epistemology gate). The amendments received their own adversarial pass at adoption (all CONTAINED/DISMISSED, none ESCAPED).

Round 2 (B1–B8, v1.3 — judgment independence): the follow-up review scored the protocol 9.7/10 and identified the remaining gap as judgment dependence — controls must be executable and evaluable by another researcher with minimal subjective interpretation. B1 — frozen evaluation rubrics per frame, pre-registered before the argument exists, verdicts applied mechanically (the rubric belongs to the frame, not HPF); B2 — objective verdict conditions (ESCAPED iff any of: cannot answer with current ontology / undocumented assumption / new primitive or kind / scope narrowing changing the claim / contradicts a previous cycle); B3 — scorecard split into objective metrics (forced-fit incidents, unresolved pressures, vocabulary additions, escaped reviews) and descriptive metrics (challenge strength, confidence), never aggregated; B4 — A/B probe comparison replaces introspection (blind authoring vs revealed probes, recorded MATCH/MISMATCH diff, decoy probes per tier, destination-bias flag = MATCH on true probes where alternatives plausibly exist); B5 — G7 epistemic-discontinuity pilot (4-object medicine/biology probe under full protocol before Programme B — engineering stress does not substitute for a change in epistemology); B6 — counterexample search strategy (search space, inclusion criteria, stopping criterion, justification; strategy-less registers are blocks); B7 — randomized frame rotation (seeded, coverage-guaranteed, order unpredictable); B8 — the Protocol Stability Principle: the protocol is presumed stable as of v1.3; future amendments require an experiment-validated deficiency, not a theoretical improvement. The B-series survived its own adversarial pass (all CONTAINED/DISMISSED).

Cycle 014 framing (design adopted at the Cycle 012 closeout review; domain selected and pre-registration completed at the pre-Cycle-014 review under the frozen protocol v1.3.1; dossier in `research/adversarial-artifact-analysis/`): the test question is the strongest remaining falsification form — "Is there an engineering category where HPF's existing complexity destinations are *insufficient*, not merely unused?" Cycle 014 is a **hostile-domain falsification experiment** — Hostile-Domain Falsification Experiment #1 — chosen by the assumption-violation criterion (which domain breaks the most assumptions previous cycles quietly relied upon), not by adversary flavor. **Domain ratified: Adversarial Artifact Analysis** — reverse engineering of obfuscated/packed binaries, firmware analysis, and forensic reconstruction as *instances*; the epistemic change is that the researcher's own knowledge becomes fundamentally inferential (same-status with the modelled system's knowledge): the modeler is inside the chain, and the chain's ground truth is intentionally inaccessible. Rejected at ratification: deception-focused operations (the corpus already expresses deception-shaped knowledge — Cycle 007's `incomplete-evidence` uses relationship verbs `blinds`/`distorts`; deception changes content, not epistemic structure), distributed AI agent ecosystems (partially a composition of 006 + 008), autonomous multi-agent coordination (consensus/arbitration re-tests), human-in-the-loop safety-critical systems (edges toward Programme B / G7 territory). The cycle's pressures: concealed semantics, confidence anchored to interpretive inference (the confidence object shifts a third time: observation → belief → interpretation-of-inference), competing hypotheses, iterative refinement, recovered intent, epistemic symmetry (the Closed Epistemic Loop watch comes due in the open), decisions under incomplete reconstruction (G6 decision-factor anomaly search pre-registered). The cycle runs under the full hardened protocol: external-frame adversarial review (A1 — frame drawn by seeded PRNG at pre-registration, before any object existed: **Formal-methods / model-theoretic**, F1–F5 rubric; the A-1 defect correction makes F1's truth-conditions pressure non-overridable), sealed F-probes + decoys + counter-probes + forced-fit audit (A2), cycle scorecard (A3), residual pressures entries. Success criterion unchanged (16 objects PASS, 0 primitives); the falsification signal is a pressure escaping every existing destination that survives the adversarial reviews (internal and external-frame) — the attractor-state criterion. If HPF compresses a deliberately hostile category without new primitives, that is a stronger engineering endpoint than another conventional domain — and the Programme B gates (A4) follow.

---

## End-of-Cycle Question

After every cycle, ask:

> **What recurring engineering concept would have forced a tenth evidence primitive?**

If the answer is:

> None.

Then ask:

> **Why were the existing primitives sufficient?**

The second question is as valuable as the first — it encourages explanation instead of merely recording absence. Both answers together constitute the primary research result for the cycle.

---

## Out of Scope

This research programme does not attempt to demonstrate:

- that HPF is the only valid knowledge representation
- that the current evidence primitives are universally optimal
- that all human knowledge shares the same evidence structure
- that presentation formats should be eliminated

The research is limited to evaluating whether engineering knowledge requires additional evidence primitives.

---

## Working Theory

If H₁ continues to withstand attempts at falsification, the most likely explanation is that engineering disciplines share a common evidence structure despite differing subject matter.

This theory remains provisional and is not itself validated by the current research programme.

---

## Design Philosophy

HPF assumes that increasing knowledge should increase the richness of the knowledge graph rather than the complexity of the representation language.

The burden of proof is therefore on architecture expansion, not on composition.

---

## What a Completed Research Programme Looks Like

If the research programme continues to support H₁, a possible contribution would be, approximately:

> Engineering disciplines differ in subject matter, but they are remarkably similar in how reliable knowledge is justified, connected, constrained, and operationalized. HPF's atomic evidence schema works because it models that shared epistemic structure rather than the vocabulary of any particular field.

The observable invariant that supports this claim:

> Knowledge diversity increased while the evidence vocabulary remained constant.
