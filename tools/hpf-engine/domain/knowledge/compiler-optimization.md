# Compiler Optimization

## Identity
- id: compiler-optimization
- type: concept
- title: Compiler Optimization
- tags: [compilers, optimization, transformation, semantics preservation, performance]
- entities: [compiler optimization, transformation, optimization opportunity, semantics preservation, performance gain]
- concepts: [abstract-syntax-tree, intermediate-representation, program-semantics, optimization-pass, constant-folding, dead-code-elimination, equivalence-checking, compiler-performance]

## Claims
- claim: "A compiler optimization is a transformation of a program's representation that preserves observable semantics while improving a target cost (speed, size, energy)."
  certainty: high
  evidence: Compiler construction practice and literature
  scope: cross-domain
- claim: "Optimization correctness is semantic preservation — a transformation that changes program meaning is a miscompilation, not an optimization."
  certainty: high
  evidence: Compiler correctness practice, miscompilation incident analyses
  scope: cross-domain
- claim: "Every optimization has enabling conditions — a transformation is valid only when its preconditions (analysis results, dominance, liveness, constancy) hold."
  certainty: high
  evidence: Compiler implementation practice
  scope: cross-domain
- claim: "Optimizations trade target costs against each other and against compilation time — speed, size, and build time are competing objectives."
  certainty: high
  evidence: Compiler engineering practice
  scope: cross-domain
- claim: "Optimization validity is relative to the observation model — transformations legal under input-output equivalence may be illegal under stricter behavioural observation."
  certainty: high
  evidence: Program equivalence research, compiler engineering experience
  scope: cross-domain

## Relationships
- concept: abstract-syntax-tree
  relationship: operates_on
  description: "Optimizations operate on the AST — tree rewriting is the simplest optimization channel."
- concept: intermediate-representation
  relationship: operates_on
  description: "Optimizations operate on the IR — most optimization passes run on intermediate representations."
- concept: program-semantics
  relationship: preserves
  description: "Optimizations preserve program semantics — meaning preservation is the correctness obligation."
- concept: optimization-pass
  relationship: organized_as
  description: "Optimizations are organized as passes — individual transformations are scheduled in pipelines."
- concept: constant-folding
  relationship: includes
  description: "Constant folding is a compiler optimization — the simplest form of compile-time evaluation."
- concept: dead-code-elimination
  relationship: includes
  description: "Dead code elimination is a compiler optimization — removal of code that cannot affect observable behaviour."
- concept: equivalence-checking
  relationship: verified_by
  description: "Optimizations are verified by equivalence checking — before/after comparison validates the transformation."
- concept: compiler-performance
  relationship: driven_by
  description: "Optimization drives compiler performance — the generated code's efficiency is the optimization objective."

## Tradeoffs
- dimension: optimization_aggressiveness_vs_compile_time
  options:
    aggressive_optimization:
      value: generated_code_quality
      rationale: "Aggressive optimization produces faster code but can cost disproportionate compile time and compile memory."
    conservative_optimization:
      value: build_speed
      rationale: "Conservative optimization keeps builds fast but leaves performance on the table."
  importance: high
- dimension: transformation_breadth_vs_risk
  options:
    broad_transformations:
      value: optimization_coverage
      rationale: "Wide transformation sets capture more optimization opportunities but enlarge the miscompilation surface."
    narrow_transformations:
      value: correctness_assurance
      rationale: "Narrow, well-understood transformations are easier to verify but miss opportunities."
  importance: high

## Failure Modes
- name: miscompilation
  description: "A transformation changes program meaning — the optimization is unsound for some input, usually due to an incorrect enabling condition."
  likelihood: medium
  observable_evidence: "Correct source producing wrong behaviour at some optimization level; code differences between -O0 and -O2; rare, input-specific wrong results"
  detection: "Differential testing across optimization levels; random program generation; equivalence checking"
  recovery: "Fix the enabling condition; disable the unsafe transformation; reduce optimization scope"
  retryable: true
- name: optimization_blowup
  description: "An optimization pass consumes disproportionate time or memory on pathological input — compilation slows or dies on real programs."
  likelihood: medium
  observable_evidence: "Compile-time spikes on specific functions; compiler OOM or timeouts; superlinear pass behaviour"
  detection: "Compile-time profiling; pass budget instrumentation; pathological input generation"
  recovery: "Add pass budget thresholds; cap work per unit; pre-analyse pathological shapes"
  retryable: true
- name: missed_opportunity
  description: "An analysis result is too weak for the transformation to fire — valid optimizations do not apply, leaving performance on the table."
  likelihood: medium
  observable_evidence: "Benchmarks lagging compiler generations; expected optimizations absent from generated code; analysis precision gaps"
  detection: "Generated-code inspection; optimization opportunity analysis; compiler regression testing"
  recovery: "Strengthen analyses; extend transformation preconditions; canonicalize inputs earlier"
  retryable: true

## Observations
- observation: "Semantic preservation is the single invariant every optimization obeys — the whole optimization space is defined by what preserves meaning."
  confidence: high
  source: Compiler construction practice
- observation: "Most miscompilations trace to a wrong enabling condition, not to a fundamentally broken transformation idea."
  confidence: high
  source: Compiler bug analyses
- observation: "Optimization validity is decided per-observation-model — the same transformation may be legal and illegal in different contexts."
  confidence: high
  source: Compiler engineering experience

## Constraints
- constraint: "Every optimization must preserve observable semantics — meaning change is a correctness failure, not a feature."
  type: invariant
  scope: cross-domain
- constraint: "A transformation is valid only where its enabling conditions hold — applying it elsewhere is unsound by construction."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Verify optimization correctness against the observation model, not against test cases."
  rationale: "Test cases cannot cover the transformation's input space; the model can."
  evidence_level: high
- heuristic: "Differential-test optimization levels against each other."
  rationale: "Level-to-level divergence is the cheapest miscompilation detector."
  evidence_level: high

## Recommendations
- recommendation: "State the enabling conditions of every transformation and gate its application on them."
  context: optimization_implementation
  certainty: strong
  rationale: "Enabling conditions are where optimization soundness lives and dies."
- recommendation: "Treat each optimization as a hypothesis — test it differentially against unoptimized output."
  context: testing
  certainty: strong
  rationale: "Differential testing is the standard miscompilation net; skip it only at known risk."
- recommendation: "Define the observation model the optimizer is allowed to change, and document it."
  context: compiler_governance
  certainty: strong
  rationale: "Undocumented behavioural freedom becomes user-facing surprises."
