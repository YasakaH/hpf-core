# Dataset Manifest v1

## Provenance Metadata

dataset_version: v1
core_version: "HPF v2 CORE — 27 files with behavioural lifecycle"
core_commit: "2026-07-27 — orchestration-vs-implementation separation complete"
generated_at: 2026-07-27T17:37:00Z
persona_count: 5
evaluation_count: 5
evaluations_processed: 5
metrics_version: 1
quality_gate_version: 1
dataset_schema_version: 1

## CORE Baseline State

### Files (27 total)
- PLANNING_FRAMEWORK.md
- DECISION_FRAMEWORK.md
- UNCERTAINTY_HANDLING.md
- VERIFICATION_PATTERNS.md
- CONTINUOUS_IMPROVEMENT.md
- EXECUTION_WORKFLOW.md
- ARCHITECTURE_PRINCIPLES.md
- BASE_PERSONALITY.md
- CAPABILITY_REGISTRY.md
- CONFLICT_RESOLUTION_POLICY.md
- CONSTITUTION.md
- ENGINEERING_PRINCIPLES.md
- ESCALATION_POLICY.md
- EVALUATION.md
- EVOLUTION_ENGINE.md
- OBSERVABILITY.md
- ORCHESTRATION_POLICY.md
- OUTPUT_STANDARD.md
- PERSONALITY_CREATION_GUIDE.md
- PERSONALITY_SCHEMA.md
- PRIORITIZATION_FRAMEWORK.md
- QUALITY_GATES.md
- QUALITY_STANDARDS.md
- REVIEW_FRAMEWORK.md
- SKILL_CREATION_GUIDE.md
- SKILL_SELECTION_POLICY.md
- THINKING_MODELS.md

### Behavioural Lifecycle
UNDERSTAND → PLAN → VALIDATE → EXECUTE → VERIFY → REFLECT

### Review Taxonomy
- Architecture (duplicate responsibility, boundary violation)
- Behaviour (missing capability, implicit behaviour)
- Evidence (weak support, unsupported claims)
- Usability (communication issue, implementation issue)

## Personas Evaluated

| Persona | Domain | Evaluations | Status |
|---------|--------|-------------|--------|
| Principal Engineer | engineering | 1 | Template filled |
| Staff Engineer | engineering | 1 | Template filled |
| Product Manager | product | 1 | Template filled |
| UX Designer | design | 1 | Template filled |
| Security Engineer | security | 1 | Template filled |

## Dataset Schema v1

### Validation Log Fields
- persona: string
- domain: string
- date: YYYY-MM-DD
- lifecycle_stages: [Understand, Plan, Validate, Execute, Verify, Reflect]
- capabilities_referenced: [PLANNING_FRAMEWORK, DECISION_FRAMEWORK, UNCERTAINTY_HANDLING, VERIFICATION_PATTERNS, EXECUTION_WORKFLOW, CONTINUOUS_IMPROVEMENT]
- friction_points: [hesitation, additional_guidance, repeated_failure, missing_document]
- performance_bottlenecks: [stage_effort, most_used_capability, least_used_capability]
- classification: [Architecture, Behaviour, Evidence, Usability]
- resolution: [None, Refine_doc, Add_capability, Architectural_change]

### Metrics Schema v1
- capability_usage: {capability: count}
- lifecycle_stage_usage: {stage: count}
- failure_modes: [{persona, evaluation, friction}]
- taxonomy_classification: {category: count}

### Quality Gates v1
- Coverage: every lifecycle stage exercised
- Persona Diversity: all planned personas evaluated
- Scenario Diversity: multiple task types
- Evidence Quality: logs completed
- Pattern Confidence: recurring findings across evaluations

## Schema Stability Policy

Changes to schema require:
1. Version bump (v1 → v2)
2. Documentation update
3. Backward compatibility note
4. Migration guide if breaking change

## Next Dataset Version (v2)

Target: 15+ evaluations with recurring patterns identified

---

**Manifest generated:** 2026-07-27  
**Next review:** After collecting 15+ evaluations