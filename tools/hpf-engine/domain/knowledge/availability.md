# Availability

## Identity
- id: availability
- type: concept
- title: Availability
- tags: [distributed-systems, availability, reliability, uptime, sla, fault-tolerance]
- entities: [availability, uptime, sla, redundancy, failover, high availability, nine nines]
- concepts: [cap-theorem, eventual-consistency, strong-consistency, quorum, backpressure, circuit-breaker]

## Claims
- claim: "Availability is the proportion of time a system remains operational and able to serve requests, typically measured as a percentage of uptime."
  certainty: high
  evidence: Systems reliability literature, industry practice
  scope: cross-system
- claim: "Availability is not binary — a system can be available for reads but not writes, available at degraded performance, or available for only a subset of clients."
  certainty: high
  evidence: Systems reliability literature, production experience
  scope: cross-system
- claim: "High availability (HA) is achieved through redundancy — multiple instances that can serve requests when one fails."
  certainty: high
  evidence: Systems reliability literature, production architecture
  scope: cross-system
- claim: "Increasing availability by one 'nine' (99.9% to 99.99%) typically requires an order of magnitude increase in architectural complexity."
  certainty: high
  evidence: Systems reliability literature, production cost analysis
  scope: cross-system
- claim: "Availability and consistency are traded off during partitions — CAP theorem formally captures this constraint."
  certainty: high
  evidence: CAP theorem (Gilbert-Lynch)
  scope: distributed-stateful
- claim: "Degraded availability (serving requests with higher latency or reduced functionality) is preferable to total unavailability for most user-facing systems."
  certainty: high
  evidence: Production experience, resilience engineering literature
  scope: cross-system

## Relationships
- concept: cap-theorem
  relationship: constrained_by
  description: "CAP theorem constrains availability — during partitions, availability must be traded against consistency."
- concept: eventual-consistency
  relationship: enables
  description: "Eventual consistency enables higher availability by allowing writes during partitions."
- concept: strong-consistency
  relationship: limits
  description: "Strong consistency limits availability during partitions because the minority partition cannot serve writes."
- concept: quorum
  relationship: affects
  description: "Quorum size directly affects availability — larger quorums reduce availability because more nodes must respond."
- concept: backpressure
  relationship: protects
  description: "Backpressure protects availability by preventing overload from cascading into complete unavailability."
- concept: circuit-breaker
  relationship: protects
  description: "Circuit breakers protect availability by failing fast and preventing retry storms from causing total unavailability."

## Tradeoffs
- dimension: availability_vs_complexity
  options:
    single_node:
      value: simple
      rationale: "No redundancy — simple operation but availability limited to single-node reliability."
    active_passive:
      value: moderate_complexity
      rationale: "One standby node — failover takes seconds to minutes but is architecturally simple."
    active_active:
      value: high_availability
      rationale: "Multiple active nodes — fastest failover but requires load balancing, session management, and consistency coordination."
  importance: high
- dimension: availability_vs_latency
  options:
    local_only:
      value: low_latency
      rationale: "Single-region deployment — lowest latency but vulnerable to regional outages."
    geo_distributed:
      value: regional_survival
      rationale: "Multi-region deployment — survives regional outages but adds cross-region replication latency."
  importance: high

## Failure Modes
- name: silent_unavailability
  description: "System appears available (accepts connections) but cannot successfully process requests."
  likelihood: medium
  observable_evidence: "Health checks pass but application-level operations fail; connections accepted but requests time out; error rate increases without corresponding availability metrics changing"
  detection: "Application-level health checks (not just TCP/HTTP-level); synthetic transaction monitoring; end-to-end success rate tracking"
  recovery: "Degrade health check to reflect application-level status; divert traffic to healthy instances; investigate root cause of silent failures"
  retryable: false
- name: availability_overshoot
  description: "System achieves high availability but at unsustainable operational cost — the complexity reduces feature velocity and increases incident rate."
  likelihood: medium
  observable_evidence: "Operational team spends >50% of time managing HA infrastructure; deployment complexity slows releases; incidents from HA infrastructure exceed incidents from primary functionality"
  detection: "Track operational cost per availability percentage point; correlate availability-related complexity with deployment frequency"
  recovery: "Reduce availability target to match actual requirements; simplify architecture; accept planned downtime for critical maintenance"
  retryable: false
- name: cascading_unavailability
  description: "Partial availability loss triggers cascading failures that escalate to total unavailability."
  likelihood: high
  observable_evidence: "Initial availability loss in one component → load redistribution → secondary failures → system-wide unavailability"
  detection: "Monitor availability per component (not just system-wide); track failure propagation paths"
  recovery: "Isolate failing components; activate circuit breakers; shed load to protect remaining capacity"
  retryable: true

## Observations
- observation: "Nine-nines availability (99.999%) is a marketing term for most systems — actual measured availability rarely exceeds 99.99%."
  confidence: high
  source: Production monitoring data, cloud provider SLA analysis
- observation: "The most common cause of unavailability in distributed systems is configuration error, not infrastructure failure."
  confidence: high
  source: Production incident analysis, cloud provider post-mortems
- observation: "Availability measurements without explicit error budgets are misleading — a system is meeting its availability target only if it stays within its error budget over the measurement window."
  confidence: high
  source: Google SRE literature, production experience

## Constraints
- constraint: "System availability cannot exceed the availability of its least redundant component — availability is constrained by the weakest link."
  type: invariant
  scope: cross-system
- constraint: "Increasing availability past 99.99% requires redundancy at every layer (compute, network, storage, power, data centre region)."
  type: invariant
  scope: cross-system

## Decision Factors
- factor: availability_target
  question: "What is the required availability level for the system?"
  supporting: "Explicit availability targets (SLOs) drive architecture decisions — higher targets justify more investment in redundancy."
  contradictory: "Availability targets are often aspirational rather than requirement-driven — the target should reflect business impact of downtime, not engineering ambition."
  weight: high
- factor: degradation_strategy
  question: "What should the system do when it cannot serve full functionality?"
  supporting: "Degraded operation (read-only mode, reduced functionality, higher latency) maintains partial availability and user trust."
  contradictory: "Degradation adds complexity and may mask the severity of the underlying issue — total unavailability is sometimes clearer."
  weight: high
- factor: error_budget_policy
  question: "How is the availability budget managed between releases and operations?"
  supporting: "Error budgets (SLO - availability) allow teams to trade availability for deployment velocity within defined limits."
  contradictory: "Error budgets require mature monitoring and organisational discipline — without enforcement, they are theoretical."
  weight: medium

## Heuristics
- heuristic: "Target 99.9% availability (8.76 hours downtime/year) for internal tools and 99.99% (52 minutes/year) for customer-facing systems."
  rationale: "Each additional nine increases cost and complexity non-linearly; target availability should match business requirements."
  evidence_level: high
- heuristic: "Measure availability at the application level, not the infrastructure level — infrastructure availability does not guarantee application availability."
  rationale: "A running server with a broken application is still unavailable despite 'green' infrastructure health checks."
  evidence_level: high
- heuristic: "Budget availability for planned maintenance — maintenance windows count as downtime if users cannot access the system."
  rationale: "Architecture decisions should consider whether planned downtime is acceptable or if zero-downtime deployments are required."
  evidence_level: high

## Recommendations
- recommendation: "Define availability SLOs in terms of user-visible behaviour, not infrastructure metrics — '99.9% of requests succeed with latency under 500ms' is more meaningful than '99.9% uptime'."
  context: service_level_objectives
  certainty: strong
  rationale: "Infrastructure uptime does not guarantee application availability; user-visible SLOs align engineering effort with user impact."
- recommendation: "Implement graceful degradation as a first-class architectural requirement, not an afterthought — define what the system does at each saturation level."
  context: architecture_design
  certainty: strong
  rationale: "Without defined degradation behaviour, the system's response to overload is undefined and likely worse than any planned degradation strategy."
- recommendation: "Test availability boundaries through chaos engineering — validate that redundancy and failover mechanisms work under realistic failure conditions."
  context: pre_production
  certainty: strong
  rationale: "Availability mechanisms that have never been tested in production will fail when first exercised under incident conditions."
