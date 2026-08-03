# Idempotency

## Identity
- id: idempotency
- type: concept
- title: Idempotency
- tags: [distributed-systems, reliability, retry, consistency, api-design, safety]
- entities: [idempotency, idempotent operation, idempotency key, retry safety, at-least-once, exactly-once]
- concepts: [retry-storm-amplification, circuit-breaker, saga-pattern, eventual-consistency]

## Claims
- claim: "An idempotent operation produces the same result regardless of how many times it is applied — retrying an idempotent operation is safe."
  certainty: high
  evidence: Distributed systems literature, REST specification (RFC 7231)
  scope: cross-system
- claim: "Idempotency is the foundation of safe retry — without idempotency, retrying a failed operation can produce duplicate side effects."
  certainty: high
  evidence: Distributed systems literature, production experience
  scope: cross-system
- claim: "Idempotency keys (unique operation identifiers) enable exactly-once processing in at-least-once delivery systems."
  certainty: high
  evidence: Distributed systems literature, payment system design
  scope: cross-system
- claim: "Natural idempotency (operation is inherently repeatable) is preferable to enforced idempotency (deduplication logic) because it has no overhead."
  certainty: high
  evidence: API design literature, production experience
  scope: cross-system
- claim: "Idempotency does not imply no side effects — it implies the same result and side effects for repeated identical requests."
  certainty: high
  evidence: Distributed systems literature
  scope: cross-system

## Relationships
- concept: retry-storm-amplification
  relationship: enables_safe_retry
  description: "Idempotency makes retry safe — without it, retry storms produce duplicate side effects in addition to load amplification."
- concept: circuit-breaker
  relationship: complementary_to
  description: "Circuit breakers control when retries happen; idempotency controls the safety of those retries."
- concept: saga-pattern
  relationship: requires
  description: "Saga compensation logic must be idempotent — compensating an already-compensated step must not produce incorrect state."
- concept: eventual-consistency
  relationship: interacts_with
  description: "Idempotency is critical in eventually consistent systems where the same operation may be processed by different replicas."

## Tradeoffs
- dimension: natural_vs_enforced_idempotency
  options:
    natural:
      value: zero_overhead
      rationale: "Design operations to be inherently idempotent (e.g. SET instead of INCREMENT) — simplest, zero deduplication cost."
    idempotency_key:
      value: universal_applicability
      rationale: "Use operation IDs and deduplication — works for any operation type but adds storage and checking overhead."
  importance: high
- dimension: idempotency_storage_duration
  options:
    short_lived:
      value: minimal_storage
      rationale: "Retain idempotency keys for minutes — adequate for retry windows but cannot detect duplicate requests outside the window."
    persistent:
      value: maximum_coverage
      rationale: "Retain keys indefinitely — prevents all duplicate processing but requires storage management and key cleanup."
  importance: operational

## Failure Modes
- name: idempotency_breach
  description: "Non-idempotent operation is retried, producing duplicate side effects — the most common retry-related data integrity failure."
  likelihood: high
  observable_evidence: "Duplicate records in database; repeated side effects (duplicate emails, charges); data integrity violation reports"
  detection: "Track idempotency key collisions; audit logs showing repeated operation IDs; deduplication check failures"
  recovery: "Manual cleanup of duplicate side effects; implement idempotency for the affected operation; compensate for duplicates where possible"
  retryable: false
- name: idempotency_storage_exhaustion
  description: "Idempotency key storage grows unbounded, exhausting disk or memory and causing idempotency enforcement to fail."
  likelihood: medium
  observable_evidence: "Idempotency check errors; increased latency on idempotency checks; storage utilisation growth"
  detection: "Monitor idempotency key store size; alert on growth rate and capacity thresholds"
  recovery: "Implement key expiry and cleanup; increase storage capacity; switch to more efficient deduplication strategy"
  retryable: false
- name: false_idempotency_assumption
  description: "An operation is assumed to be idempotent when it is not — typically from partial success scenarios (operation partially applied before failure)."
  likelihood: medium
  observable_evidence: "Intermittent duplicate side effects that cannot be reproduced consistently; side effects only under certain failure timing"
  detection: "Failure injection testing that simulates partial success; audit of idempotency claims against actual behaviour"
  recovery: "Redesign operation for true idempotency; implement idempotency key for the operation; document known idempotency limitations"
  retryable: false

## Observations
- observation: "The majority of data integrity incidents in distributed systems are caused by non-idempotent retry, not by primary failures."
  confidence: high
  source: Production incident analysis, payment system post-mortems
- observation: "Idempotency is frequently assumed but rarely verified — most 'idempotent' operations have undiscovered non-idempotent edge cases."
  confidence: high
  source: Production incident analysis, code review experience
- observation: "Idempotency keys are the most reliable mechanism for exactly-once semantics but add operational complexity for key storage and cleanup."
  confidence: high
  source: Distributed systems literature, payment system design

## Constraints
- constraint: "An operation that produced side effects before failure cannot be made idempotent without deduplication — the first application already occurred."
  type: invariant
  scope: cross-system
- constraint: "Idempotency keys have a finite lifetime — once the key retention period expires, duplicate detection is no longer possible."
  type: operational
  scope: cross-system

## Decision Factors
- factor: retry_safety_requirement
  question: "Does the operation produce side effects that would cause harm if applied multiple times?"
  supporting: "Operations with side effects (payments, emails, state mutations) require idempotency for retry safety."
  contradictory: "Read-only and stateless operations are naturally idempotent — no idempotency mechanism needed."
  weight: high
- factor: idempotency_enforcement_location
  question: "Where should idempotency be enforced — client-side, server-side, or both?"
  supporting: "Server-side enforcement is authoritative — it guarantees idempotency regardless of client behaviour."
  contradictory: "Client-side enforcement is simpler but cannot protect against multiple clients or client crashes after submission."
  weight: high
- factor: idempotency_scope
  question: "What is the scope of idempotency — single operation or multi-step transaction?"
  supporting: "Single-operation idempotency is simpler — deduplicate at the API level."
  contradictory: "Multi-step idempotency (saga-level) is more powerful but requires coordinated idempotency across steps."
  weight: medium

## Heuristics
- heuristic: "Design operations to be naturally idempotent (SET value, UPSERT, PUT) rather than relying on deduplication."
  rationale: "Natural idempotency has zero runtime cost and cannot fail; deduplication adds latency, storage, and failure modes."
  evidence_level: high
- heuristic: "Use idempotency keys for operations that cannot be naturally idempotent."
  rationale: "Idempotency keys provide exactly-once semantics for any operation at the cost of key storage and checking."
  evidence_level: high
- heuristic: "Verify idempotency by retrying the same request in testing and confirming identical results."
  rationale: "Claimed idempotency should be verified through direct testing — assumption is not evidence."
  evidence_level: high

## Recommendations
- recommendation: "Require idempotency keys for all mutating API operations as an architectural standard."
  context: api_design
  certainty: strong
  rationale: "Universal idempotency key support enables safe retry for all operations without per-operation analysis."
- recommendation: "Verify idempotency through chaos engineering — inject failures after partial operation completion and confirm retry produces correct state."
  context: pre_production
  certainty: strong
  rationale: "Standard testing does not surface partial-success idempotency failures; chaos engineering reveals them."
- recommendation: "Include idempotency key in all retry logging to enable deduplication analysis during incident investigation."
  context: observability
  certainty: strong
  rationale: "Without idempotency keys in logs, duplicate processing incidents are difficult to detect and diagnose."
