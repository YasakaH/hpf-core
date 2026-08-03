# Optimization Pass

## Identity
- id: optimization-pass
- type: pattern
- title: Optimization Pass
- tags: [compilers, optimization, pass pipeline, phase ordering, fixed point, SSA]
- entities: [optimization pass, pass pipeline, phase ordering, fixed point, pass manager, canonical form]
- concepts: [compiler-optimization, intermediate-representation, program-semantics, compiler-performance, compiler-correctness]

## Claims
- claim: "An optimization pass is a single unit of transformation — a well-scoped rewrite over a program representation, reusable across programs."
  certainty: high
  evidence: Compiler construction practice
  scope: cross-domain
- claim: "Passes are composed into pipelines — a sequence of passes whose combined effect is the optimization outcome."
  certainty: high
  evidence: Compiler implementation practice
  scope: cross-domain
- claim: "Pass ordering matters — the output of one pass changes what later passes can do, and the best order is not always obvious."
  certainty: high
  evidence: Phase ordering research and practice
  scope: cross-domain
- claim: "Many passes are fixed-point computations — they must run until no further improvement occurs, with guaranteed termination."
  certainty: high
  evidence: Dataflow analysis theory, compiler practice
  scope: cross-domain
- claim: "A pass pipeline is correct only if every constituent pass preserves semantics — pipeline correctness is the composition of per-pass correctness."
  certainty: high
  evidence: Compiler correctness practice
  scope: cross-domain

## Relationships
- concept: compiler-optimization
  relationship: composed_of
  description: "A pass pipeline is composed of compiler optimizations — passes are the organizational unit of transformations."
- concept: intermediate-representation
  relationship: operates_on
  description: "Passes operate on the IR — pipelines are defined over representation levels."
- concept: program-semantics
  relationship: preserves
  description: "Passes preserve program semantics — each constituent transformation carries the preservation obligation."
- concept: compiler-performance
  relationship: affects
  description: "Pass pipelines affect compiler performance — pass count and complexity dominate compile time."
- concept: compiler-correctness
  relationship: constrained_by
  description: "Pass pipelines are constrained by compiler correctness — ordering changes must not break preservation."

## Tradeoffs
- dimension: pass_granularity_vs_pipeline_complexity
  options:
    fine_grained_passes:
      value: composability
      rationale: "Small passes are easier to verify and reuse but create long pipelines with ordering complexity."
    coarse_grained_passes:
      value: pipeline_simplicity
      rationale: "Large passes simplify the pipeline but are harder to verify and less reusable."
  importance: high
- dimension: canonicalization_vs_opportunity_preservation
  options:
    aggressive_canonicalization:
      value: analysis_stability
      rationale: "Strong canonical forms make analyses predictable but can normalize away opportunities."
    gentle_canonicalization:
      value: opportunity_retention
      rationale: "Minimal canonicalization preserves more shapes but makes analyses less stable."
  importance: medium

## Failure Modes
- name: phase_ordering_problem
  description: "A pass order prevents later passes from firing — opportunity is lost because an earlier pass changed the shape a later pass needed."
  likelihood: high
  observable_evidence: "Identical code optimizing differently after reordering; missing expected optimizations; benchmark sensitivity to pass order"
  detection: "Pass order experiments; optimization opportunity analysis; generated-code inspection"
  recovery: "Re-order passes; iterate pipelines to fixed points; canonicalize before analysis-heavy passes"
  retryable: true
- name: pass_interaction_bug
  description: "Two passes interact badly — each is correct alone, but their composition breaks a shared assumption."
  likelihood: medium
  observable_evidence: "Correctness failures that vanish when a pass is disabled; wrong code only at specific pipeline configurations"
  detection: "Pass bisection; disabling experiments; differential testing across pipeline variants"
  recovery: "Find and fix the shared assumption; document pass contracts; regression-test the combination"
  retryable: true
- name: nontermination
  description: "A fixed-point pass fails to converge — the pass oscillates or cycles instead of reaching a stable output."
  likelihood: low
  observable_evidence: "Compiler hangs; compile-time runaway on specific inputs; version-dependent termination"
  detection: "Pass iteration logging; timeouts; convergence analysis"
  recovery: "Strengthen the ordering relation; add convergence safeguards; cap iterations"
  retryable: true

## Observations
- observation: "Pipeline composition dominates optimization architecture — most optimization design problems are pipeline design problems."
  confidence: high
  source: Compiler architecture practice
- observation: "Phase ordering is an active research problem with no general solution — compilers rely on engineered orderings, not theory."
  confidence: high
  source: Phase ordering research literature
- observation: "Canonicalization before analysis makes pipelines dramatically more stable."
  confidence: high
  source: Compiler engineering practice

## Constraints
- constraint: "Pipeline correctness is the composition of per-pass correctness — one unsound pass invalidates the pipeline."
  type: invariant
  scope: cross-domain
- constraint: "Fixed-point passes must terminate — a pass that cannot converge is a pipeline defect regardless of its quality."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Canonicalize before analysis-heavy passes."
  rationale: "Stable input shapes make downstream analyses and rewrites predictable."
  evidence_level: high
- heuristic: "Bisect pass pipelines when correctness fails."
  rationale: "The faulty pass is almost never the one you suspect; bisection finds it."
  evidence_level: high

## Recommendations
- recommendation: "Document each pass's contract — its assumptions, what it canonicalizes, and what it requires from its input."
  context: pipeline_design
  certainty: strong
  rationale: "Pass interaction bugs come from undocumented shared assumptions."
- recommendation: "Run passes to fixed points deliberately, with termination guarantees."
  context: optimization_implementation
  certainty: strong
  rationale: "Half-applied analyses are the source of missed and unsafe opportunities."
- recommendation: "Test pipelines differentially, including pass-order variants."
  context: testing
  certainty: strong
  rationale: "Ordering bugs only surface when the pipeline changes; make change cheap."
