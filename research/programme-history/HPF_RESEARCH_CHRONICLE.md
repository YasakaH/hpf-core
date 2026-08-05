# HPF Research Chronicle — Cycles 001–013

## Purpose and Provenance

This document is the **complete chronological research log** of the Hierarchical Provenance Framework (HPF) research programme, Cycles 001 through 011. It is a laboratory notebook, not a summary: every cycle is documented separately, in order, with its pre-registration (where the protocol existed), its objects, its pressure events, its discoveries, and its near-failures.

**Provenance rules:** The pre-registration discipline (predictions recorded *before* authoring) was introduced incrementally. Cycle 005 recorded the first formal pressure predictions; Cycle 006 introduced the full pre-registration dossier protocol; Cycles 007 and 008 pre-registered complete hypotheses, pressure predictions, and tier structures, with additional predictions recorded immediately before each tier's authoring. For Cycles 001–004, the chronicle records what the surviving artifacts (dossiers, cycle summaries, schema friction logs) actually contain, and marks the absence of pre-registration explicitly. Predictions are never reconstructed from outcomes.

**Primary sources:** per-cycle dossiers, per-cycle cycle-summaries, schema friction logs (from Cycle 004), PROGRAMME_STATE.md, the knowledge corpus (`tools/hpf-engine/domain/knowledge/`), and validator output.

**Definitions used throughout:**
- **Evidence vocabulary**: the 9 primitives (Claims, Relationships, Constraints, Observations, Trade-offs, Failures, Heuristics, Recommendations, Decision Factors).
- **Object kind**: the identity-layer type (concept, principle, pattern, decision).
- **Falsification**: a recurring engineering concept that cannot be represented, recurs across independent objects, cannot be resolved through composition, and requires a new evidence primitive.

---

# Cycle 001 — Browser State

*Date: 2026-07-29. Experimental target: Deterministic (pilot). Knowledge category: Deterministic.*

## 1. Research Objective

- **Original hypothesis**: Browser state knowledge — lifecycle, transitions, observability — can be captured in reusable knowledge structures for automation reliability.
- **Falsification question (implicit, no formal pre-registration existed)**: Can browser state concepts be represented at all in the early HPF object format?
- **Why this domain**: Browser State is the foundational domain for automation reliability — "every automation failure is ultimately a state management failure." Navigation lifecycle, session lifecycle, readiness models, failure modes, and state observability across CDP and WebDriver.
- **Expected pressure points**: None formally recorded. The cycle's actual bottleneck emerged post-hoc: prose-heavy knowledge objects.
- **What would have caused failure**: The object format proving unusable for expressing state lifecycle knowledge.

## 2. Pre-registration

**No pre-registration existed for Cycle 001.** The protocol had not yet been established. The dossier was authored as a domain survey; pressure predictions were not recorded before authoring.

## 3. Domain Objects Created

### navigation-lifecycle (concept)
- **Purpose**: Page-level lifecycle states and transitions (W3C Page Lifecycle + Chromium events: DOMContentLoaded, load, networkIdle).
- **Why selected**: The load-vs-networkIdle gap is the most common source of flaky automation.
- **Expected schema pressure**: Not recorded.
- **Actual representation**: Canonical (pre-atomic-schema) format — prose under headings.
- **Blocks used**: None (legacy format; does not conform to the atomic evidence schema).
- **Relationships introduced**: None recorded in schema form.
- **Validation**: FAIL (against the later atomic schema: "No atomic evidence blocks found").

### browser-readiness-model (concept)
- **Purpose**: Competing definitions of "ready" (DOM interactive, load, network idle, first paint, custom signals) and framework auto-wait strategies (Playwright, Selenium, Puppeteer, CDP).
- **Why selected**: Readiness is where automation tools differ most; the concept powers explain/decide modes.
- **Expected schema pressure**: Not recorded.
- **Actual representation**: Canonical format.
- **Blocks used**: None (legacy format).
- **Validation**: FAIL (against the later atomic schema).

### session-lifecycle-concept (expanded, not new)
- Expanded from 18 to 100 lines with failure-mode taxonomy (target crash, session detach, zombie sessions, memory pressure, process exit) and CDP observability mapping.
- **Validation**: FAIL (legacy format retained in corpus).

## 4. Primitive Pressure Analysis

None recorded. The cycle predates the primitive-pressure tracking protocol. No candidate primitives were considered or rejected in the surviving record.

## 5. Schema Interaction

```
Schema changed:      NO  (no atomic schema existed yet; format was in flux)
Parser changes:      NO
Validator changes:   NO
Analyzer changes:    NO
Friction:            Quality friction — objects were "still too prose-heavy; not all modes can consume without inference" (cycle summary, Quality Assessment: Medium)
```

## 6. Relationship Growth

Not tracked in this cycle (pre-schema).

## 7. Qualification Growth

Not tracked. The qualification metric was introduced in Cycle 007.

## 8. Object Kind Evolution

Kinds used this cycle: concept (2 objects). No new kinds. Cumulative: **1** (concept).

## 9. Discoveries

**Discovery 1 — The knowledge-object bottleneck.**
- Initial assumption: dossier → concept → object pipeline would flow naturally.
- Evidence: Cycle summary quality assessment — dossier-to-concept conversion "works well"; concept-to-object conversion "produces rich but prose-heavy files."
- Final understanding: HPF knowledge objects are the pipeline bottleneck.
- Impact on HPF theory: Set the Cycle 002 quality bar — objects must be directly consumable by each reasoning mode without engine inference.

## 10. Failed Hypotheses / Near Failures

- **Near failure**: The object format nearly failed its own purpose (consumability). Recovered by raising the quality bar rather than changing the schema — the first instance of the pattern *fix the representation discipline, not the vocabulary*.
- **Unresolved**: 10 open questions recorded (heartbeat intervals, cross-browser lifecycle events, WebDriver BiDi observability, memory pressure events, frame-detach semantics).

## 11. Validation Evidence

| Metric | Value |
|---|---|
| Objects created | 2 (both legacy format) |
| Passing objects (cumulative) | 0 |
| Corpus (cumulative) | 21 |
| Warnings | 0 |

## 12. End-of-Cycle Interpretation

- **What increased**: Domain knowledge (dossier), canonical concepts (2 added, 1 expanded).
- **What stayed constant**: The (proto-)vocabulary — no new structures were introduced to fix the quality problem.
- **Where did complexity move**: Into the object format's prose — which is precisely what the next cycle fixed.
- **Did vocabulary expand**: No.
- **Did the graph become richer**: Weakly — objects existed but were not machine-consumable.

---

# Cycle 002 — Browser Memory / Profiles

*Date: 2026-07-29. Experimental target: Deterministic. Knowledge category: Deterministic.*

## 1. Research Objective

- **Original hypothesis**: Persistent state (profiles, storage, caches), runtime memory pressure (OOM, tab discard, GC), and the fingerprinting surface of persistent identifiers can be captured in structured knowledge objects.
- **Falsification question (implicit)**: Can HPF objects be made directly consumable by each reasoning mode?
- **Why this domain**: The second foundational domain — State governs a session; Memory governs what survives across sessions.
- **Expected pressure points**: The Cycle 001 finding (prose bottleneck) was the declared pressure: structured fields per mode.
- **What would have caused failure**: Inability to structure objects so reasoning modes consume them without inference.

## 2. Pre-registration

**No formal pre-registration.** The quality bar was pre-declared in the dossier's "Implications for HPF": each object must expose structured fields per mode — definition/properties/mechanics (Explain), comparison criteria/tradeoff tables (Compare), failure modes with typed fields (Troubleshoot), approaches/pitfalls/best practices (Design), decision factors with weights (Decide).

## 3. Domain Objects Created

### browser-storage (concept)
- **Purpose**: Storage mechanisms (cookies, localStorage, IndexedDB, Cache API, HTTP cache) with scope, persistence, capacity, accessibility.
- **Why selected**: Storage is the persistence vector for tracking, auth, and supercookie fingerprinting.
- **Actual representation**: Canonical (legacy) format.
- **Blocks used**: None (legacy).
- **Validation**: FAIL (legacy format).

### memory-pressure (concept)
- **Purpose**: Memory pressure signals (tab discard, renderer OOM, Performance.metrics, DOM counters) and failure taxonomy.
- **Why selected**: Memory pressure is invisible until crash; detection is the real challenge.
- **Actual representation**: Canonical format.
- **Blocks used**: None (legacy).
- **Validation**: FAIL (legacy format).

### browser-profiles-concept (expanded — retrofitted to schema)
- Expanded 18 → 170 lines as the first atomic-schema object.
- **Blocks used**: Claims, Relationships, Tradeoffs, Failure Modes, Decision Factors, Observations, Constraints, Heuristics, Recommendations (all 9).
- **Relationships introduced**: contains, influences (profile → fingerprint persistence).
- **Decision factors used**: Present (profile reuse decision, e.g. fresh vs persistent profile).
- **Validation**: PASS 0/0 — the programme's first passing object.

## 4. Primitive Pressure Analysis

None recorded. The cycle's pressure was representational discipline (structured fields), not vocabulary.

## 5. Schema Interaction

```
Schema changed:      NO
Parser changes:      NO
Validator changes:   NO
Analyzer changes:    NO
Friction:            Authoring friction — structured fields added ~2x development time per object
Rejected changes:    None proposed
```

## 6. Relationship Growth

First typed relationships appear (contains, influences). Complexity moved from prose into structured fields — a graph-format improvement, not a vocabulary change.

## 7. Qualification Growth

Not yet tracked (metric introduced Cycle 007).

## 8. Object Kind Evolution

Kinds used: concept. No new kinds. Cumulative: **1**.

## 9. Discoveries

**Discovery 1 — Structured fields eliminate the inference gap.**
- Initial assumption (from Cycle 001): quality was a prose problem.
- Evidence: browser-profiles-concept passed validation as the first schema-native object; each field maps to a reasoning mode's expected input.
- Final understanding: the format was the bottleneck, not the vocabulary.
- Impact on HPF theory: established the "objects are consumed, not read" principle that shaped the atomic evidence schema.

**Discovery 2 — Fresh profiles' detection advantage is state absence, not fingerprint uniqueness.**
- Evidence: canvas/WebGL fingerprints vary by hardware, not profile; the decisive difference is the absence of tracking cookies and state.
- Impact: reframed anti-detection guidance before the anti-detection cycle existed.

## 10. Failed Hypotheses / Near Failures

- **Near failure (carried from 001)**: prose objects — fixed by the structured-field bar.
- **Rejected approach**: richer prose under headings (rejected after Cycle 001).
- **Unresolved**: 9 open questions (headless Memory Saver behaviour, CDP Memory domain in incognito, cross-engine profile formats, supercookie survival across "clear data", per-target memory overhead, pre-crash OOM detection, service worker interference).

## 11. Validation Evidence

| Metric | Value |
|---|---|
| Objects created | 2 (legacy) + 1 retrofitted (PASS) |
| Passing objects (cumulative) | 1 |
| Corpus (cumulative) | 21 |
| Warnings | 0 |

## 12. End-of-Cycle Interpretation

- **What increased**: Structured fidelity of objects; the passing-object count moved 0 → 1.
- **What stayed constant**: Vocabulary.
- **Where did complexity move**: Into structured fields within objects (format maturity).
- **Did vocabulary expand**: No.
- **Did the graph become richer**: Yes — typed, consumable relationships began.

---

# Cycle 003 — Browser Perception / Detection

*Date: 2026-07-29. Experimental target: Deterministic. Knowledge category: Probabilistic-adjacent (adversarial) within the deterministic series.*

## 1. Research Objective

- **Original hypothesis**: Detection surface, fingerprinting, and anti-detection strategy knowledge can be captured in schema-native objects.
- **Falsification question (implicit)**: Can the atomic evidence schema represent an adversarial, probabilistic-adjacent domain from creation?
- **Why this domain**: "The most adversarial domain — detection is an arms race... detection is never binary, and evasion is never permanent."
- **Expected pressure points**: Not formally pre-registered. The dossier's declared need: three new canonical concepts (automation-detection-surface, browser-fingerprint, anti-detection-strategy).
- **What would have caused failure**: Schema unable to represent probabilistic detection signals.

## 2. Pre-registration

**No formal pre-registration.** What was recorded before authoring: the three canonical concepts required, and benchmark impact mapping (6 benchmark questions).

## 3. Domain Objects Created

### automation-detection-surface (concept)
- **Purpose**: The complete set of observable signals distinguishing automated from human-driven sessions (JS properties, CDP/WebSocket signals, process/environment signals).
- **Why selected**: Detection surface is the unit of adversarial knowledge.
- **Actual representation**: Schema-native from creation.
- **Blocks used**: All 9 (incl. Decision Factors).
- **Relationships introduced**: composes, modifies, determines, amplifies, varies_with.
- **Failure modes captured**: Yes (detection taxonomy as failure surface).
- **Validation**: PASS 0/0, first try.

### browser-fingerprint (concept)
- **Purpose**: Persistent identity from browser/device characteristics independent of cookies (canvas, WebGL, audio, fonts, resolution, timezone).
- **Why selected**: Fingerprint consistency links sessions; the hard dimension of anti-detection.
- **Actual representation**: Schema-native.
- **Blocks used**: All 9.
- **Relationships introduced**: derived_from, targeted_by, amplified_by, persists_via, established_at.
- **Validation**: PASS 0/0, first try.

### anti-detection-strategy (concept)
- **Purpose**: Techniques for reducing detection risk, mapped to detection signals and their maintenance burden.
- **Why selected**: The decision layer over the detection surface.
- **Actual representation**: Schema-native.
- **Blocks used**: All 9.
- **Relationships introduced**: modifies, manipulates, constrained_by, profile_strategy, timing_dependent.
- **Validation**: PASS 0/0, first try.

### browser-profiles-concept (re-validated as proof of concept)
- **Validation**: PASS 0/0 (retrofit PoC confirmed).

## 4. Primitive Pressure Analysis

None recorded. The adversarial content (probabilistic detection, arms race) did not tempt a vocabulary extension in the surviving record. The schema handled it from creation.

## 5. Schema Interaction

```
Schema changed:      NO
Parser changes:      NO
Validator changes:   NO
Analyzer changes:    NO
Friction:            None
Rejected changes:    None
```

## 6. Relationship Growth

First schema-native relationship motifs appear (modifies, composes, targeted_by, persists_via). Complexity moved into typed relationships.

## 7. Qualification Growth

Not yet tracked.

## 8. Object Kind Evolution

Kinds used: concept. No new kinds. Cumulative: **1**.

## 9. Discoveries

**Discovery 1 — Schema-native objects pass on first creation; retrofits don't.**
- Evidence: 3/3 schema-native objects passed first try; the retrofit (002) required design iteration.
- Impact: justified the Phase 3 bulk-refactor plan for legacy objects.

**Discovery 2 — The detection arms race is a risk-management problem, not a technical one.**
- Initial assumption: anti-detection is a patching problem.
- Evidence: effective techniques are infrastructure-level (IP quality, TLS fingerprints); browser-level JS patching has a 3–9 month detection half-life.
- Impact: reframed the domain for HPF object content; the risk framing later anticipated Cycle 007's security treatment.

## 10. Failed Hypotheses / Near Failures

- **Unresolved**: 10 open questions — most notably whether behavioural detection is practically deployed (later resolved as yes by industry practice, not by HPF).
- **Noted**: stealth-patch half-life (3–9 months) as a knowledge-decay fact — an early, informal seed of the validity-conditions idea formalized in Cycle 008.

## 11. Validation Evidence

| Metric | Value |
|---|---|
| Objects created | 3 (all schema-native, all PASS first try) |
| Passing objects (cumulative) | 4 |
| Corpus (cumulative) | 23 |
| Knowledge compression ratio | dossier 284 lines → concepts 243 (0.86:1) → objects 528 (1.86:1 expansion — intended, adds structure) |
| Warnings | 0 |

## 12. End-of-Cycle Interpretation

- **What increased**: Schema-native object count; relationship structure.
- **What stayed constant**: Vocabulary, parser, validator, analyzer.
- **Where did complexity move**: Into typed relationships and structured blocks.
- **Did vocabulary expand**: No.
- **Did the graph become richer**: Yes — first fully structured objects, all 9 blocks.

---

# Cycle 004 — Browser Architecture / Protocols

*Date: 2026-07-30. Experimental target: Deterministic. Knowledge category: Deterministic.*

## 1. Research Objective

- **Original hypothesis**: Protocol knowledge (CDP, WebDriver Classic, BiDi) — a design-space domain of tradeoffs — is representable in the schema.
- **Falsification question (implicit)**: Can a *comparison/design-space* domain fit the schema's Tradeoffs and Decision Factors without new constructs?
- **Why this domain**: Architecture is a design-space problem: each protocol trades capability, standardisation, detectability, session model. Protocol choice is "the most important anti-detection decision."
- **Expected pressure points**: Tradeoff density — the dossier predicted heavy use of Tradeoffs and Decision Factors.
- **What would have caused failure**: A comparison-heavy domain requiring a new comparison primitive.

## 2. Pre-registration

**No formal pre-registration.** Pre-declared in the dossier: zero new canonical concepts (existing `automation-protocol` covers the landscape), three knowledge objects required (automation-protocol, cdp-mechanics, webdriver-classic).

## 3. Domain Objects Created

### automation-protocol (concept)
- **Purpose**: The protocol landscape (CDP, WebDriver Classic, BiDi) with comparison matrix, session models, execution isolation, migration trajectory.
- **Why selected**: The protocol abstraction is the design-space core.
- **Actual representation**: Schema-native.
- **Blocks used**: All 9.
- **Relationships introduced**: defines, determines, influences, specialises (protocol hierarchy).
- **Decision factors used**: Protocol selection decision factors.
- **Failure modes captured**: Protocol-specific connection/version failures.
- **Validation**: PASS 0/0.

### cdp-mechanics (concept)
- **Purpose**: CDP specifics — domains, commands, events, detection surface, session model.
- **Why selected**: CDP is the current standard; deepest protocol detail.
- **Actual representation**: Schema-native.
- **Blocks used**: All 9.
- **Relationships introduced**: specialises, exposes, controls, contrasts_with.
- **Validation**: PASS 0/0.

### webdriver-classic (deferred, not created)
- **Why deferred**: "covered by automation-protocol" — an object-boundary decision; the first recorded boundary arbitration.
- **Validation**: N/A.

## 4. Primitive Pressure Analysis

The comparison domain was the candidate pressure: "protocol comparison" could plausibly have demanded a dedicated comparison primitive. **It did not** — the existing Tradeoffs and Decision Factors blocks absorbed the entire comparison dimension. This is the first recorded instance of a structural temptation resolved by existing primitives.

## 5. Schema Interaction

```
Schema changed:      NO
Parser changes:      NO
Validator changes:   NO
Analyzer changes:    NO
Friction:            0 events — the Schema Friction Log was introduced this cycle as a measurement instrument
Rejected changes:    None
```

## 6. Relationship Growth

Relationship motifs: specialises (hierarchy), contrasts_with (comparison), exposes, controls. Comparison moved into Tradeoffs + Decision Factors + relationships — graph structure, not vocabulary.

## 7. Qualification Growth

Not yet tracked.

## 8. Object Kind Evolution

Kinds used: concept. No new kinds. Cumulative: **1**.

## 9. Discoveries

**Discovery 1 — The schema is proven stable across three cycles (002–004), 6 objects.**
- Evidence: 6 objects pass, 0 modifications to schema/parser/validator/analyzer, 0 friction events.
- Impact: declared sufficient evidence that the schema generalises beyond its initial domain; motivated the orthogonal-domain test (Cycle 005).

**Discovery 2 — Protocol migration (CDP → BiDi) is the dominant architectural trend.**
- Impact: objects document the trajectory; the decision frameworks help practitioners choose per requirement.

## 10. Failed Hypotheses / Near Failures

- **Rejected approach**: a separate webdriver-classic object (merged into automation-protocol) — recorded boundary arbitration.
- **Unresolved**: 10 open questions (BiDi detection profiling, world-isolation performance, CDP domain exclusivity, Firefox BiDi signals, port-binding security, containerised deployments).

## 11. Validation Evidence

| Metric | Value |
|---|---|
| Objects created | 2 (both PASS first try) |
| Passing objects (cumulative) | 6 |
| Corpus (cumulative) | 27 |
| Warnings | 0 |

## 12. End-of-Cycle Interpretation

- **What increased**: Confidence in schema generalisation; comparison knowledge.
- **What stayed constant**: Vocabulary and all four instrument components.
- **Where did complexity move**: Into Tradeoffs, Decision Factors, and typed relationships.
- **Did vocabulary expand**: No.
- **Did the graph become richer**: Yes — first tradeoff-dense objects.

---

# Cycle 005 — Networking

*Date: 2026-07-30. Experimental target: Deterministic Infrastructure. Knowledge category: Deterministic (layered/emergent).*

## 1. Research Objective

- **Original hypothesis**: A domain orthogonal to browser internals — layered, emergent networking infrastructure — is representable without schema change. L2 test: "the schema generalises beyond browser automation."
- **Falsification question**: Does an orthogonal infrastructure domain require domain-specific structures?
- **Why this domain**: Networking is the substrate of all browser automation (TCP carries CDP WebSockets; TLS encapsulates HTTPS; HTTP carries page loads; proxies mediate). It is layered, emergent, temporal — deliberately different from browser-internal domains.
- **Expected pressure points**: Pre-registered in the dossier (first formal pressure predictions):

| Pressure Point | Prediction |
|---|---|
| Structural (multi-layer) | Low risk — Relationships can capture layer dependencies |
| Systemic (emergent behaviour) | Medium risk — may require multiple objects referencing each other |
| Temporal (sequences) | Medium risk — sequences must be declarative, not procedural |
| Granularity | Low risk — networking boundaries match object boundaries |

- **What would have caused failure**: Any of the above converting into a schema requirement.

## 2. Pre-registration

**First formal pressure predictions** (table above), recorded in the dossier before authoring. No full hypothesis pre-registration yet.

## 3. Domain Objects Created

### tcp-tls-foundation (concept)
- **Purpose**: TCP connection lifecycle, port/TIME_WAIT management, TLS 1.3 handshake, TLS fingerprinting.
- **Why selected**: The transport/security substrate — every automation session depends on it.
- **Actual representation**: Schema-native; temporal handshake expressed declaratively as claims + observations.
- **Blocks used**: 8 (no Decision Factors — intentional: not a decision domain).
- **Relationships introduced**: underlies, interacts_with, source_of, transports, contributes_to.
- **Failure modes captured**: Port exhaustion, Nagle delay, keep-alive staleness, fingerprint mismatch, 0-RTT replay.
- **Validation**: PASS 0/0.

### http-protocol (concept)
- **Purpose**: HTTP/1.1 vs HTTP/2, request lifecycle, status categories, retry semantics, idempotency.
- **Why selected**: The dominant application protocol for page loads and APIs.
- **Blocks used**: 8 (no Decision Factors — intentional: HTTP selection is infrastructure-determined, not per-task).
- **Relationships introduced**: runs_over, traverses, triggers, distinct_from, contributes_to.
- **Failure modes captured**: 4xx/5xx handling, retry storm exposure, idempotency violations.
- **Validation**: PASS 0/0.

### proxy-infrastructure (concept)
- **Purpose**: Proxy types, forwarding behaviour, failure modes, detection impact.
- **Why selected**: Proxies mediate every client-server interaction; detection-critical.
- **Blocks used**: 8.
- **Relationships introduced**: terminates, forwards, introduces, affects, influenced_by.
- **Failure modes captured**: Connection timeout, TLS interception, rate limiting, pool exhaustion, protocol mismatch.
- **Validation**: PASS 0/0.

### network-failure-propagation (concept)
- **Purpose**: Cross-layer failure cascades, retry semantics, connection pooling, retry storms.
- **Why selected**: The emergent, systemic face of networking.
- **Blocks used**: 8.
- **Relationships introduced**: originates_from, manifests_as, amplifies, mitigates, informs.
- **Failure modes captured**: Retry storm, cascading timeout, congestion collapse.
- **Authoring friction**: Highest in the cycle — system-level phenomena with multiple causality paths required heavy cross-referencing (recorded as authoring friction, not representation friction).
- **Validation**: PASS 0/0.

## 4. Primitive Pressure Analysis

- **Candidate: temporal/sequence primitive.** Why it looked necessary: TCP and TLS handshakes are sequences. How it was tested: expressed declaratively — claims + observations. Why rejected: "temporal sequences in networking are deterministic and well-known, so they fit Claims naturally." Final representation: declarative claims, no workflow/sequence construct. **First formal rejection of a candidate primitive.**

## 5. Schema Interaction

```
Schema changed:      NO
Parser changes:      NO
Validator changes:   NO
Analyzer changes:    NO
Friction:            Minor (systemic multi-object reference; authoring friction on network-failure-propagation) — recorded, not escalated
Rejected changes:    Workflow/sequence block (temporal primitive) — rejected, see above
```

## 6. Relationship Growth

New motifs: underlies, runs_over, originates_from, manifests_as, amplifies, mitigates, transports. Complexity moved into cross-object reference: network-failure-propagation references tcp-tls-foundation, http-protocol, proxy-infrastructure. **First evidence that emergent behaviour is multi-object by nature — composition, not vocabulary.**

## 7. Qualification Growth

Not yet tracked.

## 8. Object Kind Evolution

Kinds used: concept (4). No new kinds. Cumulative: **1**.

## 9. Discoveries

**Discovery 1 — The schema models technical systems, not browser automation.**
- Initial assumption (L2 null): maybe the schema just encodes browser-internal structure.
- Evidence: an orthogonal, layered, emergent domain passed with 0 changes.
- Final understanding: the 9 blocks model *technical systems*.
- Impact: L2 hypothesis status moved to **Supported**; L3 (any abstraction level) declared the next test.

## 10. Failed Hypotheses / Near Failures

- **Near miss**: systemic emergent behaviour (retry storms) — the cycle's summary records it as the closest thing to friction so far, resolved by multi-object composition. Deliberately recorded, not escalated (per the then-emerging friction policy).
- **Unresolved**: 10 open questions (TLS fingerprint databases, failure-mode distributions, HTTP/2 prioritisation divergence, port-consumption rates, proxy TLS consistency, framework retry behaviour, CDN interaction).

## 11. Validation Evidence

| Metric | Value |
|---|---|
| Objects created | 4 (all PASS first try) |
| Passing objects (cumulative) | 10 |
| Corpus (cumulative) | 27 |
| Warnings | 0 |
| Instrument stability | Schema/parser/validator/analyzer unchanged across 4 cycles |

## 12. End-of-Cycle Interpretation

- **What increased**: Cross-object relationships; domain coverage (first non-browser domain).
- **What stayed constant**: Vocabulary and instruments.
- **Where did complexity move**: Into multi-object composition (systemic) and declarative claims (temporal).
- **Did vocabulary expand**: No.
- **Did the graph become richer**: Yes — first emergent-behaviour graph (cascade networks).

---

# Cycle 006 — Distributed Systems

*Date: 2026-07-30. Experimental target: Systemic Knowledge Test. Knowledge category: Systemic.*

## 1. Research Objective

- **Original hypothesis**: Systemic knowledge — emergence, partial information, coordination, consistency tradeoffs — is representable without schema change. L3 test: *any abstraction level*.
- **Falsification question**: Does systemic (emergent) engineering knowledge require primitives that deterministic knowledge did not?
- **Why this domain**: First fundamentally different knowledge category after browser + networking. Involves emergence, coordination, competing correctness properties.
- **Expected pressure points** (pre-registered in dossier):

| Pressure Point | Prediction |
|---|---|
| Structural (multi-layer) | Low |
| Systemic (emergent behaviour) | High |
| Temporal (sequences) | Low |
| Granularity | Medium |
| Decision Factors | High |

- **What would have caused failure**: Emergent behaviour (split brain, cascading failure, retry storms) requiring a new primitive.

## 2. Pre-registration

**First full pre-registration dossier**: hypotheses, pressure predictions recorded before authoring, tier structure, outcome classification framework. The pre-registration discipline becomes standard from this cycle.

- **H₁**: Systemic knowledge will increase graph complexity and introduce new interaction patterns without additional primitives.
- **H₀**: Systemic reasoning requires additional primitives (e.g. emergent-behaviour constructs).

## 3. Domain Objects Created (16)

### Tier 1 — Algorithmic (3)
**quorum (concept)** — Consensus prerequisites. Blocks: 8. Relationships: required_by, affects, contrasts_with. PASS 0/0.
**leader-election (concept)** — Election mechanics and failure handling. Blocks: 8. Relationships: requires, part_of, prevents, affects, triggers. PASS 0/0.
**raft-consensus (concept)** — Raft protocol. Blocks: 8. Relationships: requires, includes, prevents, survives, vulnerable_to, similar_to. PASS 0/0.

### Tier 2 — Failure (4)
**split-brain (concept)** — Partition-induced divergence. Blocks: 8. Relationships: prevents, vulnerable_to, causes, avoids, worsens. PASS 0/0.
**cascading-failure (concept)** — Failure propagation. Blocks: 8. Relationships: triggers, similar_to, prevents, worsens (mutual causal with retry-storm-amplification). PASS 0/0.
**retry-storm-amplification (concept)** — Retry-driven overload. Blocks: 8. Relationships: triggers, similar_to, prevents, reduces, vulnerable_to. PASS 0/0.
**backpressure (concept)** — Load regulation. Blocks: 8. Relationships: prevents, reduces, complementary_to, interacts_with. PASS 0/0.

### Tier 3 — Architectural (5)
**cap-theorem (principle — NEW KIND)** — Consistency/availability/partition theorem. Blocks: 9 (incl. Decision Factors). Relationships: explains, frames, constrains, relevant_to. PASS 0/0.
**strong-consistency (concept)** — Blocks: 9. Relationships: constrained_by, contrasts_with, requires, provides, trades_off_against. PASS 0/0.
**eventual-consistency (concept)** — Blocks: 9. Relationships: realises, contrasts_with, provides, may_use, requires. PASS 0/0.
**availability (concept)** — Blocks: 9. Relationships: constrained_by, enables, limits, affects, protects. PASS 0/0.
**network-partition-recovery (pattern — NEW KIND)** — Blocks: 9. Relationships: resolves, simplifies, determines, requires, affects, risk_during. PASS 0/0.

### Tier 4 — Operational (4)
**rolling-deployment (pattern)** — Blocks: 9. Relationships: preserves, interacts_with, risk_during. PASS 0/0.
**circuit-breaker (pattern)** — Blocks: 9. Relationships: prevents, complementary_to, interacts_with, protects, similar_to. PASS 0/0.
**idempotency (concept)** — Blocks: 9. Relationships: enables_safe_retry, complementary_to, requires, interacts_with. PASS 0/0.
**saga-pattern (pattern)** — Blocks: 9. Relationships: requires, relies_on, vulnerable_to, complementary_to. PASS 0/0.

## 4. Primitive Pressure Analysis

- **Candidate: "emergent behaviour" primitive.** Why it looked necessary: split brain, cascading failure, and retry storms are system-level phenomena. How it was tested: expressed as relationships between objects (triggers, worsens, vulnerable_to). Why rejected: systemic behaviour is a composition challenge, not a primitive challenge — emergent phenomena ARE multi-object by nature. Final representation: bidirectional/mutual causal relationships (retry ↔ cascade).
- **Candidate: workflow/sequence primitive.** Why it looked necessary: temporal ordering in consensus and failure sequences. How it was tested: declarative claims + relationships. Why rejected: distributed systems concepts are not expressed as sequences; the temporal pressure never materialised (predicted Low, observed Low).

## 5. Schema Interaction

```
Schema changed:      NO
Parser changes:      NO
Validator changes:   NO
Analyzer changes:    NO
Friction:            0
Rejected changes:    None
```

## 6. Relationship Growth

New motifs: triggers, worsens, prevents, vulnerable_to, similar_to, complementary_to, enables_safe_retry, trades_off_against, risk_during, may_use, survives, realises, resolves. **One new pattern discovered: mutual causal relationships (retry ↔ cascade) via standard bidirectional relationship declarations.** Complexity moved into relationships at scale.

## 7. Qualification Growth

Not yet tracked (metric formalized Cycle 007). Observations present in all objects.

## 8. Object Kind Evolution

- **principle** (cap-theorem) — NEW. Why: CAP is a law-like statement that constrains architecture; it is not a mechanism (concept) nor an operational practice (pattern). Why it is not vocabulary expansion: it is a structural role in the identity layer; the evidence blocks are identical.
- **pattern** (network-partition-recovery, rolling-deployment, circuit-breaker, saga-pattern) — NEW. Why: operational practices with repeatable structure. Same rationale.
- Cumulative kinds: **3** (concept, principle, pattern).

## 9. Discoveries

**Discovery 1 — Raft's native decomposition matches HPF's.**
- Initial assumption: Raft might need a single monolithic object.
- Evidence: Raft's own structure (leader election, log replication, safety) maps directly to HPF's object decomposition (quorum, leader-election, raft-consensus).
- Final understanding: domains that decompose well for engineers decompose well for HPF.
- Impact: supports object-boundary stability as a domain property.

**Discovery 2 — Systemic behaviour = composition, not primitive.**
- Initial assumption (pre-registered pressure High): emergence would strain the schema.
- Evidence: split brain, cascades, retry storms, backpressure all expressed through relationships.
- Final understanding: emergence is multi-object by nature; the schema's relationship layer is the mechanism.
- Impact: L3 hypothesis status → **Supported**.

**Discovery 3 — Dense interconnection is the mechanism for complexity.**
- Impact: shaped the "graph richness, not vocabulary richness" theory.

## 10. Failed Hypotheses / Near Failures

- **Pre-registered pressure miss (positive)**: Systemic pressure predicted High, observed Low — the strongest single confirmation of the Ontological Sufficiency Principle to that date.
- **Open question**: is there an upper bound on relationships per object? (circuit-breaker carries 6) — recorded as observation, no decision. Carried forward to Cycles 007–008 as an untested boundary.
- **Unresolved**: N/A beyond the relationship-bound question.

## 11. Validation Evidence

| Metric | Value |
|---|---|
| Objects created | 16 (all PASS 0/0) |
| Passing objects (cumulative) | 26 |
| Corpus (cumulative) | 43 |
| Outcome classification | 0 Failure / 2 Discovery / 14 Confirmation |
| Warnings | 0 |
| Instrument stability | 6 cycles unchanged |

## 12. End-of-Cycle Interpretation

- **What increased**: Objects (+16), relationship density, domain coverage (Systemic).
- **What stayed constant**: 9 primitives, parser, validator, analyzer.
- **Where did complexity move**: Into relationships (mutual causal motifs).
- **Did vocabulary expand**: No.
- **Did the graph become richer**: Yes — substantially (graph-pattern growth: substantial).

---

# Cycle 007 — Security

*Date: 2026-07-30. Experimental target: Probabilistic Knowledge Test. Knowledge category: Probabilistic.*

## 1. Research Objective

- **Original hypothesis (H₁)**: Probabilistic security knowledge will increase graph complexity and introduce new patterns of evidence interaction without requiring additional evidence primitives.
- **Falsification question (H₀)**: Probabilistic security reasoning requires one or more additional evidence primitives not representable in the existing vocabulary.
- **Why this domain**: Security is adversarial (intelligent opposing agent), uncertain, and decision-driven — the first Probabilistic category after Deterministic (browser, networking) and Systemic (distributed systems). Organized by **epistemic pressure, not security technology**.
- **Expected pressure points** (pre-registered):

| Pressure Area | Prediction |
|---|---|
| Structural | Low |
| Granularity | Medium |
| Decision Factors | High |
| Uncertainty Representation | Very High |
| Adversarial Reasoning | High |
| Representation Failure | None expected (primary falsification target) |

- **Pre-registered predictions**: P1 no new primitive; P2 new relationship motifs, not vocabulary; P3 greatest pressure from confidence (qualifies knowledge itself); P4 risk-acceptance is the strongest Decision Factors test (no objectively correct answer).
- **What would have caused failure**: Uncertainty or adversarial reasoning demanding new primitives.

## 2. Pre-registration

Full dossier pre-registration, including the epistemic-pressure tier structure:

| Tier | Focus | Objects |
|---|---|---|
| 1 | Evidence & Uncertainty | Confidence, Likelihood, Incomplete Evidence |
| 2 | Adversarial Reasoning | Attacker Capability, Threat Actor, Attack Surface, Kill Chain |
| 3 | Risk & Decision | Risk Acceptance, Defense in Depth, Residual Risk, Compensating Controls |
| 4 | Operational Security | Zero Trust, Incident Response, Threat Detection, Vulnerability Management |

Success criteria: no primitive, no parser/validator/analyzer changes, uncertainty expressible via existing blocks, adversarial reasoning expressible without an "attacker" primitive, stable object boundaries. Failure criteria: the four-point architecture review trigger.

## 3. Domain Objects Created (15)

### Tier 1 — Evidence & Uncertainty (3)
**confidence (concept)** — Belief-strength qualification. Blocks: 8. Relationships: qualifies, limited_by, informs, affects. Validation: PASS 0/0.
**likelihood (concept)** — Occurrence-probability qualification. Blocks: 8. Relationships: qualified_by, degraded_by, informs. PASS 0/0.
**incomplete-evidence (concept)** — Evidence gaps and their effects. Blocks: 8. Relationships: reduces, widens, blinds, distorts, complicates. PASS 0/0.

### Tier 2 — Adversarial Reasoning (4)
**attacker-capability (concept)** — What an adversary can do. Blocks: 8. Relationships: characterises, interacts_with, enables, drives, informs. PASS 0/0.
**threat-actor (concept)** — Who the adversary is. Blocks: 8. Relationships: has, executes, targets, determines, informs. PASS 0/0.
**attack-surface (concept)** — Where an adversary can engage. Blocks: 8. Relationships: multiplied_by, targeted_by, entry_point, informs, reduces. PASS 0/0.
**kill-chain (concept)** — The attack progression. Blocks: 8. Relationships: determines_progression, executes, entered_through, informs, guided_by. PASS 0/0.

### Tier 3 — Risk & Decision (4)
**risk-acceptance (decision — NEW KIND)** — Accepting unmitigated risk. Blocks: 9 (incl. Decision Factors). Relationships: requires, addresses, complicates, may_support, triggers. Decision factors: materiality, assessment_confidence, mitigation_cost, detection_compensation (all weight high). Failure modes: acceptance without owner, expired acceptance, undetectable materialisation. PASS 0/0.
**defense-in-depth (principle)** — Layered defences. Blocks: 8. Relationships: complements, resists, includes, extends, reduces_need. PASS 0/0.
**residual-risk (concept)** — Risk after mitigation. Blocks: 8. Relationships: addresses, reduces, quantified_by, required. PASS 0/0.
**compensating-controls (pattern)** — Alternative controls. Blocks: 8. Relationships: distinguishes_from, reduces, contributes_to, applies_to, enhances. PASS 0/0.

### Tier 4 — Operational Security (4)
**zero-trust (principle)** — Never trust, always verify. Blocks: 8. Relationships: reduces, extends, depends_on, supports, resists, changes. PASS 0/0.
**incident-response (pattern)** — Detection-to-recovery pipeline. Blocks: 8. Relationships: triggered_by, position_aware, operates_under, responds_to, final_layer, informs. PASS 0/0.
**threat-detection (pattern)** — Continuous detection. Blocks: 8. Relationships: designed_against, limited_by, carries, triggers, tracked_against, behaviour_based. PASS 0/0.
**vulnerability-management (pattern)** — Discovery→prioritisation→remediation. Blocks: 8. Relationships: scoped_by, prioritised_by, triggers, exploit_leveraged, bridges, complements. PASS 0/0.

## 4. Primitive Pressure Analysis

- **Candidate: "attacker" or "adversary" primitive.** Why it looked necessary: security introduces an intelligent opposing agent — a perspective previous cycles lacked. How it was tested: competing perspectives expressed as claims + relationships (targeted_by, executes, entered_through). Why rejected: the attacker is an *entity in the graph*, not a new evidence type — exactly the Ontological Sufficiency Principle's prediction. Final representation: relationships between attacker-capability, threat-actor, attack-surface, kill-chain.
- **Candidate: "uncertainty" primitive.** Why it looked necessary: confidence, likelihood, incomplete evidence are security's core vocabulary. How it was tested: expressed as qualifiers on existing evidence (claim certainty, observation confidence, tradeoff importance, decision factor weight). Why rejected: uncertainty is a *property of evidence*, not a kind of evidence. Final representation: qualification metadata (165 qualification events across the cycle, 0 new primitives).
- **Candidate: "decision" primitive.** Why it looked necessary: risk acceptance has no objectively correct answer. How it was tested: Decision Factors block (existing primitive) with factor/question/supporting/contradictory/weight structure. Why rejected as vocabulary: `decision` became an object *kind* (structural role), not a primitive.

## 5. Schema Interaction

```
Schema changed:      NO
Parser changes:      NO
Validator changes:   NO
Analyzer changes:    NO
Friction:            0
Rejected changes:    None
```

## 6. Relationship Growth

17 new relationship motifs across the cycle (qualifies, limited_by, qualified_by, degraded_by, blinds, distorts, widens, targeted_by, executed, entered_through, determines_progression, designed_against, tracked_against, behaviour_based, scoped_by, prioritised_by, exploit_leveraged, bridges, reduces_need, quantified_by, distinguishes_from...). Prediction 2 confirmed: **relationship motifs, not vocabulary**. Kill-chain demonstrated as graph composition (repeating Cycle 006's finding at the knowledge-graph level).

## 7. Qualification Growth

**New metric introduced**: evidence qualification growth — qualifiers applied to existing evidence without new primitives.

| Qualifier | Count |
|---|---|
| Claims (certainty) | 75 (5 × 15 objects) |
| Observations (confidence) | 45 (3 × 15) |
| Recommendations (certainty) | 45 (3 × 15) |
| **Total qualification events** | **165** |
| New primitives | 0 |

## 8. Object Kind Evolution

- **decision** (risk-acceptance) — NEW. Why: a choice with no objectively correct answer whose conclusion is driven entirely by weighted Decision Factors. Why not vocabulary expansion: kind = structural role in the identity layer; the block set is unchanged. Cumulative kinds: **4** (concept, principle, pattern, decision).

## 9. Discoveries

**Discovery 1 — Uncertainty is a qualifier, not a primitive.** Initial assumption (pre-registration): uncertainty is the cycle's greatest pressure. Evidence: all uncertainty content attached to existing evidence as qualification. Final understanding: probabilistic knowledge changes qualifiers, not vocabulary. Impact: origin of the qualification-growth metric and the "Complexity Migration Matrix" theory.

**Discovery 2 — Decision is a kind, not a primitive.** Impact: established the kind/primitive boundary that later became the Object Kind Stability secondary metric.

**Discovery 3 — Adversarial reasoning is composition.** Impact: the attacker-as-entity finding confirmed the Ontological Sufficiency Principle.

**Discovery 4 — Evidence qualification complexity is a new complexity destination.** Impact: extended the migration model — Deterministic→graph composition, Systemic→relationships, Probabilistic→qualification.

## 10. Failed Hypotheses / Near Failures

- **Prediction 3 confirmed as near-miss**: confidence was indeed the greatest pressure (predicted and observed), but pressure manifested as qualification, not representation failure.
- **Prediction 4 confirmed**: risk-acceptance was the hardest Decision Factors test and passed — the only object whose entire conclusion rests on Decision Factors.
- **Open questions**: (1) TTPs as entities vs claims (both representable — expressiveness evidence); (2) object-kind proliferation vs primitive proliferation — is kind growth a form of vocabulary growth? (became the Object Kind Stability metric); (3) certainty vs confidence — belief strength vs judgement-process reliability; does the schema need a formal *qualification model* (convention layer)? Decision rule recorded: if qualification changes how evidence is represented → investigate; if it only describes evidence quality → keep as metadata.

## 11. Validation Evidence

| Metric | Value |
|---|---|
| Objects created | 15 (all PASS 0/0) |
| Passing objects (cumulative) | 41 |
| Corpus (cumulative) | 58 |
| Outcome classification | 0 Failure / 3 Discovery / 12 Confirmation |
| Warnings | 0 |
| Instrument stability | 7 cycles unchanged |

## 12. End-of-Cycle Interpretation

- **What increased**: Qualification density (165 events), relationship motifs (+17).
- **What stayed constant**: 9 primitives, instruments.
- **Where did complexity move**: Into evidence qualification.
- **Did vocabulary expand**: No.
- **Did the graph become richer**: Yes — qualification layer added without vocabulary change.

---

# Cycle 008 — Machine Learning

*Date: 2026-07-31. Experimental target: Probabilistic + Adaptive Knowledge Test. Knowledge category: Probabilistic + Adaptive.*

**This is the strongest falsification attempt in the programme.** Each tier is documented separately.

## Pre-registration (recorded before authoring)

- **H₁**: Adaptive ML knowledge — uncertainty, feedback loops, changing system behaviour, evaluation ambiguity — will increase graph complexity and introduce new interaction patterns (including adaptation patterns) without additional primitives.
- **H₀**: Adaptive systems require additional primitives (temporal validity, evolution, drift constructs).
- **Test question**: Does machine intelligence introduce a new epistemic mode that cannot be decomposed into existing evidence structures?
- **Pressure predictions**: Structural Low; Granularity Medium; Decision Factors High; Uncertainty Very High; Adaptation High (new); Representation Failure none expected.
- **Predictions**: P1 no new primitive; P2 adaptation resolves as graph pattern (feedback relationships, drift as observations/constraints); P3 greatest pressure = changing validity of knowledge (time-boundedness without temporal primitives); P4 uncertainty follows Cycle 007's qualification pattern.
- **Outcome space**: (1) fits qualification complexity → strengthens theory; (2) new graph pattern → discovery; (3) vocabulary expansion → falsification.
- **Observation metrics** (no schema change): adaptation events, feedback relationships, drift representation.
- **Pre-authoring addenda**: Tier 1 (temporal trap; qualification continuity); Tier 2 (provenance; drift; generalization as inferred property; overfitting); Tier 3 (benchmark, subjective evidence, value primitives; self-referential evaluation); Tier 4 (monitoring, action-selection, deployment-risk composition; the self-updating-agent question).
- **Discipline constraint**: no ML-specific object kinds — hallucination→failure mode + uncertainty; drift→constraint violation + observation change; alignment→objective tradeoff + decision factors; benchmark→observation + measurement constraint; retraining→recommendation + feedback loop.

## Tier 1 — Model Uncertainty

- **Pressure**: uncertainty at model level; the temporal temptation (calibration decay, stale knowledge).
- **Prediction**: qualification pattern carries from 007; time-boundedness expressible without temporal constructs.
- **Objects** (all concept, all PASS 0/0):
  - **confidence-calibration** — Alignment of stated confidence with observed accuracy. Blocks: 8. Relationships: qualified_by, validates, evaluates, mitigates, depends_on, degraded_by. Failure modes: overconfidence, underconfidence, calibration_drift.
  - **probabilistic-outputs** — Belief distributions over outcomes. Blocks: 8. Relationships: requires, enabled_by, mitigates, expresses, informs (×2). Failure modes: probability_misuse, spurious_precision, format_mismatch.
  - **hallucination** — Confident fabrication. Blocks: 8. Relationships: exploits, masks, targeted_by, measured_by, aggravated_by, detected_by. Failure modes: confident_fabrication, source_misattribution, stale_knowledge_assertion. (Discipline mapping held: failure-mode-driven object, no ML primitive.)
  - **uncertainty-estimation** — Aleatoric vs epistemic quantification. Blocks: 8. Relationships: validated_by, produces, mitigates, quantifies, degrades_with, informs. Failure modes: false_precision, unvalidated_estimates, epistemic_misclassification.
- **Result**: The temporal trap failed to break HPF — time-bound validity expressed as relationships (degraded_by) + constraints ("calibration is distribution-bound"), not a temporal primitive. 44 qualification events, 0 primitives.
- **Discovery (Tier 1)**: *Adaptive systems do not appear to introduce temporal knowledge. They introduce validity conditions on existing knowledge.* Weak model (Knowledge + Time) rejected in favour of Knowledge + validity constraints + change relationships + deviation observations.

## Tier 2 — Learning Systems

- **Pressure**: data provenance (lineage primitive?), inferred properties (quality-attribute primitive?), distribution shift (drift primitive?).
- **Prediction**: lineage → observation+constraint+relationship; shift → constraint violation + failure mode; generalization → relationships + observations (hardest object); overfitting → failure modes.
- **Objects** (all concept, all PASS 0/0):
  - **training-data** — The information bound of the model. Blocks: 8. Relationships: defines_baseline, bounds, facilitated_by, informs, risks_contamination, source_of. Failure modes: data_leakage, label_noise, provenance_loss.
  - **generalization** — Inferred property of unseen-data performance. Blocks: 8. Relationships: learned_from, contrasts_with, limited_by, measured_by, affects, interacts_with. Failure modes: inflated_generalization_claims, distribution_mismatch, false_transfer_assumption. Explicitly recorded as "a property inferred from observations" bound by stated validity conditions.
  - **overfitting** — Noise absorption. Blocks: 8. Relationships: degrades, depends_on, masked_by, interacts_with, detected_by, worsens_with. Failure modes: silent_overfit, evaluation_leakage, regularization_overreach.
  - **distribution-shift** — Training/deployment divergence. Blocks: 8. Relationships: deviates_from, limits, degrades, degrades, detected_by, triggers. Failure modes: silent_shift, shift_type_misclassification, retraining_on_noise.
- **Result**: Second temporal trap (the harder case — drift itself) resolved as constraint violation + observation change + failure mode + degradation relationships. Generalization resolved without a quality-attribute primitive (evidence + validity conditions). Provenance resolved as composition. 44 qualification events (cumulative 88), 0 primitives.
- **Discovery (Tier 2)**: Inferred properties are represented as evidence + validity conditions — HPF does not model properties directly, it models evidence for them and conditions under which they hold.

## Tier 3 — Evaluation

- **Pressure**: self-referential evaluation — the system, the evaluator, and the evidence interact; the benchmark primitive, subjective-evidence primitive, and value primitive temptations.
- **Prediction**: benchmark → observation+constraint+failure+relationship; human evaluation → qualified observations + decision factors; alignment → objective+constraint+tradeoff+decision factor; metric selection → decision factors.
- **Objects** (all PASS 0/0):
  - **benchmark-validity (concept)** — Measurement instrument with scope. Blocks: 8. Relationships: estimates, contaminated_by, measures, governed_by, complements, evaluates. Failure modes: benchmark_leakage, benchmark_saturation, proxy_mismatch.
  - **metric-selection (concept)** — Decision under tradeoffs. Blocks: 9 (incl. Decision Factors: deployment_objective_match, error_type_cost, segment_sensitivity). Relationships: composes, estimates, evaluates, masks, contrasts_with, expresses_objectives. Failure modes: metric_mismatch, aggregate_mask, metric_chasing.
  - **human-evaluation (concept)** — Judgement as structured evidence. Blocks: 9 (incl. Decision Factors: agreement_level, evaluator_population_fit, sample_power). Relationships: complements, evaluates, informs, verifies, biased_by, validates. Failure modes: unmeasured_disagreement, evaluation_bias, criteria_drift. Claim 5 records: subjective judgement is structured evidence, not a separate type.
  - **alignment (concept)** — Objective correspondence, evaluated behaviourally. Blocks: 9 (incl. Decision Factors: objective_weighting, evaluation_instrument_validity, context_stability, failure_cost). Relationships: grounded_in, measured_by, expressed_through, shaped_by, destabilized_by, informs. Failure modes: misspecified_objective, objective_drift, specification_gaming.
- **Result**: No benchmark primitive (benchmark = measurement context); no subjective-evidence primitive (agreement measured as validity); no value primitive (alignment = objective structure). Decision Factors appeared only where decision pressure existed (3 of 4 objects) — block distribution content-driven, not forced.
- **Discovery (Tier 3)**: Self-referential evaluation is expressible as ordinary graph cycles — alignment → human-evaluation → benchmark-validity → alignment. The evaluator is an evidence source with measured validity conditions; the instrument has stated scope; the loop is a cycle, not a construct. 44 qualification events (cumulative 132).

## Tier 4 — Operational ML

- **Pressure**: the combination of everything — adaptation, uncertainty, monitoring, feedback loops, operational decisions; the monitoring primitive, drift primitive, action-selection primitive, and self-updating-agent questions.
- **Prediction**: monitoring → observation stream + constraint violation + failure detection + recommendation; retraining → decision factors + feedback relationship; deployment risk → composition with security's risk-acceptance.
- **Objects** (all PASS 0/0):
  - **model-monitoring (pattern)** — The deployed evidence channel. Blocks: 8. Relationships: detects, tracks, validates, informs, reduces, detects. Failure modes: telemetry_blindspot, alert_fatigue, monitoring_drift.
  - **drift-detection (pattern)** — Reference-vs-current divergence measurement. Blocks: 8. Relationships: measures, composes, triggers, protects, references, guards. Failure modes: silent_miss, false_alarm_storms, reference_decay.
  - **retraining-decisions (decision)** — The feedback intervention. Blocks: 9 (incl. Decision Factors: shift_verification, retrained_evidence, regression_risk, staleness_cost — all weight high). Relationships: triggered_by, informed_by, triggered_by, acts_on, modifies, revalidates. Failure modes: habitual_retraining, unvalidated_release, retraining_amplification.
  - **deployment-risk (concept)** — Failure likelihood × impact under validity conditions. Blocks: 8. Relationships: informs (→ risk-acceptance, security corpus — first ML↔security cross-domain link), reduced_by, modifies, increased_by, quantified_by, assessed_by. Failure modes: unknown_risk_deployment, unmonitored_rollout, residual_risk_amnesia.
- **Result**: No monitoring primitive, no drift primitive, no action-selection primitive, no self-updating-agent construct. The feedback cycle (monitoring → drift detection → retraining decision → validation → deployment → monitoring) is ordinary graph structure; the "agent that changes its own evidence model" is the cycle itself. 44 qualification events (final cumulative 176).
- **Discovery (Tier 4)**: Operational adaptation needs no agent construct — the self-updating system *is* the feedback cycle.

## Cycle 008 — Primitive Pressure Analysis (complete list of temptations)

| Candidate | Why it looked necessary | How tested | Why rejected | Final representation |
|---|---|---|---|---|
| Temporal/validity primitive | Drift, decay, recency, training history | Validity conditions in constraints + relationships | Time is a property of knowledge, not a kind | degraded_by, deviates_from, "validity bound" constraints |
| Drift primitive | Distribution shift is the adaptive-system challenge | Constraint violation + observation change + failure mode | Shift is deviation from a fixed reference, measurable | silent_shift failure mode; measures/deviates_from relationships |
| Benchmark primitive | Benchmarks look like special entities | Instrument framing | A benchmark is a measurement context | score=observation, scope=constraint, leakage=failure mode |
| Subjective-evidence primitive | Human judgement introduces disagreement/preference | Qualified observations + decision factors | Subjectivity is structured evidence with measured validity | agreement_level, evaluator_population_fit, sample_power |
| Value primitive | Alignment mixes values and objectives | Objective structure | Values enter as objectives with tradeoffs, not ontology | capability vs constraint, helpfulness vs safety; 4 decision factors |
| Monitoring primitive | Continuous observation of deployed systems | Observation stream + constraints + failure modes | Monitoring is the evidence channel, not a knowledge type | telemetry_blindspot; detects/tracks/validates relationships |
| Action-selection primitive | Retraining is a choice among actions | Decision Factors + feedback relationships | Action selection is a decision | 4 decision factors; triggered_by/acts_on relationships |
| Self-updating-agent construct | The system changes its own evidence model | Feedback cycle | The loop is the representation | monitoring → drift → retraining → validation → deployment → monitoring |

## Cycle 008 — Schema Interaction

```
Schema changed:      NO
Parser changes:      NO
Validator changes:   NO
Analyzer changes:    NO
Friction:            0
Rejected changes:    All 8 candidates above
```

## Cycle 008 — Relationship Growth

~25 new relationship motifs (contaminated_by, defines_baseline, expresses_objectives, grounded_in, guards, masks, protects, quantified_by, revalidates, risks_contamination, shaped_by, deviates_from, assessed_by, biased_by, destabilized_by, ...); ~66 distinct motifs across the 16 objects. Feedback loops expressible as relationship cycles. First cross-domain link: deployment-risk → risk-acceptance (security).

## Cycle 008 — Qualification Growth

176 total events (80 claims + 48 observations + 48 recommendations). Continuation metric confirmed: uncertainty is qualification, in a second probabilistic domain.

## Cycle 008 — Object Kind Evolution

No new kinds. 13 concept, 2 pattern, 1 decision. Cumulative: **4** (unchanged).

## Cycle 008 — Discoveries

1. Validity conditions, not temporal knowledge (Tier 1).
2. Inferred properties = evidence + validity conditions (Tier 2).
3. Self-reference = graph cycles; evaluator = evidence source with measured validity (Tier 3).
4. The self-updating system is the feedback cycle (Tier 4).

## Cycle 008 — Failed Hypotheses / Near Failures

- **All 8 candidate primitives rejected.** The temporal trap (twice), benchmark, subjective evidence, value, monitoring, action-selection, and agent constructs each approached the vocabulary boundary and were resolved through composition.
- **Outcome space result**: outcome 1 (fits qualification) and outcome 2 (new graph pattern — adaptation/validity loops) both occurred; outcome 3 (falsification) did not.
- **Open questions**: (1) is "validity conditions" a stable pattern across future adaptive domains (n=1)? (2) should qualification be measured as ratio not count? (3) where is the boundary between graph cycles and special constructs?

## Cycle 008 — Validation Evidence

| Metric | Value |
|---|---|
| Objects created | 16 (all PASS 0/0) |
| Passing objects (cumulative) | 57 |
| Corpus (cumulative) | 74 |
| Outcome classification | 0 Failure / 4 Discovery / 12 Confirmation |
| Warnings | 0 |
| Instrument stability | 8 cycles unchanged |

## Cycle 008 — End-of-Cycle Interpretation

- **What increased**: Objects (+16), qualification (176 events), relationship motifs (+25), domain coverage (Adaptive).
- **What stayed constant**: 9 primitives, 4 object kinds, all instruments.
- **Where did complexity move**: Into validity conditions (constraints) + feedback relationships + qualification — a composition of existing destinations.
- **Did vocabulary expand**: No.
- **Did the graph become richer**: Yes — substantially (feedback cycles, cross-domain links).

---

# Cycle 009 — Compilers / Static Analysis

*Date: 2026-07-31. Experimental target: Transformational Knowledge Test. Knowledge category: Transformational — knowledge about changing a system's representation while preserving properties.*

**The cycle that tests whether *change itself* requires a new primitive.** The tested categories were deterministic (state), systemic (coordination), probabilistic (uncertainty), and adaptive (adaptation); compilers attack the remaining untested abstraction: transformation + correctness. Each tier is documented separately.

## Pre-registration (recorded before authoring)

- **H₁**: Transformational knowledge — representation, transformation, correctness, equivalence — will resolve through composition: before-state relationships + transformation actions + after-state observations + correctness constraints.
- **H₀**: Transformational knowledge requires additional primitives (transformation, representation, proof, formal rule, or equivalence constructs).
- **Test question**: Does transformational knowledge require a new evidence primitive for representing systems that change form while preserving properties?
- **Pressure predictions**: Structural High (new — first multi-level representation ladder); Granularity Medium; Correctness Very High (new — proof temptation); Equivalence High (new); Transformation High (new); Representation Failure none expected (falsification target).
- **Predictions**: P1 no new primitive; P2 transformation resolves as before-state + action + after-state + correctness constraint; P3 greatest pressure = correctness — proof is the possible failure candidate, expected to resolve as claim + evidence + constraints + relationships; P4 Tier 4 resolves as Decision Factors + Trade-offs.
- **Outcome space**: A — composition (strengthens HPF); B — discovery (transformation becomes its own reusable relationship motif); C — vocabulary expansion (falsification).
- **Observation metrics** (no schema change): transformation events, correctness relationships, equivalence representation.
- **Pre-authoring addenda**: Tier 1 (representation pressure — AST/IR ladder; program-semantics as hardest object; no compiler-specific kinds); Tier 2 (transformation = composition formula; constant folding purest case; liveness as observation; pipeline/sequence temptation); Tier 3 (proof as evidence artifact; equivalence as relationship over semantics; type-safety as guarantee object; compiler-correctness as quality-claim object; DFs only on formal-verification); Tier 4 (measurement objects; decision destination; artifact validity; mode divergence).
- **Discipline constraint**: no compiler-specific object kinds — AST → entities + relationships + constraints; type rules → constraints (invariants); type errors → failure modes; proof → evidence + constraints; equivalence → relationship; transformation → before/after + correctness constraint.

## Tier 1 — Program Representation

- **Pressure**: the first multi-level representation ladder (source → AST → IR → machine code); the representation primitive temptation; the formal-rule temptation (type systems); the "meaning" temptation (semantics).
- **Prediction**: representation is not a knowledge kind — an AST is entities + relationships + constraints; program-semantics is the hardest object (meaning is the yardstick against which correctness is judged).
- **Objects** (all concept, all PASS 0/0):
  - **abstract-syntax-tree** — The structured representation of source. Blocks: 8. Relationships: annotated_by, lowered_from, expresses, operates_on, enables (×2). Failure modes: parse_failure, grammar_ambiguity, precedence_misbinding.
  - **type-system** — Formal rules assigning types to terms. Blocks: 8. Relationships: annotates, guarantees, constrains, must_preserve, verified_by, relied_upon_by. Failure modes: unsoundness_hole, checker_divergence, inference_ambiguity.
  - **intermediate-representation** — A program representation between source and machine code. Blocks: 8. Relationships: lowered_from, preserves, substrate_for, organizes, constrained_by. Failure modes: information_loss, lowering_semantics_violation, ir_level_bloat.
  - **program-semantics** — The meaning of a program, the correctness yardstick. Blocks: 8. Relationships: expressed_by, preserved_through, judged_by, based_on, anchored_in. Failure modes: semantic_mischaracterization, observation_model_mismatch, undefined_behaviour_leakage.
- **Result**: The representation pressure resolved through composition — the AST → IR → code ladder is entities + relationships (lowered_from, expressed_by, preserved_through) + constraints (meaning invariant under representation; information-retention invariant). No nesting construct, no representation primitive; representation-of-representation is a relationship chain. Type rules resolved as constraints with invariants — "type rules are invariants, not a new primitive kind" — the validity-conditions pattern from Cycle 008 appearing in a static, non-temporal domain. Program semantics was the hardest object, as predicted, and produced the cycle's deepest result.
- **Discovery (Tier 1)**: *Correctness is relative to a stated observation model.* Equivalence and correctness are not properties of a program alone — they are relations judged against a chosen notion of observable behaviour. The qualification pattern from Cycles 007/008 (claims scoped by stated conditions) applies to correctness itself — the strongest candidate for the programme's biggest theoretical contribution.

## Tier 2 — Transformation

- **Pressure**: the transformation primitive temptation (the cycle's centre); the pipeline/sequence temptation (pass ordering); analysis-result temptations (constancy, liveness).
- **Prediction**: transformation = before-state + transformation action + after-state + correctness constraint; folding is the purest case; analysis results are observations, not primitives; ordering is a graph property, not a knowledge type.
- **Objects** (all PASS 0/0):
  - **compiler-optimization (concept)** — Semantic-preserving representation change. Blocks: 8. Relationships: operates_on (×2), preserves, organized_as, includes (×2), verified_by, driven_by. Failure modes: miscompilation, optimization_blowup, missed_opportunity.
  - **optimization-pass (pattern)** — A single unit of transformation; pipelines of passes. Blocks: 8. Relationships: composed_of, operates_on, preserves, affects, constrained_by. Failure modes: phase_ordering_problem, pass_interaction_bug, nontermination.
  - **constant-folding (concept)** — Compile-time evaluation of constant expressions. Blocks: 8. Relationships: instance_of, operates_on, preserves, verifiable_by, bounded_by. Failure modes: unsound_fold, nonconstant_fold, fold_blowup.
  - **dead-code-elimination (concept)** — Removal of unobservable computation. Blocks: 8. Relationships: instance_of, operates_on, preserves, verifiable_by, improves. Failure modes: live_code_elimination, observability_misclassification, retained_dead_code.
- **Result**: The transformation temptation resolved exactly as pre-registered — miscompilation defined as *wrong enabling condition*; the transformation's soundness lives in its preconditions. Every unsound fold traces to a wrong assumption about what is constant; liveness analysis results are observations, not guarantees. The pipeline temptation resolved as relationships (composed_of, depends_on) + constraints (termination; pipeline correctness = composition of per-pass correctness) — the phase-ordering problem is a relationship-level failure, not a sequencing construct. The ordering question ("does ordering create a new knowledge type, or just a graph property?") was answered: **a graph property**.
- **Discovery (Tier 2)**: *Validity conditions generalize from knowledge to actions.* Cycle 008 bound knowledge (model claims valid only within distribution); compilers bind transformations — enabling conditions are validity conditions on actions. The preserve/verify pair (operates_on + preserves + verified_by) emerged as the cycle's new graph motif.

## Tier 3 — Correctness

- **Pressure**: the strongest tier — proof, equivalence, and verification; the pre-registered possible failure candidate (proof primitive); the equivalence primitive temptation.
- **Prediction**: proof = claim + evidence + constraints + relationships (machine-checked proof is the strongest-confidence observation, not a new primitive); equivalence is a relationship over semantics; type-safety is the guarantee object; compiler-correctness is the quality-claim object (the analogue of Cycle 008's generalization); Decision Factors only on formal-verification.
- **Objects** (all PASS 0/0):
  - **type-safety (concept)** — The scoped language guarantee. Blocks: 8. Relationships: guaranteed_by, defined_over, must_preserve, verifiable_by, bounded_by, enabled_by. Failure modes: soundness_hole, unsound_optimization, guarantee_scope_erosion.
  - **compiler-correctness (concept)** — Semantic preservation as the correctness definition. Blocks: 8. Relationships: preserves, constrains, must_preserve, supported_by, verified_by, depends_on, affected_by. Failure modes: miscompilation, wrong_code_generation, rejection_of_valid_program.
  - **formal-verification (concept)** — Machine-checked establishment of properties. Blocks: 9 (incl. Decision Factors: verification_target, proof_tractability, cost_assurance_tradeoff — all weight high). Relationships: verifies (×3), uses, requires. Failure modes: specification_error, verification_gap, proof_system_unsoundness.
  - **equivalence-checking (concept)** — Mechanical before/after comparison. Blocks: 8. Relationships: based_on, verifies (×3), used_by. Failure modes: false_positive, false_negative, observation_model_mismatch.
- **Result**: The proof temptation resolved exactly as predicted — the decisive framing: *a proof is an artifact of evidence, not a new knowledge kind.* Machine-checked proof is the strongest-confidence observation in engineering, represented as evidence + constraints + relationships, with the specification as the residual risk ("garbage in, verified garbage out"). Equivalence resolved as a relationship over semantics, valid only under a stated observation model; the checker's soundness split (false positives = correctness failures, false negatives = precision issues) is the equivalence domain's answer to the observation model. Prediction 5 held: Decision Factors appeared only on formal-verification (3 of 4 objects none) — block distribution stayed content-driven. The sharpened falsification question — can the corpus represent machine-checked proof without a proof primitive? — was answered: yes.
- **Discovery (Tier 3)**: *Evidence about evidence.* Formal verification is knowledge about the strength of other knowledge (proofs about guarantees about transformations) — resolved as ordinary composition via verifies relationships: a second-order evidence graph, no meta-primitive.

## Tier 4 — Optimization Reality

- **Pressure**: decision complexity (pre-registered destination); measurement objects; artifact validity; mode divergence.
- **Prediction**: performance = observations (benchmarks as instruments) + constraints (measurement validity — the Cycle 008 benchmark-validity pattern); tradeoffs = decision kind with 4 Decision Factors; build systems = pattern with artifact validity as constraint; debug/release = decision kind; transformation complexity moves into constraint-carrying relationships + qualification + decision structure.
- **Objects** (all PASS 0/0):
  - **compiler-performance (concept)** — Generated-code quality vs compilation cost. Blocks: 8. Relationships: driven_by, informed_by, constrained_by, affected_by, differentiated_by. Failure modes: performance_regression, benchmark_noise_obscuring, benchmark_gaming.
  - **optimization-tradeoffs (decision)** — The optimization posture decision. Blocks: 9 (incl. Decision Factors: optimization_aggressiveness, compile_time_budget, binary_size_target, debuggability_requirement). Relationships: decides_over, shapes, configures, defines, bounded_by. Failure modes: defaulted_tradeoff, debuggability_collapse, tradeoff_reversal.
  - **build-systems (pattern)** — Deriving artifacts from sources via dependency graphs. Blocks: 8. Relationships: constrains, executes, produces, invokes. Failure modes: stale_artifact, rebuild_storm, nonhermetic_build.
  - **debug-vs-release-modes (decision)** — The two build postures. Blocks: 9 (incl. Decision Factors: optimization_level, assertion_policy, debug_info_retention, environment_fidelity). Relationships: configured_by, instantiates, produced_by, affected_by, differentiates. Failure modes: release_only_bug, assertion_dependence, debug_only_behaviour.
- **Result**: Prediction 4 confirmed — Tier 4 resolved as decision complexity: two decision-kind objects with 4 Decision Factors each, carrying the decision pattern from Cycle 007 (risk-acceptance) and Cycle 008 (retraining-decisions). Compiler performance resolved without a performance primitive (benchmarks as instruments — the benchmark-validity pattern from Cycle 008). Build systems produced the third validity-conditions appearance: *artifact validity* — an artifact is valid iff derived from current sources + toolchain state. Debug vs release carried the strongest Tier 4 finding.
- **Discovery (Tier 4)**: *Mode divergence is a behavioural decision, not a speed accident.* Debug and release builds are distinct programs with distinct behaviour contracts — assertion removal changes the program; release-only bugs are decision consequences. Validation must be per-mode: each mode is a program, and testing one validates one.

## Cycle 009 — Primitive Pressure Analysis (complete list of temptations)

| Candidate | Why it looked necessary | How tested | Why rejected | Final representation |
|---|---|---|---|---|
| Representation primitive | Source → AST → IR → code is a multi-level representation stack | Entities + relationships + constraints; representation-of-representation as a relationship chain | A representation is a concept with stated contracts, not a knowledge type | lowered_from, expressed_by, preserved_through; "meaning invariant under representation" |
| Formal-rule primitive | Type systems look like formal rule objects | Constraints (type rules as invariants) + failure modes (unsoundness hole) | Type rules are invariants — the same pattern as constraints elsewhere | guaranteed_by, must_preserve; soundness-scope constraints |
| Semantics/"meaning" primitive | Meaning is not a mechanism, observation, or constraint | Semantics as the yardstick object: claims + constraints + relationships | Correctness is relative to a stated observation model — meaning is the reference, not a construct | judged_by, based_on, anchored_in; observation-model constraints |
| Transformation primitive | Changing form is the cycle's central epistemic pressure | Before-state + transformation action + after-state + correctness constraint | Transformation is a composition, exactly the pre-registered formula | preserves, operates_on; enabling-conditions constraints |
| Fold primitive | Compile-time evaluation looks like a new operation | Observation (constancy) + constraint (semantics preservation) + relationship | Folding correctness reduces to a constancy question — analysis results are observations | verifiable_by, bounded_by |
| Analysis-result/liveness primitive | Liveness proves code unobservable | Liveness as observations with constraints | Analysis results are observations, not guarantees | instance_of, improves; observability-model constraints |
| Pipeline/sequence primitive | Pass pipelines introduce ordering A → B → C | Relationships (composed_of, depends_on) + constraints (termination, composition correctness) | Ordering is a graph property — the phase-ordering problem is a relationship-level failure | composed_of, operates_on; termination constraint |
| Proof primitive | Proof is the strongest form of engineering evidence | Claim + evidence artifacts (proof obligations) + constraints (specification bounds, machine-checked) | A proof is an artifact of evidence, not a new knowledge kind | verifies, requires; "verification bounded by specification" |
| Equivalence primitive | Before/after relations define transformation correctness | Equivalence as a relationship over semantics under a stated observation model | Equivalence is a relation defined over semantics, not syntax | based_on, verifies; observation-model constraint |
| Performance primitive | Generated-code quality is a distinct concern | Observations (benchmarks as instruments) + constraints (measurement validity) | Performance is measured, not a knowledge type | driven_by, informed_by; benchmark-validity constraints |
| Artifact-validity construct | Stale artifacts are a distinct failure class | Constraint (valid iff derived from current sources + toolchain state) + failure modes | Artifact validity is the validity-conditions pattern applied to artifacts | constrains, executes; derivation invariant |
| Mode-divergence construct | Debug/release builds behave differently | Two decision factors sets + tradeoffs + failure modes | Mode divergence is a behavioural decision, not a construct | configured_by, instantiates; per-mode behaviour contracts |

## Cycle 009 — Schema Interaction

```
Schema changed:      NO
Parser changes:      NO
Validator changes:   NO
Analyzer changes:    NO
Friction:            0
Rejected changes:    All 12 candidates above
```

## Cycle 009 — Relationship Growth

88 relationship edges across 16 objects; 52 unique motifs in-cycle; **37 new to the corpus** (affected_by, anchored_in, annotated_by, annotates, based_on, bounded_by, composed_of, configured_by, configures, decides_over, defined_over, differentiated_by, differentiates, driven_by, expressed_by, guaranteed_by, guarantees, improves, instance_of, instantiates, invokes, judged_by, lowered_from, must_preserve, operates_on, organized_as, organizes, preserved_through, produced_by, relied_upon_by, shapes, substrate_for, supported_by, used_by, uses, verifiable_by, verified_by). The preserve/verify pair (operates_on + preserves + verified_by) is the cycle's new graph motif — transformation complexity moved into constraint-carrying relationships.

## Cycle 009 — Qualification Growth

176 total events (80 claims + 48 observations + 48 recommendations); 517 cumulative across Cycles 007–009. Continuation metric confirmed for a third consecutive cycle, now at the correctness pole: uncertainty and guarantees are both expressed as qualification of evidence, not as new evidence types.

## Cycle 009 — Object Kind Evolution

No new kinds. 12 concept, 2 pattern (optimization-pass, build-systems), 2 decision (optimization-tradeoffs, debug-vs-release-modes). Cumulative: **4** (unchanged). Decision Factors on exactly 3 of 16 objects (formal-verification, optimization-tradeoffs, debug-vs-release-modes) — all decision-bearing objects; none of the 13 representation/transformation/guarantee/measurement objects carried them.

## Cycle 009 — Discoveries

1. Correctness is relative to a stated observation model — the qualification counterpart of uncertainty; candidate for the programme's biggest theoretical contribution (Tier 1).
2. Validity conditions generalize from knowledge to actions: enabling conditions bind transformations; artifact validity binds builds (Tiers 2 + 4).
3. Evidence about evidence: machine-checked proof is the strongest-confidence observation, represented as evidence + constraints + relationships, with the specification as the residual risk (Tier 3).
4. Mode divergence is a behavioural decision: debug/release builds are distinct programs with distinct behaviour contracts; release-only bugs are decision consequences (Tier 4).

## Cycle 009 — Failed Hypotheses / Near Failures

- **The pre-registered possible failure candidate (proof) was the closest approach to falsification** — and resolved through composition: the decisive framing was "a proof is an artifact of evidence", moving the risk to the specification rather than the vocabulary.
- **All 12 recorded temptations rejected** — representation, formal rule, semantics, transformation, fold, liveness, pipeline/sequence, proof, equivalence, performance, artifact validity, mode divergence.
- **Outcome space result**: outcome A (composition) dominant and outcome B (new motif — preserve/verify pair) both occurred; outcome C (falsification) did not. Two consecutive "not a separate class" results (008 adaptive, 009 transformational).
- **Open questions**: (1) are validity conditions and enabling conditions one pattern with two instantiations — the unification hypothesis: every validity claim in engineering is bound by stated conditions, and the conditions are constraints (n=2, needs a third domain); (2) is observation-model scoping the qualification counterpart of correctness — same structure as uncertainty qualification, opposite pole (confidence vs guarantee), not yet formalized as a metric; (3) does the second-order evidence graph (proofs about guarantees) need a depth metric as corpora grow, or is ordinary graph growth sufficient?

## Cycle 009 — Validation Evidence

| Metric | Value |
|---|---|
| Objects created | 16 (all PASS 0/0) |
| Passing objects (cumulative) | 73 |
| Corpus (cumulative) | 90 |
| Outcome classification | 0 Failure / 4 Discovery / 12 Confirmation |
| Warnings | 0 |
| Instrument stability | 9 cycles unchanged |

## Cycle 009 — End-of-Cycle Interpretation

- **What increased**: Objects (+16), qualification (176 events), relationship motifs (+37 — the cycle's largest), domain coverage (Transformational).
- **What stayed constant**: 9 primitives, 4 object kinds, all instruments.
- **Where did complexity move**: Into constraint-carrying relationships (preserve/verify pair) + qualification (observation-model scoping) + decision structure — three existing destinations, no new one.
- **Did vocabulary expand**: No.
- **Did the graph become richer**: Yes — the transformation ladder, the preserve/verify motif, and the second-order evidence graph (verification objects relating to guarantee objects).

---

# Cycle 010 — Databases / Data Semantics

*Date: 2026-07-31. Experimental target: Data Semantics Knowledge Test. Knowledge category: Data semantics — the schema as a model of the world, and the guarantees held over it.*

**The cycle that tests whether *holding data* requires a new primitive.** Databases were selected at the Phase 5 checkpoint for falsification value, not novelty: data is the only untested universal — every prior category consumes data — and the domain re-tests two established resolutions at higher n (transformation via query optimization, validity conditions via schema migration — the unification hypothesis n=3 test). Each tier is documented separately.

## Pre-registration (recorded before authoring)

- **H₁**: Data semantics — the schema as a model of the world and the guarantees held over it — will resolve through composition: constraints (integrity, consistency, normal forms) + relationships (schema evolution, query equivalence) + qualification (validity under stated conditions) + decision structure.
- **H₀**: Data semantics requires a new epistemic mode — data/entity, ACID/transaction, query/index, migration/replication constructs.
- **Test question**: Does data semantics — the schema as a model of the world, and the guarantees held over it — introduce a new epistemic mode that cannot be decomposed into existing evidence structures?
- **Pressure predictions**: Data Semantics Very High (new — the schema as model of the world); Structural Medium; Granularity Medium; Constraints Very High (new — the cycle's sharpest pressure); Decision Factors High; Representation Failure none expected (falsification target).
- **Predictions**: P1 no new primitive; P2 integrity/ACID = guarantee-object pattern (from 009 type-safety); P3 unification hypothesis n=3 test via schema migration (schema validity joins knowledge validity 008, enabling conditions 009, artifact validity 009); P4 query optimization = transformation pattern n=2 with cross-domain link to equivalence-checking; P5 data/entity temptation = coincidence is evidence.
- **Outcome space**: A — composition (decomposition into existing destinations); B — discovery (cross-domain recognition motif); C — vocabulary expansion (falsification).
- **Observation metrics** (no schema change): constraint-carrying objects, guarantee objects, derivation events, cross-domain links.
- **Pre-authoring addenda**: Tier 1 (relational-model coincidence prediction; schema-design as hardest object; normalization as pattern; no DB-specific kinds); Tier 2 (ACID temptation; transaction as unit-of-work — temporal trap prediction; isolation-levels as decision; transaction-failures with retry cross-domain link); Tier 3 (query optimization n=2 re-test; query-planning and index-selection as decisions; database-indexing as pattern; redundant-structure question); Tier 4 (schema migration as unification n=3; replication as consistency re-test; backup RPO/RTO; governance as decision with lineage reappearing; backup validity as derivation).
- **Discipline constraint**: no database-specific object kinds — ACID → constraints + guarantees; transaction → concept with failure modes; isolation → decision; index → pattern; migration → validity conditions; integrity → constraints.

## Tier 1 — Data Model

- **Pressure**: the data/entity primitive temptation; the schema-as-model-of-the-world pressure (the cycle's central question); the relational-model coincidence question.
- **Prediction**: the relational model's entities/relationships/keys map onto HPF's entities/relationships/constraints — coincidence is evidence, not accident; schema-design is the hardest object (structurally identical to program-semantics in 009); normalization resolves as pattern with normal forms as structural constraints; no DB-specific kinds.
- **Objects** (all PASS 0/0):
  - **relational-model (concept)** — Data as relations. Blocks: 8. Relationships: defines, describes, scopes, shapes, guides. Failure modes: relation_design_error, implicit_schema, normalization_violation.
  - **schema-design (concept)** — The model of the world. Blocks: 8. Relationships: constrained_by, influenced_by, executed_under, must_preserve, preserved_by, reinforced_by. Failure modes: schema_mismatch, inflexible_schema, silent_schema_change.
  - **data-integrity (concept)** — The scoped data guarantee. Blocks: 8. Relationships: protected_by, rationalized_by, manipulated_by, governed_by, enables. Failure modes: integrity_violation, silent_corruption, validation_gap.
  - **normalization (pattern)** — Normal forms as structural constraints. Blocks: 8. Relationships: instantiates, protects, eliminates, guided_by. Failure modes: over_normalization, denormalization_without_discipline, update_anomaly.
- **Result**: Prediction 5 held by coincidence — the relational model's entities/relationships/keys map directly onto HPF's entities/relationships/constraints, treated as evidence (coincidence-as-evidence), not accident. Schema-design was the hardest object as predicted, structurally identical to program-semantics (009): the schema is the model of the world, and the model is a concept with constraints. Data-integrity resolved as guarantee object #2 (type-safety pattern from 009). Normal forms resolved as structural constraints — no normal-form primitive.
- **Discovery (Tier 1)**: *Coincidence-as-evidence.* The relational model is an independent re-discovery of entity/relationship structure — the mapping onto HPF vocabulary is a data point, not a coincidence to explain away.

## Tier 2 — Transactions & Consistency

- **Pressure**: the ACID/transaction primitive temptation (the cycle's sharpest); the temporal-trap temptation (transaction as duration); the anomaly taxonomy as constraint structure.
- **Prediction**: ACID resolves as constraints + guarantee objects; a transaction is "a unit of work with constraints on its outcome, not on its duration" (the temporal trap defused); isolation-levels is a decision with 4 Decision Factors; transaction-failures links cross-domain to retry-pattern (006).
- **Objects** (all PASS 0/0):
  - **transactions (concept)** — A unit of work. Blocks: 8. Relationships: executes_under, scoped_by, influenced_by, constrained_by, requires. Failure modes: partial_commit, lost_update, transaction_abort.
  - **atomicity (concept)** — The all-or-nothing guarantee. Blocks: 8. Relationships: guaranteed_by, contained_by, determines, requires. Failure modes: partial_commit, corrupted_state, masking_guarantee_violation.
  - **isolation-levels (decision)** — The concurrency posture decision. Blocks: 9 (incl. Decision Factors: consistency_requirement, concurrency_demand, failure_cost, retry_tolerance). Relationships: selects_among, scopes, defines, constrains. Failure modes: isolation_misconfiguration, phantom_read_surprise, serializability_degradation.
  - **transaction-failures (concept)** — Failure and recovery of transactional work. Blocks: 8. Relationships: caused_by, mitigated_by (→ retry-pattern), influenced_by, executes_under. Failure modes: lock_timeout, distributed_commit_failure, in_doubt_transaction.
- **Result**: ACID resolved exactly as predicted — atomicity is guarantee object #3 (scoped claim + invariants + failure modes, structurally identical to type-safety 009 and data-integrity 010); the anomaly taxonomy is constraint structure, not a primitive. The temporal trap was defused: a transaction is a unit of work with constraints on its outcome, not on its duration — the fourth temporal trap resolved in the programme. The cycle's first cross-domain link landed: `transaction-failures → retry-pattern: mitigated_by` (Cycle 006 corpus) — the second cross-domain link after deployment-risk → risk-acceptance (008↔007).
- **Discovery (Tier 2)**: *Temporal traps recur and resolve identically.* Four times now (005 sequence, 008 drift, 009 ordering, 010 transaction) the temporal temptation resolved as constraints on outcome validity, not duration — the programme's most robust rejection channel.

## Tier 3 — Query & Indexing

- **Pressure**: the query/index primitive temptation; the redundant-structure question (indexes as copies); the transformation re-test at n=2.
- **Prediction**: query optimization = the Cycle 009 transformation pattern (before-state + rewrite + after-state + equivalence constraint under the relational observation model, the result relation as contract) with cross-domain link to compiler-optimization/equivalence-checking; query-planning and index-selection both decisions with 4 Decision Factors; database-indexing as pattern; redundant-structure needs no construct (redundancy-with-controls).
- **Objects** (all PASS 0/0):
  - **query-planning (decision)** — The execution strategy decision. Blocks: 9 (incl. Decision Factors: statistics_reliability, join_order_freedom, cost_model_fidelity, plan_stability). Relationships: selects_among, informs, evaluates. Failure modes: stale_statistics, plan_regression, cartesian_plan.
  - **index-selection (decision)** — The access-path decision. Blocks: 9 (incl. Decision Factors: query_workload, write_amplification, storage_cost, selectivity). Relationships: informs, depends_on, constrained_by. Failure modes: index_bloat, unused_index, write_amplification.
  - **query-optimization (concept)** — Semantic-preserving query rewriting. Blocks: 8. Relationships: analogous_to (→ compiler-optimization), bounded_by (→ equivalence-checking), operates_upon, preserves. Failure modes: suboptimal_plan, wrong_result_optimization, cost_model_drift.
  - **database-indexing (pattern)** — Maintained copies in alternate orderings. Blocks: 8. Relationships: serves, supported_by, constrained_by, contained_by. Failure modes: index_staleness, index_bloat, full_scan_fallback.
- **Result**: All 5 addendum predictions held. Query optimization re-tested the transformation pattern at n=2 with the cross-domain recognition: "An optimizer is a compiler for a declarative language; its bugs are miscompilations" — the first database↔compiler link (`analogous_to` compiler-optimization, `bounded_by` equivalence-checking). Query planning produced a finding: "the planner's output is a recommendation, not a guarantee — plans are hypotheses about cost that runtime evidence can falsify" — the quality-claim pattern from 009 applied to plans. Database-indexing resolved as redundancy-with-controls: "an index is a maintained copy of data in a different ordering"; "A B-tree is an ordering discipline, not a new category of information."
- **Discovery (Tier 3)**: *Cross-domain recognition.* The optimizer-is-compiler recognition tied the 009 transformation pattern to data — the first time two tested categories recognized each other in the corpus, adding the analogous_to motif as the cycle's new graph pattern.

## Tier 4 — Operational Data

- **Pressure**: the migration/replication/recovery primitive temptations; the unification hypothesis n=3 test; lineage's third resolution.
- **Prediction**: schema migration = unification n=3 (schema validity joins knowledge validity 008, enabling conditions 009, artifact validity 009 — validity as derivation, no migration primitive); replication = consistency re-test (pattern constrained by the consistency model, links to 006 corpus); backup recovery = pattern with RPO/RTO as constraints (backup validity = derivation); data governance = decision with 4 Decision Factors (lineage reappears — resolved again as observation + constraint, no lineage primitive).
- **Objects** (all PASS 0/0):
  - **schema-migration (concept)** — Disciplined schema change. Blocks: 8. Relationships: evolves (→ schema-design), must_preserve (→ data-integrity), executed_under (→ transactions), analogous_to (→ build-systems), affected_by (→ query-optimization). Failure modes: contract_break, data_loss, migration_failure_partial.
  - **replication (pattern)** — Maintained copies across nodes. Blocks: 8. Relationships: constrained_by (→ strong-consistency), allows (→ eventual-consistency), subject_to (→ split-brain), supports (→ transactions), complicates (→ atomicity). Failure modes: divergence, split_brain, lag_surprise.
  - **backup-recovery (pattern)** — Restoring data to a defined point. Blocks: 8. Relationships: restores (→ data-integrity), supported_by (→ atomicity), guards (→ schema-migration), governed_by (→ data-governance), analogous_to (→ build-systems). Failure modes: unverified_backup, rpo_violation, restore_failure_at_incident.
  - **data-governance (decision)** — The data value/risk decision. Blocks: 9 (incl. Decision Factors: retention_requirement, access_scope, lineage_traceability, compliance_cost). Relationships: protects (→ data-integrity), constrains (→ schema-migration), directs (→ backup-recovery), analogous_to (→ training-data). Failure modes: shadow_data, lineage_gap, policy_decay.
- **Result**: All 5 addendum predictions held. The unification hypothesis survived n=3: schema validity = derivation ("the migrated schema is valid if derived from its predecessor under stated conditions") — structurally identical to knowledge validity (008), enabling conditions (009), and artifact validity (009). Replication re-tested consistency at n=2: "the corpus already modeled the consistency spectrum; replication added the operational layer, not a new construct." Backup validity = derivation, with the sharpest observation: "Backups are a claim until a restore proves them — rehearsal is the only verification." Lineage resolved as observation + constraint for the third time (008 training-data, 010 governance) — "Lineage is an observation with a traceability obligation."
- **Discovery (Tier 4)**: *The unification hypothesis at n=3.* Three domains now agree that every validity claim in engineering is bound by stated conditions, and the conditions are constraints — validity-as-derivation spans build artifacts (009), schema versions (010), and backups (010). The hypothesis is now a theory candidate, not a pattern.

## Cycle 010 — Primitive Pressure Analysis (complete list of temptations)

| Candidate | Why it looked necessary | How tested | Why rejected | Final representation |
|---|---|---|---|---|
| Data/entity primitive | The relational model maps entities/relationships/keys onto schema structure | Entities + relationships + constraints | The mapping onto HPF vocabulary is coincidence-as-evidence — the relational model is an independent re-discovery of the same structure | defines, describes, scopes; relational-model → schema-design |
| ACID/transaction primitive | Transactions guarantee atomicity, consistency, isolation, durability | Constraints (invariants) + guarantee objects (type-safety pattern) + failure modes | ACID decomposes into constraints on outcome, not a new construct — atomicity is guarantee object #3 | guaranteed_by, contained_by, requires; outcome-validity constraints |
| Temporal-trap construct | Transactions look duration-bound (begin/commit) | A unit of work with constraints on its outcome | Constraints bind outcome validity, not duration — the fourth temporal trap resolved | executes_under, scoped_by; outcome-validity constraints |
| Isolation/consistency primitive | Isolation levels look like a distinct knowledge type | Decision object with 4 Decision Factors | Isolation is a posture decision — same structure as risk-acceptance (007) | selects_among, scopes, defines; consistency_requirement, concurrency_demand, failure_cost, retry_tolerance |
| Query/index primitive | Query planning and index selection look like DB-specific constructs | Two decision objects + one pattern (redundancy-with-controls) | Planning/selection are decisions; indexes are maintained copies — no construct | informs, depends_on; query_workload, write_amplification, storage_cost, selectivity |
| Migration/evolution primitive | Schema evolution looks like a distinct operation | Validity-as-derivation + enabling conditions + failure modes | Migration is the unification hypothesis n=3 — schema validity = derivation, same as build artifacts | evolves, analogous_to (build-systems); derivation invariant |
| Replication primitive | Copying data across nodes looks new | Pattern constrained by the consistency model (006 corpus) | The corpus already modeled the consistency spectrum — replication adds the operational layer | constrained_by (strong-consistency), subject_to (split-brain); model-constrains-replicas invariant |
| Lineage primitive (third appearance) | Derivation history looks like a new knowledge type | Observation + constraint, as resolved in 008 (training-data) | Lineage is an observation with a traceability obligation — resolved the same way three times | analogous_to (training-data); traceability constraints |

## Cycle 010 — Schema Interaction

```
Schema changed:      NO
Parser changes:      NO
Validator changes:   NO
Analyzer changes:    NO
Friction:            0
Rejected changes:    All 8 candidates above (19 temptations recorded across 4 addenda, all rejected)
```

## Cycle 010 — Relationship Growth

82 relationship edges across 16 objects; 60 unique motifs in-cycle; **34 new to the corpus** (afflict, allows, analogous_to, audited_by, caused_by, conditioned_by, contained_by, dependent_on, directs, evolves, executed_under, exploited_by, governs, guides, independent_of, manipulated_by, mitigated_by, operated_upon_by, operates_upon, performed_by, performs, preserved_by, protected_by, rationalized_by, reinforced_by, reinforces, restores, scopes, selected_by, selects_among, serves, subject_to, threatened_by). The cycle's new graph motif is cross-domain recognition: `analogous_to` (4 uses) tying database objects to the 006/008/009 corpora — transaction-failures → retry-pattern, query-optimization → compiler-optimization/equivalence-checking, schema-migration → build-systems, backup-recovery → build-systems, data-governance → training-data, replication → strong-consistency/eventual-consistency/split-brain. The corpus became a single cross-domain graph, not a collection of silos.

## Cycle 010 — Qualification Growth

176 total events (80 claims + 48 observations + 48 recommendations); 693 cumulative across Cycles 007–010. Continuation metric confirmed for a fourth consecutive cycle: uncertainty, guarantees, and now data semantics are all expressed as qualification of evidence, not as new evidence types.

## Cycle 010 — Object Kind Evolution

No new kinds. 8 concept, 4 pattern (normalization, database-indexing, replication, backup-recovery), 4 decision (isolation-levels, query-planning, index-selection, data-governance). Cumulative: **4** (unchanged). All 4 decision objects carried exactly 4 Decision Factors — the factor count held at 4 across all decision objects since 007 (risk-acceptance, retraining-decisions, optimization-tradeoffs, debug-vs-release-modes, isolation-levels, query-planning, index-selection, data-governance).

## Cycle 010 — Discoveries

1. The unification hypothesis at n=3: schema validity = derivation — joining knowledge validity (008), enabling conditions (009), and artifact validity (009); three domains agree that every validity claim in engineering is bound by stated conditions, and the conditions are constraints (Tier 4).
2. Coincidence-as-evidence: the relational model's entities/relationships/keys map onto HPF's entities/relationships/constraints — an independent domain rediscovering the same structure, treated as evidence (Tier 1).
3. Cross-domain recognition: "An optimizer is a compiler for a declarative language; its bugs are miscompilations" — the 009 transformation pattern recognized across execution targets, the first database↔compiler link (Tier 3).
4. Backup validity = derivation: "Backups are a claim until a restore proves them" — the artifact-validity pattern applied to data, RPO/RTO as the recovery contract (Tier 4).
5. Lineage's third resolution: observation + constraint in 008 (training-data) and again in 010 (governance) — never a primitive, now the most frequently re-tempted primitive in the programme (Tier 4).

## Cycle 010 — Failed Hypotheses / Near Failures

- **The strongest candidate — data semantics as a new epistemic mode — resolved through composition**: the schema-as-model-of-the-world is a concept with constraints; ACID guarantees are guarantee objects; query equivalence is a relationship under the relational observation model; migration is validity-as-derivation. No near-failure this cycle — the closest approach was the unification hypothesis itself, which was a predicted confirmation, not a failure.
- **All 19 recorded temptations rejected** (8 candidate families): data/entity, ACID, temporal-trap, isolation, query/index, migration, replication, lineage (third appearance).
- **Outcome space result**: outcome A (composition) dominant and outcome B (new motif — cross-domain recognition: analogous_to) both occurred; outcome C (falsification) did not. Three consecutive "not a separate class" results (008 adaptive, 009 transformational, 010 data semantics).
- **Open questions**: (1) unification hypothesis boundary — three domains agree; a fourth non-obvious domain where validity is not bound by stated conditions would falsify it; (2) observation-model limit — the abstraction found its third application (result relation, consistency model, recovery contract); (3) the coincidence finding — is the relational model mapping deep or shallow?; (4) lineage's frequency — most re-tempted primitive; is the frequency itself meaningful?; (5) derivation vs qualification — does derivation subsume the temporal-validity pattern (008's validity_until)?; (6) cross-domain graph as theory locus — is the cross-domain graph the actual locus of the theory?; (7) decision-factor count — every decision object has exactly 4 factors; an object needing five would be the anomaly; (8) governance as the ethics boundary — compliance cost is the first constraint source that is legal, not engineering.

## Cycle 010 — Validation Evidence

| Metric | Value |
|---|---|
| Objects created | 16 (all PASS 0/0) |
| Passing objects (cumulative) | 89 |
| Corpus (cumulative) | 106 |
| Outcome classification | 0 Failure / 5 Discovery / 11 Confirmation |
| Warnings | 0 |
| Instrument stability | 10 cycles unchanged |

## Cycle 010 — End-of-Cycle Interpretation

- **What increased**: Objects (+16), qualification (176 events), relationship motifs (+34), domain coverage (Data semantics), cross-domain links (6, corpus became a single graph).
- **What stayed constant**: 9 primitives, 4 object kinds, all instruments.
- **Where did complexity move**: Into constraints + validity conditions (unification n=3) + decision structure + cross-domain relationships — existing destinations, no new one.
- **Did vocabulary expand**: No.
- **Did the graph become richer**: Yes — the corpus is now a single cross-domain graph with recognition links between databases, compilers, distributed systems, and machine learning.

---

# Cycle 011 — Real-Time Systems / Temporal Guarantees

*Date: 2026-08-01. Experimental target: Temporal Guarantees Knowledge Test. Knowledge category: Temporal guarantees — time as a correctness condition itself, not a qualifier.*

**The cycle that tests whether *time as a correctness condition* requires a new primitive.** Real-time systems were selected at the Cycle 010 review for falsification value, not novelty: the programme has defused temporal temptations four times (005 sequence, 008 drift, 009 ordering, 010 transaction — "constraints bind outcome validity, not duration"), and real-time is the strongest remaining form of the pressure. If deadline/schedulability/WCET resolve through composition, the temporal-trap chain reaches its fifth defusal; if the pressure maps onto no existing destination, that is the attractor-state falsification signal. Each tier is documented separately.

## Pre-registration (recorded before authoring)

- **H₁**: Hard temporal guarantees will resolve through composition: constraints (time as validity condition) + qualification (WCET as observation with confidence) + decision structure (scheduling as posture decision) + motif topology (arbitration candidate).
- **H₀**: Temporal guarantees require a new epistemic mode — time/deadline, scheduling, schedulability-guarantee, overload/isolation constructs.
- **Test question**: Do hard temporal guarantees — deadlines, schedulability, worst-case execution time — introduce a new epistemic mode that cannot be decomposed into existing evidence structures?
- **Pressure predictions**: Temporal Guarantees Very High (new); Structural Medium; Granularity Medium; Decision Factors High; Representation Failure none expected (falsification target).
- **Predictions**: P1 no new primitive; P2 deadline = validity condition on completion (unification at the temporal pole); P3 WCET = observation; P4 scheduling policy = decision with 4 Decision Factors; P5 cross-domain links.
- **Outcome space**: A — composition (decomposition into existing destinations); B — discovery (arbitration motif candidate); C — vocabulary expansion (falsification).
- **Observation metrics** (no schema change): Temporal Constraint Density (new — added at the research lead's request before authoring; edge-level: how many validity relationships are expressed through time-bounded constraints), temporal-trap chain, guarantee objects, arbitration watch.
- **Pre-authoring addenda**: 5 per tier (19 predictions total), each recorded before its tier's authoring.
- **Discipline constraint**: time may appear as constraint content but never as ontology — the hidden-primitive-through-language watch; the `temporal_constraint` category label was rejected in Tier 1. No real-time object kinds.

## Tier 1 — Temporal Model

- **Pressure**: the time/deadline primitive temptation; the temporal-trap chain's fifth test.
- **Prediction**: deadline = validity condition on completion (completion ≤ T as a constraint on outcome validity); WCET = observation with confidence, not a guarantee; the scheduling-policy temptation deferred to Tier 2; no temporal category label.
- **Objects** (all PASS 0/0):
  - **real-time-system (concept)** — The system whose correctness depends on timing. Blocks: 8. Relationships: affected_by (→ deployment-risk), analogous_to (→ build-systems). Failure modes: deadline_miss, jitter_violation, timing_validation_gap.
  - **deadline (concept)** — The validity condition on completion. Blocks: 8. Relationships: analogous_to (→ transactions, → backup-recovery). Failure modes: missed_deadline, implicit_deadline, deadline_ambiguity.
  - **worst-case-execution-time (concept)** — The timing estimate. Blocks: 8. Relationships: analogous_to (→ benchmark-validity, → query-planning). Failure modes: wcet_underestimation, wcet_optimism, measurement_unsoundness.
  - **task-scheduling (concept)** — Allocation of CPU time to tasks. Blocks: 8. Relationships: analogous_to (→ quorum, → backpressure). Failure modes: priority_starvation, missed_deadline, overload.
- **Result**: All 5 addendum predictions held. The fifth temporal defusal landed: "a result produced after its deadline is invalid regardless of its content" — deadline = validity condition on completion, the unification hypothesis extended to the temporal pole (n=5). WCET resolved as observation with confidence: "the strongest guarantee in real-time rests on an estimate" — the same prediction-object structure as benchmarks (008) and query plans (010). The `temporal_constraint` category label was rejected as hidden-primitive-through-language: time is constraint content, not ontology.
- **Discovery (Tier 1)**: *The fifth temporal defusal.* The temporal-trap chain (005 sequence, 008 drift, 009 ordering, 010 transaction, 011 deadline) now resolves identically five times: time binds outcome validity, never duration, never ontology. The unification hypothesis reached n=5.

## Tier 2 — Scheduling

- **Pressure**: the scheduling-policy primitive temptation; the arbitration question (allocation structures recurring across 006 consensus, 010 locking, 011 scheduling).
- **Prediction**: scheduling-policy = decision with 4 Decision Factors; fixed-priority-scheduling = pattern; rate-monotonic-analysis = concept (feasibility test as claim + evidence + constraints); earliest-deadline-first = concept with conditional optimality; the arbitration structure resolved as graph topology, not a construct.
- **Objects** (all PASS 0/0):
  - **scheduling-policy (decision)** — The task-allocation posture decision. Blocks: 9 (incl. Decision Factors: deadline_priority, utilization_target, task_criticality, preemption_allowance). Relationships: analogous_to (→ isolation-levels). Failure modes: policy_mismatch, priority_inversion, head_of_line_blocking.
  - **fixed-priority-scheduling (pattern)** — Static priority assignment. Blocks: 8. Relationships: analogous_to (→ leader-election). Failure modes: priority_inversion, priority_starvation, utilization_overrun.
  - **rate-monotonic-analysis (concept)** — The feasibility test. Blocks: 8. Relationships: analogous_to (→ equivalence-checking, → benchmark-validity). Failure modes: utilization_overrun, analysis_pessimism, deadline_miss.
  - **earliest-deadline-first (concept)** — Deadline-ordered dynamic scheduling. Blocks: 8. Relationships: analogous_to (→ leader-election, → quorum). Failure modes: overload_instability, deadline_miss.
- **Result**: All 5 addendum predictions held. The arbitration watch (recorded at the research lead's direction) resolved: contenders + selection rule + allocation + guarantee = graph topology, not a construct — arbitration is a motif candidate (n≥3: scheduling 011, consensus 006, locking 010), recorded as candidate, not catalogue entry. Feasibility testing resolved as claim + evidence + constraints: "a schedulability test is a claim about the task set, evidenced by analysis under stated assumptions."
- **Discovery (Tier 2)**: none new — Tier 2 confirmed the decision + pattern structure from 009/010 (the arbitration candidate is a motif observation, not a construct).

## Tier 3 — Guarantees

- **Pressure**: the schedulability-guarantee primitive temptation; the pre-registered danger object (priority inversion — does concurrency semantics force a new primitive?); the isolation family.
- **Prediction**: schedulability-analysis = concept generalizing rate-monotonic-analysis; real-time-guarantee = the fourth guarantee object (type-safety 009 pattern); priority-inversion resolved as failure mode + constraint + mitigation pattern, no concurrency-failure primitive; temporal-isolation = the isolation family's third member.
- **Objects** (all PASS 0/0):
  - **schedulability-analysis (concept)** — The feasibility claim. Blocks: 8. Relationships: analogous_to (→ formal-verification). Failure modes: analysis_pessimism, unsound_analysis, deadline_miss.
  - **real-time-guarantee (concept)** — The scoped timing guarantee. Blocks: 8. Relationships: analogous_to (→ type-safety, → data-integrity). Failure modes: guarantee_overreach, validation_gap, deadline_miss.
  - **priority-inversion (concept)** — The timing anomaly. Blocks: 8. Relationships: analogous_to (→ split-brain). Failure modes: unbounded_blocking, priority_inheritance_breakdown, deadlock.
  - **temporal-isolation (pattern)** — Partitioning to contain timing interference. Blocks: 8. Relationships: analogous_to (→ isolation-levels, → strong-consistency). Failure modes: cross_partition_interference, partition_violation.
- **Result**: All 5 addendum predictions held. The guarantee-object motif reached n=4 (type-safety 009, data-integrity 010, atomicity 010, real-time-guarantee 011). Priority-inversion — the cycle's declared danger object — resolved without a concurrency-failure primitive: failure mode + priority-ordering invariant ("the priority ordering is an invariant of correct scheduling") + mitigation pattern (priority inheritance/ceiling). The isolation family now spans three domains: consistency (006 strong-consistency), concurrency (010 isolation-levels), timing (011 temporal-isolation) — "guarantee separation is one structure across the corpus."
- **Discovery (Tier 3)**: *The isolation family across three domains.* Temporal isolation joined consistency isolation and concurrency isolation — guarantee separation recognized as a single structure at n=3, confirming the 010 finding that guarantees are separated by stated bounds, not by domain.

## Tier 4 — Operational Reality

- **Pressure**: the overload/isolation temptation; the mode-divergence question; the watchdog/health-check temptation.
- **Prediction**: hard-vs-soft-real-time = decision with 4 Decision Factors (mode-divergence pattern from 009); watchdog-timer = pattern with a reset-discipline invariant; overload-handling = concept in the bounded-response family; real-time-throughput-tradeoff = decision with 4 Decision Factors.
- **Objects** (all PASS 0/0):
  - **hard-vs-soft-real-time (decision)** — The timing-posture decision. Blocks: 9 (incl. Decision Factors: miss_consequence, timing_strictness, workload_variability, degradation_policy). Relationships: analogous_to (→ optimization-tradeoffs). Failure modes: posture_mismatch, soft_system_degradation, hard_system_overload.
  - **watchdog-timer (pattern)** — The temporal health check. Blocks: 8. Relationships: analogous_to (→ incident-response, → health-check-pattern). Failure modes: false_trigger, missed_stall, reset_abuse.
  - **overload-handling (concept)** — Admission and shedding under overload. Blocks: 8. Relationships: analogous_to (→ backpressure, → circuit-breaker). Failure modes: cascading-failure, shed_essential_work, overload_oscillation.
  - **real-time-throughput-tradeoff (decision)** — The timing/throughput posture decision. Blocks: 9 (incl. Decision Factors: timing_sensitivity, throughput_target, resource_budget, deadline_margin). Relationships: analogous_to (→ optimization-tradeoffs, → compiler-performance). Failure modes: throughput_overreach, deadline_margin_erosion, measurement_drift.
- **Result**: All 5 addendum predictions held. The bounded-response family reached n=4 (overload-handling, backpressure, circuit-breaker, cascading-failure — the same structure in 006 and 011). Hard-vs-soft resolved as mode divergence: "the same system can change posture by decision" — per-mode validation required. Watchdog resolved with the sharpest invariant: "a stalled task must not reset its own watchdog" — the reset discipline is the invariant. The cycle's last observation: "throughput is measured; the guarantee is claimed."
- **Discovery (Tier 4)**: *The bounded-response family at n=4.* Overload handling is the same structure as backpressure and circuit-breaker (006) — bounded response to pressure, now at n=4 across the corpus.

## Cycle 011 — Primitive Pressure Analysis (complete list of temptations)

| Candidate | Why it looked necessary | How tested | Why rejected | Final representation |
|---|---|---|---|---|
| Time/deadline primitive | Real-time correctness looks like a new category — time as the correctness condition itself | Constraints (time as validity condition on completion) | "A result produced after its deadline is invalid regardless of its content" — time binds outcome validity, the fifth temporal defusal | deadline as concept; completion ≤ T as constraint |
| Scheduling-policy primitive | Task allocation/discipline looks distinct from general knowledge | Decision object with 4 Decision Factors | Scheduling is a posture decision — same structure as isolation-levels (010) | scheduling-policy as decision; deadline_priority, utilization_target, task_criticality, preemption_allowance |
| Schedulability-guarantee primitive | Feasibility analysis looks like a proof construct | Claim + evidence + constraints (generalizes rate-monotonic-analysis) | A schedulability test is a claim about the task set under stated assumptions | schedulability-analysis as concept; analogous_to formal-verification (009) |
| Concurrency/priority primitive | Priority inversion looks like concurrency semantics | Failure mode + invariant + mitigation pattern | Priority is constraint + relationship; no concurrency-failure primitive | priority-inversion as concept; analogous_to split-brain (006) |
| Temporal-constraint category (hidden primitive) | "Time" as a category label in constraints | Rejected in Tier 1 as hidden-primitive-through-language | Time is constraint content, not ontology | time-bounded constraints (100% of Tier 1–4 constraints) |
| Overload/isolation primitive | Overload handling looks like admission-control logic | Bounded-response constraints (backpressure/circuit-breaker family) | Prevents cascading-failure — same structure as 006, n=4 | overload-handling as concept |
| Watchdog/health-check primitive | Detection mechanisms look like a new knowledge type | Pattern with reset-discipline invariant | Detection = temporal health check — a pattern, not a construct | watchdog-timer as pattern; false_trigger, missed_stall, reset_abuse |
| Arbitration construct | Allocation recurs across scheduling (011), consensus (006), locking (010) | Resolved as graph topology — contenders + selection rule + allocation + guarantee | Graph topology, not a construct; recorded as motif candidate | Arbitration candidate (n≥3), not catalogue entry |

## Cycle 011 — Schema Interaction

```
Schema changed:      NO
Parser changes:      NO
Validator changes:   NO
Analyzer changes:    NO
Friction:            0
Rejected changes:    All 8 candidate families above (19 temptations recorded across 4 addenda, all rejected)
```

## Cycle 011 — Relationship Growth

80 relationship edges across 16 objects; 44 unique motifs in-cycle; **26 new to the corpus** (including afflicts, allocates_within, realizes, consumes, generalizes, orders_by, trades_against). Cross-domain recognition continued: 8 `analogous_to` links bind the real-time corpus to the 006/008/009/010 corpora — real-time-system → build-systems, deadline → transactions/backup-recovery, WCET → benchmark-validity/query-planning, scheduling-policy → isolation-levels, RMA → equivalence-checking, schedulability-analysis → formal-verification, real-time-guarantee → type-safety/data-integrity, priority-inversion → split-brain, temporal-isolation → isolation-levels/strong-consistency, overload-handling → backpressure/circuit-breaker, watchdog → incident-response, throughput-tradeoff → optimization-tradeoffs/compiler-performance. The single cross-domain graph now spans five tested categories.

## Cycle 011 — Temporal Constraint Density (new observation dimension)

Added at the research lead's request before authoring. Edge-level metric: how many validity relationships are expressed through time-bounded constraints.

| Tier | Constraints time-bounded | Edges time-bounded |
|---|---|---|
| T1 — Temporal Model | 100% (8/8) | 45% (9/20) |
| T2 — Scheduling | 100% (8/8) | 40% (8/20) |
| T3 — Guarantees | 100% (8/8) | 45% (9/20) |
| T4 — Operational Reality | 100% (8/8) | 40% (8/20) |
| **Cycle total** | **100% (32/32)** | **42.5% (34/80)** |

The metric discriminated exactly as predicted: the temporal core (T1) and guarantee tier (T3) peak at 45% edges; the decision layers (T2, T4) dilute to 40%. No earlier cycle had 100% temporal constraints — the metric cleanly separates the real-time category from all prior cycles.

## Cycle 011 — Qualification Growth

176 total events (80 claims + 48 observations + 48 recommendations); 869 cumulative across Cycles 007–011. Continuation metric confirmed for a fifth consecutive cycle: temporal guarantees are expressed as qualification of evidence, not as new evidence types.

## Cycle 011 — Object Kind Evolution

No new kinds. 8 concept, 4 pattern (fixed-priority-scheduling, temporal-isolation, watchdog-timer), 4 decision (scheduling-policy, hard-vs-soft-real-time, real-time-throughput-tradeoff). Cumulative: **4** (unchanged). All 3 decision objects carried exactly 4 Decision Factors — the factor count held at 4 across all decision objects since 007 (risk-acceptance, retraining-decisions, optimization-tradeoffs, debug-vs-release-modes, isolation-levels, query-planning, index-selection, data-governance, scheduling-policy, hard-vs-soft-real-time, real-time-throughput-tradeoff — 11 total). The decision-object count as a fraction of the corpus is stable; an object needing five factors would be the anomaly.

## Cycle 011 — Discoveries

1. The fifth temporal defusal: deadline = validity condition on completion — "a result produced after its deadline is invalid regardless of its content" — the unification hypothesis reached n=5 (knowledge validity 008, enabling conditions 009, artifact validity 009, schema validity 010, completion validity 011) (Tier 1).
2. The isolation family across three domains: consistency (006), concurrency (010), timing (011) — guarantee separation is one structure, confirming 010 at n=3 (Tier 3).
3. The bounded-response family at n=4: overload-handling joins backpressure, circuit-breaker, cascading-failure (006) — the same structure under pressure (Tier 4).

## Cycle 011 — Failed Hypotheses / Near Failures

- **The strongest candidate — time as a correctness condition itself — resolved through composition**: deadline = validity condition (constraint), WCET = observation with confidence ("the strongest guarantee in real-time rests on an estimate"), scheduling = decision + pattern, priority inversion = failure mode + mitigation pattern, overload = bounded-response constraints. No near-failure this cycle. The closest approach was the hidden-primitive-through-language trap in Tier 1 (the `temporal_constraint` category label), rejected at prediction time. Priority-inversion — the pre-registered danger object — resolved without a concurrency-failure primitive.
- **All 19 recorded temptations rejected** (8 candidate families): time/deadline, scheduling-policy, schedulability-guarantee, concurrency/priority, temporal-constraint hidden primitive, overload/isolation, watchdog/health-check, arbitration construct.
- **Outcome space result**: outcome A (composition) dominant and outcome B (new motif candidate — arbitration, n≥3 across scheduling/consensus/locking) both occurred; outcome C (falsification) did not. Four consecutive "not a separate class" results (008 adaptive, 009 transformational, 010 data semantics, 011 temporal guarantees).
- **Open questions** (8): (1) temporal-trap chain completeness — five defusals; is there a sixth form of temporal pressure?; (2) unification hypothesis boundary — n=5; a non-obvious domain where validity is not bound by stated conditions would falsify it; (3) arbitration motif candidate — does it satisfy all five acceptance criteria and survive a further cycle to catalogue entry?; (4) isolation family candidate — n=3 across consistency/concurrency/timing; (5) decision-factor count — 11 decision objects, all exactly 4 factors; an object needing five would be the anomaly; (6) prediction-object motif candidate — benchmarks (008), query plans (010), WCET (011) — n=4; (7) guarantee vs temporal density — do the two edge-level metrics interact?; (8) watchdog reset-discipline invariant vs audit-independence (006) — are the two independence rules one pattern?

## Cycle 011 — Validation Evidence

| Metric | Value |
|---|---|
| Objects created | 16 (all PASS 0/0) |
| Passing objects (cumulative) | 105 |
| Corpus (cumulative) | 122 |
| Outcome classification | 0 Failure / 3 Discovery / 13 Confirmation |
| Warnings | 0 |
| Instrument stability | 11 cycles unchanged |

## Cycle 011 — End-of-Cycle Interpretation

- **What increased**: Objects (+16), qualification (176 events), relationship motifs (+26), domain coverage (Temporal guarantees), cross-domain links (8 analogous_to, corpus now spans five tested categories), the guarantee-object motif (n=4).
- **What stayed constant**: 9 primitives, 4 object kinds, all instruments.
- **Where did complexity move**: Into constraints (time as validity condition — the fifth defusal) + qualification (WCET as observation) + decision structure (posture decisions, factor count still 4) + motif topology (arbitration candidate) — existing destinations, no new one.
- **Did vocabulary expand**: No.
- **Did the graph become richer**: Yes — the fifth temporal defusal completed the temporal-trap chain; the unification hypothesis reached n=5; the isolation and bounded-response families generalized across domains; the arbitration candidate gave the motif catalogue its strongest new test.

---

# Cycle 012 — Robotics / Autonomous Cyber-Physical Systems (Cyber-Physical Knowledge Test)

*Date: 2026-08-01. Experimental target: Cyber-Physical Knowledge Test. Knowledge category: Cyber-physical — epistemic separation (knowledge whose truth is never directly observable, only inferred through layered models).*

**The cycle that tests whether *knowledge that never touches its object directly* requires a new primitive.** Robotics was selected at the Cycle 011 review as the compound stress test: it combines nearly every validated pressure (temporal 011, uncertainty 007/008, arbitration 006/010/011, bounded response 006, guarantees 009/010/011) and adds two pressures never tested in any form — continuous dynamics and epistemic separation (World → Sensors → Noise → Estimator → Belief → Decision → Actuation). The central hypothesis (research lead): the real novelty is not continuity but indirect knowledge of reality. If epistemic separation resolves through composition (reality → observation → qualified observation → claim → decision), the chain of "not a separate class" results reaches five; if pressure maps onto no existing complexity destination — no primitive, but no destination either — that is the attractor-state falsification signal. Each tier is documented separately.

## Pre-registration (recorded before authoring)

- **H₁**: Epistemic separation will resolve through composition: constraints (dynamics as constraint relationships over state) + qualification (observations at maximum epistemic distance) + verification (stability, safety certification as claim + evidence + constraints) + decision structure (autonomy as decision under an incomplete world model). The chain reality → observation → qualified observation → claim → decision is not a new evidence type.
- **H₀**: Knowledge of a physical world through layered inference requires new primitives or a new complexity destination — state/signal, perception/estimation, control/stability, safety-case/argument, or autonomous-decision constructs that cannot be decomposed into existing evidence structures.
- **Test question**: Do engineering systems whose knowledge depends on continuous interaction with an external physical world require additional evidence structures beyond those already observed? Sharpened: **can HPF represent knowledge whose truth is never directly observable, but only inferred through layered models?**
- **Primary Endpoint**: does epistemic separation map onto an existing complexity destination (qualification, constraints, verification, decision structure, relationships, graph composition) or require a new destination? The deeper failure is *no primitive, but no destination either*.
- **Pressure predictions**: Estimation Very High (highest risk — observation about a model's best belief, not about reality); Safety certification Very High; Stability High; Continuous dynamics High; Autonomy High (action generation under uncertainty); Structural Medium; Decision Factors High; Representation Failure none expected (falsification target).
- **Predictions**: P1 no new primitive; P2 estimation = qualified observation at maximum indirection; P3 safety case = fifth verification-family member (claim + evidence + constraints); P4 stability = verification pattern (demonstrated, not claimed); P5 epistemic separation, not continuous mathematics, is the greatest pressure (pre-registered by the research lead — expected resolution Reality → Observation → Qualified observation → Claim → Decision); P6 autonomy = decision under an incomplete world model (generating options, not choosing predefined ones); P7 dynamics = constraint relationships over state; P8 physical harm = failure modes with physical-consequence framing; P9 layering will not become ontology (the plant/computer boundary is architectural, not epistemic).
- **Outcome space**: A — composition; B — discovery (new motif or graph property); C — falsification (attractor state: pressure mapping onto no destination).
- **Observation metrics** (no schema change): **Epistemic Distance** (new — programme-wide; inferential layers between a claim and directly observable reality; distance structural, confidence qualificational; generalizes to ML/economics/medicine), safety-argument density, guarantee objects (does a fifth appear?), verification-family events, Temporal Constraint Density (011 re-test), cross-domain links.
- **Pre-authoring addenda**: 5 per tier (20 predictions total — Tier 1's addendum was repaired at closeout after the Tier 2 insertion overwrote predictions 2–5; restored from the contemporaneous Tier 1 prediction summary, repair note in dossier), each recorded before its tier's authoring.
- **Discipline constraint**: no robotics/cyber-physical object kinds; "signal", "state", "world", "belief" must appear as constraint content or qualified observation, never as ontology (hidden-primitive-through-language watch, 011).
- **Motif watches** (not expected discoveries): Epistemic Chain — Reality → Observation → Inference → Claim → Decision (named if it recurs across objects); Closed Epistemic Loop (added at the research lead's Tier 3 review) — Reality → Observation → Qualified Observation → Model → Decision → Action → Reality; Prediction-Object Family tracking table (benchmarks 008, plans 010, WCET 011, estimates 012, belief-state 012); verification-family watch (safety certification as predicted fifth member, stability predicted to join).

## Tier 1 — World Representation

- **Pressure**: the state/signal primitive temptation; the layering temptation (P9 — plant/computer boundary); the epistemic-separation baseline (P5 — sensing as the birth of the gap); physical-consequence pressure (P8).
- **Prediction**: cyber-physical-system is the hardest object (the model object holding the physical/computational boundary together); physical-state resolves as concept with dynamics as constraints (P7); sensing resolves as the observation source (P5 entry — "the sensor never reports reality, only a measurement of it under stated conditions"); actuation resolves as the action destination (idempotency discipline, 006); Epistemic Distance baseline established; P9 tested at the plant/computer boundary.
- **Objects** (all PASS 0/0):
  - **cyber-physical-system (concept)** — The compound system. Blocks: 8. Relationships: requires (→ physical-state, sensing, actuation), analogous_to (→ real-time-system, → schema-design). Failure modes: sensor_denial, actuation_failure, model_mismatch.
  - **physical-state (concept)** — The model of reality. Blocks: 8. Relationships: describes (→ cyber-physical-system), evaluated_through (→ sensing), analogous_to (→ schema-design), constrained_by (→ deadline), informs (→ actuation). Failure modes: state_divergence, unobservable_state, stale_state.
  - **sensing (concept)** — The observation source. Blocks: 8. Relationships: serves (→ cyber-physical-system), informs (→ physical-state), analogous_to (→ model-monitoring), affected_by (→ deployment-risk), constrained_by (→ deadline). Failure modes: sensor_failure, measurement_noise, calibration_drift.
  - **actuation (concept)** — The action destination. Blocks: 8. Relationships: serves (→ cyber-physical-system), changes (→ physical-state), analogous_to (→ idempotency), mitigated_by (→ retry-pattern), executed_under (→ real-time-system). Failure modes: actuation_failure, saturation, duplicate_actuation.
- **Result**: All 5 addendum predictions held. The hardest object behaved as predicted — structurally identical to real-time-system (011) / schema-design (010). P9 tested: "the boundary between computer and world is architectural, not epistemic." P5 entered at the sensing end: "the sensor never reports reality, only a measurement of it under stated conditions." No state/signal/sensing/actuation primitive; no hidden-primitive-through-language event. Epistemic Distance baseline: sensing = 1, physical-state = 1–2, system-level = 2+. Temporal Constraint Density: 25% (2/8 constraints), 15% (3/20 edges) — sharply below 011 (100%/45%), exactly as expected for a model-and-observation tier. Cross-domain links: 10 (nearly every prior corpus at Tier 1 alone; 011 T1 had 2).
- **Discovery (Tier 1)**: none new — the tier established the Epistemic Distance baseline (first readings, gradient confirmed) and tested P9 (architectural, not epistemic); the Epistemic Chain appeared at the relationship level (sensing `informs` state, state `informs` actuation, actuation under real-time constraints, the loop closing via the world acting back on sensing).

## Tier 2 — Estimation & Perception

- **Pressure**: the estimator/estimate primitive temptation; the belief primitive temptation (**P5 danger object** — the strongest belief-construct candidate in the programme); the fusion/agreement structure; the qualification pole re-test.
- **Prediction**: state-estimation resolves as concept (claim + qualified observations + constraints; analogous_to query-planning 010 — prediction-object family n=4); belief-state resolves as composition — "a distribution over possible states expressed as claims qualified by confidence," no belief primitive (if belief forces a new construct, P5 fails and the central hypothesis is in trouble); sensor-fusion resolves as pattern (sensor-level quorum — "independence is the precondition of agreement"); perception-uncertainty resolves as the 007/008 qualification model re-test (overconfidence = "a qualification failure, not a perception failure"); Epistemic Distance rises in gradients (2–3).
- **Objects** (all PASS 0/0):
  - **state-estimation (concept)** — Inference from observations through a model. Blocks: 8. Relationships: produces (→ belief-state), evaluated_through (→ sensing), analogous_to (→ query-planning), describes (→ physical-state), constrained_by (→ deadline). Failure modes: estimator_divergence, unobservable_dimensions, model_mismatch.
  - **belief-state (concept)** — The internal world model. Blocks: 8. Relationships: produced_by (→ state-estimation), informs (→ actuation), analogous_to (→ probabilistic-outputs), describes (→ physical-state), constrained_by (→ incomplete-evidence). Failure modes: belief_divergence, overconfidence, stale_belief.
  - **sensor-fusion (pattern)** — The agreement structure of redundant observation. Blocks: 8. Relationships: serves (→ cyber-physical-system), produces (→ belief-state), evaluates (→ sensing), analogous_to (→ quorum, → model-monitoring). Failure modes: fusion_misalignment, correlated_noise, single_source_dominance.
  - **perception-uncertainty (concept)** — Qualification of observation at epistemic distance. Blocks: 8. Relationships: afflicts (→ belief-state), constrained_by (→ sensing, → incomplete-evidence), analogous_to (→ confidence-calibration, → uncertainty-estimation). Failure modes: overconfidence, unmodeled_uncertainty, ambiguity_misclassification.
- **Result**: All 5 addendum predictions held. **P5 survived its sharpest test** — belief-state resolved as composition: "belief is composition, not ontology"; "the epistemic gap lives inside the belief — belief is about the model, never about reality directly." Overconfidence resolved as the belief's characteristic failure: "a qualification failure, not a perception failure." Fusion resolved as the sensor-level quorum with the sharpest invariant: "independence is the precondition of agreement — correlated sources are one source." Prediction-object family at n=4 (estimates joining benchmarks 008, plans 010, WCET 011). Epistemic Distance gradients confirmed (2–3); fusion tightens uncertainty at a given distance — distance structural, confidence qualificational (wording corrected at the research lead's Tier 2 review). Temporal Constraint Density: 0% (0/8), 5% (1/20). Cross-domain links: 9 (19 cumulative).
- **Discovery (Tier 2)**: *P5 at maximum depth.* The danger object resolved as composition — epistemic separation is a chain of qualified observations and models, never ontology. The hidden-primitive-through-language watch stayed clear through the programme's strongest belief-construct temptation.

## Tier 3 — Control & Stability

- **Pressure**: the controller/stability primitive temptations; the verification-family test (P4 — is stability demonstrated, not claimed?); the guarantee-object test (n=5); the compound pressure of temporal guarantees (011) meeting physical control (012).
- **Prediction**: feedback-control resolves as concept (loop = relationship structure; the error signal is "an observation of divergence"); stability resolves as verification pattern (P4 — Lyapunov/boundedness conditions as invariants, analysis/simulation/test as evidence; verification family gains its fifth member); closed-loop-guarantee resolves as the fifth guarantee object (n=5: type-safety 009, data-integrity 010, atomicity 010, real-time-guarantee 011); control-scheduling-interaction resolves as pattern (the temporal-epistemic junction — sampling jitter, delay, missed periods as temporal constraints on the loop); Temporal Constraint Density rises above T1/T2 but below 011.
- **Objects** (all PASS 0/0):
  - **feedback-control (concept)** — The closed-loop structure. Blocks: 8. Relationships: serves (→ cyber-physical-system), directs (→ actuation), evaluated_through (→ belief-state), analogous_to (→ model-monitoring), constrained_by (→ deadline). Failure modes: loop_instability, windup, delayed_correction.
  - **stability (concept)** — Demonstrated closed-loop correctness. Blocks: 8. Relationships: constrains (→ feedback-control), supports (→ closed-loop-guarantee), analogous_to (→ formal-verification, → schedulability-analysis), governs (→ physical-state). Failure modes: instability, marginal_stability, envelope_exit.
  - **closed-loop-guarantee (concept)** — The fifth guarantee object. Blocks: 8. Relationships: guaranteed_by (→ feedback-control), depends_on (→ stability), analogous_to (→ type-safety, → data-integrity, → real-time-guarantee). Failure modes: guarantee_overreach, envelope_exit, verification_gap.
  - **control-scheduling-interaction (pattern)** — The temporal-epistemic junction. Blocks: 8. Relationships: afflicts (→ feedback-control), analogous_to (→ task-scheduling), constrained_by (→ deadline), supports (→ closed-loop-guarantee), serves (→ cyber-physical-system). Failure modes: jitter_induced_instability, missed_period, delayed_actuation.
- **Result**: All 5 addendum predictions held. P4 confirmed — stability resolved as verification pattern: "stability is demonstrated, not claimed — analysis, simulation, and test provide the evidence," joining the verification family at n=5. The guarantee-object motif reached n=5 (closed-loop-guarantee). The error signal resolved as observation: "the error signal is an observation of divergence, qualified by measurement uncertainty." The interaction resolved as composition of the 011 and 012 corpora — the sharpest invariant: "a loop whose timing conditions are unstated has no guarantee." Temporal Constraint Density: 37.5% (3/8), 20% (4/20) — the predicted rise at the temporal-epistemic junction confirmed, above T1 (25%/15%) and T2 (0%/5%), below 011 (100%/45%). Epistemic Distance: 2–3 throughout, with control-scheduling-interaction at 1–2 (timing is the directly observable dimension). Cross-domain links: 9 (28 cumulative).
- **Discovery (Tier 3)**: *The boundary between the verification and guarantee families.* "Stability is the boundary between the verification and guarantee families — demonstrated by the first, scoped by the second." Two of the programme's strongest motifs grew simultaneously (verification n=5 via stability; guarantee n=5 via closed-loop-guarantee). Research lead's Tier 3 review: the verification family is a **candidate strengthened at n=5**, not a mature motif — every member so far is engineering; a family should survive at least one completely different discipline before maturity (see Cycle 013 closeout protocol).

## Tier 4 — Safety & Autonomy

- **Pressure**: the safety-case/argument primitive temptation (P3 — certification as claim + evidence + argument); the fail-safe primitive temptation (mode-divergence re-applied to failure); the autonomy decision (P6 — action generation under an incomplete world model); the arbitration candidate re-test at n=4 (006 consensus, 010 locking, 011 scheduling, 012 arbitration); the Epistemic Chain's predicted close into a loop.
- **Prediction**: safety-case resolves as pattern — the sixth verification-family candidate member (P3: "the safety case is an artifact of evidence, exactly as a proof is"; ISO 26262 / IEC 61508 / DO-178C as constraint sets over evidence); fail-safe resolves as pattern — the posture under failure (mode-divergence re-applied; "fail-safe is not safety — it is the bounded response to failure"); autonomy-decision resolves as decision with 4 Decision Factors (P6 — 12th decision object; expected DFs information_gain, risk_tolerance, action_irreversibility, oversight_availability); resource-arbitration resolves as decision with 4 Decision Factors — the arbitration candidate re-test at n=4, NOT promoted; the Epistemic Chain closes into a loop at cycle level (action → safety → reality → sensing); Temporal Constraint Density stays low (decision/posture tiers dilute temporal content, mirroring 011's T2/T4 pattern).
- **Objects** (all PASS 0/0):
  - **safety-case (pattern)** — The assurance artifact. Blocks: 8. Relationships: serves (→ cyber-physical-system), supports (→ closed-loop-guarantee), analogous_to (→ formal-verification), verified_by (→ stability), bounds (→ autonomy-decision). Failure modes: invalidated_case, missing_evidence, argument_erosion.
  - **fail-safe (pattern)** — The posture under failure. Blocks: 8. Relationships: serves (→ cyber-physical-system), bounds (→ safety-case), analogous_to (→ hard-vs-soft-real-time, → debug-vs-release-modes), mitigates (→ actuation). Failure modes: unsafe_fallacy, stuck_in_degraded, no_safe_state.
  - **autonomy-decision (decision)** — The open-world decision. Blocks: 9. Decision Factors: information_gain, risk_tolerance, action_irreversibility, oversight_availability. Relationships: constrained_by (→ belief-state), informs (→ actuation), constrained_by (→ safety-case), analogous_to (→ risk-acceptance, → scheduling-policy). Failure modes: overreach, unsafe_option_generation, decision_stall.
  - **resource-arbitration (decision)** — The contention allocation. Blocks: 9. Decision Factors: contention_severity, allocation_fairness, deadline_priority, preemption_cost. Relationships: serves (→ cyber-physical-system), analogous_to (→ raft-consensus, → scheduling-policy, → isolation-levels), constrained_by (→ deadline). Failure modes: allocation_starvation, arbitration_delay, unfair_allocation.
- **Result**: All 5 addendum predictions held. P3 confirmed — safety-case resolved as pattern: "an artifact of evidence, exactly as a proof is — claim, evidence, and argument as relationship structure." The verification family candidate reached n=6 (equivalence-checking 009, formal-verification 009, benchmark-validity 008, schedulability-analysis 011, stability 012, safety-case 012). Fail-safe resolved as mode-divergence re-applied to failure — the circuit-breaker (006) structure in posture form. **P6 confirmed** — autonomy-decision resolved as "a decision under an incomplete world model — generating options, not choosing among predefined ones"; action generation stayed inside the decision object. The arbitration candidate re-test at n=4 confirmed the structure (contenders + selection rule + allocation + guarantee = graph topology, not construct) but was **NOT promoted**. Decision-factor count held at 4 — the 13th decision object (007–012) sustains the factor-count invariant. Temporal Constraint Density: 0% (0/8), 5% (1/20 — the deadline edge in resource-arbitration) — the predicted low confirmed, exactly equal to T2's reading; the 011 T2/T4 dilution pattern reproduces. Epistemic Distance: resource-arbitration = 1–2; fail-safe = 1–2; autonomy-decision = 3; safety-case = 3+ (the corpus maximum — the assurance artifact reasons above the system's claims). Cross-domain links: 9 (37 cumulative — every prior corpus 006–011 now links into 012).
- **Discovery (Tier 4)**: *The Epistemic Chain closes into the Closed Epistemic Loop.* Autonomy-decision `informs` actuation, actuation is `mitigated_by` fail-safe and bounded by safety-case, and the world acts back on sensing (T1 cyber-physical-system) — the chain is now a complete loop through the corpus: reality → sensing → belief → decision → action → safety → reality. Watch recorded, not elevated.

## Cycle 012 — Primitive Pressure Analysis (complete list of temptations)

| Candidate | Why it looked necessary | How tested | Why rejected | Final representation |
|---|---|---|---|---|
| State/signal primitive | Continuous dynamics + physical reality look like a new category | Constraints over state evolution | Dynamics are constraint relationships; "the boundary between computer and world is architectural, not epistemic" (P9) | physical-state as concept; dynamics as constraints |
| Sensing primitive | Sensors look like a perception construct | Observation chain | "The sensor never reports reality, only a measurement of it under stated conditions" — sensing = observation source at distance 1 | sensing as concept |
| Estimation/estimator primitive | Inference from observations through a model looks distinct | Relationship structure (observations → belief) | The estimator is a relationship structure; an estimate is a hypothesis about state (prediction-object family n=4) | state-estimation as concept; analogous_to query-planning |
| Belief primitive (P5 danger object) | The POMDP belief is the strongest belief-construct candidate in the programme | Composition — claims qualified by confidence | "Belief is composition, not ontology" — belief is about the model, never reality directly | belief-state as concept |
| Fusion construct | Combining observations looks like a new evidence mechanism | Sensor-level quorum | "Independence is the precondition of agreement — correlated sources are one source" | sensor-fusion as pattern |
| Controller primitive | Closed-loop control looks like a new knowledge type | Relationship structure (observation → comparison → correction, repeated) | The error signal is "an observation of divergence, qualified by measurement uncertainty" | feedback-control as concept |
| Stability construct | Lyapunov theory looks like a proof category | Verification pattern | "Stability is demonstrated, not claimed" — analysis/simulation/test as evidence (P4) | stability as concept; verification family n=5 |
| Safety-case/argument primitive | Certification looks like argumentation ontology | Claim + evidence + argument structure | "An artifact of evidence, exactly as a proof is" — certification standards as constraint sets over evidence (P3) | safety-case as pattern; verification family n=6 |
| Fail-safe primitive | Failure postures look like a new state semantics | Mode-divergence re-applied to failure | "Fail-safe is not safety — it is the bounded response to failure" | fail-safe as pattern |
| Action-generation construct | Generating options in open action spaces looks distinct from choosing | Decision structure | Autonomy = decision under an incomplete world model; generation inside the decision (P6) | autonomy-decision as decision, 4 DFs |
| Arbitration construct | Contention allocation recurs across 006/010/011/012 | Decision object; re-test at n=4 | Graph topology, not a construct; candidate re-tested and NOT promoted | resource-arbitration as decision, 4 DFs |

## Cycle 012 — Schema Interaction

```
Schema changed:      NO
Parser changes:      NO
Validator changes:   NO
Analyzer changes:    NO
Friction:            0
Rejected changes:    All 11 candidate families above (20 predictions recorded across 4 addenda, all held)
```

## Cycle 012 — Relationship Growth

80 relationship edges across 16 objects; 21 unique relationship verbs in-cycle; **1 new to the corpus** (`describes` — physical-state, state-estimation, belief-state). The relationship-verb set is near-saturated after 12 cycles. Cross-domain recognition: 37 links from 012 to the 006–011 corpora — cyber-physical-system → real-time-system/schema-design; sensing → model-monitoring/deployment-risk; actuation → idempotency/retry-pattern; state-estimation → query-planning; belief-state → probabilistic-outputs/incomplete-evidence; sensor-fusion → quorum; perception-uncertainty → confidence-calibration/uncertainty-estimation; feedback-control → model-monitoring; stability → formal-verification/schedulability-analysis; closed-loop-guarantee → type-safety/data-integrity/real-time-guarantee; control-scheduling-interaction → task-scheduling/deadline; safety-case → formal-verification; fail-safe → hard-vs-soft-real-time/debug-vs-release-modes; autonomy-decision → risk-acceptance/scheduling-policy; resource-arbitration → raft-consensus/isolation-levels/deadline. **Every prior corpus (006–011) now links into 012** — the single cross-domain graph spans all eight tested categories.

## Cycle 012 — Epistemic Distance (new observation dimension, cycle 1 of use)

Added at the research lead's request before authoring (renamed from Estimation Indirection Depth). Programme-wide metric: the number of inferential layers separating a claim from directly observable reality. Distance is structural; confidence is qualificational.

| Tier | Reading |
|---|---|
| T1 — World Representation | sensing = 1; physical-state = 1–2; system-level claims = 2+ |
| T2 — Estimation & Perception | state-estimation = 2–3; belief-state = 2–3; perception-uncertainty = 2+; fusion tightens uncertainty at a given distance (independent chains bound the belief tighter — distance unchanged) |
| T3 — Control & Stability | feedback-control = 2–3; stability = 2–3; closed-loop-guarantee = 2–3; control-scheduling-interaction = 1–2 (timing is the directly observable dimension) |
| T4 — Safety & Autonomy | resource-arbitration = 1–2; fail-safe = 1–2; autonomy-decision = 3; safety-case = 3+ (corpus maximum) |

Full gradient measured without schema change: 1 → 1–2 → 2–3 → 3+. Generalizes beyond robotics: ML (weights → prediction → claim), medicine (biomarker → diagnosis → treatment), economics (market → indicator → policy).

## Cycle 012 — Temporal Constraint Density (observation dimension re-test)

| Tier | Constraints time-bounded | Edges time-bounded |
|---|---|---|
| T1 — World Representation | 25% (2/8) | 15% (3/20) |
| T2 — Estimation & Perception | 0% (0/8) | 5% (1/20) |
| T3 — Control & Stability | 37.5% (3/8) | 20% (4/20) |
| T4 — Safety & Autonomy | 0% (0/8) | 5% (1/20) |
| **Cycle total** | **15.6% (5/32)** | **11.25% (9/80)** |

The metric discriminated within the category exactly as predicted: the model tier (T1) and the temporal-epistemic junction (T3) read highest; the belief and decision tiers (T2, T4) dilute to near zero — the 011 T2/T4 dilution pattern reproduced precisely. Compared with 011 (100% constraints, 42.5% edges), the compound domain concentrates temporal pressure in the control-junction tier only: temporal density tracks *guarantee structure*, not domain category.

## Cycle 012 — Qualification Growth

176 total events (80 claims + 48 observations + 48 recommendations); 1045 cumulative across Cycles 007–012. Continuation metric confirmed for a sixth consecutive cycle: knowledge whose truth is never directly observable is expressed as qualification of evidence, not as new evidence types.

## Cycle 012 — Object Kind Evolution

No new kinds. 10 concept, 4 pattern (sensor-fusion, control-scheduling-interaction, safety-case, fail-safe), 2 decision (autonomy-decision, resource-arbitration). Cumulative: **4** (unchanged). Both decision objects carried exactly 4 Decision Factors — the factor count held at 4 across all 13 decision objects since 007 (risk-acceptance, retraining-decisions, optimization-tradeoffs, debug-vs-release-modes, isolation-levels, query-planning, index-selection, data-governance, scheduling-policy, hard-vs-soft-real-time, real-time-throughput-tradeoff, autonomy-decision, resource-arbitration). An object needing five factors would be the anomaly.

## Cycle 012 — Discoveries

1. P5 at maximum depth: the danger object (belief-state) resolved as composition — "belief is composition, not ontology" — epistemic separation is a chain of qualified observations and models, never ontology; the programme's sharpest falsification test survived (Tier 2).
2. The Epistemic Distance gradient measured across the full range 1 → 3+ without schema change — the programme-wide metric validated, separating distance (structural) from confidence (qualificational) (Tiers 1–4).
3. The Epistemic Chain closes into the Closed Epistemic Loop at cycle level: reality → sensing → belief → decision → action → safety → reality (Tier 4) — watch recorded, not elevated.

## Cycle 012 — Failed Hypotheses / Near Failures

- **The strongest candidate — knowledge never directly observable — resolved through composition**: belief = claims qualified by confidence, estimation = relationship structure, safety case = claim + evidence + argument artifact, autonomy = decision under incomplete world model, arbitration = allocation decision. The Primary Endpoint's deeper criterion — "no primitive, but no destination either" — did not trigger: every pressure mapped onto an existing complexity destination. No near-failure at the object level this cycle; the closest approach was the P5 danger object (belief-state), resolved at prediction time as predicted.
- **All 20 recorded predictions held** (5 per tier × 4); all 11 candidate families rejected (state/signal, sensing, estimation, belief, fusion, controller, stability, safety-case/argument, fail-safe, action-generation, arbitration).
- **Outcome space result**: outcome A (composition) dominant and outcome B elements (the Closed Epistemic Loop named as a watch) both occurred; outcome C (falsification) did not. Five consecutive "not a separate class" results (008 adaptive, 009 transformational, 010 data semantics, 011 temporal guarantees, 012 cyber-physical).
- **Protocol-level near-miss (Cycle 012 closeout review)**: the research began to optimize itself — predictions becoming extremely precise (exact factor counts, exact motif growth, exact pattern resolutions) creates destination bias: the unconscious pressure to "find the destination" rather than "discover whether one exists." The pre-registration discipline controls hindsight bias but not this. Prescription adopted as protocol: the adversarial-review control (after every cycle, an appointed reviewer argues HPF is wrong in this domain — a cycle with no attempted negative claim does not close), the strengthened Phase 5 criterion (record how hard the cycle tried to prove there was no destination — attempted-falsification intensity), and the motif maturity gate (engineering must not mature engineering motifs; maturity requires a genuinely different epistemology — mathematical proof, clinical evidence, legal burden of proof — at Programme B). Cycle 012's own adversarial review was conducted by the research lead at closeout and produced the destination-bias finding above; it could not produce a pressure escaping the existing destinations.
- **Open questions** (8): (1) verification family candidate — n=6, all engineering members; does it survive a genuinely different epistemology (math/medicine/law) at Programme B? (maturity gate); (2) Closed Epistemic Loop watch — does it appear where there is no obvious loop (scientific research, judicial process, markets, organizations)?; (3) destination-bias control — does the adversarial review produce an escaping pressure in a hostile domain (Cycle 014)?; (4) Epistemic Distance — does the gradient survive non-engineering domains?; (5) arbitration candidate — n=4 re-test not promoted; promotion requires surviving further cycles; (6) prediction-object family — n=4 with belief-state tracked as fifth row; (7) decision-factor count — 13 objects, all exactly 4 factors; (8) guarantee motif — n=5; Programme B boundary.

## Cycle 012 — Validation Evidence

| Metric | Value |
|---|---|
| Objects created | 16 (all PASS 0/0) |
| Passing objects (cumulative) | 121 |
| Corpus (cumulative) | 138 |
| Outcome classification | 0 Failure / 3 Discovery / 13 Confirmation |
| Warnings | 0 |
| Instrument stability | 12 cycles unchanged |

## Cycle 012 — End-of-Cycle Interpretation

- **What increased**: Objects (+16), qualification (176 events), domain coverage (Cyber-physical — epistemic separation), cross-domain links (37 — every prior corpus 006–011 links in), the guarantee-object motif (n=5), the verification family candidate (n=6), the prediction-object family (n=4), a new programme-wide observation dimension (Epistemic Distance, gradient 1 → 3+).
- **What stayed constant**: 9 primitives, 4 object kinds, all instruments, relationship-verb growth (1 new verb — near-saturated).
- **Where did complexity move**: Into constraints (dynamics as constraint relationships) + qualification (belief at distance 2–3; Epistemic Distance as the cycle's signature metric) + verification (stability, safety-case — candidate n=6) + decision structure (autonomy, arbitration re-test) + motif topology (Epistemic Chain → Closed Epistemic Loop watch) — existing destinations, no new one.
- **Did vocabulary expand**: No.
- **Did the graph become richer**: Yes — the Epistemic Chain closed into the Closed Epistemic Loop across the cycle's four tiers; the full Epistemic Distance gradient was measured; the corpus became a single graph spanning all eight tested categories.
- **Did the experiment design hold**: Partially — and this is the cycle's most important negative result. The research began to optimize itself; the closeout review identified destination bias as an uncontrolled variable and added the adversarial-review control, the strengthened Phase 5 criterion, and the motif maturity gate to the protocol. Cycle 013 became the Protocol Hardening cycle; Cycle 014 is pre-registered as the hostile-domain falsification experiment under the fully hardened protocol.

---

# Cycle 013 — Protocol Hardening

*Date: 2026-08-01. Experimental target: research-protocol hardening. Knowledge category: N/A (no object authoring).*

**The cycle that hardens the experiment rather than the ontology.** At the Cycle 012 closeout review the research lead identified destination bias and the protocol was amended (adversarial review, strengthened Phase 5, motif maturity gate). At this cycle's review, the research lead identified five further methodological issues, all recorded before implementation: (1) the adversarial review is still internal — a reviewer operating inside the HPF framework cannot escape HPF's own assumptions; (2) destination bias is reduced, not eliminated — extremely specific predictions make the destination visible during authoring; (3) cycle success remains binary — "0 primitives" without quality measures; (4) Programme B entry criteria are narrative, not gates; (5) motif candidates lack statistical discipline — appearance counts without recurrence/independence/discriminative-power/counterexample-search requirements. No knowledge objects were authored this cycle; the artifacts are the amendments A1–A5 (full text: `research/protocol-hardening/dossier.md`; adopted in PROGRAMME_STATE Research Method section).

## Amendment A1 — External-frame adversarial review

The internal reviewer shares the ontology under test. From Cycle 014, every object-authoring cycle must include at least one external-frame adversarial review, written entirely in a competing philosophy's own terms, standards, and vocabulary, from a rotating frame list (never the same frame twice in succession): **Ontology-first** (BFO/DOLCE-style upper ontology — kinds, roles, dispositions, boundaries), **Category-theoretic** (compositional laws — identity, associativity, functoriality), **Formal-methods / model-theoretic** (truth conditions, formal semantics, proof obligations), **MBSE / systems engineering** (executability, SysML/UML conformance). Each review produces at least one negative claim in the frame's own terms; the research lead responds with counter-evidence or concedes. Outcome recorded: **CONTAINED** / **DISMISSED** / **ESCAPED** (ESCAPED triggers architecture review).

## Amendment A2 — Prediction specificity control (sealed probes)

Predictions split into two tiers in every tier addendum: **coarse expectations (H-level)** — falsifiable direction claims that guide authoring; **fine-grained predictions (F-probes)** — exact counts, exact resolutions, exact factor sets, recorded marked **sealed**, not consulted during authoring, checked only at tier close. Probe discipline: an F-probe that fails is an **overfitting signal**, not a falsification event; a success adds weak confirmation only. Every addendum records at least one **counter-probe** — the specific way the tier would falsify its central expectation. At tier close, the **forced-fit audit** checks whether any object would have been authored differently had a probe differed; strained analogies, convenient scoping, and contorted claims are recorded as forced-fit incidents.

## Amendment A3 — Non-binary cycle scorecard

Every cycle summary records the Cycle Scorecard alongside the outcome classification: **forced-fit incidents** (counted by the audit and reviews; 0 = 5 … systematic = 0), **unresolved pressures** (dossier Residual Pressures entries with disposition RESOLVED / DEFERRED / LATENT; deferred/latent counted), **adversarial challenge strength** (1 trivial … 5 falsification-adjacent, descriptive), **explanation simplicity** (new relationship verbs; 0 = 5 … 4+ = 1). Scored prospectively from Cycle 014. **Cycle 012 is not retro-scored** — the dimensions were not measured during the cycle, and retrospective calibration is itself a hindsight-bias risk. A cycle with a degraded scorecard is recorded as a *low-confidence pass*.

## Amendment A4 — Explicit Programme B entry gates

Transition to Programme B (biology → economics → social) requires all of: **G1** two hostile-domain cycles passed (0 primitives, 0 new kinds, 0 ESCAPED reviews); **G2** two external-frame reviews from two distinct frames, none ESCAPED; **G3** no recurring escape pressure (recurrence without resolution blocks transition); **G4** scorecard discipline (forced-fit incidents ≤ 1, unresolved pressures ≤ 1 with disposition, explanation simplicity ≥ 3 per hostile cycle); **G5** every promoted motif has a non-empty attempted-counterexample register; **G6** the decision-factor anomaly search (documented search for a decision object with ≠ 4 factors, finding none) ran in at least one hostile cycle.

## Amendment A5 — Motif promotion gate and attempted-counterexample register

A motif candidate may be promoted to catalogue entry only when all of: the five acceptance criteria; **recurrence** ≥ 5 independent appearances across ≥ 3 distinct domains (a domain's sub-tiers count as one); **independence** (no shared sub-domain lineage); **discriminative power** (documented ablation argument — removing the motif's structure must materially degrade a representative object); **failed counterexample search** (a documented, pre-registered search for counter-instances — an empty register is a block, not a pass); **no ESCAPED external review**. Promotion (catalogue entry) is distinct from maturity: architectural maturity still requires the Programme B epistemology gate (math/medicine/law).

## Amendment Round 2 (B1–B8) — judgment independence

The follow-up review scored the protocol 9.7/10 and identified the remaining gap: the controls are still executed by the research lead — the protocol must be executable and evaluable by another researcher with minimal subjective interpretation. Full text: `research/protocol-hardening/dossier.md` (v1.3).

- **B1 — Independent evaluation rubric (de-simulated review).** The review pipeline becomes: frame appointed (randomized) → **rubric frozen** (pre-registered and versioned *before* the argument exists, in the frame's own vocabulary, no reference to HPF outcomes) → argument (citing the specific rubric conditions HPF allegedly fails) → response (counter-evidence, cited to corpus content) → **verdict** (mechanical application of the frozen rubric + B2 conditions; the research lead's only role is factual verification of citations). Rubric templates are frozen per frame: ontology-first (R1–R5: kind/role, disposition/process, boundary/continuant, dependence, generality), category-theoretic (C1–C5: identity, associativity, functoriality, universal constructions, morphisms), formal-methods (F1–F5: truth conditions, grammar, proof obligations, semantics, consistency), MBSE (M1–M5: executability, conformance, integration, traceability, lifecycle).
- **B2 — Objective verdict conditions.** ESCAPED iff ANY of: (1) cannot answer using the current ontology; (2) requires an undocumented assumption; (3) requires a new primitive or object kind; (4) requires scope narrowing (recorded as a forced-fit incident; narrowing that changes the claim's meaning = ESCAPED); (5) contradicts a previous cycle result or claim. Otherwise CONTAINED (counter-evidence satisfies the cited rubric conditions). Otherwise DISMISSED (the negative claim fails on its own terms against the frozen rubric). Verdicts are re-derivable from the record.
- **B3 — Scorecard separation.** Objective metrics (forced-fit incidents; unresolved pressures with disposition; vocabulary additions — primitives/kinds/verbs/analogy targets; escaped reviews) and descriptive metrics (challenge strength 1–5; research-lead confidence), never aggregated. The v1.2 composite is withdrawn; G4 references objective metrics only.
- **B4 — A/B probe comparison replaces introspection.** Sealed authoring = blind condition (Version A); probes revealed at tier close (Version B); recorded diff per tier (MATCH/MISMATCH/NOT-APPLICABLE per probe and per **decoy** — one plausible-but-wrong probe per tier). Outcomes tracking true probes but not decoys = seal working; tracking both = contamination; MATCH on a true probe where alternatives plausibly exist = destination-bias flag (forced-fit incident).
- **B5 — Epistemic discontinuity gate (G7).** Before full Programme B: a 4-object pilot in a categorically different justification structure (medicine — clinical evidence; or biology — evolved knowledge) under the full protocol, passing with 0 primitives and objective metrics within thresholds. Engineering stress does not substitute: biology changes the epistemology, not merely the complexity. If medicine, the pilot doubles as the verification-family epistemology test.
- **B6 — Counterexample search strategy.** Every attempted-counterexample register pre-registers: search space, inclusion criteria, stopping criterion (stated in advance), justification. A strategy-less register is a block.
- **B7 — Randomized frame rotation.** Frames drawn by seeded pseudo-random selection; all four frames within every four object-authoring cycles; no frame twice in succession; seed recorded at cycle start. Coverage guaranteed, order unpredictable.
- **B8 — Protocol Stability Principle.** The protocol is presumed stable as of v1.3. Future amendments require a demonstrated deficiency exposed by a completed cycle under the current protocol — not a theoretical improvement. Amendments are rare, explicitly justified, and versioned. A success under a frozen protocol is stronger than a success under an evolving one.

## Cycle 013 — Adversarial pass on the amendments

Per the protocol's own discipline, the amendments received an internal adversarial pass at adoption. **Round 1 (A1–A5)**: against A3, "a 1–5 scorecard invites post-hoc calibration" — countered: scores are prospective, the raw incident counts and registers are the recorded data, and a score that disagrees with its raw record is itself a finding. Against A2, "sealed probes depend on author discipline and cannot be independently verified" — conceded; enforcement is via the forced-fit audit and the external reviewer, who now has the probe record to check against. Against A5, "five appearances across domains is still a frequency heuristic" — conceded; the failed-search requirement is load-bearing, frequency is a gate, not a proof. **Round 2 (B1–B8)**: against B4, "decoy probes could bias authoring if the decoy pattern leaks" — countered: decoys are sealed under the same discipline, and a decoy-channel leak is itself a finding. Against B2, "response wording could game the verdict conditions" — countered: citations are factually verified, the rubric is frozen, the verdict is re-derivable. Against B8, "freezing the protocol locks in errors" — accepted: that is the intent; future changes require a demonstrated deficiency, and the v1.3 bar is deliberately higher. Outcomes: all CONTAINED or DISMISSED; none ESCAPED.

## Cycle 013 — Schema Interaction

```
Schema changed:      NO
Parser changes:      NO
Validator changes:   NO
Analyzer changes:    NO
Friction:            0
Objects authored:    0 (protocol cycle)
Protocol version:    v1.3 (v1.0 → v1.1 Cycle 012 controls → v1.2 A1–A5 → v1.3 B1–B8 + Stability Principle)
```

## Cycle 013 — End-of-Cycle Interpretation

- **What increased**: protocol controls in two rounds — round 1 (A1–A5): external-frame review, sealed probes + counter-probes, forced-fit audit, cycle scorecard, Programme B gates G1–G6, motif promotion gate; round 2 (B1–B8): frozen evaluation rubrics, objective verdict conditions, scorecard split (objective/descriptive, never aggregated), A/B probe comparison with decoys, epistemic-discontinuity gate G7, counterexample search strategies, randomized frame rotation, and the Protocol Stability Principle.
- **What stayed constant**: 9 primitives, 4 object kinds, all instruments, the primary falsification endpoint (0 primitives / no vocabulary growth), and the central invariant.
- **Where did complexity move**: Into the experimental design, not the ontology — first the controls, then the controls' independence from the research lead's judgment. The review's scoring of the protocol's evolution: original 8.5/10 → after Cycle 012 controls 9.2/10 → after round 1 9.7/10; the remaining gap was judgment dependence, closed by B1–B8.
- **Did vocabulary expand**: No (no objects authored).
- **Did the experiment become more hostile**: Yes — hostile-domain Cycle 014 runs under the frozen v1.3 protocol: an external reviewer with a frozen rubric arguing in a competing philosophy's own terms, mechanical verdicts, sealed probes with decoys, and a protocol that cannot be moved mid-stream. The Protocol Stability Principle means Cycle 014's success — or failure — is the protocol's verdict on HPF, not the protocol's verdict on itself.

**Pre-Cycle-014 adversarial review (2026-08-01)**: the first full-stack review ran against the consolidated canonical protocol (`research/protocol/HPF_PROTOCOL.md`) — internal consistency → executability → adversarial gaming → freeze integrity, under the three-bucket discipline (A integrity defect / B carry-and-record / C design preference, C explicitly rejected). The review objective was the false-positive-success question: "Can I produce a false-positive success under this protocol?" Three Category A defects were found, ratified, and corrected as **v1.3.1** (defect corrections, not amendments): A-1 — verdict conditions contained evaluative predicates ("satisfies"/"misapplied") and the DISMISSED branch let the response override the frame's own frozen standards (worked counterexample: the same formal-methods review yields DISMISSED or ESCAPED from the same record); A-2 — the frame draw specified no PRNG/procedure, so it was not re-derivable and the seed could be searched (fix: named PRNG + pre-registered nonce digest + full draw log); A-4 — internal-review outcomes had no adjudication standard, hollowing the destination-bias control (fix: B2 conditions apply, CONTAINED requires directly-answering citations). A fourth finding (A-3 — no document-control rule) was reclassified at ratification to Category B: its honest-researcher test fails (divergence requires a text edit — governance, not experimental execution), and its fix was retained as administration hardening. Eleven B-items were recorded (hostile-cycle threshold scope, seal-leak consequence, pre-narrowing, n-free counterexample search, rubric authorship, classification administration, timestamp discipline, verb-channel growth, residual frame-order gaming, document control) and C-preferences rejected. The near-miss register gains #12: the DISMISSED-override — a genuine escape path for any external review, closed before Cycle 014 could be corrupted by it. The protocol stands frozen at v1.3.1; Cycle 014 is the first cycle under it.

---

# Final Programme Evolution Section

## Evidence Vocabulary Evolution

```
Cycle 001:  (atomic schema not yet established; canonical format)
Cycle 002:  retrofitted object passes — schema in use
Cycle 003:  schema-native from creation
Cycle 004:  9 primitives in operation
Cycle 005:  9 primitives
Cycle 006:  9 primitives
Cycle 007:  9 primitives
Cycle 008:  9 primitives
Cycle 009:  9 primitives
Cycle 010:  9 primitives
Cycle 011:  9 primitives
Cycle 012:  9 primitives
Cycle 013:  9 primitives (protocol cycle — no objects authored)

Growth: 0
```

The 9 primitives — Claims, Relationships, Constraints, Observations, Trade-offs, Failures, Heuristics, Recommendations, Decision Factors — were established during Cycles 002–003 and have never changed.

## Complexity Migration Evolution

```
Deterministic:     Graph composition
Systemic:          Relationships
Probabilistic:     Evidence qualification
Adaptive:          Validity conditions + feedback relationships
Transformational:  Constraint-carrying relationships + qualification (observation-model scoping) + decision structure
Data semantics:    Constraints + validity conditions (unification n=3) + decision structure + cross-domain relationships
Temporal guarantees: Constraints (time as validity condition) + qualification (WCET as observation) + decision structure (posture) + motif topology (arbitration candidate)
Cyber-physical:    Constraints (dynamics as constraint relationships) + qualification (belief at distance 2–3, Epistemic Distance gradient 1→3+) + verification (stability, safety-case — candidate n=6) + decision structure (autonomy, arbitration re-test) + motif topology (Epistemic Chain → Closed Epistemic Loop watch)
```

The emerging theory, refined at the Cycle 012 closeout review: **across tested engineering categories, increasing complexity has so far migrated through composition, relationships, qualification, verification, and decision structure rather than requiring vocabulary expansion.** Five consecutive "not a separate class" results (008 adaptive, 009 transformational, 010 data semantics, 011 temporal guarantees, 012 cyber-physical) — every category tested so far has resolved into existing complexity destinations. The unification hypothesis — every validity claim in engineering is bound by stated conditions, and the conditions are constraints — survived its fifth domain (011 deadline validity joining 008 knowledge validity, 009 enabling/artifact validity, and 010 schema validity); the 012 result extended the pattern to the epistemic pole: every belief about reality is a qualified observation, never ontology. The closeout review added the destination-bias control (adversarial review per cycle) so that the migration matrix's "existing destinations" column remains a tested claim, not a self-fulfilling one.

## Evidence Graph Motifs (catalogue v0.1)

Refined at the Cycle 011 review: complexity organizes into recurring graph structures that repeat across domains without becoming vocabulary. **Provisional — not finalized.** The catalogue remains empirical; candidates must satisfy the acceptance criteria and survive further cycles. A primitive changes the representation language; a motif changes how existing primitives are composed. Motifs are measured at the edge level — block ratios are disciplined into uniformity and reveal nothing.

**Motif acceptance criteria** — a candidate motif must satisfy all of: (1) appears independently in multiple objects; (2) appears across multiple cycles or domains; (3) explains composition rather than vocabulary; (4) improves understanding without changing representation; (5) is optional — never required — for valid modelling.

**Anti-primitive rule**: every motif must always be expressible as an optional composition of existing primitives. A motif that becomes mandatory for valid modelling is a hidden primitive and triggers architecture review.

**Motifs** (reusable structures):

| Motif | Appeared | Representative objects |
|---|---|---|
| Guarantee Object | 009, 010, 011, 012 | type-safety, data-integrity, atomicity, real-time-guarantee, closed-loop-guarantee — scoped claim + invariants + failure modes (n=5) |
| Transformation Chain | 009, 010 | compiler-optimization, query-optimization — before-state + action + after-state + correctness constraint (n=2, cross-domain) |
| Validity Derivation | 008, 009, 010 | training-data, build-systems, schema-migration, backup-recovery — validity as derivation under stated conditions (n=3, unification hypothesis) |
| Feedback Loop | 008 | model-monitoring → retraining-decisions — observation → recommendation → action → new observation |
| Failure-Recovery Loop | 006, 010 | retry-pattern/circuit-breaker, transaction-failures, backup-recovery — failure mode + mitigation link + recovery discipline |
| Decision Tradeoff | 007, 009, 010, 011, 012 | risk-acceptance, optimization-tradeoffs, isolation-levels, query-planning, index-selection, data-governance, scheduling-policy, hard-vs-soft-real-time, real-time-throughput-tradeoff, autonomy-decision, resource-arbitration — decision object with exactly 4 Decision Factors (n=13) |

**Motif candidates** (observed, not yet catalogue entries — must satisfy all acceptance criteria and survive further cycles): **Arbitration** (012 arbitration, 011 scheduling, 006 consensus, 010 locking — contenders + selection rule + allocation + guarantee; resolved as graph topology, not a construct; re-tested at n=4 in 012 and NOT promoted), **Isolation** (006 strong-consistency, 010 isolation-levels, 011 temporal-isolation — guarantee separation across 3 domains), **Prediction-object** (012 state-estimation and belief-state, 008 benchmarks, 010 query plans, 011 WCET — model of the world as evidence source feeding a decision; comparison metrics tracked), **Verification family** (012 stability + safety-case, 009 equivalence-checking + formal-verification, 008 benchmark-validity, 011 schedulability-analysis — claim + evidence + constraints, where verification does not become ontology; candidate at n=6).

**Motif maturity gate (Cycle 012 closeout review):** engineering must not mature engineering motifs. No candidate — including the verification family at n=6 — may be treated as mature until it has survived at least one genuinely different epistemology that justifies truth differently (e.g., mathematical proof, clinical evidence, legal burden of proof). Maturity is deferred to Programme B at the earliest. This is a strengthening of the earlier claim discipline: the verification family is a *candidate strengthened at n=6*, never a mature motif on engineering evidence alone.

**Motif promotion gate (Amendment A5, Cycle 013):** catalogue entry additionally requires recurrence (≥ 5 independent appearances across ≥ 3 distinct domains; a domain's sub-tiers count as one), independence (no shared sub-domain lineage), discriminative power (documented ablation argument — removing the motif's structure must materially degrade a representative object), a failed counterexample search (documented, pre-registered; an empty register is a block, not a pass), and no ESCAPED external review (A1). Promotion is distinct from maturity; a promoted motif can be demoted by a later counter-instance.

**Graph properties** (measurements, not motifs):

| Property | Cycles | Measurement |
|---|---|---|
| Guarantee Hub | 009, 010, 011 | Guarantee-family edge share clusters around guarantee objects (010: 32.9%, 009: 39.8%, 007: 4.5%) — topology, not a construct |
| Cross-domain recognition | 010, 011, 012 | analogous_to links binding the corpus into a single graph (010: 4; 011: 8; 012: 37 — every prior corpus 006–011 links in) |
| Temporal Constraint Density | 011, 012 | 011: constraints 100% time-bounded all tiers, edges 40–45%; 012: model tier 25%/15%, junction tier 37.5%/20%, belief/decision tiers 0%/5% — temporal pressure concentrates in guarantee structure; discriminates within a category |
| Epistemic Distance | 012 | Inferential layers between a claim and directly observable reality: gradient 1 → 3+ (sensing 1, state 1–2, belief/estimation 2–3, autonomy-decision 3, safety-case 3+); distance structural, confidence qualificational — programme-wide metric |

Current explanatory hypothesis: **across the engineering categories tested so far, new knowledge has consistently increased graph organization rather than evidence vocabulary. Recurring graph motifs are the current explanatory hypothesis for that organization.** An emerging theory — it must survive several more orthogonal cycles before it earns architectural status, and (per the Cycle 012 maturity gate) at least one non-engineering epistemology.

## Current Defensible Claim

> "HPF has remained domain-independent across tested engineering categories."

This claim is limited to: deterministic (browser automation, networking), systemic (distributed systems), probabilistic (security), adaptive (machine learning), transformational (compilers / static analysis), data semantics (databases), temporal guarantees (real-time systems), and cyber-physical (robotics — epistemic separation) engineering knowledge. It is not upgraded to universal claims. Per the Cycle 012 maturity gate, the claim's status is formally contingent on the adversarial-review control: a hostile domain (Cycle 013) must fail to produce pressure that escapes the existing destinations before L3 is considered further strengthened.

## Untested Boundaries

Explicitly preserved as untested:

- biological systems
- economics
- social systems
- non-engineering knowledge
- broader adaptive intelligence (beyond ML engineering)
- L4: domain-independence for *all* engineering
- deliberately hostile engineering categories (Cycle 013 candidates): distributed AI agent ecosystems, adversarial cybersecurity operations, autonomous multi-agent coordination, human-in-the-loop safety-critical systems
- genuinely different epistemologies (mathematical proof, clinical evidence, legal burden of proof) — required by the maturity gate before any motif is treated as mature

## Near-Misses and Rejected Alternatives (complete list)

1. **Cycle 001**: prose-under-headings object format — rejected in favour of structured fields (002).
2. **Cycle 004**: separate webdriver-classic object — rejected as boundary duplication (merged into automation-protocol).
3. **Cycle 005**: workflow/sequence (temporal) block — rejected; deterministic sequences fit Claims.
4. **Cycle 006**: "emergent behaviour" primitive — rejected; emergence is composition. Relationship-count upper bound — open question, never decided.
5. **Cycle 007**: "attacker" primitive — rejected (entity in graph); "uncertainty" primitive — rejected (qualifier); "decision" primitive — rejected (became an object kind instead). Qualification model (certainty vs confidence) — open, with a decision rule recorded.
6. **Cycle 008**: temporal, drift, benchmark, subjective-evidence, value, monitoring, action-selection, and self-updating-agent constructs — all rejected (8 recorded temptations).
7. **Cycle 009**: representation, formal-rule, semantics, transformation, fold, liveness, pipeline/sequence, proof, equivalence, performance, artifact-validity, and mode-divergence constructs — all rejected (12 recorded temptations). The proof candidate was the closest approach to falsification since the programme began; it resolved when "a proof is an artifact of evidence" moved the residual risk to the specification. The pipeline/sequence temptation confirmed Cycle 005's declarative principle at a new level: ordering is a graph property, not a knowledge type.
8. **Cycle 010**: data/entity, ACID/transaction, temporal-trap, isolation/consistency, query/index, migration/evolution, replication, and lineage (third appearance) constructs — all rejected (19 recorded temptations). The data semantics test — the strongest remaining candidate — resolved through composition; the unification hypothesis survived n=3; and the relational model's direct mapping onto HPF vocabulary was treated as coincidence-as-evidence rather than dismissed.
9. **Cycle 011**: time/deadline, scheduling-policy, schedulability-guarantee, concurrency/priority, temporal-constraint hidden primitive, overload/isolation, watchdog/health-check, and arbitration constructs — all rejected (19 recorded temptations). The temporal test — time as a correctness condition itself — resolved through composition; the temporal-trap chain reached its fifth defusal; the unification hypothesis survived n=5; the arbitration structure was recorded as a motif candidate, not a construct; and the temporal-constraint category label was rejected as hidden-primitive-through-language.
10. **Cycle 012**: state/signal, sensing, estimation/estimator, belief, fusion, controller, stability, safety-case/argument, fail-safe, action-generation, and arbitration constructs — all rejected (11 candidate families, 20 predictions, all held). The epistemic test — knowledge whose truth is never directly observable — resolved through composition: belief as claims qualified by confidence ("belief is composition, not ontology"), estimation as relationship structure, safety case as claim + evidence + argument artifact, autonomy as decision under an incomplete world model, arbitration re-tested at n=4 and not promoted. The Epistemic Distance gradient (1 → 3+) was measured without schema change; the Epistemic Chain closed into the Closed Epistemic Loop watch. The cycle's closest approach to failure was at the experimental-design level, not the ontology level: the closeout review identified destination bias — the research beginning to optimize itself — and adopted the adversarial-review control, the strengthened Phase 5 criterion (attempted-falsification intensity), and the motif maturity gate (engineering must not mature engineering motifs; a genuinely different epistemology — mathematical proof, clinical evidence, legal burden — is required before maturity).
11. **Cycle 013 (protocol)**: no object-level temptations — the cycle's rejection targets were methodological. Round 1: five issues identified at review and amended — (1) adversarial review still internal — fixed by the external-frame review (A1, rotating competing philosophies with CONTAINED/DISMISSED/ESCAPED outcomes); (2) destination bias reduced, not eliminated — fixed by sealed F-probes + counter-probes + the forced-fit audit (A2); (3) binary cycle success — fixed by the scorecard (A3, prospective from Cycle 014); (4) implicit Programme B criteria — fixed by explicit gates G1–G6 (A4); (5) motif candidates without statistical discipline — fixed by the promotion gate (A5). Round 2 (judgment independence): the review scored the protocol 9.7/10 and closed the remaining gap — (B1) frozen evaluation rubrics per frame pre-registered before the argument exists, verdicts mechanical; (B2) objective ESCAPED/CONTAINED/DISMISSED conditions; (B3) scorecard split objective/descriptive, never aggregated; (B4) A/B probe comparison with decoy probes replaces introspection; (B5) G7 epistemic-discontinuity pilot (medicine/biology) before Programme B; (B6) counterexample search strategies (space/inclusion/stopping/justification); (B7) randomized frame rotation (seeded, coverage-guaranteed); (B8) the Protocol Stability Principle — protocol presumed stable at v1.3, future amendments require an experiment-validated deficiency. Both rounds survived their own adversarial passes (all CONTAINED/DISMISSED).
12. **Pre-Cycle-014 full-stack adversarial review**: the canonical consolidated protocol was reviewed under the three-bucket discipline (A/B/C, C rejected). Three Category A defects were ratified and corrected as v1.3.1 — the sharpest was the **DISMISSED-override** (A-1): the verdict conditions' evaluative predicates let the response declare a frame's own frozen condition "misapplied," legally defusing any ESCAPED-eligible review (worked counterexample: the same formal-methods review yields DISMISSED or ESCAPED from the same record). Also corrected: A-2 (frame draw not re-derivable / seed-searchable — fixed by named PRNG + pre-registered nonce), A-4 (internal-review outcomes had no adjudication standard — fixed by applying B2). A fourth finding (A-3 — no document-control rule) failed the ratification test (two honest researchers cannot diverge on the same record without a text edit) and was reclassified to Category B, its fix retained as administration hardening. Eleven B-items carried; C-preferences rejected. The protocol stands frozen at v1.3.1; Cycle 014 runs under it.
13. **Cycle 014 (T1-T4, adversarial artifact analysis)**: object-level temptations were exercised through the pre-registered counter-probe structure rather than free-form rejection logs - six construct families were attempted and failed, each in-pass: adversarial-evidence (evidence that withholds/deceives as a new evidence kind), inference-chain (staged pipeline object kind, decoy D2.1), interpretation primitive (the analyst's reading as a new knowledge type), intent-as-evidence (creator's intent as directly accessible), attacker-intent object kind with its own block (decoy D3.1), and decision-under-concealment kind (decoy D4.1). All resolved as composition: claims + qualification (confidence anchored to interpretive inference for the first time) + constraints (surface != semantics; intent accessed only through the artifact; chain inheritance at the decision layer) + relationships. All sealed probes MATCHed, both decoys absent (no destination-bias flags), all 16 objects PASS 0/0, 0 primitives/kinds/verbs; H1-H9 held (H2: the confidence object shifted a third time - observation -> belief -> interpretation-of-inference - with no metadata change; H6: the Closed Epistemic Loop recurred in the open and was named a motif candidate; H8: Epistemic Distance reached 4 without schema change). G6 first-pass: 11 canonical + 4 new decision objects at exactly 4 factors; 14 legacy !=4-factor objects documented as pre-invariant corpus artifacts.
14. **Cycle 014 — external-frame review (formal-methods / model-theoretic, F1)**: the first genuine ESCAPED in programme history, and the one the A-1 fix was built for. The frame's F1 charge — claims carry natural-language validity conditions, not satisfaction clauses; "true" is not a defined predicate over the corpus — escaped: the counter-evidence's equivalence move (validity condition = truth condition) narrows F1's applicability without rubric exclusion, which A-1 forbids; the escape is terminal. F2-F5 contained. The pressure (no model-theoretic semantics among the complexity destinations) engaged the pre-registered attractor-state falsification signal — outcome class C signal recorded; the cycle was recorded **FAILED-EXTERNAL-REVIEW**; an architecture review is triggered to decide whether a semantics destination is required (H1 falsified per protocol §3) or F1's demand sits outside the programme's epistemic remit (engineering evidence practice, not formal semantics) — the first experiment-validated deficiency, making the B8 amendment path eligible. G1 is not met by 014 alone; Cycle 015 re-tests under the frozen protocol. Near-miss/milestone character: the methodology functioned as designed — the A-1 worked counterexample (the DISMISSED-override) was constructed on exactly this frame's F1; the correction made the escape real; the first hostile cycle then delivered it.

## Why HPF Looks the Way It Does Today

A future researcher reconstructing the design from this chronicle should see the following causal chain:

1. **Cycle 001's bottleneck** (prose objects unconsumable by reasoning modes) forced the structured-field quality bar in Cycle 002 — this is why objects have typed blocks instead of prose.
2. **Cycle 003's first-try successes** proved schema-native authoring, which justified retiring legacy formats (the 17 legacy corpus files that still FAIL validation are the residue of this decision — they were superseded, not migrated).
3. **Cycle 005's temporal rejection** established the declarative principle — sequences are claims, not constructs — which is why no workflow/sequence block exists.
4. **Cycle 006's systemic result** established that emergence is multi-object composition — the root of the "complexity moves into the graph" theory.
5. **Cycle 007's qualification discovery** separated *qualification metadata* from *evidence vocabulary* — the distinction that created the Complexity Migration Matrix and the Object Kind Stability metric, and which keeps uncertainty from becoming the tenth primitive.
6. **Cycle 008's validity-conditions discovery** generalised the temporal problem into "knowledge + conditions under which it remains true" — the current strongest form of the working theory.
7. **Cycle 009's observation-model discovery** extended qualification to the correctness pole: guarantees, equivalence, and verification are all relative to a stated observation model, exactly as uncertainty was relative to qualifiers in 007 — the same structure, opposite pole. Cycle 009 also generalized validity conditions from knowledge to actions (enabling conditions) and artifacts (artifact validity), and confirmed for a fifth category that change is a graph property, not a vocabulary item.
8. **Cycle 010's unification result** completed the chain: validity-as-derivation now spans knowledge (008), actions and artifacts (009), and data (010) — schema versions and backups are valid exactly as build artifacts are, under stated conditions. The cross-domain recognition motif (analogous_to) turned the corpus into a single graph, and the relational model's mapping onto HPF vocabulary became the programme's first coincidence-as-evidence result.
9. **Cycle 011's temporal result** closed the strongest remaining pressure: time as a correctness condition itself resolved as a validity condition on completion (deadline), extending the unification hypothesis to n=5 — every validity claim, including temporal ones, is bound by stated conditions that are constraints. The fifth temporal defusal completed the temporal-trap chain, the isolation family generalized across consistency/concurrency/timing, and the arbitration structure became the motif catalogue's first strong candidate — recorded as a candidate, not a construct.
10. **Cycle 012's epistemic result** resolved the strongest remaining pressure: knowledge never directly observable resolved as a chain of qualified observations and models — belief is composition, safety case is an evidence artifact, autonomy is a decision, and the chain closed into the Closed Epistemic Loop watch. The Epistemic Distance metric (distance structural, confidence qualificational) gave the programme its first measurement of how far a claim can stand from reality and still be represented with the same nine primitives.
11. **The Cycle 012 closeout review changed the experiment, not the ontology**: destination bias — the research beginning to optimize itself — was identified as an uncontrolled variable. The adversarial-review control (every cycle must produce a recorded, reasoned attempt to prove the ontology insufficient), the strengthened Phase 5 criterion (how hard did we try to prove there was no destination?), and the motif maturity gate (engineering must not mature engineering motifs) are now protocol. Confidence in HPF now grows for the right reason: survival of hostile pressure, not repeated successful fits.
12. **Cycle 013 hardened the protocol, not the objects**: five methodological gaps (internal-only adversarial review, remaining destination bias, binary cycle success, implicit Programme B criteria, motifs without statistical discipline) were amended as A1–A5 — external-frame adversarial review, sealed probes + counter-probes + forced-fit audit, the cycle scorecard, explicit Programme B gates G1–G6, and the motif promotion gate with attempted-counterexample registers. Round 2 (B1–B8) made the controls judgment-independent: frozen rubrics, mechanical verdicts, split scorecard, A/B probe comparison, the G7 epistemic-discontinuity gate, search strategies, randomized frames, and the Protocol Stability Principle (v1.3) that froze the protocol itself. The amendments withstood their own adversarial passes. The protocol is now a first-class experimental artifact: "a stronger protocol makes every future result more credible."
14. **The pre-Cycle-014 adversarial review closed the last judgment holes before the first hostile cycle**: the canonical text's verdict conditions were shown to contain evaluative predicates that let the research lead override the frames' own frozen standards (the DISMISSED-override) — the external review would have collapsed to self-review at the decisive step. The frame draw was not re-derivable, and internal-review outcomes had no adjudication standard. Three narrow defect corrections plus one administration hardening (v1.3.1) closed them; the freeze then held, and Cycle 014 is the protocol's first genuine test — not another round of protocol design.
15. **Cycle 014's first hostile-domain result (T1-T4, pre-review)**: concealed-truth knowledge composed. The modeler's own knowledge became inferential - same-status with the modelled system's - and the chain of claims carried it: surface (T1), reconstruction (T2), intent and symmetry (T3), decision (T4). The qualification model survived its deepest test (H2: confidence anchored to interpretive inference with no schema change), the first hostile cycle produced no in-cycle falsification signal (attractor-state criterion not reached at the authoring level), and the Closed Epistemic Loop - named at 012 as a watch - recurred in the open and was recorded as a motif candidate awaiting the A5+B6 promotion gate. The decision-factor invariant held (H7/G6); the pre-invariant legacy corpus was documented. The external-frame review (formal-methods, drawn at pre-registration) then returned **ESCAPED on F1 (terminal)** - the first genuine ESCAPED in programme history - engaging the attractor-state falsification signal at the review level; the F1 pressure's disposition is deferred to the triggered architecture review, and the cycle is recorded FAILED-EXTERNAL-REVIEW.
16. **Cycle 014's architecture review — the first disposition of a genuine escape (2026-08-03)**: the §6.4 review **recommended interpreting** the F1 semantics pressure as a **remit-boundary signal, not an eleventh destination** — a programme-level decision (best fit to the record: the programme's claim, SCHEMA's "independently verifiable", and the 010 validity-conditions-as-constraints precedent never included model-theoretic truth conditions), **not an experimentally demonstrated fact**; the remit clause is failure-elicited by design under B8 and carries no independent evidence value; the F1 verdict itself is immutable. No primitive, destination, ontology, or verdict-pipeline deficiency was found; one genuine scope deficiency was exposed: the protocol never declared the programme's epistemic remit — the **B8 amendment path's first use** (v1.3.2 Scope-and-remit clause, drafted; ratification pending). The blind framework reconstruction test delivered **Discovery B, recorded as two findings — B1: the representation language is reconstructible from the corpus alone; B2: the authoring process leaves statistical fingerprints independent of the schema** (a first-class finding: the reader recovered the scheme and the reasoning model, and since the fixed cardinalities are authoring-template choices rather than schema mandates, count-based evidence must control authoring-channel confounds) — the **authoring-variation discipline** was adopted, and the discrimination experiment becomes the B2 measurement instrument. The deepest open problem was named — **object identity** (Assumptions list: "engineering knowledge is decomposable into independent knowledge objects"; no convergence experiment exists) — queued as a Cycle 015 domain-selection criterion / G7 pilot item. A true-believer **kill review** was proposed as a final negative gate before Programme B. The research question was made explicit as a shift from sufficiency testing to boundary-mapping. Cycle 014 stands FAILED-EXTERNAL-REVIEW immutably; the escape is the programme's first bounded, understood limitation rather than a framework failure.
17. **The owner's dispositions of the Cycle 014 ratifications — the F1 deferral, the kill review, and Cycle 015's re-framing (2026-08-03)**: the F1 recommendation was **not ratified as a boundary** — neither arm (a) nor arm (b). Adding the remit clause immediately after the first genuine hostile failure would expose the programme to the charge that the boundary was drawn in response to the result; arm (a) over-reads one frame's expectation as a demonstrated deficiency. **F1 is recorded as an unresolved architectural tension (arm (c) deferral): the protocol is not amended (v1.3.2 stays a draft, unratified), H₁ is not falsified and not yet narrowed, and one independent replication decides the arms** — if the F1 pressure replicates under an independently drawn hostile frame, arm (a) or arm (b) is chosen on two independent observations; if it does not replicate, F1 becomes a frame-specific pressure and the remit clause earns the stronger justification the deferral was designed to buy. The evidential standard applied is the programme's own: one observation triggers investigation; repeated observations justify architectural decisions. The **kill review was ratified with four owner refinements** — mission reframed from belief in falsity to **maximization of falsification probability** (Popperian: attempt falsification with the strongest technically defensible arguments; document if it succeeds, explain why if it fails); **unrestricted attack surfaces** (any assumption, protocol, inference, decomposition, validation rule, ontology, scope decision, conclusion); **four auditable verdicts** (K1 successfully falsified / K2 previously unknown architectural defect / K3 only implementation-documentation defects / K4 could not falsify despite attempting); and a **mandatory single-experiment answer** ("What single experiment would most likely falsify HPF if I had one more cycle?") — frozen as `research/KILL_REVIEW_INSTRUMENT.md`, gated to run only after the engineering programme completes (running now would invite "the programme wasn't finished"). **Cycle 015 was ratified with its primary experiment re-framed from contested decomposition to independent decomposition convergence**: independent authors decompose the same engineering source material; the primary endpoint is whether object boundaries and relationships converge sufficiently to support stable representation — convergence, not identity, judged by scoring pre-registered before authoring begins (exact match / semantic match / split / merge / missing / novel); the hostile-domain re-test and the v1.3.2 validation are secondary outcomes. The engineering domain is the vehicle; object identity — the programme's deepest open problem — is the hypothesis. The validation argument (`research/HPF_VALIDATION_ARGUMENT.md`, v1.0) was written and carries all of this, with demonstrated results separated from programme-level decisions throughout.
18. **Cycle 015's pre-registration was frozen and ratified (2026-08-03)** — the cycle is one experiment: **independent decomposition convergence** (primary endpoint), with everything else observational and non-co-equal. Four instruments frozen before any authoring: (1) convergence bands (ratified as drafted: A ≥ 75% canonical / split-merge ≤ 10%; B ≥ 50% / ≤ 25%; C otherwise) with **lexicographic hard gates** — maximal disagreement disqualifies A, new object kinds disqualify B, an irreconcilable ontology floors at C, all regardless of percentages; (2) the independence protocol — three schema-blind fresh-context authors, identical source pack, sealed verbatim outputs, no contact, no corrections; (3) the **blind reconciliation stage** — an independent adjudicator aligning the three outputs using only frozen mapping rules, blind to hypotheses, bands, and authorship, declared the foundation of the measurement (statistics are computed exclusively on its output); (4) the interpretation table — Band A supports the object-identity assumption in its strong form, Band B makes the ontology "stable up to equivalence, not uniquely canonical" (the owner's predicted outcome: multiple equally valid decompositions without new primitives), Band C falsifies the strong assumption and triggers architecture review. The **F1-replication criterion was operationalized**: replication = a semantic-class ESCAPED (the drawn frame escapes on a charge of lacking formal-semantics machinery) under an independently drawn frame; the frame is drawn at pre-registration from the remaining rotation (ontology-first / category-theoretic / MBSE — formal-methods excluded to keep the draw independent). **Domain ratified: APT campaign-level threat analysis** — selected independently because it naturally contains contested object boundaries and inferential reconstruction; whether its epistemic profile resembles Cycle 014 is an experimental outcome, not a selection assumption. The research-psychology clause was recorded at the top of the pre-registration: the cycle is designed to be able to weaken the programme, and the interpretation table binds outcomes before the data exists.
13. Every cycle produced a candidate extension; every candidate was rejected through composition; the rejection reasons (declarative sequences, multi-object emergence, qualification as metadata, validity as constraints, evaluators as evidence sources, proof as evidence artifacts, ordering as graph property, data guarantees as constraints, time as validity condition, belief as qualification, destination-bias control and external-frame review as experimental design, protocol stability as experimental governance) are the load-bearing decisions that give HPF its current shape.

19. **Cycle 015 executed and closed — the primary endpoint was met and the F1 pressure replicated under an independently drawn frame (2026-08-03)**: the cycle ran its full pre-registered structure. **Phase 0** sealed the Source Material Pack (Midnight Foundry threat brief; SHA-256 `37020d99…86c5`), the Decomposition Task Pack, the seeded frame draw (nonce `HPF-cycle-015-frame-draw-2026-08-03` → **ontology-first**, index 0 of the remaining rotation), predictions P1–P4, frame probes T1–T4, decoys D1–D2, and the risk register R1–R4. **Phase 1** ran three fresh-context authors strictly sequentially, outputs sealed verbatim (19/17/15 objects; no corrections, no contact). **Phase 2** executed the blind reconciliation stage — three pairwise alignments by a fresh-context adjudicator blind to hypotheses, bands, and authorship (documented mechanics deviation after two void runs; rubric unchanged): **30/51 objects canonical (58.8%)**, 5 split/merge events (9.8%), **one maximal disagreement (E1 — the Hammer boundary: one author's single object aligning with 3 and 4 objects of the others, engaging H1 and making Band A unreachable)**, 0 unresolvable → **BAND B — convergence up to equivalence** (the owner's predicted outcome; P2/P3/P4 confirmed; P1 failed — the top-level campaign boundary held in all three decompositions, the divergence concentrated at the Hammer family/variant boundary). **Phase 3** authored the adjudicated union into 21 full HPF objects under the current schema (canonical referents + finer-granularity residuals per r1), all validator PASS 0/0, corpus 154 → 175 (29 pre-existing errors unchanged), authoring-variation discipline and D2/D4–D6 refinements applied (graded certainty, no overstatement candidates), relationship vocabulary exactly 8 verbs. **Phase 4** ran the ontology-first external-frame review (fresh-context reviewer, frozen R1–R5 rubric from protocol §6.3, same A-1/B2 mechanics as 014): **ESCAPED on all five conditions** — the frame's standard of formal-ontology machinery (kind/role, disposition/process, boundary/continuant, dependence, defined universals) is not expressible in the current representation. All five conditions are **semantic-class** (formal-ontology axioms) → **the F1 pressure REPLICATED**: two independent observations now exist (014 formal-methods F1; 015 ontology-first R1–R5), and per the pre-registered criterion the programme may now ratify arm (a) (semantics in scope) or arm (b) (Scope-and-remit clause, v1.3.2) **on evidence** — the arm decision is the owner's ratification point; the architecture review's retained recommendation remains arm (b). The cycle's **primary endpoint was met independently of the frame outcome** (Band B — object identity stable up to equivalence with a recorded tolerance, not uniquely canonical: the object-identity assumption survives in its bounded form, no new primitive, and the interpretation is a discovery about the ontology's semantics of identity rather than a failure). Scorecard: forced-fit 0, unresolved pressures 1 (F1 semantics pressure, disposition DEFERRED to the arm decision), vocabulary additions 0/0/0, **escaped reviews 1 (threshold 0 — violated on this review instrument)**; probes 4/4 MATCH, decoys 2/2 not realized; no protocol violations (two documented mechanics deviations, recorded at the time). Post-015 commitments queued: external replication on an unedited third-party incident report (R1 handling), dual-adjudicator consideration, Phase-6 semantic validator, kill review as the final negative gate before Programme B.
20. **Cycle 015 became the first cycle in which an independent adjudicator-level audit weakened multiple supporting statements while leaving the primary endpoint unchanged (2026-08-03)** — the audit (`research/decomposition-convergence/CYCLE_015_ADJUDICATOR_REVIEW.md`) re-derived the alignment from the raw pair files (no reliance on compiled totals): (a) **corrected arithmetic** — exact-only rate is 18/51 = 35.3% (6 referents), not the recorded 21/51 = 41.2% (7); (b) **corrected disagreement characterization** — pair 2v3's own record contains a second maximal disagreement (E5: D2.15 ↔ five D3 carriers), so E1 is not "the only maximal disagreement"; (c) **softened causal language** — the R3 structure confound is restated as a strong correspondence (referent set tracks document organization) rather than causation, with causal testing deferred to the R1 replication; (d) **unchanged primary verdict** — Band B, canonical 58.8%, split/merge 9.8%, H1 engaged via E1, 0 unresolvable — all re-confirmed from raw evidence; the band is not an artifact of counting choices. The fresh-context second adjudicator voided three times (execution-environment finding, not an HPF finding; five adjudication void runs total across the cycle). The audit named two pre-existing measurement dimensions — **referent convergence** (entities identified) and **boundary convergence** (partitioning of entities) — and elevated **R1** (replication on unedited third-party incident reports) to the programme's highest-priority external-validity experiment; both recorded as research-methodology notes in PROGRAMME_STATE.md, not protocol changes. Research-governance significance: the audit found mistakes that weaken the narrative without moving the primary conclusion — exactly what independent review is supposed to produce.

21. **Research Session 001 established research review as a first-class, mandatory stage before publication (2026-08-05)**: the first full review of a research session (`2026-08-05-0512-web-automation-pain-points-202`, "Web automation pain points (2026)") demonstrated that HPF's review process **rejects unsupported or weak findings rather than preserving them** — 14 of 21 mechanically drafted findings were rejected (restatements of official docs, nav chrome, product pitches, query drift), 7 were revised into extracted claims, and 1 was added by the reviewer. The primary defect discovered was **provenance discontinuity between findings and evidence**: findings cited a synthetic pseudo-URL while the real source threads, scores, and dates existed only in the evidence layer, unlinked. The correction (findings now carry evidence ids, real source URLs, and dates; a prose filter prevents nav chrome from becoming evidence; the planner no longer claims high relevance for off-topic evidence classes) **strengthened the evidence chain without altering the underlying research architecture** — no new primitives, no schema change. The session also established **adjudication as a mandatory stage before publication**: the review layer (`adjudication.json`) is a separate immutable artifact beside the mechanical session record, and the **Publishing Compiler refuses to compile unadjudicated sessions — rejected findings never enter a publish pack**. The first publish pack was compiled (8 accepted findings, 14 rejected excluded, six renderings: comparison, article, LinkedIn, X thread, FAQ, documentation). The research process itself is now what is evolving; UI, connectors, and deployment are background infrastructure.

22. **The v1 release of the research platform and the feature freeze (2026-08-05)**: "Release HPF Workbench" was dispatched and completed — deployment of the full pipeline (research intake, evidence collection with classes, community signals, adjudication, accepted findings, publishing compiler, publish packs). The architecture phase is declared over; the question shifts from "How should HPF work?" to "How well does HPF research?" — answerable empirically, not architecturally. **v1 is feature-frozen**: allowed are bug fixes, new evidence connectors only when a session fails without them, better extraction/adjudication/publishing quality, performance improvements; **not allowed without repeated evidence** are new dashboards, workflow pages, navigation, governance, and architecture. The programme split into two independent roadmaps — **Roadmap A: Research Engine** (success metric: can HPF consistently produce high-quality adjudicated findings; planner/connector/extraction/adjudication quality) and **Roadmap B: Publishing Compiler** (success metric: how much editing does a publish pack require before publication — per-render editing minutes recorded per session, Blog/LinkedIn/X/Documentation; the metric trends downward as the compiler improves). A **Research Yield** KPI was adopted — Evidence → Draft Findings → Accepted Findings; Session 001: 21 draft → 8 accepted ≈ 38% — to be tracked across sessions: not to be maximized (a lower yield can indicate a stricter review), but observed for stability as planner and extraction improve. **Session 001 is declared the regression test**: whenever planner, connector, extraction, adjudication, or publishing compiler change, re-run the identical session and compare evidence, draft findings, accepted findings, and publish pack quality; an improvement that worsens accepted findings or introduces unsupported claims is a regression. From this point, research quality and publish pack quality drive evolution, not further design discussion.

23. **The development phase formally closed; HPF entered operation (2026-08-05)**: the platform was declared complete enough for its intended purpose, and the phase shifted from development ("what should we build?") to operation ("what did today's research teach us?"). The fundamental change is that HPF now has **feedback loops** — Research → Review → Publish → Measure → Improve — replacing the build/add-feature cycle. Every layer is declared stable: ontology, validation protocol, export contract, research orchestrator, adjudication, publishing compiler (v1), workbench, release process. An **operating routine** was established in place of release thinking: choose research topic in the morning, run HPF, review findings, generate publish packs, publish if ready, log friction — daily operation naturally reveals where the system needs improvement. The **KPI set is declared complete**: Research Yield (pipeline selectivity), Editing Time (compiler usefulness), Usage Log (workbench friction), Regression Session 001 (change quality) — no new KPIs until several weeks of data accumulate. An owner-only dashboard card ("Today's Research": sessions, accepted findings, yield, packs, editing time) was explicitly **deferred until 30–50 sessions** make trends meaningful without digging through sessions. Priorities for the next six months: run real research daily, publish from HPF rather than ad hoc prompts, measure editing time honestly, and improve only what repeatedly slows the work down. No architecture review is scheduled; the next 20–30 sessions speak for the system, and evolution waits for recurring evidence — the programme's focus has evolved from how knowledge should be represented to how knowledge is created, validated, and reused.

---

*Compiled 2026-08-01 from per-cycle dossiers, cycle summaries, schema friction logs, PROGRAMME_STATE.md, the knowledge corpus, and validator output. Predictions and results are kept chronologically separate throughout; nothing was reconstructed from hindsight. Cycle 012 closeout updates (cycle summary, PROGRAMME_STATE, protocol controls, dossier repair), Cycle 013 protocol hardening (amendments A1–A5 round 1 + B1–B8 round 2, protocol version v1.3, Protocol Stability Principle), and the pre-Cycle-014 full-stack adversarial review (defect corrections A-1/A-2/A-4 + A-3 administration hardening, ratified protocol v1.3.1), and Cycle 014 T1–T4 authoring (16 objects, adversarial artifact analysis, all probes MATCH, H1–H9 held, Closed Epistemic Loop motif candidate named), and the Cycle 014 external-frame review (formal-methods: F1 ESCAPED terminal, F2–F5 CONTAINED — cycle FAILED-EXTERNAL-REVIEW, attractor-state falsification signal recorded, architecture review triggered) recorded on the same date, and the Cycle 014 closeout (purification passes 2–3, two-mode authoring discipline formalized, blind framework reconstruction test with divergence record, freeze-era corrections, Discovery B, architecture review — F1 adjudicated as a remit-boundary signal with B8 amendment v1.3.2 drafted, object-identity assumption queued, authoring-variation discipline adopted) recorded 2026-08-03, and the owner dispositions of the same date (F1 arm-(c) deferral with the Cycle 015 replication criterion, kill review ratified with four refinements and instrument frozen, Cycle 015 re-framed as independent decomposition convergence, validation argument v1.0 written) recorded 2026-08-03, and the Cycle 015 pre-registration ratification (independent decomposition convergence as the primary endpoint with four frozen instruments, lexicographic band gates, blind reconciliation stage, APT campaign-level vehicle, F1-replication criterion operationalized as a semantic-class ESCAPED under an independently drawn frame) recorded 2026-08-03, and the Cycle 015 execution and closeout (Phase 0 seals and ontology-first frame draw, Phase 1 three sealed decompositions, Phase 2 blind reconciliation with the Band B verdict — 58.8% canonical, maximal disagreement at the Hammer boundary, P1 failed / P2–P4 confirmed, Phase 3 authoring of the 21-object adjudicated union, Phase 4 ontology-first review ESCAPED on all five R-conditions with the F1-replication observation confirmed — the arm decision now eligible on two independent observations — primary endpoint met) recorded 2026-08-03.*
