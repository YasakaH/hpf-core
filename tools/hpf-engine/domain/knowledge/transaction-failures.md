# Transaction Failures

## Identity
- id: transaction-failures
- type: concept
- title: Transaction Failures
- tags: [databases, transaction failures, deadlock, abort, lost update, retry, recovery]
- entities: [transaction failure, deadlock, abort, lost update, retry, recovery]
- concepts: [transactions, atomicity, isolation-levels, data-integrity, retry-pattern]

## Claims
- claim: "Transaction failures are a normal class of concurrency outcomes — deadlock, abort, and lost updates are expected failure modes, not exceptional bugs."
  certainty: high
  evidence: Database practice, concurrency theory
  scope: cross-domain
- claim: "Deadlock is a cycle in resource waiting — detection and victim selection are the standard resolution."
  certainty: high
  evidence: Concurrency control theory and practice
  scope: cross-domain
- claim: "Lost updates are silent failures — the system reports success while discarding work — making them the most dangerous transaction failure class."
  certainty: high
  evidence: Database incident analyses
  scope: cross-domain
- claim: "Retry is the recovery mechanism for retryable failures — retrying non-retryable failures (lost updates, constraint violations) amplifies the problem."
  certainty: high
  evidence: Retry practice, distributed systems experience
  scope: cross-domain
- claim: "Failure classification precedes recovery — a transaction must know whether its failure is retryable before choosing a response."
  certainty: high
  evidence: Transaction practice
  scope: cross-domain

## Relationships
- concept: transactions
  relationship: afflict
  description: "Transaction failures afflict transactions — failure is an outcome class of transactional work."
- concept: atomicity
  relationship: contained_by
  description: "Transaction failures are contained by atomicity — aborts leave no partial effect."
- concept: isolation-levels
  relationship: caused_by
  description: "Transaction failures are caused by isolation levels — anomalies are level-dependent failures."
- concept: data-integrity
  relationship: preserved_by
  description: "Transaction failures preserve data integrity — atomicity keeps failures from corrupting state."
- concept: retry-pattern
  relationship: mitigated_by
  description: "Transaction failures are mitigated by the retry pattern — the cross-domain link to the Cycle 006 corpus."

## Tradeoffs
- dimension: retry_aggressiveness_vs_amplification
  options:
    aggressive_retry:
      value: completion_chance
      rationale: "Aggressive retry completes more work but amplifies load during contention."
    cautious_retry:
      value: system_stability
      rationale: "Cautious retry protects the system but abandons more work."
  importance: high
- dimension: detection_depth_vs_overhead
  options:
    full_classification:
      value: correct_recovery
      rationale: "Deep failure classification enables correct recovery responses."
    cheap_detection:
      value: speed
      rationale: "Cheap detection is fast but risks misclassifying failure types."
  importance: medium

## Failure Modes
- name: deadlock
  description: "Cyclic wait among transactions — none can proceed until one is aborted."
  likelihood: medium
  observable_evidence: "Deadlock errors; wait timeouts; hung work"
  detection: "Deadlock detection; lock-wait monitoring; timeout analysis"
  recovery: "Abort a victim; retry with backoff; reduce lock contention"
  retryable: true
- name: lost_update
  description: "Concurrent writes silently discard one update — the transaction reports success but its work is gone."
  likelihood: medium
  observable_evidence: "Disappearing updates; wrong counters; conflicts only under concurrency"
  detection: "Version checks; anomaly testing; isolation audit"
  recovery: "Conditional writes; raise isolation; restructure access"
  retryable: false
- name: retry_storm
  description: "Retries on non-retryable failures multiply — every retry fails identically and the system pays the cost repeatedly."
  likelihood: medium
  observable_evidence: "Retry amplification; load spikes during failures; logs of identical failures"
  detection: "Retry analysis; failure-class review; rate monitoring"
  recovery: "Classify failures; separate retryable from terminal; cap retries"
  retryable: true

## Observations
- observation: "Retrying non-retryable failures is the standard operational mistake — classification is the missing discipline."
  confidence: high
  source: Operations practice, incident analyses
- observation: "Lost updates are disproportionately expensive — silent failure costs more than loud failure."
  confidence: high
  source: Database incident analyses
- observation: "Deadlock handling is mature practice — detection, victim, backoff — while anomaly handling remains application-dependent."
  confidence: high
  source: Database engineering practice

## Constraints
- constraint: "Recovery must be preceded by failure classification — retrying without classification amplifies damage."
  type: invariant
  scope: cross-domain
- constraint: "Retryable failures are bounded — unbounded retry is an amplifier, not a recovery."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Classify failures before designing retry."
  rationale: "Retry is correct only for the class it is built for."
  evidence_level: high
- heuristic: "Treat lost updates as correctness failures, not concurrency noise."
  rationale: "Silent loss is the highest-cost failure class in transactional systems."
  evidence_level: high

## Recommendations
- recommendation: "Explicitly classify transaction failures as retryable or terminal."
  context: application_design
  certainty: strong
  rationale: "Classification is the precondition for correct recovery."
- recommendation: "Retry deadlocks and aborts with bounded backoff and idempotence."
  context: operations
  certainty: strong
  rationale: "Bounded, idempotent retry completes work without amplification."
- recommendation: "Detect lost updates with version checks or conditional writes."
  context: design
  certainty: strong
  rationale: "Silent loss is only detectable through explicit conflict detection."
