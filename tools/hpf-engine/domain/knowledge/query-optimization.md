# Query Optimization

## Identity
- id: query-optimization
- type: concept
- title: Query Optimization
- tags: [databases, query optimization, rewriting, logical equivalence, semantics preservation, plans]
- entities: [query optimization, query rewrite, logical equivalence, result relation, cost reduction]
- concepts: [query-planning, equivalence-checking, relational-model, compiler-optimization, index-selection]

## Claims
- claim: "Query optimization is the transformation of a query into an equivalent form with lower execution cost — the result relation is the correctness contract."
  certainty: high
  evidence: Query optimization theory and practice
  scope: cross-domain
- claim: "Optimization correctness is logical equivalence — a rewrite that changes the result relation is a miscompilation of the query."
  certainty: high
  evidence: Query optimization literature, database incident analyses
  scope: cross-domain
- claim: "Query rewrites are judged against the relational observation model — two query forms are equivalent when they produce the same relation under the model's semantics."
  certainty: high
  evidence: Relational algebra theory
  scope: cross-domain
- claim: "Every rewrite has enabling conditions — equivalence holds only where the rewrite's preconditions (semantics of operators, data independence, NULL handling) hold."
  certainty: high
  evidence: Query optimization implementation practice
  scope: cross-domain
- claim: "Query optimization is the same epistemic structure as compiler optimization — a transformation of representation that preserves meaning."
  certainty: high
  evidence: Cross-domain comparison, compiler and database practice
  scope: cross-domain

## Relationships
- concept: query-planning
  relationship: performs
  description: "Query optimization performs query planning — the optimizer produces the execution plan."
- concept: equivalence-checking
  relationship: bounded_by
  description: "Query optimization is bounded by equivalence checking — rewrites must be judged for logical equivalence."
- concept: relational-model
  relationship: preserves
  description: "Query optimization preserves the relational model's semantics — result relations are the contract."
- concept: compiler-optimization
  relationship: analogous_to
  description: "Query optimization is analogous to compiler optimization — the cross-domain link to the Cycle 009 corpus."
- concept: index-selection
  relationship: shaped_by
  description: "Query optimization is shaped by index selection — the index set determines achievable rewrites."

## Tradeoffs
- dimension: rewrite_aggressiveness_vs_correctness_risk
  options:
    aggressive_rewrites:
      value: cost_reduction
      rationale: "Aggressive rewriting finds cheaper plans but widens the equivalence-risk surface."
    conservative_rewrites:
      value: correctness
      rationale: "Conservative rewriting avoids risky transforms but leaves cost on the table."
  importance: high
- dimension: optimization_depth_vs_plan_stability
  options:
    deep_optimization:
      value: plan_quality
      rationale: "Deep optimization finds better plans but changes them more often."
    shallow_optimization:
      value: predictability
      rationale: "Shallow optimization is stable but misses opportunities."
  importance: medium

## Failure Modes
- name: non_equivalent_rewrite
  description: "A rewrite changes the result relation — the optimized query returns different data than the original."
  likelihood: medium
  observable_evidence: "Different results across execution plans; data discrepancies tied to query form; NULL/duplicate edge-case divergence"
  detection: "Differential query testing; equivalence checks; edge-case conformance tests"
  recovery: "Disable the unsafe rewrite; fix its enabling conditions; regression test"
  retryable: true
- name: rewrite_blowup
  description: "Optimization explodes in cost — rewrite search consumes disproportionate time and memory."
  likelihood: medium
  observable_evidence: "Query compile-time spikes; optimizer resource exhaustion; pathological query shapes"
  detection: "Optimizer profiling; rewrite budget instrumentation; complexity analysis"
  recovery: "Bound rewrite search; add budget thresholds; simplify the query"
  retryable: true
- name: missed_optimization
  description: "Enabling conditions fail to fire — equivalent cheaper forms exist but are never reached."
  likelihood: medium
  observable_evidence: "Slow plans for optimizable queries; planner missing obvious rewrites; cost-model surprises"
  detection: "Plan inspection; rewrite-opportunity analysis; query benchmarking"
  recovery: "Strengthen enabling conditions; canonicalize earlier; extend rewrite coverage"
  retryable: true

## Observations
- observation: "Query optimization and compiler optimization share the same structure — transformation + equivalence contract — across different execution targets."
  confidence: high
  source: Cross-domain comparison (Cycle 009)
- observation: "Most wrong-result incidents trace to rewrites whose enabling conditions were weaker than assumed."
  confidence: high
  source: Database incident analyses
- observation: "The result relation is the observation model — every rewrite question reduces to it."
  confidence: high
  source: Relational theory and practice

## Constraints
- constraint: "Every rewrite must preserve the result relation — semantic change is a correctness failure."
  type: invariant
  scope: cross-domain
- constraint: "Rewrites are legal only where their enabling conditions hold — equivalence is conditional, not universal."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Verify rewrites against the relational observation model."
  rationale: "The result relation is the only contract that matters."
  evidence_level: high
- heuristic: "Differential-test optimized queries against unoptimized forms."
  rationale: "Divergence is the cheapest equivalence detector."
  evidence_level: high

## Recommendations
- recommendation: "Gate rewrites on their enabling conditions."
  context: optimizer_engineering
  certainty: strong
  rationale: "Enabling conditions are where equivalence lives and dies."
- recommendation: "Differential-test query optimization against unoptimized execution."
  context: testing
  certainty: strong
  rationale: "Equivalence violations surface as plan-dependent data differences."
- recommendation: "Treat optimizer correctness with compiler correctness discipline."
  context: governance
  certainty: strong
  rationale: "An optimizer is a compiler for a declarative language; its bugs are miscompilations."
