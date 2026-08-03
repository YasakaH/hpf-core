# Saga Pattern

## Identity
- id: saga-pattern
- type: pattern
- title: Saga Pattern
- tags: [distributed-systems, transaction, orchestration, choreography, compensation, consistency]
- entities: [saga pattern, distributed transaction, compensation, orchestration, choreography, saga, long-running transaction]
- concepts: [idempotency, eventual-consistency, cascading-failure, circuit-breaker, quorum]

## Claims
- claim: "A saga is a sequence of local transactions where each step has a compensating transaction that can undo its effects."
  certainty: high
  evidence: Distributed systems literature, saga pattern (Garcia-Molina & Salem)
  scope: cross-system
- claim: "Sagas avoid distributed transactions (two-phase commit) by breaking multi-step operations into independently committable steps."
  certainty: high
  evidence: Distributed systems literature, saga pattern original paper
  scope: cross-system
- claim: "If a step in a saga fails, the compensating transactions for all completed steps are executed to maintain overall consistency."
  certainty: high
  evidence: Saga pattern literature
  scope: cross-system
- claim: "Sagas provide eventual consistency — during execution, intermediate states are visible to other components before the saga completes."
  certainty: high
  evidence: Distributed systems literature
  scope: cross-system
- claim: "There are two saga implementation models: choreography (each service publishes events that trigger the next step) and orchestration (a central coordinator manages the sequence)."
  certainty: high
  evidence: Distributed systems literature, microservices architecture
  scope: cross-system
- claim: "Compensation logic must be idempotent — a compensating transaction may be executed multiple times in failure scenarios."
  certainty: high
  evidence: Distributed systems literature, production experience
  scope: cross-system

## Relationships
- concept: idempotency
  relationship: requires
  description: "Saga compensation logic must be idempotent — compensating an already-compensated step must not produce incorrect state."
- concept: eventual-consistency
  relationship: relies_on
  description: "Sagas rely on eventual consistency — intermediate states are visible and the system must handle partial saga execution."
- concept: cascading-failure
  relationship: vulnerable_to
  description: "Sagas spanning many services are vulnerable to cascading failures — compensation may also fail if downstream is unavailable."
- concept: circuit-breaker
  relationship: complementary_to
  description: "Circuit breakers protect saga execution by failing fast when downstream components are unavailable, triggering compensation earlier."

## Tradeoffs
- dimension: choreography_vs_orchestration
  options:
    choreography:
      value: loose_coupling
      rationale: "Services communicate through events — no central coordinator, but saga flow is distributed across services and harder to monitor."
    orchestration:
      value: centralised_control
      rationale: "Central coordinator manages the saga sequence — easier to monitor and manage but introduces a single point of coordination."
  importance: high
- dimension: compensation_complexity
  options:
    simple_compensation:
      value: easy_to_implement
      rationale: "Each step has a single compensating action — simplest but may not handle partial-step failures."
    tiered_compensation:
      value: failure_resilience
      rationale: "Multiple compensation strategies per step (fast, thorough) — handles more failure modes but adds complexity."
  importance: high
- dimension: forward_recovery_vs_backward_recovery
  options:
    forward_recovery:
      value: complete_saga
      rationale: "On failure, retry the step or perform an alternative action to complete the saga — preserves progress."
    backward_recovery:
      value: clean_state
      rationale: "On failure, compensate all completed steps — returns to initial state but wastes completed work."
  importance: operational

## Failure Modes
- name: compensation_failure
  description: "A compensating transaction fails, leaving the system in an inconsistent state with partial saga execution."
  likelihood: high
  observable_evidence: "Saga marked as failed but compensation cannot complete; partially executed saga with unreconciled state; alerting on failed compensations"
  detection: "Monitor saga completion rate; alert on compensation failures; track incomplete sagas"
  recovery: "Retry compensation with backoff; escalate to manual intervention after retry limit; accept inconsistency if bounded and understood"
  retryable: true
- name: saga_starvation
  description: "A saga step neither succeeds nor fails within acceptable time — it is pending indefinitely, blocking the saga."
  likelihood: medium
  observable_evidence: "Saga stuck in intermediate state; timeout not configured or too long; pending saga count grows"
  detection: "Monitor saga step duration; alert on steps exceeding expected duration; track pending saga age"
  recovery: "Implement step-level timeouts; trigger compensation on timeout; manual investigation of hung steps"
  retryable: true
- name: cascading_compensation
  description: "Compensating one saga triggers compensation in dependent sagas, creating a chain of compensation that is difficult to coordinate."
  likelihood: low
  observable_evidence: "Compensation of one saga triggers unintended compensation of related sagas; system-wide rollback cascades"
  detection: "Cross-saga dependency mapping; monitoring correlated compensation activations"
  recovery: "Isolate saga boundaries; implement saga-level idempotency to prevent recursive compensation; manual coordination of multi-saga compensation"
  retryable: false

## Observations
- observation: "Saga compensation failures are more common than saga execution failures — implementing robust compensation is harder than implementing forward progress."
  confidence: high
  source: Production incident analysis, distributed systems literature
- observation: "Choreography-based sagas are harder to monitor and debug than orchestration-based sagas because the flow is not centralised."
  confidence: high
  source: Production operational experience
- observation: "Sagas are most commonly used in e-commerce and financial systems where multi-step transactions must span service boundaries."
  confidence: high
  source: Architecture survey, production experience

## Constraints
- constraint: "A saga cannot provide atomicity — intermediate states are visible to other components during execution."
  type: invariant
  scope: cross-system
- constraint: "Compensation must be idempotent — a compensating transaction may be executed multiple times for the same saga step."
  type: invariant
  scope: cross-system

## Decision Factors
- factor: consistency_requirement
  question: "Does the multi-step operation require atomic visibility or is eventual consistency acceptable?"
  supporting: "Sagas provide eventual consistency — suitable for operations where intermediate visible states are acceptable."
  contradictory: "If atomic visibility is required (all steps become visible simultaneously), distributed transactions (2PC) must be used instead."
  weight: high
- factor: saga_coordination_model
  question: "Is the organisation better suited to centralised orchestration or distributed choreography?"
  supporting: "Orchestration suits teams with centralised architecture and strong operational monitoring."
  contradictory: "Choreography suits teams with domain-driven design and event-savvy infrastructure."
  weight: high
- factor: compensation_design_capacity
  question: "Can the team design and maintain correct compensating transactions for every saga step?"
  supporting: "Well-designed compensation is essential for saga correctness — teams must invest in compensation design and testing."
  contradictory: "If compensation cannot be reliably implemented, consider alternative patterns (distributed transactions, or redesign to avoid multi-step operations)."
  weight: high

## Heuristics
- heuristic: "Prefer orchestration for sagas with more than 3 steps — choreography becomes difficult to trace beyond simple chains."
  rationale: "Choreography-based saga flow is distributed across event handlers; beyond 3 steps, the flow becomes difficult to reason about."
  evidence_level: high
- heuristic: "Test compensation paths as rigorously as forward paths — compensation is executed less frequently but is more likely to fail when needed."
  rationale: "Compensation paths are exercised less often than forward paths, so they are more likely to contain bugs that surface during incidents."
  evidence_level: high
- heuristic: "Implement timeout-based compensation for stalled saga steps — indefinite pending is worse than compensated failure."
  rationale: "A pending saga that never completes blocks resources and may hold locks; bounded execution with compensation is preferable."
  evidence_level: high
- heuristic: "Design sagas to be retryable at the saga level — if a saga fails and is compensated, a new saga with the same intent should succeed."
  rationale: "Saga-level retry enables recovery from transient failures without manual intervention."
  evidence_level: high

## Recommendations
- recommendation: "Always design compensation logic before implementing forward logic — if you cannot compensate, you cannot safely execute the saga."
  context: implementation
  certainty: strong
  rationale: "Compensation is a first-class correctness requirement, not a failure path to be designed later."
- recommendation: "Monitor saga execution and compensation metrics separately — compensation rate is a leading indicator of system health."
  context: observability
  certainty: strong
  rationale: "Rising compensation rates indicate increasing failure rates in saga execution — earlier signal than end-user visible failures."
- recommendation: "Test saga compensation under realistic failure patterns — compensation that works in isolation may fail when multiple compensations execute concurrently."
  context: pre_production
  certainty: strong
  rationale: "Concurrent compensation can cause resource contention and ordering issues that isolated testing does not reveal."
