# Build Systems

## Identity
- id: build-systems
- type: pattern
- title: Build Systems
- tags: [build systems, incremental builds, dependency graph, caching, artifact validity, toolchain]
- entities: [build system, dependency graph, build artifact, incremental build, cache invalidation, toolchain]
- concepts: [compiler-performance, optimization-tradeoffs, debug-vs-release-modes, compiler-optimization]

## Claims
- claim: "A build system derives artifacts from sources through a dependency graph — the graph defines what must rebuild when anything changes."
  certainty: high
  evidence: Build system design practice
  scope: cross-domain
- claim: "Artifact validity is the core correctness property — an artifact is valid if and only if it was derived from the current sources and toolchain state."
  certainty: high
  evidence: Build engineering practice, stale-artifact incident analyses
  scope: cross-domain
- claim: "Incremental builds are caching over the dependency graph — correctness requires invalidation to match the dependency relation exactly."
  certainty: high
  evidence: Build system implementation practice
  scope: cross-domain
- claim: "The dependency graph is an engineering artifact with its own failure modes — missing edges produce stale artifacts; extra edges produce rebuild storms."
  certainty: high
  evidence: Build incident analyses
  scope: cross-domain
- claim: "Build reproducibility depends on hermeticity — builds that consume ambient state (time, network, environment) cannot be reproduced or trusted."
  certainty: high
  evidence: Reproducible builds practice
  scope: cross-domain

## Relationships
- concept: compiler-performance
  relationship: constrains
  description: "Build systems constrain compiler performance — incremental expectations bound what compilation work is acceptable."
- concept: optimization-tradeoffs
  relationship: executes
  description: "Build systems execute optimization tradeoffs — posture decisions are realized as build configuration."
- concept: debug-vs-release-modes
  relationship: produces
  description: "Build systems produce debug and release modes — both postures are build products."
- concept: compiler-optimization
  relationship: invokes
  description: "Build systems invoke compiler optimizations — the optimizer runs inside the build's dependency graph."

## Tradeoffs
- dimension: build_parallelism_vs_determinism
  options:
    maximum_parallelism:
      value: speed
      rationale: "Parallel builds are fast but introduce scheduling-dependent outputs and harder reproducibility."
    serial_determinism:
      value: reproducibility
      rationale: "Deterministic builds are reproducible and auditable but slower."
  importance: high
- dimension: caching_aggressiveness_vs_correctness
  options:
    aggressive_caching:
      value: build_speed
      rationale: "Aggressive caching makes builds fast but increases the surface for stale artifacts."
    conservative_caching:
      value: correctness
      rationale: "Conservative caching rebuilds more than necessary but avoids stale artifacts."
  importance: high

## Failure Modes
- name: stale_artifact
  description: "A build reuses an artifact whose sources or toolchain changed — the product does not match the code it claims to be."
  likelihood: medium
  observable_evidence: "Behaviour not matching current source; bugs fixed in code persisting in builds; version-mismatch incidents"
  detection: "Clean-build comparison; hash verification; dependency-graph audits"
  recovery: "Fix the missing dependency edge; invalidate caches; verify from clean build"
  retryable: true
- name: rebuild_storm
  description: "Extra dependency edges cause excessive rebuilding — legitimate changes invalidate unrelated artifacts."
  likelihood: medium
  observable_evidence: "Build times exploding after small changes; unrelated modules rebuilding; CI wall-clock growth"
  detection: "Dependency-graph analysis; incremental-build profiling; change-impact review"
  recovery: "Prune dependency edges; refine granularity; add change-tracking granularity"
  retryable: true
- name: nonhermetic_build
  description: "The build depends on ambient state — output varies with environment, time, or network, defeating reproducibility."
  likelihood: medium
  observable_evidence: "Different outputs from identical inputs; build failures that succeed on retry; machine-dependent behaviour"
  detection: "Clean-environment rebuilds; reproducibility checks; ambient-state auditing"
  recovery: "Hermetic toolchains; pinned dependencies; environment capture"
  retryable: true

## Observations
- observation: "Stale artifacts are the dominant correctness failure class in build engineering — invalidation logic is where trust is won and lost."
  confidence: high
  source: Build incident analyses
- observation: "Dependency-graph correctness degrades silently — missing edges accumulate until an incident exposes them."
  confidence: high
  source: Build engineering experience
- observation: "Incremental build correctness is rarely tested deliberately — most teams trust the graph until it betrays them."
  confidence: high
  source: Build engineering practice

## Constraints
- constraint: "Artifact validity is defined by derivation — an artifact is valid only if derived from current sources and toolchain state."
  type: invariant
  scope: cross-domain
- constraint: "Invalidation must match the dependency relation exactly — over-invalidation wastes builds; under-invalidation ships stale artifacts."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Treat the dependency graph as code with tests."
  rationale: "Graph errors are silent until incident; deliberate testing makes them visible."
  evidence_level: high
- heuristic: "Verify from clean builds periodically."
  rationale: "Clean builds are the only ground truth for incremental-build claims."
  evidence_level: high

## Recommendations
- recommendation: "Derive invalidation from the declared dependency graph, and test the graph."
  context: build_architecture
  certainty: strong
  rationale: "Correctness follows the graph; untested graphs accumulate missing edges."
- recommendation: "Make builds hermetic — pin toolchains and eliminate ambient-state dependence."
  context: build_governance
  certainty: strong
  rationale: "Reproducibility is the precondition for trust in any build artifact."
- recommendation: "Compare incremental and clean builds as a routine check."
  context: build_testing
  certainty: strong
  rationale: "Stale artifacts present as divergence between the two; make divergence visible."
