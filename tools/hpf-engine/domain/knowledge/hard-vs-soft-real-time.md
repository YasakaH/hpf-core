# Hard vs Soft Real-Time

## Identity
- id: hard-vs-soft-real-time
- type: decision
- title: Hard vs Soft Real-Time
- tags: [real-time systems, hard real-time, soft real-time, timing posture, degradation]
- entities: [hard real-time, soft real-time, timing posture, degradation, miss consequence]
- concepts: [real-time-guarantee, deadline, scheduling-policy, debug-vs-release-modes, optimization-tradeoffs]
- decision-factors:
  - miss_consequence
  - timing_strictness
  - workload_variability
  - degradation_policy

## Claims
- claim: "Hard vs soft real-time is a behavioural decision — the choice of what a deadline miss means — not a property of the system."
  certainty: high
  evidence: Cross-domain comparison (mode-divergence pattern 009)
  scope: cross-domain
- claim: "Hard real-time treats a miss as a failure; soft real-time treats it as degradation — the same system can change posture by decision."
  certainty: high
  evidence: Real-time systems practice
  scope: cross-domain
- claim: "The decision is structurally identical to debug-vs-release-modes — a posture choice with distinct behaviour contracts — the Cycle 009 cross-domain link."
  certainty: high
  evidence: Cross-domain comparison (mode-divergence pattern 009)
  scope: cross-domain
- claim: "The posture decision carries four factors — miss_consequence, timing_strictness, workload_variability, and degradation_policy — the decision-object pattern at 4."
  certainty: high
  evidence: Cross-domain comparison (decision objects 007-011)
  scope: cross-domain
- claim: "Each posture is a distinct guarantee contract — hard and soft modes are different promises, and validation must be per-mode."
  certainty: high
  evidence: Cross-domain comparison (mode-divergence 009: per-mode validation)
  scope: cross-domain

## Relationships
- concept: real-time-guarantee
  relationship: decides
  description: "Hard vs soft real-time decides the real-time guarantee — the posture determines the contract."
- concept: deadline
  relationship: interprets
  description: "Hard vs soft real-time interprets the deadline — miss meaning depends on posture."
- concept: scheduling-policy
  relationship: informs
  description: "Hard vs soft real-time informs the scheduling policy — posture constrains policy choice."
- concept: debug-vs-release-modes
  relationship: analogous_to
  description: "Hard vs soft real-time is analogous to debug vs release modes — a posture decision with distinct behaviour contracts — the Cycle 009 cross-domain link."
- concept: optimization-tradeoffs
  relationship: analogous_to
  description: "Hard vs soft real-time is analogous to optimization tradeoffs — a performance posture decision — the Cycle 009 cross-domain link."

## Tradeoffs
- dimension: strictness_vs_adaptability
  options:
    hard_posture:
      value: correctness
      rationale: "Hard posture treats misses as failures — strong but rigid."
    soft_posture:
      value: adaptability
      rationale: "Soft posture tolerates degradation — flexible but weaker."
  importance: high
- dimension: validation_cost_vs_guarantee
  options:
    per_mode_validation:
      value: correctness
      rationale: "Per-mode validation is complete but doubles the cost."
    single_mode_validation:
      value: cost
      rationale: "Single-mode validation is cheap but misses mode-specific behaviour."
  importance: high

## Failure Modes
- name: posture_mismatch
  description: "The chosen posture contradicts the miss consequence — a hard system is operated soft, or vice versa."
  likelihood: medium
  observable_evidence: "Unexpected tolerance of misses; surprise failures; contract violations"
  detection: "Posture audits; consequence review"
  recovery: "Re-decide the posture; align operations"
  retryable: true
- name: silent_degradation
  description: "A soft system degrades without notice — degradation is invisible until it compounds."
  likelihood: medium
  observable_evidence: "Unreported degradation; cascading quality loss"
  detection: "Degradation monitoring; quality tracking"
  recovery: "Add degradation visibility; repair the silent path"
  retryable: true
- name: cross_mode_validation_gap
  description: "The system is validated in one posture only — mode-specific behaviour escapes testing."
  likelihood: medium
  observable_evidence: "Mode-only bugs; behaviour differences between modes"
  detection: "Per-mode test review; behaviour comparison"
  recovery: "Validate each mode; add mode-crossing tests"
  retryable: true

## Observations
- observation: "Posture is a decision, not a property — the same system chooses what a miss means."
  confidence: high
  source: Cross-domain comparison (mode-divergence 009)
- observation: "Hard and soft are distinct guarantee contracts — validation must be per-mode, exactly as debug/release required."
  confidence: high
  source: Cross-domain comparison (mode-divergence 009)
- observation: "The posture decision carries the four-factor pattern — miss_consequence anchors the choice."
  confidence: high
  source: Cross-domain comparison (decision objects 007-011)

## Constraints
- constraint: "The posture defines the miss meaning — a hard system's miss is a failure, a soft system's is degradation."
  type: invariant
  scope: cross-domain
- constraint: "Each posture's guarantee is valid under its own contract — cross-mode promises are invalid."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Decide the posture before the guarantees."
  rationale: "Miss meaning determines every contract downstream."
  evidence_level: high
- heuristic: "Validate each mode separately."
  rationale: "Mode-specific behaviour is the validation gap."
  evidence_level: high

## Recommendations
- recommendation: "Treat hard vs soft as a decision with stated factors."
  context: engineering
  certainty: strong
  rationale: "Posture is a decision; decisions need factors and re-decision."
- recommendation: "State the miss meaning explicitly with the contract."
  context: governance
  certainty: strong
  rationale: "An unstated miss meaning is an ambiguous guarantee."
- recommendation: "Validate per-mode."
  context: engineering
  certainty: strong
  rationale: "Each posture is a distinct program with a distinct contract."
