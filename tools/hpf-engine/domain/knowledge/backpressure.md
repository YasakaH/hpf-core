# Backpressure

## Identity
- id: backpressure
- type: concept
- title: Backpressure
- tags: [distributed-systems, resilience, flow-control, load-management, reactive-systems]
- entities: [backpressure, flow control, load shedding, reactive streams, capacity management]
- concepts: [cascading-failure, retry-storm-amplification, circuit-breaker, quorum]

## Claims
- claim: "Backpressure is the mechanism by which a downstream component signals its capacity to upstream components, creating a feedback loop that prevents overload."
  certainty: high
  evidence: Reactive streams specification, distributed systems literature
  scope: cross-system
- claim: "Backpressure propagates capacity information against the direction of data flow — downstream saturation is communicated upstream so upstream can reduce its emission rate."
  certainty: high
  evidence: Reactive streams specification, systems literature
  scope: cross-system
- claim: "Without backpressure, a downstream component can be overwhelmed by upstream production that exceeds its processing capacity."
  certainty: high
  evidence: Reactive streams specification, production experience
  scope: cross-system
- claim: "Backpressure can be implemented at multiple levels: TCP receive window (transport), gRPC flow control (RPC), message queue credits (application)."
  certainty: high
  evidence: TCP spec, gRPC documentation, message queue documentation
  scope: cross-system
- claim: "Backpressure is distinct from load shedding — backpressure reduces upstream emission; load shedding drops excess requests at the current level."
  certainty: high
  evidence: Systems literature, resilience engineering
  scope: cross-system

## Relationships
- concept: cascading-failure
  relationship: prevents
  description: "Backpressure prevents cascading failures by reducing upstream load before downstream capacity is exhausted."
- concept: retry-storm-amplification
  relationship: reduces
  description: "Backpressure signals upstream to slow down, reducing the volume of retries that reach a stressed component."
- concept: circuit-breaker
  relationship: complementary_to
  description: "Backpressure reduces load continuously; circuit breakers act as a binary trip when backpressure is insufficient."
- concept: quorum
  relationship: interacts_with
  description: "Backpressure on quorum operations can reduce the effective throughput of a consensus cluster under load."

## Tradeoffs
- dimension: push_vs_pull_flow_control
  options:
    push_with_backpressure:
      value: producer_initiated
      rationale: "Producer pushes data but honours capacity signals from consumer — common in reactive streams."
    pull_based:
      value: consumer_initiated
      rationale: "Consumer requests data at its own pace — simpler backpressure but may increase latency."
  importance: high
- dimension: buffering_vs_dropping
  options:
    buffer:
      value: throughput
      rationale: "Buffers smooth out load spikes but increase memory pressure and end-to-end latency."
    drop:
      value: freshness
      rationale: "Dropping excess data preserves system responsiveness but loses work."
  importance: operational

## Failure Modes
- name: backpressure_stall
  description: "Backpressure signal propagates upstream but the upstream component is blocked on a downstream dependency, creating a system-wide stall."
  likelihood: medium
  observable_evidence: "System-wide latency increase; upstream components at capacity waiting on downstream; no component saturated individually"
  detection: "Trace end-to-end request flow; identify components waiting on downstream responses; measure queue depth at each stage"
  recovery: "Introduce timeouts on backpressure propagation; implement circuit breakers to break backpressure chains; add capacity at bottleneck"
  retryable: true
- name: backpressure_ignored
  description: "Upstream ignores or misinterprets backpressure signals, continuing to send at full rate."
  likelihood: medium
  observable_evidence: "Downstream continues to receive load despite signalling capacity exhaustion; backpressure metrics show signal sent but emission rate unchanged"
  detection: "Monitor backpressure signal compliance ratio; alert when upstream emission rate exceeds signalled capacity"
  recovery: "Fail requests from non-compliant upstreams; implement circuit breaker at ingress for repeated violations"
  retryable: false
- name: cascading_backpressure
  description: "Backpressure from a downstream component propagates all the way to the system edge, reducing or halting all external requests."
  likelihood: low
  observable_evidence: "End-to-end request rate drops despite adequate capacity at intermediate layers; backpressure chain visible in tracing"
  detection: "Trace backpressure propagation across component chain; identify root cause downstream component"
  recovery: "Address root cause at the original bottleneck; consider selective backpressure that only affects relevant traffic classes"
  retryable: true

## Observations
- observation: "TCP's built-in backpressure (receive window) is the most widely deployed backpressure mechanism — every TCP connection implements it."
  confidence: high
  source: TCP specification (RFC 793), universal deployment
- observation: "Application-level backpressure is frequently omitted because it adds complexity — most systems rely on circuit breakers as a simpler alternative."
  confidence: high
  source: Architecture review experience, production pattern analysis
- observation: "Backpressure works best when applied at the boundary of the system — edge-level backpressure protects internal components naturally."
  confidence: medium
  source: Reactive systems literature, production architecture

## Constraints
- constraint: "Backpressure cannot increase total system capacity — it can only distribute load within existing capacity constraints."
  type: invariant
  scope: cross-system
- constraint: "Backpressure propagation has latency — a downstream overload can persist for one propagation cycle before the upstream responds."
  type: invariant
  scope: cross-system

## Heuristics
- heuristic: "Implement backpressure at component boundaries rather than within components for maximum effectiveness."
  rationale: "Boundary backpressure protects the entire downstream component; intra-component backpressure only protects specific resources."
  evidence_level: high
- heuristic: "Combine backpressure with circuit breakers — backpressure handles gradual overload, circuit breakers handle sudden spikes."
  rationale: "Backpressure and circuit breakers address different overload patterns; together they provide comprehensive protection."
  evidence_level: high
- heuristic: "Prefer backpressure over unbounded buffering — unbounded buffers hide overload until capacity is exhausted catastrophically."
  rationale: "Bounded buffers with backpressure make capacity limits visible; unbounded buffers delay failure and amplify recovery cost."
  evidence_level: high

## Recommendations
- recommendation: "Implement explicit backpressure at every asynchronous boundary in the system — implicit backpressure (TCP) only covers transport-level flow."
  context: architecture_design
  certainty: strong
  rationale: "Transport-level backpressure protects individual connections but not application-level processing capacity."
- recommendation: "Monitor backpressure signals as leading indicators of saturation — backpressure activation precedes circuit-breaker activation."
  context: observability
  certainty: strong
  rationale: "Backpressure is an early warning signal; reacting at the backpressure stage prevents circuit-breaker activation."
- recommendation: "Test backpressure behaviour under load patterns that exceed capacity — validate that signals propagate correctly and upstreams honour them."
  context: pre_production
  certainty: strong
  rationale: "Backpressure correctness can only be verified under overload — idle testing confirms plumbing but not behaviour."
