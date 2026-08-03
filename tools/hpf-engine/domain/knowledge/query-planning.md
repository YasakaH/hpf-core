# Query Planning

## Identity
- id: query-planning
- type: decision
- title: Query Planning
- tags: [databases, query planning, optimizer, join order, statistics, cost model, execution plan]
- entities: [query planning, execution plan, join order, cost model, statistics, access path]
- concepts: [relational-model, query-optimization, index-selection, database-indexing, equivalence-checking]

## Claims
- claim: "Query planning is the decision of how to execute a declarative query — the planner chooses join order, access paths, and algorithms under a cost model."
  certainty: high
  evidence: Query optimization practice and literature
  scope: cross-domain
- claim: "Plan quality is bounded by statistics quality — the planner decides on evidence, and unreliable statistics produce unreliable plans."
  certainty: high
  evidence: Query optimizer engineering practice
  scope: cross-domain
- claim: "Planner choices trade plan quality against planning cost — exhaustive search is impossible for complex queries."
  certainty: high
  evidence: Query optimization theory and practice
  scope: cross-domain
- claim: "The planner's output is a recommendation, not a guarantee — plans are hypotheses about cost that runtime evidence can falsify."
  certainty: high
  evidence: Database practice, plan-analysis experience
  scope: cross-domain
- claim: "Plan stability is a correctness-adjacent property — plan changes alter performance without altering results, and destabilized plans become operational incidents."
  certainty: high
  evidence: Database operations practice
  scope: cross-domain

## Relationships
- concept: relational-model
  relationship: operates_upon
  description: "Query planning operates upon the relational model — plans execute relational operations."
- concept: query-optimization
  relationship: performed_by
  description: "Query planning is performed by query optimization — the optimizer produces the plan."
- concept: index-selection
  relationship: dependent_on
  description: "Query planning is dependent on index selection — available indexes bound the access paths the planner can choose."
- concept: database-indexing
  relationship: bounded_by
  description: "Query planning is bounded by database indexing — index structure determines access path cost."
- concept: equivalence-checking
  relationship: bounded_by
  description: "Query planning is bounded by equivalence checking — every planned execution must return the query's result relation."

## Tradeoffs
- dimension: planning_depth_vs_planning_cost
  options:
    exhaustive_search:
      value: plan_quality
      rationale: "Deep search finds better plans but costs compile time on every query."
    heuristic_planning:
      value: speed
      rationale: "Heuristic planning is fast but settles for suboptimal plans."
  importance: high
- dimension: plan_stability_vs_adaptivity
  options:
    stable_plans:
      value: predictability
      rationale: "Stable plans make performance predictable but miss better plans as data changes."
    adaptive_plans:
      value: optimality
      rationale: "Adaptive planning tracks data changes but destabilizes performance."
  importance: high

## Failure Modes
- name: bad_plan
  description: "The planner selects an execution plan whose cost is far from optimal — a query runs orders of magnitude slower than it should."
  likelihood: medium
  observable_evidence: "Slow queries; plan differences from expectation; cost-model mismatches"
  detection: "Plan inspection; cost-vs-actual comparison; query regression monitoring"
  recovery: "Update statistics; adjust cost model; use plan hints or rewrites"
  retryable: true
- name: stale_statistics
  description: "The planner decides on outdated statistics — the evidence base no longer matches the data distribution."
  likelihood: medium
  observable_evidence: "Plan regressions after data changes; bad joins on skewed data; periodic slowdown patterns"
  detection: "Statistics freshness monitoring; plan regression tracking; histogram staleness checks"
  recovery: "Refresh statistics; re-analyze; verify plan recovery"
  retryable: true
- name: plan_destabilization
  description: "Plans change between runs — performance oscillates without data changes, producing unpredictable incidents."
  likelihood: medium
  observable_evidence: "Alternating fast/slow executions; plan diffs across runs; incident patterns tied to plan flips"
  detection: "Plan stability monitoring; plan cache analysis; diff tracking"
  recovery: "Pin plans where stable; tune statistics; stabilize the cost model"
  retryable: true

## Observations
- observation: "Planner decisions are only as good as their evidence — statistics quality is the planner's data quality."
  confidence: high
  source: Query optimizer engineering
- observation: "Most query-performance incidents trace to plan choice, not to the database's intrinsic speed."
  confidence: high
  source: Database operations analyses
- observation: "Plans are falsifiable hypotheses — runtime evidence routinely overrides planner assumptions."
  confidence: high
  source: Database practice

## Constraints
- constraint: "Plan choice is bounded by correctness — no plan may return a different result than the query's semantics require."
  type: invariant
  scope: cross-domain
- constraint: "Plan decisions are bounded by evidence — decisions without statistics are guesses."
  type: invariant
  scope: cross-domain

## Decision Factors
- factor: statistics_reliability
  question: "How trustworthy are the statistics describing the data this plan will process?"
  supporting: "Reliable statistics produce reliable plans."
  contradictory: "Stale or skewed statistics produce disastrous plans."
  weight: high
- factor: join_order_freedom
  question: "How much freedom does the planner have in ordering joins and choosing access paths?"
  supporting: "Freedom enables better plans."
  contradictory: "Freedom plus weak evidence produces unstable plans."
  weight: high
- factor: cost_model_fidelity
  question: "How well does the cost model predict actual execution cost?"
  supporting: "Faithful models make planner choices trustworthy."
  contradictory: "Model mismatches make every plan a gamble."
  weight: high
- factor: plan_stability
  question: "How important is performance predictability for this workload?"
  supporting: "Stability protects operational predictability."
  contradictory: "Pinned plans block adaptation to data change."
  weight: medium

## Heuristics
- heuristic: "Treat the planner as a decision maker with evidence needs."
  rationale: "Planning quality is statistics quality."
  evidence_level: high
- heuristic: "Inspect plans when performance surprises."
  rationale: "The plan is where performance incidents are visible first."
  evidence_level: high

## Recommendations
- recommendation: "Maintain statistics freshness as an operational duty."
  context: operations
  certainty: strong
  rationale: "The planner's evidence is the database's data quality."
- recommendation: "Monitor plan stability and treat flips as incidents."
  context: operations
  certainty: strong
  rationale: "Destabilized plans are the hidden cause of performance incidents."
- recommendation: "Verify plans against runtime evidence periodically."
  context: governance
  certainty: strong
  rationale: "Cost models drift; verification catches the drift."
