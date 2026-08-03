# Index Selection

## Identity
- id: index-selection
- type: decision
- title: Index Selection
- tags: [databases, indexes, index selection, write amplification, selectivity, workload]
- entities: [index selection, index, selectivity, write amplification, workload, access path]
- concepts: [database-indexing, query-planning, query-optimization, relational-model, schema-design]

## Claims
- claim: "Index selection is the decision of which indexes to maintain — every index trades read speed against write cost and storage."
  certainty: high
  evidence: Database engineering practice
  scope: cross-domain
- claim: "The right index set is workload-dependent — queries define value; unused indexes are pure cost."
  certainty: high
  evidence: Database practice, index tuning experience
  scope: cross-domain
- claim: "Index value is a function of selectivity — an index that rarely narrows the result set is not worth its write tax."
  certainty: high
  evidence: Query optimization theory and practice
  scope: cross-domain
- claim: "Index selection is an ongoing decision — workload change invalidates index decisions as it invalidates schema decisions."
  certainty: high
  evidence: Database operations practice
  scope: cross-domain
- claim: "Index governance is redundancy governance — every index is a maintained copy, and unmaintained copies decay."
  certainty: high
  evidence: Database practice, incident analyses
  scope: cross-domain

## Relationships
- concept: database-indexing
  relationship: selects_among
  description: "Index selection selects among database indexing structures — which index types to maintain."
- concept: query-planning
  relationship: constrains
  description: "Index selection constrains query planning — available indexes bound the planner's access paths."
- concept: query-optimization
  relationship: shaped_by
  description: "Index selection shapes query optimization — the index set determines achievable plans."
- concept: relational-model
  relationship: serves
  description: "Index selection serves the relational model — indexes accelerate relational operations without changing semantics."
- concept: schema-design
  relationship: influenced_by
  description: "Index selection is influenced by schema design — key structure determines natural index opportunities."

## Tradeoffs
- dimension: read_speed_vs_write_cost
  options:
    rich_indexing:
      value: query_speed
      rationale: "Many indexes accelerate reads but tax every write."
    lean_indexing:
      value: write_efficiency
      rationale: "Few indexes keep writes fast but slow reads."
  importance: high
- dimension: coverage_vs_governance
  options:
    broad_coverage:
      value: query_freedom
      rationale: "Broad coverage serves many query shapes but multiplies maintenance."
    narrow_coverage:
      value: maintainability
      rationale: "Narrow coverage is maintainable but leaves queries slow."
  importance: high

## Failure Modes
- name: index_bloat
  description: "Indexes accumulate without governance — dead indexes tax writes and storage indefinitely."
  likelihood: high
  observable_evidence: "Write slowdowns; storage growth; indexes never used in plans"
  detection: "Index usage analysis; write-cost attribution; unused-index reports"
  recovery: "Drop unused indexes; establish index lifecycle; monitor usage"
  retryable: true
- name: missing_index
  description: "A workload lacks the index it needs — queries scan instead of seek, and performance degrades silently."
  likelihood: medium
  observable_evidence: "Table scans on hot paths; slow lookups; planner hints about missing indexes"
  detection: "Missing-index suggestions; plan analysis; workload profiling"
  recovery: "Add the index; verify the plan change; monitor the write tax"
  retryable: true
- name: index_deceit
  description: "An index is assumed faster than it is — the optimizer or the operator trusts a structure whose selectivity is poor."
  likelihood: medium
  observable_evidence: "Indexed queries no faster than scans; low selectivity usage; plan surprises"
  detection: "Selectivity analysis; access-path review; cost comparison"
  recovery: "Replace with better structures; adjust statistics; drop and rebuild"
  retryable: true

## Observations
- observation: "Unused indexes are the most common silent cost in production databases."
  confidence: high
  source: Database operations practice
- observation: "Index decisions expire — workload drift invalidates them on a schedule nobody tracks."
  confidence: high
  source: Database engineering experience
- observation: "Index selection is a decision process with an evidence channel (usage data) that most teams do not feed."
  confidence: high
  source: Database practice

## Constraints
- constraint: "Every index is a maintained copy — an index without governance is redundancy without a control."
  type: invariant
  scope: cross-domain
- constraint: "Index decisions are workload-scoped — an index justified by one workload is unjustified by another."
  type: invariant
  scope: cross-domain

## Decision Factors
- factor: query_workload
  question: "Which queries does this index actually serve, and how often?"
  supporting: "Workload evidence justifies index investment."
  contradictory: "Unmeasured workloads justify nothing."
  weight: high
- factor: write_amplification
  question: "What write cost does this index impose per write?"
  supporting: "Low write tax makes indexes cheap to maintain."
  contradictory: "High write tax makes indexes expensive on hot paths."
  weight: high
- factor: storage_cost
  question: "What does this index cost in storage and memory?"
  supporting: "Cheap storage tolerates extra indexes."
  contradictory: "Storage constraints force index discipline."
  weight: medium
- factor: selectivity
  question: "How much does this index narrow the result set?"
  supporting: "High selectivity justifies index investment."
  contradictory: "Low selectivity indexes are write taxes without benefit."
  weight: high

## Heuristics
- heuristic: "Justify every index with usage evidence."
  rationale: "Unjustified indexes are the standard silent cost."
  evidence_level: high
- heuristic: "Review index sets when workloads change."
  rationale: "Decisions expire with the workload that justified them."
  evidence_level: high

## Recommendations
- recommendation: "Measure index usage and drop what is unused."
  context: operations
  certainty: strong
  rationale: "Dead indexes are permanent taxes."
- recommendation: "Base index selection on workload evidence, not intuition."
  context: design
  certainty: strong
  rationale: "Evidence-driven selection is auditable; intuition is archaeology."
- recommendation: "Govern indexes with the same lifecycle as schema."
  context: governance
  certainty: strong
  rationale: "Indexes are schema-adjacent decisions with the same expiry behavior."
