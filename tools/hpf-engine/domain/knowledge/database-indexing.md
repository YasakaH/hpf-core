# Database Indexing

## Identity
- id: database-indexing
- type: pattern
- title: Database Indexing
- tags: [databases, indexing, b-tree, hash index, access path, redundant structure]
- entities: [index, b-tree, hash index, access path, key ordering, maintained copy]
- concepts: [index-selection, query-planning, relational-model, schema-design, query-optimization]

## Claims
- claim: "An index is a maintained copy of data in a different ordering — a redundant structure that exists to accelerate access."
  certainty: high
  evidence: Database implementation practice and literature
  scope: cross-domain
- claim: "An index is a structure with a tradeoff contract — reads are accelerated at the price of write cost and storage."
  certainty: high
  evidence: Database engineering practice
  scope: cross-domain
- claim: "Index correctness is coherence — the index must reflect the data it indexes; incoherent indexes return wrong results."
  certainty: high
  evidence: Database implementation practice, incident analyses
  scope: cross-domain
- claim: "Index structures are access-path mechanisms, not knowledge types — a B-tree is an ordering discipline, not a new category of information."
  certainty: high
  evidence: Database theory and practice
  scope: cross-domain
- claim: "The right index structure is workload-shaped — range queries favor ordered structures; point lookups favor hashes."
  certainty: high
  evidence: Database practice, access-path research
  scope: cross-domain

## Relationships
- concept: index-selection
  relationship: selected_by
  description: "Database indexing structures are selected by index selection — which structures to maintain is a decision."
- concept: query-planning
  relationship: enables
  description: "Database indexing enables query planning — access paths are index-driven."
- concept: relational-model
  relationship: serves
  description: "Database indexing serves the relational model — indexes accelerate operations without changing semantics."
- concept: schema-design
  relationship: informed_by
  description: "Database indexing is informed by schema design — keys determine natural index opportunities."
- concept: query-optimization
  relationship: exploited_by
  description: "Database indexing is exploited by query optimization — rewrites unlock index-based access paths."

## Tradeoffs
- dimension: read_performance_vs_write_tax
  options:
    dense_indexing:
      value: read_speed
      rationale: "Dense indexes accelerate every read pattern but tax every write."
    sparse_indexing:
      value: write_speed
      rationale: "Sparse indexes keep writes cheap but leave reads slow."
  importance: high
- dimension: structure_specificity_vs_flexibility
  options:
    specialized_structures:
      value: workload_fit
      rationale: "Specialized structures fit narrow workloads perfectly."
    general_structures:
      value: adaptability
      rationale: "General structures serve varied workloads adequately."
  importance: medium

## Failure Modes
- name: index_incoherence
  description: "The index diverges from the data — reads through the index return stale or wrong results."
  likelihood: low
  observable_evidence: "Index reads differing from table reads; stale lookups after writes; rebuild fixing results"
  detection: "Coherence checks; index validation scans; read-vs-scan comparison"
  recovery: "Rebuild the index; fix the maintenance path; verify coherence"
  retryable: true
- name: index_bloat
  description: "The index grows without bound — fragmentation, dead entries, and over-insertion waste storage."
  likelihood: medium
  observable_evidence: "Storage growth; degraded performance; oversized index files"
  detection: "Index size monitoring; fragmentation analysis; bloat reports"
  recovery: "Rebuild or reorganize; adjust fill factors; prune dead entries"
  retryable: true
- name: stale_index_guidance
  description: "Optimizer statistics about the index are stale — access-path decisions are made on outdated structure information."
  likelihood: medium
  observable_evidence: "Plans ignoring good indexes; bad access-path choices; statistics warnings"
  detection: "Statistics freshness checks; plan analysis; index usage review"
  recovery: "Refresh statistics; re-analyze; verify plan improvement"
  retryable: true

## Observations
- observation: "Indexes are the purest example of redundancy with discipline — maintained copies with coherence obligations."
  confidence: high
  source: Database engineering practice
- observation: "Index incoherence is rare but catastrophic when it occurs — the silent-wrong-results class."
  confidence: high
  source: Database incident analyses
- observation: "Access-path structure shapes what optimizers can even consider — structure choice precedes plan quality."
  confidence: high
  source: Query optimization practice

## Constraints
- constraint: "An index must remain coherent with its data — divergence is a correctness failure, not a performance issue."
  type: invariant
  scope: cross-domain
- constraint: "Every index is a maintained copy — maintenance obligations are part of the structure's contract."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Match structure to workload shape."
  rationale: "Range-heavy and point-heavy workloads need different structures."
  evidence_level: high
- heuristic: "Treat index coherence as a correctness property."
  rationale: "Silent wrong results are the costliest failure class."
  evidence_level: high

## Recommendations
- recommendation: "Choose index structures by access-path demand."
  context: design
  certainty: strong
  rationale: "The workload defines the structure that serves it."
- recommendation: "Verify index coherence after maintenance events."
  context: operations
  certainty: strong
  rationale: "Rebuilds and maintenance are where coherence is lost."
- recommendation: "Monitor index bloat as a storage and performance signal."
  context: operations
  certainty: strong
  rationale: "Bloat is slow, cumulative, and invisible without monitoring."
