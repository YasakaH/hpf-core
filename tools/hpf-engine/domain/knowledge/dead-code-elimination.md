# Dead Code Elimination

## Identity
- id: dead-code-elimination
- type: concept
- title: Dead Code Elimination
- tags: [compilers, optimization, dead code, liveness, analysis, code size]
- entities: [dead code, dead code elimination, liveness analysis, unreachable code, unused computation, code size]
- concepts: [compiler-optimization, abstract-syntax-tree, program-semantics, equivalence-checking, compiler-performance]

## Claims
- claim: "Dead code is code that cannot affect observable behaviour — unreachable code, unused results, and redundant computation."
  certainty: high
  evidence: Compiler construction practice and literature
  scope: cross-domain
- claim: "Dead code elimination removes dead code from the program — a transformation that shrinks the program without changing its observable behaviour."
  certainty: high
  evidence: Compiler implementation practice
  scope: cross-domain
- claim: "Elimination correctness depends on liveness analysis — code is removed only when analysis proves it cannot be observed."
  certainty: high
  evidence: Dataflow analysis theory and practice
  scope: cross-domain
- claim: "Liveness analysis results are observations, not guarantees — an analysis bug that marks live code dead produces a miscompilation."
  certainty: high
  evidence: Compiler bug analyses
  scope: cross-domain
- claim: "Elimination must respect the observation model — side effects, volatile access, and external observability make code live even when its result is unused."
  certainty: high
  evidence: Compiler engineering practice
  scope: cross-domain

## Relationships
- concept: compiler-optimization
  relationship: instance_of
  description: "Dead code elimination is a compiler optimization — removal of unobservable computation."
- concept: abstract-syntax-tree
  relationship: operates_on
  description: "Dead code elimination operates on program structure — dead subtrees are located through the AST or IR."
- concept: program-semantics
  relationship: preserves
  description: "Dead code elimination preserves program semantics — removal is legal only for unobservable code."
- concept: equivalence-checking
  relationship: verifiable_by
  description: "Dead code elimination is verifiable by equivalence checking — before/after comparison under the observation model."
- concept: compiler-performance
  relationship: improves
  description: "Dead code elimination improves compiler performance outputs — smaller binaries and less wasted runtime work."

## Tradeoffs
- dimension: elimination_aggressiveness_vs_soundness
  options:
    aggressive_elimination:
      value: size_savings
      rationale: "Aggressive elimination removes more code but increases reliance on precise liveness analysis."
    conservative_elimination:
      value: safety
      rationale: "Conservative elimination keeps suspicious code but leaves size and speed on the table."
  importance: high
- dimension: analysis_precision_vs_cost
  options:
    precise_analysis:
      value: elimination_coverage
      rationale: "Precise liveness finds more dead code but costs analysis time and complexity."
    cheap_analysis:
      value: compile_speed
      rationale: "Cheap analysis is fast but misses dead code that precise analysis would find."
  importance: medium

## Failure Modes
- name: live_code_elimination
  description: "Liveness analysis marks live code dead — the elimination removes computation the program could observe, changing behaviour."
  likelihood: medium
  observable_evidence: "Behaviour differences after optimization; missing side effects; crashes in optimized builds only"
  detection: "Differential testing across optimization levels; liveness analysis audits; targeted edge-case tests"
  recovery: "Fix the liveness analysis; add conservative guards; regression tests for observability edges"
  retryable: true
- name: observability_misclassification
  description: "Code with external effects (volatile access, I/O, exception paths) is treated as unobservable — elimination strips behaviour the program's contract guarantees."
  likelihood: medium
  observable_evidence: "Removed side effects in optimized builds; volatile reads disappearing; error paths vanishing"
  detection: "Observability conformance tests; semantic audits; differential testing"
  recovery: "Model external observability explicitly; exclude observable constructs from elimination; regression tests"
  retryable: true
- name: retained_dead_code
  description: "Dead code survives elimination — unreachable or unused computation remains, costing size and runtime."
  likelihood: medium
  observable_evidence: "Unreachable blocks in generated code; unused computations surviving optimization; larger binaries than expected"
  detection: "Generated-code inspection; coverage analysis; binary size analysis"
  recovery: "Strengthen reachability analysis; extend liveness; iterate to fixed points"
  retryable: true

## Observations
- observation: "Elimination soundness is entirely an analysis property — the removal step is trivial once liveness is right."
  confidence: high
  source: Compiler implementation practice
- observation: "Observability edge cases (volatile, I/O, exceptions) are where elimination bugs actually live."
  confidence: high
  source: Compiler bug analyses
- observation: "Dead code elimination is a size optimization as much as a speed one — it is the backbone of binary size reduction."
  confidence: high
  source: Compiler engineering practice

## Constraints
- constraint: "Code may be eliminated only when analysis proves it unobservable — elimination without proof is a miscompilation."
  type: invariant
  scope: cross-domain
- constraint: "The observation model bounds elimination — external observability (side effects, volatile, I/O) makes code live."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Treat liveness analysis output as a hypothesis until the observation model is checked."
  rationale: "Liveness and observability are different questions; conflating them is the elimination bug."
  evidence_level: high
- heuristic: "Test elimination on side-effect-heavy and exception-heavy code specifically."
  rationale: "Observability edges are where sound elimination becomes miscompilation."
  evidence_level: high

## Recommendations
- recommendation: "Base elimination decisions on explicit liveness and reachability evidence."
  context: optimization_implementation
  certainty: strong
  rationale: "Analysis-driven elimination is sound; appearance-driven elimination is a bug."
- recommendation: "Model external observability explicitly before designing elimination."
  context: compiler_architecture
  certainty: strong
  rationale: "The observation model decides which code is live; get it wrong and the optimizer deletes behaviour."
- recommendation: "Differential-test elimination across optimization levels on observability-heavy programs."
  context: testing
  certainty: strong
  rationale: "Elimination bugs present as build-dependent behaviour; differential testing finds them."
