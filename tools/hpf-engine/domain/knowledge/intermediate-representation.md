# Intermediate Representation

## Identity
- id: intermediate-representation
- type: concept
- title: Intermediate Representation
- tags: [compilers, IR, optimization, lowering, SSA, code generation, representation]
- entities: [intermediate representation, lowering, SSA form, control flow graph, code generation, representation level]
- concepts: [abstract-syntax-tree, program-semantics, compiler-optimization, optimization-pass, compiler-correctness]

## Claims
- claim: "An intermediate representation is a representation of a program between source and machine code — designed to make analysis and transformation tractable."
  certainty: high
  evidence: Compiler construction practice and literature
  scope: cross-domain
- claim: "IRs are nested — compilers lower through multiple representation levels, each closer to machine semantics than the last."
  certainty: high
  evidence: Compiler implementation practice (front-end IR, SSA, machine IR)
  scope: cross-domain
- claim: "IR choice determines which optimizations are possible — a representation that hides information makes that information unoptimizable."
  certainty: high
  evidence: Compiler design experience (SSA enabling sparse dataflow)
  scope: cross-domain
- claim: "Lowering must preserve program semantics — each representation transition is a transformation with the same correctness obligation as an optimization."
  certainty: high
  evidence: Compiler correctness practice
  scope: cross-domain
- claim: "The final IR is the substrate for code generation — machine-level decisions (register allocation, scheduling, instruction selection) operate on it."
  certainty: high
  evidence: Compiler implementation practice
  scope: cross-domain

## Relationships
- concept: abstract-syntax-tree
  relationship: lowered_from
  description: "The IR is lowered from the AST — the front end produces the first IR from the syntax tree."
- concept: program-semantics
  relationship: preserves
  description: "IR lowering preserves program semantics — every representation transition keeps program meaning."
- concept: compiler-optimization
  relationship: substrate_for
  description: "The IR is the substrate for compiler optimizations — most optimizations run on IR, not source."
- concept: optimization-pass
  relationship: organizes
  description: "The IR organizes optimization passes — pass pipelines are defined over IR levels."
- concept: compiler-correctness
  relationship: constrained_by
  description: "Compiler correctness constrains IR design — representation gaps that lose information make correct lowering unachievable."

## Tradeoffs
- dimension: abstraction_level_vs_transformation_power
  options:
    high_level_ir:
      value: source_fidelity
      rationale: "High-level IRs retain source-like constructs and enable source-level optimizations but carry machine-irrelevant baggage."
    low_level_ir:
      value: machine_fidelity
      rationale: "Low-level IRs expose machine semantics for code generation but lose structure that higher-level analyses need."
  importance: high
- dimension: information_retention_vs_simplicity
  options:
    rich_metadata:
      value: analysis_quality
      rationale: "Retaining debug, type, and provenance information enables better analysis but complicates the IR."
    lean_ir:
      value: speed
      rationale: "Minimal IRs are fast to build and traverse but force analyses to re-derive lost information."
  importance: high

## Failure Modes
- name: information_loss
  description: "Lowering discards information a later stage needs — a representation gap makes a valid transformation impossible to express."
  likelihood: medium
  observable_evidence: "Missed optimizations; repeated source re-parsing; hacks to recover lost context"
  detection: "IR inspection; optimization capability analysis; lowering design review"
  recovery: "Extend the IR; carry the needed information as metadata; re-order lowering"
  retryable: true
- name: lowering_semantics_violation
  description: "A lowering step changes program meaning — the IR claims to represent the program but does not."
  likelihood: low
  observable_evidence: "Correct source producing wrong behaviour after optimization; IR-level tests passing with source-level failures"
  detection: "Differential testing (source vs IR semantics); IR-level test suites; formal lowering validation"
  recovery: "Fix the lowering rule; add semantic preservation checks; differential fuzzing"
  retryable: true
- name: ir_level_bloat
  description: "IR levels multiply without clear boundaries — representations proliferate and the pipeline loses a coherent meaning."
  likelihood: medium
  observable_evidence: "Ad-hoc IR variants; unclear lowering responsibility; duplicated transformations across levels"
  detection: "IR inventory review; pass placement analysis; design review"
  recovery: "Consolidate levels; define each IR's contract; document the lowering ladder"
  retryable: true

## Observations
- observation: "Every IR transition is a transformation with the same correctness obligation as an optimization — representation change is not exempt from semantic preservation."
  confidence: high
  source: Compiler correctness practice
- observation: "SSA form demonstrably changed which optimizations are practical — representation choice shapes the reachable optimization space."
  confidence: high
  source: Compiler research and implementation history
- observation: "IR design is where compiler architecture is actually decided — front ends and back ends meet at the IR contract."
  confidence: high
  source: Compiler architecture practice

## Constraints
- constraint: "Every lowering step must preserve program semantics — the IR is a representation of the program, not a new program."
  type: invariant
  scope: cross-domain
- constraint: "Representation must retain the information later stages depend on — information discarded at one level cannot be recovered at a lower one."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Define the contract of each IR level explicitly — what it represents, what it drops, what stages consume it."
  rationale: "Undocumented IR contracts produce information-loss surprises at the worst moment."
  evidence_level: high
- heuristic: "Differential-test lowering stages against the source program's semantics."
  rationale: "Semantic preservation is an obligation, not an assumption."
  evidence_level: high

## Recommendations
- recommendation: "Design the IR ladder deliberately — each level's contract, not its data structures, is the architecture."
  context: compiler_architecture
  certainty: strong
  rationale: "The IR contract determines what the whole pipeline can and cannot do."
- recommendation: "Never drop information without a recorded decision that no later stage needs it."
  context: lowering_design
  certainty: strong
  rationale: "Information loss is the most common cause of representation gaps."
- recommendation: "Treat lowering steps with the same verification discipline as optimizations."
  context: verification
  certainty: strong
  rationale: "Semantics violations in lowering are miscompilations like any other."
