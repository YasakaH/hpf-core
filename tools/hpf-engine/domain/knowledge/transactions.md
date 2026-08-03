# Transactions

## Identity
- id: transactions
- type: concept
- title: Transactions
- tags: [databases, transactions, ACID, unit of work, commit, rollback, concurrency]
- entities: [transaction, unit of work, commit, rollback, ACID, write set]
- concepts: [atomicity, isolation-levels, transaction-failures, data-integrity, relational-model, schema-migration]

## Claims
- claim: "A transaction is a unit of work — a bounded set of operations that either applies fully or not at all."
  certainty: high
  evidence: Database theory and practice
  scope: cross-domain
- claim: "ACID is the transaction's contract — atomicity, consistency, isolation, and durability are the guarantees a transaction system provides."
  certainty: high
  evidence: Database theory
  scope: cross-domain
- claim: "A transaction is a unit of work with constraints on its outcome, not on its duration — temporal extent is an implementation detail."
  certainty: high
  evidence: Transaction theory, database practice
  scope: cross-domain
- claim: "Transactions manage concurrency — isolation levels trade consistency guarantees against throughput."
  certainty: high
  evidence: Concurrency control theory and practice
  scope: cross-domain
- claim: "The transaction boundary is a correctness decision — too coarse deadlocks and blocks; too fine breaks atomicity."
  certainty: high
  evidence: Database practice, performance engineering
  scope: cross-domain

## Relationships
- concept: atomicity
  relationship: guaranteed_by
  description: "Transactions are guaranteed by atomicity — all-or-nothing is the core transaction property."
- concept: isolation-levels
  relationship: scoped_by
  description: "Transactions are scoped by isolation levels — the chosen level defines what anomalies are possible."
- concept: transaction-failures
  relationship: subject_to
  description: "Transactions are subject to transaction failures — deadlock, abort, and lost updates are failure classes."
- concept: data-integrity
  relationship: protects
  description: "Transactions protect data integrity — atomicity prevents partial states."
- concept: relational-model
  relationship: manipulates
  description: "Transactions manipulate the relational model — data changes happen as units of work."
- concept: schema-migration
  relationship: executes_under
  description: "Schema migration executes under transactions — structural changes are transactional work."

## Tradeoffs
- dimension: transaction_scope_vs_concurrency
  options:
    coarse_transactions:
      value: atomicity_safety
      rationale: "Coarse transactions preserve atomicity but hold locks longer and reduce concurrency."
    fine_transactions:
      value: throughput
      rationale: "Fine transactions allow concurrency but risk breaking logical atomicity."
  importance: high
- dimension: isolation_strength_vs_throughput
  options:
    serializable:
      value: correctness
      rationale: "Serializable isolation prevents all anomalies but serializes or heavily penalizes concurrent work."
    weak_isolation:
      value: throughput
      rationale: "Weak isolation maximizes throughput but admits anomalies consumers must tolerate."
  importance: high

## Failure Modes
- name: deadlock
  description: "Transactions wait on each other's locks cyclically — no transaction can proceed."
  likelihood: medium
  observable_evidence: "Deadlock errors; hung transactions; lock-wait timeouts"
  detection: "Deadlock detection; lock-wait monitoring; cycle analysis"
  recovery: "Detect and abort a victim; retry with backoff; reduce lock contention"
  retryable: true
- name: lost_update
  description: "Two transactions read the same value and write it back independently — one update is silently lost."
  likelihood: medium
  observable_evidence: "Disappearing updates; counters and balances wrong under concurrency; unexplained data loss"
  detection: "Anomaly testing; isolation-level audit; version-check detection"
  recovery: "Raise isolation; use conditional updates (version checks); restructure the write path"
  retryable: true
- name: long_running_transaction
  description: "A transaction holds resources too long — blocking, lock accumulation, and recovery risk grow with duration."
  likelihood: medium
  observable_evidence: "Growing lock contention; timeouts; slow checkpoints; recovery delays"
  detection: "Transaction duration monitoring; lock-hold analysis; workload profiling"
  recovery: "Split transactions; move work outside the boundary; bound durations"
  retryable: true

## Observations
- observation: "The transaction boundary is the most consequential concurrency decision — it sets the shape of every other tradeoff."
  confidence: high
  source: Database practice
- observation: "Most 'consistency bugs' in production systems trace to isolation expectations mismatching the configured level."
  confidence: high
  source: Database incident analyses
- observation: "Transactions convert multi-step work into testable units — the boundary is what makes the system provable."
  confidence: high
  source: Transaction theory and practice

## Constraints
- constraint: "A transaction applies fully or not at all — partial application is a correctness failure, not a performance concern."
  type: invariant
  scope: cross-domain
- constraint: "The transaction's guarantees are scoped by its isolation level — behaviour valid at one level may be invalid at another."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Keep transactions short — duration is a risk multiplier."
  rationale: "Every held resource is a concurrency cost and a recovery exposure."
  evidence_level: high
- heuristic: "Match isolation expectations to reality — document what anomalies the configured level permits."
  rationale: "Mismatched expectations are the standard source of consistency bugs."
  evidence_level: high

## Recommendations
- recommendation: "Design the transaction boundary deliberately — it is the unit of correctness."
  context: application_design
  certainty: strong
  rationale: "The boundary decides atomicity, concurrency, and recovery behavior."
- recommendation: "Choose isolation levels by anomaly tolerance, documented per workload."
  context: configuration
  certainty: strong
  rationale: "The level is a decision, not a default."
- recommendation: "Detect deadlocks and retry transactionally — with backoff and idempotence."
  context: operations
  certainty: strong
  rationale: "Deadlock is a normal failure mode of concurrency, not a bug."
