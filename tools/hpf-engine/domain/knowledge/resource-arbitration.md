# Resource Arbitration

## Identity
- id: resource-arbitration
- type: decision
- title: Resource Arbitration
- tags: [arbitration, resource allocation, contention, bus arbitration, scheduling]
- entities: [contention, arbitration, allocation, contender, shared resource]
- concepts: [cyber-physical-system, raft-consensus, scheduling-policy, isolation-levels, deadline]

## Claims
- claim: "Resource arbitration is the allocation decision under contention — bus, memory, and compute shared under physical constraints."
  certainty: high
  evidence: Real-time and embedded systems practice
  scope: cross-domain
- claim: "Arbitration is the fourth appearance of the structure — consensus (006), locking (010), scheduling (011), arbitration (012): contenders + selection rule + allocation + guarantee."
  certainty: high
  evidence: Arbitration watch (Cycle 011)
  scope: cross-domain
- claim: "Arbitration is graph topology, not a construct — the allocation discipline is a decision structure, exactly as resolved in 011."
  certainty: high
  evidence: Arbitration watch resolution (Cycle 011)
  scope: cross-domain
- claim: "Arbitration validity is conditional — the allocation is valid under its stated contention and priority conditions."
  certainty: high
  evidence: Cross-domain comparison (validity conditions 008-011)
  scope: cross-domain
- claim: "The arbitration candidate is re-tested at n=4 but not promoted — the five acceptance criteria must survive further cycles."
  certainty: high
  evidence: Motif acceptance criteria (catalogue v0.1)
  scope: cross-domain

## Decision Factors
- factor: contention_severity
  question: "How heavily is the shared resource contended, and how often?"
  supporting: "Measured contention justifies an explicit allocation rule."
  contradictory: "Unmeasured contention is an unbounded allocation claim."
  weight: high
- factor: allocation_fairness
  question: "How evenly must access be shared among contenders?"
  supporting: "Fair allocation keeps every contender alive."
  contradictory: "Unfair allocation starves the excluded contender."
  weight: high
- factor: deadline_priority
  question: "How strongly do timing deadlines weigh in the allocation?"
  supporting: "Deadline awareness keeps guarantees intact."
  contradictory: "Ignored deadlines convert arbitration into a timing failure."
  weight: high
- factor: preemption_cost
  question: "How costly is it to interrupt an allocation in progress?"
  supporting: "Cheap preemption keeps the rule flexible."
  contradictory: "Costly preemption makes the rule reluctant to re-decide."
  weight: medium

## Relationships
- concept: cyber-physical-system
  relationship: serves
  description: "Resource arbitration serves the cyber-physical system — the shared-resource discipline under physical constraints."
- concept: raft-consensus
  relationship: analogous_to
  description: "Resource arbitration is analogous to consensus — contenders agreeing on one allocation — the Cycle 006 cross-domain link."
- concept: scheduling-policy
  relationship: analogous_to
  description: "Resource arbitration is analogous to scheduling policy — allocation under constraints — the Cycle 011 cross-domain link."
- concept: isolation-levels
  relationship: analogous_to
  description: "Resource arbitration is analogous to isolation levels — access discipline under contention — the Cycle 010 cross-domain link."
- concept: deadline
  relationship: constrained_by
  description: "Resource arbitration is constrained by deadlines — the allocation must respect timing — the Cycle 011 cross-domain link."

## Tradeoffs
- dimension: fairness_vs_priority
  options:
    fair_allocation:
      value: equity
      rationale: "Fair allocation serves all contenders."
    priority_allocation:
      value: criticality
      rationale: "Priority allocation serves the critical contenders."
  importance: high
- dimension: determinism_vs_utilization
  options:
    deterministic_arbitration:
      value: guarantee_strength
      rationale: "Deterministic arbitration holds guarantees."
    high_utilization:
      value: efficiency
      rationale: "High utilization packs more work."
  importance: medium

## Failure Modes
- name: allocation_starvation
  description: "A contender never receives the resource — the allocation discipline permanently excludes a participant."
  likelihood: medium
  observable_evidence: "Starved contender; missed deadlines; degraded function"
  detection: "Allocation monitoring; fairness tracking; starvation detection"
  recovery: "Re-balance the rule; add fairness bounds; re-verify"
  retryable: true
- name: arbitration_delay
  description: "The allocation decision itself takes too long — arbitration latency exceeds its timing budget."
  likelihood: medium
  observable_evidence: "Timing violations; delayed access; missed windows"
  detection: "Arbitration-latency monitoring; timing audits; deadline checks"
  recovery: "Speed the rule; pre-compute allocations; widen the budget"
  retryable: true
- name: unfair_allocation
  description: "The allocation rule drifts from its stated conditions — the discipline no longer matches its contention assumptions."
  likelihood: medium
  observable_evidence: "Systematic bias; unexpected contenders; assumption drift"
  detection: "Allocation audits; condition review; contention measurement"
  recovery: "Re-state conditions; re-balance the rule; re-verify"
  retryable: true

## Observations
- observation: "Arbitration resolved as the allocation decision under contention — the fourth appearance of the structure (006, 010, 011, 012), still topology, not construct."
  confidence: high
  source: Arbitration watch (Cycle 011, 012)
- observation: "The candidate is re-tested at n=4 and remains a candidate — the acceptance criteria require survival across further cycles."
  confidence: high
  source: Motif acceptance criteria (catalogue v0.1)
- observation: "Epistemic Distance at arbitration is 1–2 — the allocation is directly observable, close to the physical resource it orders."
  confidence: high
  source: Epistemic Distance metric (Cycle 012)
- observation: "Starvation is the arbitration failure that surfaces late — the excluded contender fails after the discipline looks stable."
  confidence: high
  source: Real-time systems practice

## Constraints
- constraint: "The allocation is valid under its stated conditions — contention and priority conditions bound the decision."
  type: invariant
  scope: cross-domain
- constraint: "Arbitration is topology, not construct — the discipline must remain an optional composition of existing primitives."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Measure contention before choosing the rule."
  rationale: "The allocation is valid under its stated contention conditions — unmeasured contention is an unbounded claim."
  evidence_level: high
- heuristic: "Bound the worst-case allocation latency."
  rationale: "Arbitration delay is a timing failure — the budget is a stated condition."
  evidence_level: high

## Recommendations
- recommendation: "Represent arbitration as a decision object — contenders, selection rule, allocation, and guarantee as structure."
  context: modelling
  certainty: strong
  rationale: "The structure is topology — the fourth appearance confirms it, it does not construct it."
- recommendation: "State the contention conditions with the allocation rule."
  context: engineering
  certainty: strong
  rationale: "An unstated contention assumption is an unbounded claim."
- recommendation: "Monitor starvation, not only throughput."
  context: operations
  certainty: strong
  rationale: "The excluded contender is the arbitration failure that surfaces late."
