# Program Semantics

## Identity
- id: program-semantics
- type: concept
- title: Program Semantics
- tags: [compilers, semantics, meaning, operational semantics, denotational semantics, correctness]
- entities: [program semantics, program meaning, observable behaviour, operational semantics, semantic equivalence, specification]
- concepts: [abstract-syntax-tree, intermediate-representation, compiler-optimization, equivalence-checking, compiler-correctness]

## Claims
- claim: "Program semantics is the meaning of a program — the behaviour it exhibits when executed, independent of its representation."
  certainty: high
  evidence: Programming language theory
  scope: cross-domain
- claim: "Semantics is the correctness yardstick — every transformation, lowering, and code-generation step is judged against semantic preservation."
  certainty: high
  evidence: Compiler correctness practice and theory
  scope: cross-domain
- claim: "Semantics is defined by formal models — operational and denotational semantics give meaning a checkable form instead of an informal gloss."
  certainty: high
  evidence: Programming language semantics literature
  scope: cross-domain
- claim: "Semantic equivalence is relative to a chosen notion of observable behaviour — two programs equivalent under one observation model may differ under another."
  certainty: high
  evidence: Program equivalence research
  scope: cross-domain
- claim: "Formalizing semantics is a modelling act with its own failure modes — the model can misrepresent the language it claims to define."
  certainty: high
  evidence: Semantics research experience, specification bugs
  scope: cross-domain

## Relationships
- concept: abstract-syntax-tree
  relationship: expressed_by
  description: "Program semantics is expressed by the AST — tree structure determines meaning."
- concept: intermediate-representation
  relationship: preserved_through
  description: "Program semantics is preserved through IR lowering — meaning survives representation change."
- concept: compiler-optimization
  relationship: judged_by
  description: "Compiler optimizations are judged against program semantics — correctness means meaning preservation."
- concept: equivalence-checking
  relationship: based_on
  description: "Equivalence checking is based on program semantics — equivalence is a relation defined over meaning, not syntax."
- concept: compiler-correctness
  relationship: anchored_in
  description: "Compiler correctness is anchored in program semantics — the compiler's correctness property is defined as semantic preservation."

## Tradeoffs
- dimension: semantic_formality_vs_practicality
  options:
    formal_semantics:
      value: checkability
      rationale: "Formal semantics make meaning checkable and provable but are costly to construct and maintain."
    informal_gloss:
      value: accessibility
      rationale: "Informal descriptions are cheap and readable but leave meaning ambiguous."
  importance: high
- dimension: observation_granularity_vs_equivalence_strength
  options:
    coarse_observation:
      value: transformation_freedom
      rationale: "Coarse observation models (input-output equivalence) permit aggressive optimization but admit behaviour differences users may notice."
    fine_observation:
      value: fidelity
      rationale: "Fine observation models (full trace equivalence) preserve more behaviour but restrict legal transformations."
  importance: high

## Failure Modes
- name: semantic_mischaracterization
  description: "The language's semantics are described wrongly — the specification or model disagrees with actual language behaviour."
  likelihood: medium
  observable_evidence: "Spec-violating behaviour in production code; correct-looking programs behaving unexpectedly; standard disagreements"
  detection: "Behavioural conformance testing; formal model validation; standards process review"
  recovery: "Correct the specification; align implementation and model; regression tests"
  retryable: true
- name: observation_model_mismatch
  description: "Two parties assume different observation models — a transformation judged correct under one model changes behaviour under another."
  likelihood: medium
  observable_evidence: "Optimized programs behaving differently from source expectations; equivalence disputes; 'it works differently in release' bugs"
  detection: "Observation model review; equivalence criteria audits; differential testing across modes"
  recovery: "Agree the observation model explicitly; adjust transformation legality; document behavioural boundaries"
  retryable: true
- name: undefined_behaviour_leakage
  description: "The semantics declares some programs undefined — but implementation freedom leaks into defined programs through unstated assumptions."
  likelihood: medium
  observable_evidence: "Programs depending on undefined behaviour behaving differently across compilers or versions; optimization exposing UB assumptions"
  detection: "UB sanitization; cross-compiler differential testing; flag analysis"
  recovery: "Keep UB out of defined programs; document implementation assumptions; sanitize early"
  retryable: true

## Observations
- observation: "Semantic preservation is the invariant that unifies the entire compiler pipeline — parsing, lowering, optimization, and code generation all obey it."
  confidence: high
  source: Compiler construction practice
- observation: "Programmers experience semantics through observable behaviour — meaning matters through the lens of what a program does."
  confidence: high
  source: Programming practice
- observation: "Equivalence disputes in practice are usually disputes about the observation model, not about the transformation."
  confidence: high
  source: Compiler engineering experience

## Constraints
- constraint: "Meaning is invariant under representation — the same program in different forms has the same semantics."
  type: invariant
  scope: cross-domain
- constraint: "Correctness claims are valid only under a stated observation model — unstated observation assumptions make equivalence claims untestable."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "State the observation model before claiming equivalence or correctness."
  rationale: "Every correctness claim is relative to how much behaviour is observed."
  evidence_level: high
- heuristic: "Treat the semantic model as code — version it, test it, and treat its bugs as product bugs."
  rationale: "A wrong model poisons every correctness argument that rests on it."
  evidence_level: high

## Recommendations
- recommendation: "Write the semantics down in a checkable form before designing transformations."
  context: language_design
  certainty: strong
  rationale: "Transformations without a semantic yardstick cannot be judged correct."
- recommendation: "Define correctness against an explicit observation model and document the behavioural boundary it permits."
  context: compiler_governance
  certainty: strong
  rationale: "Undocumented observation assumptions surface as 'works in debug, broken in release' surprises."
- recommendation: "Validate the semantic model against real program behaviour continuously."
  context: language_evolution
  certainty: strong
  rationale: "Specification drift is a slow, costly failure mode that only conformance testing catches."
