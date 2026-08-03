# Constant Folding

## Identity
- id: constant-folding
- type: concept
- title: Constant Folding
- tags: [compilers, optimization, constant folding, compile-time evaluation, semantics preservation]
- entities: [constant folding, constant expression, compile-time evaluation, fold, literal]
- concepts: [compiler-optimization, abstract-syntax-tree, program-semantics, equivalence-checking, compiler-correctness]

## Claims
- claim: "Constant folding is the compile-time evaluation of constant expressions — replacing a computable expression with its value."
  certainty: high
  evidence: Compiler construction practice
  scope: cross-domain
- claim: "Folding preserves semantics only when the operands are truly constant under the language's rules — value-dependent effects break the precondition."
  certainty: high
  evidence: Compiler implementation practice, correctness literature
  scope: cross-domain
- claim: "Folding interacts with undefined and implementation-defined behaviour — integer overflow, division by zero, and rounding rules decide what folding is legal."
  certainty: high
  evidence: Language standard practice, compiler bug analyses
  scope: cross-domain
- claim: "Folding is the simplest transformation — no control flow, no liveness, just value computation — making it the canonical test case for transformation correctness."
  certainty: high
  evidence: Compiler implementation practice
  scope: cross-domain
- claim: "Folding shifts work from runtime to compile time — the tradeoff is compile-time cost against the runtime value of the eliminated computation."
  certainty: high
  evidence: Compiler engineering practice
  scope: cross-domain

## Relationships
- concept: compiler-optimization
  relationship: instance_of
  description: "Constant folding is a compiler optimization — the simplest member of the transformation family."
- concept: abstract-syntax-tree
  relationship: operates_on
  description: "Constant folding operates on AST subtrees — constant expressions are visible as tree shapes."
- concept: program-semantics
  relationship: preserves
  description: "Constant folding preserves program semantics — folding is legal only when the folded value equals the evaluated expression."
- concept: equivalence-checking
  relationship: verifiable_by
  description: "Constant folding is verifiable by equivalence checking — before/after comparison is trivial when values are known."
- concept: compiler-correctness
  relationship: bounded_by
  description: "Constant folding is bounded by compiler correctness — an unsound fold is a miscompilation."

## Tradeoffs
- dimension: folding_aggressiveness_vs_semantics_risk
  options:
    aggressive_folding:
      value: more_elimination
      rationale: "Aggressive folding eliminates more computation but must make delicate judgements about undefined behaviour."
    conservative_folding:
      value: soundness
      rationale: "Conservative folding avoids risky evaluations but leaves many foldable expressions in place."
  importance: high
- dimension: compile_time_work_vs_runtime_savings
  options:
    eager_folding:
      value: runtime_savings
      rationale: "Eager folding eliminates runtime work for constants but costs compile time on large expression trees."
    lazy_folding:
      value: build_speed
      rationale: "Skipping marginal folds keeps builds fast but leaves trivial computation in the binary."
  importance: medium

## Failure Modes
- name: unsound_fold
  description: "A fold evaluates an expression the language does not define the way the compiler assumed — the folded value differs from the program's actual behaviour."
  likelihood: medium
  observable_evidence: "Wrong results on overflow, rounding, or signedness edge cases; behaviour differing between optimized and unoptimized builds"
  detection: "Differential testing across optimization levels; UB and edge-case test suites; conformance testing"
  recovery: "Restrict folding to well-defined cases; align with the language standard; add edge-case tests"
  retryable: true
- name: nonconstant_fold
  description: "An expression that looks constant is folded, but its value depends on runtime state — the fold changes program behaviour."
  likelihood: low
  observable_evidence: "Folded values ignoring runtime input; behaviour differences between builds; constant-assumption violations"
  detection: "Constancy analysis review; differential testing; static analysis of folded sites"
  recovery: "Tighten constancy analysis; gate folding on verified constancy; regression tests"
  retryable: true
- name: fold_blowup
  description: "Folding a large expression tree explodes in cost — huge folds waste compile time or memory for negligible runtime gain."
  likelihood: medium
  observable_evidence: "Compile-time spikes on expression-heavy generated code; macro-generated constant trees; disproportionate build cost"
  detection: "Compile-time profiling; fold size instrumentation; pathological input generation"
  recovery: "Cap fold size; defer or skip marginal folds; rework generating code"
  retryable: true

## Observations
- observation: "Folding correctness reduces to a constancy question — every unsound fold traces to a wrong assumption about what is constant."
  confidence: high
  source: Compiler bug analyses
- observation: "Undefined behaviour is the folding hazard — languages that define overflow behaviour make folding dramatically safer."
  confidence: high
  source: Language design and compiler practice
- observation: "Folding is the canonical teaching example of a sound transformation — its simplicity exposes the general correctness structure."
  confidence: high
  source: Compiler construction education and practice

## Constraints
- constraint: "Folding is legal only for verified constant operands under well-defined semantics — any other fold is a miscompilation."
  type: invariant
  scope: cross-domain
- constraint: "The folded value must equal the evaluated expression under the language's rules — standards compliance bounds folding."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Gate folds on constancy analysis, not on syntactic appearance."
  rationale: "Syntactic constancy and semantic constancy differ exactly where bugs live."
  evidence_level: high
- heuristic: "Decide folding legality against the standard's defined/undefined boundary."
  rationale: "The standard is the fold's contract; the compiler's interpretation is a bug report."
  evidence_level: high

## Recommendations
- recommendation: "Fold only expressions verified constant by analysis and well-defined by the language standard."
  context: optimization_implementation
  certainty: strong
  rationale: "Both conditions are necessary; either failure is a miscompilation."
- recommendation: "Differential-test folding against unoptimized evaluation on edge cases."
  context: testing
  certainty: strong
  rationale: "Overflow, rounding, and signedness edges are where unsound folds hide."
- recommendation: "Cap folding work per expression to bound pathological compile time."
  context: compiler_architecture
  certainty: strong
  rationale: "Folding blowup is a compile-time failure mode, not a runtime one."
