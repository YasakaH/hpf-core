# Retry Storm Amplification

## Identity
- id: retry-storm-amplification
- type: concept
- title: Retry Storm Amplification
- tags: [distributed-systems, fault-tolerance, retry, cascading-failure, overload, resilience]
- entities: [retry storm, retry amplification, thundering herd, exponential backoff, jitter, retry]
- concepts: [cascading-failure, network-failure-propagation, circuit-breaker, backpressure]

## Claims
- claim: "A retry storm occurs when many clients retry failed operations simultaneously, amplifying load beyond what the recovering system can handle."
  certainty: high
  evidence: Production incident analysis, distributed systems literature
  scope: cross-system
- claim: "Retry storms transform transient failures into sustained overload — the initial trigger resolves but the retry-induced load keeps the system saturated."
  certainty: high
  evidence: Production incident analysis, resilience engineering
  scope: cross-system
- claim: "Without jitter, clients using exponential backoff synchronise naturally — identical backoff schedules produce coordinated retry waves."
  certainty: high
  evidence: Distributed systems literature, AWS architecture documentation
  scope: cross-system
- claim: "Fixed-interval retries without backoff guarantee overload on recovery — all clients retry simultaneously at the same interval."
  certainty: high
  evidence: Systems literature, production experience
  scope: cross-system
- claim: "A retry storm can sustain itself: overload causes failures, failures trigger retries, retries maintain overload."
  certainty: high
  evidence: Production incident analysis
  scope: cross-system

## Relationships
- concept: cascading-failure
  relationship: triggers
  description: "Retry storms amplify cascading failures by adding retry-induced load on top of redistributed load from failed components."
- concept: network-failure-propagation
  relationship: similar_to
  description: "Retry storms at the application layer mirror the amplification pattern of TCP retransmission storms at the transport layer."
- concept: circuit-breaker
  relationship: prevents
  description: "Circuit breakers prevent retry storms by failing fast and blocking retries from reaching the stressed component."
- concept: backpressure
  relationship: reduces
  description: "Backpressure signals upstream to reduce request rate, preventing downstream retries from amplifying load."
- concept: leader-election
  relationship: vulnerable_to
  description: "Leader election is particularly vulnerable to retry storms — repeated election timeouts trigger cascading elections."

## Tradeoffs
- dimension: retry_aggressiveness_vs_downstream_protection
  options:
    aggressive_retry:
      value: faster_recovery
      rationale: "More retries increase chance of success but risk overload on recovering systems."
    conservative_retry:
      value: system_protection
      rationale: "Fewer retries protect downstream systems but extend individual operation latency."
  importance: high
- dimension: jitter_vs_predictability
  options:
    with_jitter:
      value: load_spreading
      rationale: "Randomised delays prevent retry synchronisation at the cost of unpredictable individual retry timing."
    without_jitter:
      value: deterministic_timing
      rationale: "Predictable retry windows aid debugging but synchronise retries across clients."
  importance: operational

## Failure Modes
- name: self_sustaining_retry_storm
  description: "Retry-induced load maintains saturation even after the original failure is resolved."
  likelihood: high
  observable_evidence: "System remains saturated after trigger condition clears; retry traffic dominates incoming request volume; metric showing retry vs. new request ratio exceeds threshold"
  detection: "Instrument retry identification in request metadata; monitor retry-to-request ratio; alert on sustained elevation"
  recovery: "Rate-limit or reject retries at ingress; circuit-breaker activation on downstream dependencies; cooldown period with retry debouncing"
  retryable: true
- name: retry_deadlock
  description: "Two or more services retry operations against each other simultaneously, each dependent on the other's recovery."
  likelihood: medium
  observable_evidence: "Mutual retry loop between services; no progress on either side; both services show elevated retry counts without success"
  detection: "Cross-service retry correlation; identify paired retry patterns in metrics"
  recovery: "Break the loop by circuit-breaking one direction; prioritise one service for recovery"
  retryable: false
- name: thundering_herd_on_recovery
  description: "Many clients retry simultaneously on detecting recovery, creating a load spike that exceeds capacity."
  likelihood: medium
  observable_evidence: "Recovery signal triggers immediate load spike; system returns to saturation; retry-backoff cycle repeats"
  detection: "Monitor request rate at recovery signal time; correlate recovery broadcasts with load spikes"
  recovery: "Introduce randomised delay between recovery signal and retry; use incremental recovery with capped acceptance rate"
  retryable: true

## Observations
- observation: "Retry storms are the leading cause of prolonged outages in distributed systems — more common than hardware failures or software bugs."
  confidence: high
  source: Production incident analysis, AWS post-mortem reviews
- observation: "The majority of production retry storms are caused by default retry configurations in client libraries, not application code."
  confidence: high
  source: Operational incident reviews, library default analysis
- observation: "Adding jitter to exponential backoff is the single highest-impact change for retry storm prevention."
  confidence: high
  source: AWS architecture documentation, production experience

## Constraints
- constraint: "Retry amplification is bounded by the ratio of retry interval to recovery time — faster retries produce more amplification."
  type: invariant
  scope: cross-system
- constraint: "Without coordination, N clients with identical retry policy produce N-fold load amplification on every retry wave."
  type: invariant
  scope: cross-system

## Heuristics
- heuristic: "Use exponential backoff with jitter as the default retry strategy for all distributed service calls."
  rationale: "Backoff with jitter is the most effective general-purpose retry strategy — it balances recovery speed with load protection."
  evidence_level: high
- heuristic: "Implement retry budgets that cap total retry volume across all clients for a given service."
  rationale: "Retry budgets prevent sustained storms even when individual clients are well-behaved."
  evidence_level: high
- heuristic: "Differentiate retryable from non-retryable errors at the application level — retrying non-retryable errors wastes capacity."
  rationale: "Non-retryable errors (validation, authorisation) will never succeed on retry; retrying them produces load with zero benefit."
  evidence_level: high

## Recommendations
- recommendation: "Set a maximum retry limit of 3 attempts with exponential backoff (base 1s, max 30s) as the organisation-wide default."
  context: service_design
  certainty: strong
  rationale: "3 retries with exponential backoff provides adequate coverage for transient failures while limiting amplification."
- recommendation: "Instrument every retry with a unique identifier that survives across retry attempts for observability."
  context: observability
  certainty: strong
  rationale: "Retry storms are difficult to diagnose without retry-aware tracing — retry identifiers link individual attempts to the overall storm."
- recommendation: "Never use fixed-interval retries in distributed systems — they guarantee thundering herd on recovery."
  context: architecture_design
  certainty: strong
  rationale: "Fixed-interval retries synchronise across clients; exponential backoff with jitter is strictly superior."
