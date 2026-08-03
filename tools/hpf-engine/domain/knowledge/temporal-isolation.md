# Temporal Isolation

## Identity
- id: temporal-isolation
- type: pattern
- title: Temporal Isolation
- tags: [real-time systems, isolation, guarantees, contention, partitioning]
- entities: [temporal isolation, partitioning, guarantee separation, budget enforcement]
- concepts: [real-time-guarantee, task-scheduling, scheduling-policy, isolation-levels, strong-consistency]

## Claims
- claim: "Temporal isolation is the discipline of keeping one task's timing behaviour from breaking another's guarantee."
  certainty: high
  evidence: Real-time systems practice (ARINC 653 partitioning)
  scope: cross-domain
- claim: "Temporal isolation is an invariant — each task's guarantee holds independently of others' behaviour."
  certainty: high
  evidence: Partitioning practice and literature
  scope: cross-domain
- claim: "Isolation is enforced by budget and partition constraints, not by a new construct — execution budgets bound each task's impact."
  certainty: high
  evidence: Cross-domain comparison (constraints as enforcement)
  scope: cross-domain
- claim: "Temporal isolation is the real-time form of isolation — the same guarantee-separation structure as consistency isolation in databases."
  certainty: high
  evidence: Cross-domain comparison (isolation family 006-010)
  scope: cross-domain
- claim: "Temporal isolation is a pattern — a reusable enforcement discipline, not a knowledge kind."
  certainty: high
  evidence: Cross-domain comparison (pattern resolutions 009-010)
  scope: cross-domain

## Relationships
- concept: real-time-guarantee
  relationship: protects
  description: "Temporal isolation protects the real-time guarantee — separation preserves each claim."
- concept: task-scheduling
  relationship: structures
  description: "Temporal isolation structures task scheduling — budgets bound the allocation."
- concept: scheduling-policy
  relationship: supported_by
  description: "Temporal isolation is supported by the scheduling policy — the policy enforces the separation."
- concept: isolation-levels
  relationship: analogous_to
  description: "Temporal isolation is analogous to isolation levels — guarantee separation across domains — the Cycle 010 cross-domain link."
- concept: strong-consistency
  relationship: analogous_to
  description: "Temporal isolation is analogous to strong consistency — separation as a guarantee — the Cycle 006 cross-domain link."

## Tradeoffs
- dimension: isolation_strength_vs_utilization
  options:
    strong_partitioning:
      value: guarantee_independence
      rationale: "Strong partitioning isolates guarantees but wastes capacity."
    budget_sharing:
      value: efficiency
      rationale: "Shared budgets are efficient but leak between tasks."
  importance: high
- dimension: separation_vs_flexibility
  options:
    fixed_partitions:
      value: predictability
      rationale: "Fixed partitions are predictable but rigid."
    dynamic_budgets:
      value: flexibility
      rationale: "Dynamic budgets adapt but complicate guarantees."
  importance: high

## Failure Modes
- name: isolation_breach
  description: "One task's behaviour breaks another's guarantee — the separation fails."
  likelihood: medium
  observable_evidence: "Cross-task timing impact; guarantee violations; interference"
  detection: "Isolation testing; interference monitoring"
  recovery: "Re-partition; enforce budgets; repair the separation"
  retryable: true
- name: budget_exhaustion
  description: "A task exhausts its budget — enforcement stops the task and its guarantee fails."
  likelihood: medium
  observable_evidence: "Budget overruns; throttled tasks; missed deadlines"
  detection: "Budget monitoring; overrun detection"
  recovery: "Adjust budget; re-analyse; repair the allocation"
  retryable: true
- name: interference_leak
  description: "Indirect interference crosses partitions — caches, buses, or shared hardware leak timing between tasks."
  likelihood: medium
  observable_evidence: "Unexplained timing variance; cross-partition impact"
  detection: "Interference analysis; timing variance monitoring"
  recovery: "Partition shared resources; add interference bounds"
  retryable: true

## Observations
- observation: "Isolation is an invariant enforced by budgets — the same separation structure appears in databases (010) and consistency (006)."
  confidence: high
  source: Cross-domain comparison (isolation family 006-010)
- observation: "The pattern carries the guarantee without a construct — enforcement is constraint content."
  confidence: high
  source: Cross-domain comparison (pattern resolutions)
- observation: "Interference is the hardest isolation problem — shared hardware leaks timing across partitions."
  confidence: high
  source: Real-time systems practice

## Constraints
- constraint: "Each task's guarantee must hold independently — temporal isolation is an invariant."
  type: invariant
  scope: cross-domain
- constraint: "Execution budgets bound each task's impact — an unbudgeted task can break isolation."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Partition first; share later."
  rationale: "Separation is the guarantee's foundation; sharing is the risk."
  evidence_level: high
- heuristic: "Bound interference as part of the guarantee."
  rationale: "Shared hardware is the isolation leak."
  evidence_level: high

## Recommendations
- recommendation: "Model temporal isolation as a pattern with budget constraints."
  context: modelling
  certainty: strong
  rationale: "Enforcement is constraint content, not a construct."
- recommendation: "Enforce budgets at the partition boundary."
  context: engineering
  certainty: strong
  rationale: "Unbudgeted tasks break isolation."
- recommendation: "Test isolation under worst-case interference."
  context: operations
  certainty: strong
  rationale: "Interference leaks are the silent isolation failure."
