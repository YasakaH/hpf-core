# Watchdog Timer

## Identity
- id: watchdog-timer
- type: pattern
- title: Watchdog Timer
- tags: [real-time systems, watchdog, failure detection, timeout, reset]
- entities: [watchdog timer, timeout, reset, stall detection, heartbeat]
- concepts: [real-time-system, hard-vs-soft-real-time, incident-response, health-check-pattern, retry-pattern]

## Claims
- claim: "A watchdog timer is a failure-detection pattern — a timing sentinel that detects when a system stops making progress."
  certainty: high
  evidence: Embedded systems practice
  scope: cross-domain
- claim: "The watchdog detects stalls by deadline, not by inspection — a bounded expectation of progress is the detection mechanism."
  certainty: high
  evidence: Embedded systems practice
  scope: cross-domain
- claim: "A watchdog is a pattern with timeout constraints and reset discipline — the detection bound is a constraint, not a construct."
  certainty: high
  evidence: Cross-domain comparison (pattern resolutions 009-011)
  scope: cross-domain
- claim: "Watchdog detection is the temporal form of health checking — a bounded liveness expectation, analogous to health-check-pattern."
  certainty: high
  evidence: Cross-domain comparison (health-check-pattern)
  scope: cross-domain
- claim: "The watchdog's value is bounded reaction time — detection without a bounded response is a false promise."
  certainty: high
  evidence: Cross-domain comparison (incident-response 007)
  scope: cross-domain

## Relationships
- concept: real-time-system
  relationship: guards
  description: "A watchdog timer guards the real-time system — detection of stall is the protection."
- concept: hard-vs-soft-real-time
  relationship: enforces
  description: "A watchdog timer enforces the hard-vs-soft posture — the miss detection is the mechanism."
- concept: incident-response
  relationship: analogous_to
  description: "A watchdog timer is analogous to incident response — bounded reaction to failure — the Cycle 007 cross-domain link."
- concept: health-check-pattern
  relationship: analogous_to
  description: "A watchdog timer is analogous to health-check patterns — bounded liveness expectations — the cross-domain link."
- concept: retry-pattern
  relationship: complements
  description: "A watchdog timer complements the retry pattern — detection pairs with recovery."

## Tradeoffs
- dimension: timeout_length_vs_false_triggers
  options:
    short_timeout:
      value: fast_detection
      rationale: "Short timeouts detect fast but risk false triggers."
    long_timeout:
      value: reliability
      rationale: "Long timeouts avoid false triggers but delay detection."
  importance: high
- dimension: watchdog_scope_vs_overhead
  options:
    per_component:
      value: granularity
      rationale: "Per-component watchdogs localize but add overhead."
    system_wide:
      value: simplicity
      rationale: "System-wide watchdogs are simple but coarse."
  importance: medium

## Failure Modes
- name: false_trigger
  description: "The watchdog fires when the system is healthy — a false positive stalls or resets normal operation."
  likelihood: medium
  observable_evidence: "Spurious resets; unnecessary stalls; system restart cycles"
  detection: "Trigger analysis; timeout calibration review"
  recovery: "Calibrate the timeout; add health confirmation"
  retryable: true
- name: missed_stall
  description: "The watchdog fails to detect a real stall — the sentinel is defeated by reset discipline abuse."
  likelihood: medium
  observable_evidence: "Undetected stalls; heartbeat resetting despite no progress"
  detection: "Reset discipline audit; liveness review"
  recovery: "Separate reset from progress; harden the discipline"
  retryable: true
- name: reset_abuse
  description: "The reset path becomes a progress signal — a stalled task resets its own watchdog to avoid detection."
  likelihood: medium
  observable_evidence: "Frequent resets; no progress yet no trigger"
  detection: "Reset monitoring; discipline review"
  recovery: "Require independent progress; enforce reset separation"
  retryable: true

## Observations
- observation: "The watchdog is a deadline on progress — a validity condition on liveness, exactly the Tier 1 resolution."
  confidence: high
  source: Cross-domain comparison (deadline as validity condition, Tier 1)
- observation: "Detection is the temporal health check — the pattern carries the liveness expectation without a construct."
  confidence: high
  source: Cross-domain comparison (health-check-pattern)
- observation: "The reset discipline is the watchdog's weak point — abuse defeats the sentinel."
  confidence: high
  source: Embedded systems incident analyses

## Constraints
- constraint: "The watchdog timeout is a validity condition on progress — a system that exceeds it is presumed stalled."
  type: invariant
  scope: cross-domain
- constraint: "Reset must be independent of progress — a task must not reset its own watchdog."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Separate the reset signal from the progress signal."
  rationale: "Reset abuse defeats the sentinel."
  evidence_level: high
- heuristic: "Calibrate timeouts against real worst-case progress."
  rationale: "False triggers are calibration errors."
  evidence_level: high

## Recommendations
- recommendation: "Model the watchdog as a pattern with timeout constraints."
  context: modelling
  certainty: strong
  rationale: "Detection is a bound on liveness, expressed as a constraint."
- recommendation: "Enforce reset independence."
  context: engineering
  certainty: strong
  rationale: "A self-resetting watchdog is a false promise."
- recommendation: "Pair detection with a bounded response."
  context: engineering
  certainty: strong
  rationale: "Detection without response is a half-guarantee."
