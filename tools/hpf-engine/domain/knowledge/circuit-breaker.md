# Circuit Breaker

## Identity
- id: circuit-breaker
- type: pattern
- title: Circuit Breaker
- tags: [distributed-systems, resilience, fault-tolerance, retry, failure-handling, stability]
- entities: [circuit breaker, fail fast, retry, cascading failure, bulkhead, resilience pattern]
- concepts: [cascading-failure, retry-storm-amplification, backpressure, rolling-deployment, availability, raft-consensus]

## Claims
- claim: "A circuit breaker is a resilience pattern that detects failures and prevents calls to a failing component until it is likely to recover."
  certainty: high
  evidence: Distributed systems literature, circuit breaker pattern (Fowler)
  scope: cross-system
- claim: "Circuit breakers operate in three states: closed (normal operation), open (failing fast), and half-open (testing recovery)."
  certainty: high
  evidence: Circuit breaker pattern literature, production implementations
  scope: cross-system
- claim: "The transition from open to half-open occurs after a cooldown period — a single probe request tests whether the downstream component has recovered."
  certainty: high
  evidence: Circuit breaker pattern literature
  scope: cross-system
- claim: "Circuit breakers prevent cascading failures by failing fast instead of waiting for timeouts — this preserves thread and connection pool capacity."
  certainty: high
  evidence: Production incident analysis, resilience engineering literature
  scope: cross-system
- claim: "Circuit breakers are complementary to retry — retries handle transient failures; circuit breakers handle sustained failures."
  certainty: high
  evidence: Distributed systems literature
  scope: cross-system

## Relationships
- concept: cascading-failure
  relationship: prevents
  description: "Circuit breakers prevent cascading failures by isolating failing components and preventing load amplification."
- concept: retry-storm-amplification
  relationship: prevents
  description: "Circuit breakers prevent retry storms by failing fast — retries never reach the failing component after the breaker opens."
- concept: backpressure
  relationship: complementary_to
  description: "Backpressure reduces load continuously; circuit breakers act as a binary trip when backpressure is insufficient."
- concept: rolling-deployment
  relationship: interacts_with
  description: "Circuit breaker thresholds may need adjustment during rolling deployments to avoid false positives from mixed-version behaviour."
- concept: availability
  relationship: protects
  description: "Circuit breakers protect system availability by preventing partial failures from escalating to total unavailability."
- concept: raft-consensus
  relationship: similar_to
  description: "Raft's leader-based model shares architectural assumptions with circuit breaker state management — both rely on single coordinators with failover."

## Tradeoffs
- dimension: sensitivity_vs_false_positives
  options:
    sensitive:
      value: early_protection
      rationale: "Open circuit quickly — protects downstream but may trigger on transient issues that would self-resolve."
    conservative:
      value: continuity
      rationale: "Require sustained failures before opening — maintains normal flow longer but risks downstream overload."
  importance: high
- dimension: recovery_probing
  options:
    single_probe:
      value: simple
      rationale: "One request tests recovery — fast recovery but may miss lingering issues."
    multi_probe:
      value: thorough
      rationale: "Multiple successful probes before closing — safer but delays recovery confirmation."
  importance: operational

## Failure Modes
- name: circuit_breaker_oscillation
  description: "Circuit breaker cycles open-close rapidly as it opens on failure, cools down, probes, closes, and immediately fails again."
  likelihood: medium
  observable_evidence: "Circuit breaker state changes at high frequency; requests alternately succeed (probe) and fail; recovery never stabilises"
  detection: "Monitor circuit breaker state transition frequency; alert on high-frequency cycling"
  recovery: "Increase cooldown period; require multiple successful probes before closing; investigate root cause of continued failures"
  retryable: true
- name: circuit_breaker_starvation
  description: "Circuit breaker opens permanently because probes never succeed — the downstream is degraded but not completely down."
  likelihood: low
  observable_evidence: "Circuit breaker open for extended period; downstream component partially functional but probes fail; traffic is blackholed"
  detection: "Monitor circuit breaker open duration; correlate with downstream health metrics"
  recovery: "Adjust probe criteria to match actual recovery state; implement partial-circuit (degrade rather than block); manual reset if appropriate"
  retryable: false
- name: cascading_circuit_breakers
  description: "One circuit breaker opens, causing its callers to fail, which triggers their circuit breakers, propagating the failure chain."
  likelihood: medium
  observable_evidence: "Chain of open circuit breakers from downstream to upstream; system-wide degradation from localised failure"
  detection: "Map circuit breaker dependency chains; monitor correlated circuit breaker activations"
  recovery: "Bypass circuit breakers for critical path components during incident; address root cause at the origin of the chain"
  retryable: true

## Observations
- observation: "Circuit breakers are the most widely adopted resilience pattern in distributed systems — nearly every production service uses them."
  confidence: high
  source: Architecture survey, production experience
- observation: "Circuit breaker configuration is frequently set incorrectly — thresholds that work in testing cause false positives or missed failures in production."
  confidence: high
  source: Production incident analysis, architecture review
- observation: "Circuit breakers without half-open probing never recover automatically — the breaker stays open until manual intervention."
  confidence: high
  source: Production implementation review
- observation: "Circuit breakers paired with exponential backoff retry provide the most robust failure handling pattern."
  confidence: high
  source: Distributed systems literature, production experience

## Constraints
- constraint: "A circuit breaker cannot distinguish between a downstream failure and increased latency — both count toward the failure threshold."
  type: invariant
  scope: cross-system
- constraint: "Circuit breaker state is local to each caller — different callers may have different circuit states for the same downstream component."
  type: invariant
  scope: cross-system

## Decision Factors
- factor: failure_threshold
  question: "How many failures within the measurement window should trigger the circuit breaker?"
  supporting: "Low thresholds protect downstream more aggressively but may false-positive on transient issues."
  contradictory: "High thresholds reduce false positives but allow more failures to reach the downstream component before protection activates."
  weight: high
- factor: cooldown_period
  question: "How long should the circuit breaker wait before attempting recovery?"
  supporting: "Short cooldown (5-30s) recovers quickly from transient issues but may retry into still-failing downstream."
  contradictory: "Long cooldown (60-300s) ensures the downstream has time to recover but extends the protection window unnecessarily."
  weight: high
- factor: probe_strategy
  question: "How should the circuit breaker test downstream recovery?"
  supporting: "Single probe is simplest and fastest — adequate for most systems."
  contradictory: "Multi-probe with success count thresholds is more reliable for critical dependencies but adds recovery latency."
  weight: medium

## Heuristics
- heuristic: "Set circuit breaker thresholds based on actual downstream recovery time, not arbitrary values."
  rationale: "Thresholds derived from downstream recovery behaviour are more effective than generic defaults."
  evidence_level: high
- heuristic: "Always implement half-open state — circuit breakers without automatic recovery require manual intervention for every incident."
  rationale: "Half-open state enables automatic recovery without operator attention for transient issues."
  evidence_level: high
- heuristic: "Log every circuit breaker state transition with full context (downstream, failure count, decision reason)."
  rationale: "Circuit breaker activations are critical diagnostic signals — incomplete logging delays incident diagnosis."
  evidence_level: high

## Recommendations
- recommendation: "Deploy circuit breakers at every synchronous dependency boundary — any component that calls another component synchronously should be protected."
  context: architecture_design
  certainty: strong
  rationale: "Unprotected synchronous dependencies are the most common propagation path for cascading failures."
- recommendation: "Instrument circuit breaker state as a observable metric with alerts on state transitions — open circuit breaker is an operational event."
  context: observability
  certainty: strong
  rationale: "Circuit breaker state transitions are leading indicators of system instability — alerting on them enables proactive response."
- recommendation: "Test circuit breaker behaviour under realistic failure patterns — circuit breakers configured in isolation behave differently under cascading conditions."
  context: pre_production
  certainty: strong
  rationale: "Individual circuit breaker behaviour is predictable; cascading circuit breaker behaviour requires system-level testing."
