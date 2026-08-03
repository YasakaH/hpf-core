# Actuation

## Identity
- id: actuation
- type: concept
- title: Actuation
- tags: [actuation, actuators, physical action, command, idempotency]
- entities: [actuator, command, physical effect, actuation loop]
- concepts: [cyber-physical-system, physical-state, idempotency, retry-pattern, real-time-system]

## Claims
- claim: "Actuation is the action end of the loop — decisions become physical commands that change the world."
  certainty: high
  evidence: Robotics and control practice
  scope: cross-domain
- claim: "An actuator command is the consequence of a decision about a belief — action under an incomplete world model, never under direct knowledge."
  certainty: high
  evidence: State estimation theory (P6 action under incomplete model)
  scope: cross-domain
- claim: "Repeated physical commands are not harmless — actuation inherits the idempotency discipline of distributed systems."
  certainty: high
  evidence: Cross-domain comparison (idempotency, retry-pattern 006)
  scope: cross-domain
- claim: "Actuation failure is physical — the consequence is in the world, and the failure mode must carry its physical effect."
  certainty: high
  evidence: Cyber-physical incident analyses (P8)
  scope: cross-domain
- claim: "The Epistemic Chain closes at actuation — reality acts back on the next observation, making the loop the unit of knowledge, not the object."
  certainty: high
  evidence: Epistemic Chain watch (Cycle 012 pre-registration)
  scope: cross-domain

## Relationships
- concept: cyber-physical-system
  relationship: serves
  description: "Actuation serves the cyber-physical system — the physical consequence of decisions."
- concept: physical-state
  relationship: changes
  description: "Actuation changes physical state — the decision's action on the represented world."
- concept: idempotency
  relationship: analogous_to
  description: "Actuation is analogous to idempotency — repeated commands must be safe — the distributed-systems cross-domain link."
- concept: retry-pattern
  relationship: mitigated_by
  description: "Actuation failure is mitigated by retry — under idempotency discipline — the Cycle 006 cross-domain link."
- concept: real-time-system
  relationship: executed_under
  description: "Actuation is executed under real-time constraints — late commands are invalid — the Cycle 011 cross-domain link."

## Tradeoffs
- dimension: responsiveness_vs_safety
  options:
    immediate_action:
      value: responsiveness
      rationale: "Immediate action reacts at physical speed."
    verified_action:
      value: safety
      rationale: "Verified action checks before acting on belief."
  importance: high
- dimension: precision_vs_power
  options:
    precise_actuation:
      value: accuracy
      rationale: "Precise commands act with fine control."
    powerful_actuation:
      value: effect_margin
      rationale: "Powerful commands overcome disturbances."
  importance: medium

## Failure Modes
- name: actuation_failure
  description: "A command is not applied to the world — the decision has no physical consequence."
  likelihood: medium
  observable_evidence: "No effect despite command; actuator error; mismatch between commanded and actual state"
  detection: "Actuator feedback; state divergence; effect monitoring"
  recovery: "Retry with idempotency discipline; switch actuation path; enter safe state"
  retryable: true
- name: saturation
  description: "The actuator is at its physical limit — the command exceeds what the world permits, and further demand has no effect."
  likelihood: medium
  observable_evidence: "Command/effect divergence at the limit; demand beyond capacity; degraded tracking"
  detection: "Saturation monitoring; command/effect comparison; limit checks"
  recovery: "Reduce demand; accept degraded response; re-plan within the envelope"
  retryable: true
- name: duplicate_actuation
  description: "A command is applied more than once — retry without idempotency turns a recovery into a physical hazard."
  likelihood: medium
  observable_evidence: "Repeated physical effect; double application; unintended motion"
  detection: "Command tracking; idempotency checks; effect cross-verification"
  recovery: "Idempotent command design; deduplication; verify-then-apply"
  retryable: false

## Observations
- observation: "Actuation is where action meets the world — the same action structure as retries and compensating controls, with physical consequence."
  confidence: high
  source: Cross-domain comparison (006 corpus)
- observation: "The actuator is the far end of the Epistemic Chain — action exits at actuation, and the next sensing closes the loop."
  confidence: medium
  source: Epistemic Chain watch (Cycle 012 pre-registration)
- observation: "Duplicate actuation is the physical form of the retry hazard — idempotency discipline is not optional in the physical world."
  confidence: high
  source: Cyber-physical incident analyses
- observation: "Every actuation is an action on belief — the epistemic gap is present at the moment of action, not only at estimation."
  confidence: high
  source: State estimation theory (P6)

## Constraints
- constraint: "An actuator command is valid only under its timing and idempotency conditions — duplicate or late actuation is a failure."
  type: invariant
  scope: cross-domain
- constraint: "Action is taken on belief, never on direct knowledge — the epistemic gap is closed by verification, not eliminated."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Design commands to be idempotent before relying on retry."
  rationale: "Retry is safe only when repetition is safe — the physical world does not forgive duplicates."
  evidence_level: high
- heuristic: "Verify effect, not just command."
  rationale: "A command is a claim about intended effect; the world's response is the evidence."
  evidence_level: high

## Recommendations
- recommendation: "Represent actuation as the action destination of the decision — a command is a consequence, not a construct."
  context: modelling
  certainty: strong
  rationale: "Actuation is the far end of an existing chain; the decision structure already carries it."
- recommendation: "Apply the idempotency discipline to every physical command."
  context: engineering
  certainty: strong
  rationale: "Retry without idempotency converts recovery into hazard."
- recommendation: "Close the loop with verification — treat the world's response as the evidence for the command."
  context: operations
  certainty: strong
  rationale: "The epistemic gap ends where observation meets action again."
