# Cascading Failure

## Identity
- id: cascading-failure
- type: concept
- title: Cascading Failure
- tags: [distributed-systems, fault-tolerance, failure-propagation, resilience, overload]
- entities: [cascading failure, failure propagation, overload, resource exhaustion, domino effect]
- concepts: [network-failure-propagation, retry-storm-amplification, circuit-breaker, backpressure, split-brain]

## Claims
- claim: "A cascading failure is a failure that propagates through a system as each component's failure increases the load on remaining components."
  certainty: high
  evidence: Distributed systems literature, production incident analysis
  scope: cross-system
- claim: "Cascading failures follow a characteristic pattern: initial failure → load redistribution → remaining components exceed capacity → secondary failures."
  certainty: high
  evidence: Production incident analysis, systems literature
  scope: cross-system
- claim: "The propagation speed of a cascading failure depends on the coupling between components — tightly coupled systems fail faster."
  certainty: high
  evidence: Systems theory, production experience
  scope: cross-system
- claim: "Cascading failures are not caused by the initial failure alone — they require overload of the remaining capacity to propagate."
  certainty: high
  evidence: Failure analysis literature
  scope: cross-system
- claim: "Cascading failures can be arrested if the remaining capacity can absorb the redistributed load or if load shedding is activated in time."
  certainty: high
  evidence: Production incident analysis, resilience engineering literature
  scope: cross-system

## Relationships
- concept: retry-storm-amplification
  relationship: triggers
  description: "Cascading failures often trigger retry storms as clients retry failed requests, amplifying the load on already-stressed components."
- concept: network-failure-propagation
  relationship: similar_to
  description: "Network failure propagation follows the same cascading mechanism at the transport layer — TCP timeouts cascade up to application failures."
- concept: circuit-breaker
  relationship: prevents
  description: "Circuit breakers interrupt cascading failures by failing fast instead of allowing retries to amplify load."
- concept: backpressure
  relationship: prevents
  description: "Backpressure mechanisms limit cascading by propagating load signals upstream, allowing upstream components to reduce their request rate."
- concept: split-brain
  relationship: worsens
  description: "Split brain conditions can trigger cascading failures when partitions rejoin and attempt to reconcile divergent state under load."

## Tradeoffs
- dimension: fail_fast_vs_graceful_degradation
  options:
    fail_fast:
      value: containment
      rationale: "Immediate failure prevents load amplification but increases visible error rate."
    graceful_degradation:
      value: partial_service
      rationale: "Reduced functionality maintains some service but may mask the severity of the failure."
  importance: high
- dimension: load_shedding_vs_availability
  options:
    aggressive_shedding:
      value: system_survival
      rationale: "Drops excess requests to protect core capacity — preserves system at cost of partial availability."
    no_shedding:
      value: maximum_availability
      rationale: "Attempts to serve all requests risks total collapse when capacity is exceeded."
  importance: high
- dimension: automated_recovery_vs_human_intervention
  options:
    automated:
      value: speed
      rationale: "Faster recovery but may repeat incorrect recovery patterns."
    manual:
      value: judgement
      rationale: "Operator can assess context but recovery is slower, extending failure window."
  importance: operational

## Failure Modes
- name: uncontrolled_cascade
  description: "Failure propagation cannot be arrested — each failure increases load on remaining components, creating a chain reaction."
  likelihood: high
  observable_evidence: "Monotonic increase in failure rate; sequential component failures; system-wide collapse within predictable timeframe"
  detection: "Monitor per-component failure rates; alert on correlation between failures across components; track capacity utilisation trends"
  recovery: "Kill all traffic (total halt); bring up replacement capacity; reintroduce traffic gradually with load protection"
  retryable: false
- name: partial_cascade_with_oscillation
  description: "Cascade partially triggers, recovery mechanisms activate, but the system oscillates between degraded and recovered states."
  likelihood: medium
  observable_evidence: "Cyclic failure-recovery pattern; intermittent availability; resource utilisation oscillates between high and normal"
  detection: "Monitor oscillation frequency; correlate with recovery mechanism activations"
  recovery: "Increase recovery thresholds; add cooldown periods before recovery attempts; investigate root cause of oscillation trigger"
  retryable: true
- name: hidden_cascade_primer
  description: "A latent condition exists that will trigger a cascade if a specific failure occurs — cascade is primed but not yet active."
  likelihood: low
  observable_evidence: "System operates normally but capacity margins are below cascade threshold; single failure will trigger chain reaction"
  detection: "Chaos engineering; capacity planning analysis; load testing beyond expected peak"
  recovery: "Add capacity; reduce coupling; implement load shedding before the primed condition becomes active"
  retryable: false

## Observations
- observation: "Most cascading failures in production are not caused by the initial trigger — they are caused by the system's inability to absorb redistributed load."
  confidence: high
  source: Production incident analysis, post-mortem reviews
- observation: "The most effective defence against cascading failure is capacity headroom — systems with >50% headroom rarely cascade."
  confidence: high
  source: Operational experience, capacity planning literature
- observation: "Cascading failures often follow deployment or configuration changes — the initial trigger is correlated with recent modifications."
  confidence: medium
  source: Incident analysis, change management reviews

## Constraints
- constraint: "Total system capacity is always less than the sum of component capacities during a cascade — redistributed load has overhead."
  type: invariant
  scope: cross-system
- constraint: "A cascading failure cannot be stopped without either adding capacity or reducing load — one of these must happen before the cascade completes."
  type: invariant
  scope: cross-system

## Heuristics
- heuristic: "Always deploy with load shedding configured before it is needed — configuring under incident pressure leads to mistakes."
  rationale: "Load shedding configuration requires careful calibration of thresholds and priority — ad-hoc configuration during incidents is error-prone."
  evidence_level: high
- heuristic: "Use circuit breakers at integration points to prevent cascading across service boundaries."
  rationale: "Circuit breakers localise failures by failing fast instead of allowing retries to propagate load."
  evidence_level: high
- heuristic: "Run chaos engineering experiments that simulate component failures to validate cascade boundaries."
  rationale: "Theoretical analysis of cascade boundaries is insufficient — empirical testing reveals unexpected propagation paths."
  evidence_level: high

## Recommendations
- recommendation: "Implement automatic load shedding at 80% of component capacity — waiting for 100% risks uncontrolled cascade."
  context: capacity_management
  certainty: strong
  rationale: "At 100% utilisation, any additional load triggers failure; shedding before saturation provides a safety margin."
- recommendation: "Map cascade boundaries explicitly — document which component failures can propagate to which dependent components."
  context: architecture_documentation
  certainty: strong
  rationale: "Unknown cascade paths are the most dangerous — they cannot be monitored or defended against until they are documented."
- recommendation: "Test cascade scenarios under production-like load — idle-system cascade behaviour differs significantly from loaded-system behaviour."
  context: pre_production
  certainty: strong
  rationale: "Load amplifies cascading effects; idle testing underestimates propagation speed and severity."
