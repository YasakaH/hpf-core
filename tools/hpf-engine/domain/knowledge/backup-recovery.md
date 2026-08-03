# Backup Recovery

## Identity
- id: backup-recovery
- type: pattern
- title: Backup Recovery
- tags: [databases, backup, recovery, RPO, RTO, restore, disaster recovery]
- entities: [backup, recovery, RPO, RTO, restore, backup validity]
- concepts: [data-integrity, atomicity, schema-migration, data-governance, build-systems]

## Claims
- claim: "Backup recovery is the discipline of restoring data to a defined point after loss — a recovery capability, not a storage practice."
  certainty: high
  evidence: Database operations practice
  scope: cross-domain
- claim: "RPO and RTO are the recovery contract — how much data loss is acceptable and how fast recovery must be."
  certainty: high
  evidence: Recovery planning practice
  scope: cross-domain
- claim: "Backup validity is derivation — a backup is valid if it faithfully represents the source at its snapshot point."
  certainty: high
  evidence: Backup practice, recovery incident analyses
  scope: cross-domain
- claim: "An untested backup is a claim — restorability is only established by actually restoring."
  certainty: high
  evidence: Recovery incident analyses
  scope: cross-domain
- claim: "Recovery is the proof of the system's failure tolerance — every other guarantee is exercised at recovery time."
  certainty: high
  evidence: Operations practice, incident analyses
  scope: cross-domain

## Relationships
- concept: data-integrity
  relationship: restores
  description: "Backup recovery restores data integrity — recovery re-establishes the integrity state."
- concept: atomicity
  relationship: supported_by
  description: "Backup recovery is supported by atomicity — logs enable point-in-time recovery."
- concept: schema-migration
  relationship: guards
  description: "Backup recovery guards schema migration — migration failures are recovered by restore."
- concept: data-governance
  relationship: governed_by
  description: "Backup recovery is governed by data governance — retention and access requirements bound backup policy."
- concept: build-systems
  relationship: analogous_to
  description: "Backup validity is analogous to artifact validity — both are derivation claims — the cross-domain link to the Cycle 009 corpus."

## Tradeoffs
- dimension: recovery_speed_vs_cost
  options:
    frequent_full_backups:
      value: fast_recovery
      rationale: "Frequent fulls restore fast but cost storage and bandwidth."
    incremental_strategy:
      value: efficiency
      rationale: "Incremental backups are cheap but slow restores through chains."
  importance: high
- dimension: rpo_strictness_vs_operational_overhead
  options:
    tight_rpo:
      value: data_safety
      rationale: "Tight RPO minimizes loss but demands continuous or frequent capture."
    loose_rpo:
      value: simplicity
      rationale: "Loose RPO is simple but accepts more data loss."
  importance: high

## Failure Modes
- name: unverified_backup
  description: "The backup cannot restore — corruption, incomplete capture, or tooling failure makes the backup a false promise."
  likelihood: medium
  observable_evidence: "Restore failures; corrupt archives; missing data after restore"
  detection: "Restore rehearsals; backup integrity checks; validation restores"
  recovery: "Repair backup pipeline; restore from older verified backup; re-verify"
  retryable: true
- name: rpo_violation
  description: "Recovery loses more data than the contract allows — the restored state is older than the RPO."
  likelihood: medium
  observable_evidence: "Data loss beyond policy; recovery point older than contract; missing recent work"
  detection: "Recovery timeline analysis; RPO conformance checks"
  recovery: "Tighten capture frequency; repair pipeline gaps; recover from logs"
  retryable: true
- name: restore_failure_at_incident
  description: "Recovery fails exactly when needed — the only time backups matter."
  likelihood: medium
  observable_evidence: "Failed restores during incidents; environment mismatches; procedure gaps"
  detection: "Recovery drills; runbook verification; environment rehearsal"
  recovery: "Fall back to secondary backups; fix environment; document the gap"
  retryable: true

## Observations
- observation: "Backups are a claim until a restore proves them — rehearsal is the only verification."
  confidence: high
  source: Recovery incident analyses
- observation: "Recovery failures cluster at the moment of need — the least-tested path is the most critical."
  confidence: high
  source: Operations incident analyses
- observation: "Backup validity is the artifact-validity pattern applied to data — a derivation claim with stated conditions."
  confidence: high
  source: Cross-domain comparison (Cycle 009)

## Constraints
- constraint: "Backup validity is a derivation claim — a backup is valid only if it faithfully represents its source at snapshot."
  type: invariant
  scope: cross-domain
- constraint: "Recovery must meet the stated contract — RPO/RTO violations are operational failures, not details."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Rehearse restores on a schedule."
  rationale: "The capability is only proven by use."
  evidence_level: high
- heuristic: "Treat RPO/RTO as a contract with owners."
  rationale: "Unowned recovery contracts expire quietly."
  evidence_level: high

## Recommendations
- recommendation: "Verify restorability continuously, not at incident time."
  context: operations
  certainty: strong
  rationale: "An unverified backup is a false promise at the worst moment."
- recommendation: "Define RPO/RTO explicitly and review them as the contract changes."
  context: governance
  certainty: strong
  rationale: "The contract must match the data's value."
- recommendation: "Practice incident-time recovery in realistic environments."
  context: preparedness
  certainty: strong
  rationale: "Environment differences are where rehearsed recovery fails."
