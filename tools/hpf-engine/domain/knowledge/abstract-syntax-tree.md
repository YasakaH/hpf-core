# Abstract Syntax Tree

## Identity
- id: abstract-syntax-tree
- type: concept
- title: Abstract Syntax Tree
- tags: [compilers, parsing, syntax, AST, representation, source code]
- entities: [abstract syntax tree, syntax node, parse tree, grammar, token, source code]
- concepts: [type-system, intermediate-representation, program-semantics, compiler-optimization, constant-folding, dead-code-elimination]

## Claims
- claim: "An abstract syntax tree is the structured representation of source code — a tree of syntax nodes produced by a parser, discarding non-essential surface syntax."
  certainty: high
  evidence: Compiler construction practice and literature
  scope: cross-domain
- claim: "The AST is defined by the grammar — node structure, precedence, and associativity all derive from the language's grammar."
  certainty: high
  evidence: Parser design practice, formal language theory
  scope: cross-domain
- claim: "ASTs are the transformation substrate — optimizations and lowering operate on the AST or structures derived from it."
  certainty: high
  evidence: Compiler implementation practice
  scope: cross-domain
- claim: "AST nodes carry identity and position — source location, lexical context, and ancestry determine what transformations are valid at a node."
  certainty: high
  evidence: Compiler implementation practice, tooling (linting, refactoring)
  scope: cross-domain
- claim: "An AST is an abstraction over parse trees — it drops punctuation and grouping details while preserving the structure that matters for semantics."
  certainty: high
  evidence: Compiler construction literature
  scope: cross-domain

## Relationships
- concept: type-system
  relationship: annotated_by
  description: "The AST is annotated by the type system — type checking attaches type information to syntax nodes."
- concept: intermediate-representation
  relationship: lowered_from
  description: "The AST is lowered to an intermediate representation — the IR is derived from the AST by a lowering transformation."
- concept: program-semantics
  relationship: expresses
  description: "The AST expresses program semantics — the structure of the tree determines the meaning of the program."
- concept: compiler-optimization
  relationship: operates_on
  description: "Compiler optimizations operate on the AST or its derived forms — tree rewriting is the simplest optimization channel."
- concept: constant-folding
  relationship: enables
  description: "Constant folding operates on AST subtrees — the tree structure makes constant expressions visible."
- concept: dead-code-elimination
  relationship: enables
  description: "Dead code elimination uses AST structure — unreachable and unused subtrees are located via the tree."

## Tradeoffs
- dimension: fidelity_vs_abstraction
  options:
    rich_ast:
      value: precision
      rationale: "A detailed AST preserves source structure for tools and accurate diagnostics but is heavier to build and transform."
    lean_ast:
      value: simplicity
      rationale: "A minimal AST is cheap to construct and transform but loses information later stages must recover."
  importance: medium
- dimension: grammar_driven_vs_pragmatic_structure
  options:
    grammar_faithful:
      value: formality
      rationale: "Grammar-faithful trees are predictable and verifiable against the grammar but can encode incidental structure."
    pragmatic_structure:
      value: usability
      rationale: "Pragmatic trees serve transformation and tooling directly but blur the grammar mapping."
  importance: medium

## Failure Modes
- name: parse_failure
  description: "Input fails to parse — the AST cannot be constructed for malformed or unsupported syntax."
  likelihood: medium
  observable_evidence: "Parser errors at compile time; rejected source; partial AST with error nodes"
  detection: "Parser error reporting; grammar conformance tests; fuzzing"
  recovery: "Improve error recovery; extend grammar; report precise diagnostics"
  retryable: true
- name: grammar_ambiguity
  description: "The grammar admits multiple parse trees for one input — structure becomes non-deterministic and semantics hang off the wrong subtree."
  likelihood: medium
  observable_evidence: "Ambiguity warnings; parser conflicts; wrong behavior for syntactically valid input"
  detection: "Grammar analysis tools (LALR/LL conflict reports); construction of adversarial inputs"
  recovery: "Restructure grammar; add precedence and associativity; validate against ambiguity finders"
  retryable: true
- name: precedence_misbinding
  description: "Precedence or associativity binds operands to the wrong subtree — the tree is structurally valid but semantically wrong."
  likelihood: medium
  observable_evidence: "Subtle wrong results for expression-heavy code; correct syntax, incorrect behavior"
  detection: "Expression-focused test suites; operator precedence conformance tests"
  recovery: "Correct precedence tables; test against language standard examples"
  retryable: true

## Observations
- observation: "ASTs make transformations composable — every optimization can be expressed as tree structure changes."
  confidence: high
  source: Compiler implementation practice
- observation: "Tooling (linters, formatters, refactorers) is built on AST structure — it is the common substrate for program manipulation."
  confidence: high
  source: Language tooling ecosystem practice
- observation: "Parser quality dominates early-stage compiler reliability — most compiler front-end bugs originate in grammar and tree construction."
  confidence: high
  source: Compiler development incident analysis

## Constraints
- constraint: "AST structure must be derivable from the grammar — tree shape that contradicts the grammar produces untrustworthy tooling and transformations."
  type: invariant
  scope: cross-domain
- constraint: "Transformation validity is bound to tree position — a rewrite that ignores node ancestry or scope can change program meaning."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Keep source location attached to every node."
  rationale: "Diagnostics and tooling depend on position; dropping location makes errors unmappable to source."
  evidence_level: high
- heuristic: "Test the AST against the language standard's precedence and associativity rules."
  rationale: "Precedence misbinding is the subtlest AST failure class and only surfaces through conformance testing."
  evidence_level: high

## Recommendations
- recommendation: "Define the AST directly from the grammar and validate structure against it."
  context: frontend_design
  certainty: strong
  rationale: "Grammar-derived trees are predictable; ad-hoc trees accumulate structural surprises."
- recommendation: "Carry source position through every lowering and transformation stage."
  context: compiler_pipeline
  certainty: strong
  rationale: "Position is needed for diagnostics and for transformations whose validity depends on source context."
- recommendation: "Fuzz and conformance-test the parser independently of the rest of the pipeline."
  context: testing
  certainty: strong
  rationale: "Parser defects surface as confusing errors downstream; isolating them bounds their blast radius."
