# Isolation Levels

## Identity
- id: isolation-levels
- type: decision
- title: Isolation Levels
- tags: [databases, isolation, concurrency, anomalies, serializable, read committed]
- entities: [isolation level, anomaly, dirty read, non-repeatable read, phantom read, serializable]
- concepts: [transactions, transaction-failures, data-integrity, atomicity]

## Claims
- claim: "Isolation levels define which concurrency anomalies a transaction system permits — each level is a contract about what concurrent behaviour can be observed."
  certainty: high
  evidence: Database theory and practice
  scope: cross-domain
- claim: "The anomaly taxonomy (dirty reads, non-repeatable reads, phantoms) is the constraint structure of concurrency — anomalies are constraint violations, not events."
  certainty: high
  evidence: Concurrency control theory
  scope: cross-domain
- claim: "Serializable isolation eliminates all anomalies at the cost of concurrency — every weaker level trades correctness for throughput."
  certainty: high
  evidence: Isolation research and practice
  scope: cross-domain
- claim: "Isolation selection is a decision with cost consequences — the chosen level determines which application bugs are possible."
  certainty: high
  evidence: Database incident analyses
  scope: cross-domain
- claim: "Application expectations often exceed the configured level — 'consistency bugs' are usually isolation-mismatch bugs."
  certainty: high
  evidence: Database practice, incident analyses
  scope: cross-domain

## Relationships
- concept: transactions
  relationship: scopes
  description: "Isolation levels scope transactions — the level defines the transaction's concurrency contract."
- concept: transaction-failures
  relationship: determines
  description: "Isolation levels determine which transaction failures are possible — anomalies are level-dependent."
- concept: data-integrity
  relationship: conditioned_by
  description: "Data integrity is conditioned by isolation — integrity visible at one level may be violated at another."
- concept: atomicity
  relationship: independent_of
  description: "Isolation levels are independent of atomicity — the two guarantees answer different questions."

## Tradeoffs
- dimension: isolation_strength_vs_concurrency
  options:
    serializable:
      value: anomaly_freedom
      rationale: "Serializable guarantees correctness under concurrency but heavily restricts parallel throughput."
    read_committed:
      value: throughput
      rationale: "Weak levels allow maximum concurrency but require application tolerance of anomalies."
  importance: high
- dimension: guarantee_simplicity_vs_implementation_cost
  options:
    simple_contract:
      value: understandability
      rationale: "Simple level contracts are easy to reason about but implement weak guarantees."
    strong_contract:
      value: safety
      rationale: "Strong contracts are safe but costly to implement and maintain."
  importance: medium

## Failure Modes
- name: dirty_read_exposure
  description: "A transaction reads uncommitted data from another — the read reflects work that may roll back."
  likelihood: medium
  observable_evidence: "Reads of rolled-back values; decisions based on uncommitted state; transient inconsistencies"
  detection: "Isolation audit; anomaly reproduction tests; level documentation review"
  recovery: "Raise isolation; document the level's anomalies; fix affected logic"
  retryable: true
- name: isolation_mismatch
  description: "Application code assumes stronger isolation than configured — the configured level permits anomalies the code does not tolerate."
  likelihood: high
  observable_evidence: "Rare concurrency bugs; wrong aggregates under load; incidents that vanish when load drops"
  detection: "Level-vs-expectation audit; load testing; anomaly injection"
  recovery: "Align configuration with expectations; raise the level or fix the code"
  retryable: true
- name: serialization_explosion
  description: "Serializable isolation is applied broadly — throughput collapses and the database becomes the bottleneck."
  likelihood: medium
  observable_evidence: "Latency spikes; lock contention; saturation at low concurrency"
  detection: "Lock profiling; throughput analysis; isolation usage review"
  recovery: "Narrow serializable usage to where correctness demands it; optimize the rest"
  retryable: true

## Observations
- observation: "Isolation level is the most under-documented decision in production databases — most systems run defaults nobody chose."
  confidence: high
  source: Database practice
- observation: "Anomaly-free under one level is not anomaly-free under another — correctness claims are level-scoped."
  confidence: high
  source: Concurrency control theory
- observation: "The cost of weak isolation is paid in application complexity, not database performance."
  confidence: high
  source: Database engineering experience

## Constraints
- constraint: "Correctness claims are scoped to the isolation level — behaviour verified at one level is not guaranteed at another."
  type: invariant
  scope: cross-domain
- constraint: "Anomalies permitted by the configured level are not defects — they are the contract."
  type: invariant
  scope: cross-domain

## Decision Factors
- factor: consistency_requirement
  question: "What anomalies can this workload tolerate, and which would be incorrect behaviour?"
  supporting: "Explicit tolerance makes the level decision auditable."
  contradictory: "Unstated tolerance makes every anomaly an incident."
  weight: high
- factor: concurrency_demand
  question: "How much concurrent throughput does this workload need?"
  supporting: "High demand justifies weaker isolation."
  contradictory: "Weak isolation under low demand buys nothing and costs correctness."
  weight: high
- factor: failure_cost
  question: "What is the cost of an anomaly materializing (wrong aggregate, stale read)?"
  supporting: "High failure cost justifies serializable isolation."
  contradictory: "Low failure cost makes serializable isolation wasted spend."
  weight: high
- factor: retry_tolerance
  question: "Can the application detect and retry on anomaly exposure?"
  supporting: "Retry-capable applications tolerate weaker isolation safely."
  contradictory: "Retry-intolerant applications turn anomalies into user-visible bugs."
  weight: medium

## Heuristics
- heuristic: "Document the isolation contract per workload."
  rationale: "Undocumented levels make every anomaly a mystery."
  evidence_level: high
- heuristic: "Test under the configured isolation level."
  rationale: "Development-default isolation is not production isolation."
  evidence_level: high

## Recommendations
- recommendation: "Choose isolation levels by anomaly tolerance with recorded rationale."
  context: configuration
  certainty: strong
  rationale: "The level is a decision with correctness consequences."
- recommendation: "Document permitted anomalies for each workload."
  context: governance
  certainty: strong
  rationale: "A documented contract converts anomalies from bugs into terms."
- recommendation: "Test concurrency behaviour at production isolation levels."
  context: testing
  certainty: strong
  rationale: "Isolation bugs only reproduce where the configuration reproduces."
