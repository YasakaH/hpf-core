# Data Governance

## Identity
- id: data-governance
- type: decision
- title: Data Governance
- tags: [databases, governance, retention, access, lineage, compliance]
- entities: [data governance, retention policy, access scope, lineage, ownership]
- concepts: [data-integrity, schema-migration, backup-recovery, training-data]
- decision-factors:
  - retention_requirement
  - access_scope
  - lineage_traceability
  - compliance_cost

## Claims
- claim: "Data governance is the decision structure for data value and risk — what is kept, who sees it, and how it is traced."
  certainty: high
  evidence: Data governance practice
  scope: cross-domain
- claim: "Retention is a policy decision — what data is kept and for how long, balancing value against risk and cost."
  certainty: high
  evidence: Compliance and data management practice
  scope: cross-domain
- claim: "Access scope is a security boundary decision — who may read and modify data, expressed as constraints."
  certainty: high
  evidence: Access control practice
  scope: cross-domain
- claim: "Lineage is an observation — the derivation chain of data — not a new primitive; it was resolved in Cycle 008 for training-data."
  certainty: high
  evidence: Cross-domain composition (Cycle 008 corpus)
  scope: cross-domain
- claim: "Governance is a decision object, not a concept — it varies with retention requirement, access scope, lineage traceability, and compliance cost."
  certainty: high
  evidence: Cross-domain comparison (all decision objects 007-010)
  scope: cross-domain

## Relationships
- concept: data-integrity
  relationship: protects
  description: "Data governance protects data integrity — policy constraints prevent corruption and misuse."
- concept: schema-migration
  relationship: constrains
  description: "Data governance constrains schema migration — retention and access rules bound migration design."
- concept: backup-recovery
  relationship: directs
  description: "Data governance directs backup recovery — retention requirements bound backup policy."
- concept: training-data
  relationship: analogous_to
  description: "Data governance is analogous to training-data governance — lineage as observation plus constraint, the Cycle 008 cross-domain link."

## Tradeoffs
- dimension: retention_breadth_vs_risk
  options:
    keep_everything:
      value: analytic_freedom
      rationale: "Keeping everything preserves future options but multiplies risk surface."
    keep_minimum:
      value: risk_reduction
      rationale: "Keeping minimum reduces risk but destroys future options."
  importance: high
- dimension: access_openness_vs_security
  options:
    open_access:
      value: productivity
      rationale: "Open access enables analysis but expands the breach surface."
    restricted_access:
      value: security
      rationale: "Restricted access is safer but taxes every request with friction."
  importance: high
- dimension: lineage_depth_vs_cost
  options:
    full_lineage:
      value: traceability
      rationale: "Full lineage proves derivation chains but costs instrumentation at every step."
    minimal_lineage:
      value: cost
      rationale: "Minimal lineage is cheap but leaves provenance claims unanswerable."
  importance: medium

## Failure Modes
- name: shadow_data
  description: "Data exists outside governance — copies and pipelines bypass retention, access, and lineage controls."
  likelihood: high
  observable_evidence: "Copies without lineage; ungoverned exports; retention gaps in derived stores"
  detection: "Data inventory audits; lineage completeness checks; copy discovery"
  recovery: "Fold shadow data into governance; retire ungoverned copies"
  retryable: true
- name: lineage_gap
  description: "Derivation cannot be traced — a governance or compliance question finds no answer."
  likelihood: medium
  observable_evidence: "Unanswerable provenance questions; audit failures; untraceable data quality issues"
  detection: "Lineage spot checks; audit rehearsal; derivation-chain review"
  recovery: "Instrument the gaps; document known lineage limits"
  retryable: true
- name: policy_decay
  description: "Governance policy becomes stale — the rules no longer match the data, the value, or the risk."
  likelihood: medium
  observable_evidence: "Policies contradicted by practice; unreviewed retention schedules; expired scope decisions"
  detection: "Policy audits; ownership review; compliance checks"
  recovery: "Re-decide the decision factors; refresh policies; re-map to reality"
  retryable: true

## Observations
- observation: "Lineage reappears exactly as Cycle 008 resolved it — observation plus constraint, never a primitive."
  confidence: high
  source: Cross-domain composition (Cycle 008)
- observation: "Governance failures are usually shadow data — the governed system is fine; the copies are not."
  confidence: high
  source: Data governance practice
- observation: "The four decision factors recur across domains — governance is structurally identical to every other decision object."
  confidence: high
  source: Cross-domain comparison (decision objects 007-010)

## Constraints
- constraint: "Governance decisions are bound by stated factors — retention, access, lineage, and cost requirements are the validity conditions."
  type: invariant
  scope: cross-domain
- constraint: "Lineage is an observation with a traceability obligation — a derivation chain must be answerable or its absence known."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Ask what is kept, who sees it, and how it is traced — the three governance questions."
  rationale: "The three questions cover retention, access, and lineage."
  evidence_level: high
- heuristic: "Review governance decisions on a schedule, like code."
  rationale: "Policy decays as data and risk change."
  evidence_level: high

## Recommendations
- recommendation: "Make governance a decided policy, not an accident of practice."
  context: governance
  certainty: strong
  rationale: "Ungoverned data is shadow data in progress."
- recommendation: "Track lineage as a first-class observation."
  context: operations
  certainty: strong
  rationale: "Lineage answers the questions compliance asks."
- recommendation: "Re-decide the four factors as the data changes."
  context: governance
  certainty: strong
  rationale: "A stale governance decision is a false confidence."
