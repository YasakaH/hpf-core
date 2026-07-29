# Dataset Schema v1 (Frozen)

## Purpose

Define the stable schema for Operational Validation Dataset v1. Any changes require version bump to v2 and documentation of the change.

## Schema Definition

### 1. Validation Log Structure

**File:** `dataset-v1/evaluations/{persona}/{evaluation-id}.md`

**Required Fields:**
```markdown
## Persona Details
- **Domain:** [engineering/product/design/security]
- **Date:** [YYYY-MM-DD]
- **Persona ID:** [principal-engineer/staff-engineer/product-manager/ux-designer/security-engineer]

### Scenario Executed
**Task:** [What the persona was asked to do]
**Context:** [Relevant background]

### Lifecycle Stages Observed
- [ ] Understand
- [ ] Plan
- [ ] Validate
- [ ] Execute
- [ ] Verify
- [ ] Reflect

### Capability Documents Referenced
| Document | Purpose | Friction Level (1-5) | Notes |
|----------|---------|----------------------|-------|
| PLANNING_FRAMEWORK.md | Task decomposition, estimation |  |  |
| DECISION_FRAMEWORK.md | Option selection, prioritisation |  |  |
| UNCERTAINTY_HANDLING.md | Confidence calibration |  |  |
| VERIFICATION_PATTERNS.md | Correctness validation |  |  |
| CONTINUOUS_IMPROVEMENT.md | Adaptation and learning |  |  |
| EXECUTION_WORKFLOW.md | Orchestration |  |  |

### Observations
**Friction Points:**
- [ ] Hesitation at lifecycle stage: 
- [ ] Required additional guidance: 
- [ ] Repeated failure at stage: 
- [ ] Document not referenced but needed: 

**Performance Bottlenecks:**
- [ ] Stage consuming most reasoning effort: 
- [ ] Most-used capability document: 
- [ ] Least-used capability document: 

### Classification
| Finding | Classification | Resolution | Evidence |
|---------|----------------|------------|----------|
|  | Architecture / Behaviour / Evidence / Usability | None / Refine doc / Add capability / Architectural change |  |

### Next Steps
- [ ] Document refinement needed
- [ ] Candidate behavioural improvement
- [ ] Candidate architectural change
- [ ] No action required
```

### 2. Metrics Structure

**Files:**
- `dataset-v1/metrics/capability-usage.json`
- `dataset-v1/metrics/lifecycle-coverage.json`
- `dataset-v1/metrics/failure-modes.json`
- `dataset-v1/metrics/taxonomy-summary.json`

**Schema:**
```json
{
  "capability_usage": {
    "PLANNING_FRAMEWORK": 5,
    "DECISION_FRAMEWORK": 8,
    "UNCERTAINTY_HANDLING": 3,
    "VERIFICATION_PATTERNS": 7,
    "EXECUTION_WORKFLOW": 10,
    "CONTINUOUS_IMPROVEMENT": 4
  },
  "lifecycle_stage_usage": {
    "Understand": 12,
    "Plan": 15,
    "Validate": 8,
    "Execute": 20,
    "Verify": 14,
    "Reflect": 6
  },
  "failure_modes": [
    {
      "persona": "principal-engineer",
      "evaluation": "evaluation-001.md",
      "friction": "Hesitated at Validate stage"
    }
  ],
  "taxonomy_classification": {
    "Architecture": 2,
    "Behaviour": 8,
    "Evidence": 1,
    "Usability": 3
  }
}
```

### 3. Quality Gates Definition

**File:** `dataset-v1/quality-gates.md`

**Gates:**
1. **Coverage:** Every lifecycle stage exercised at least once
2. **Persona Diversity:** All planned personas evaluated
3. **Scenario Diversity:** Multiple task types represented
4. **Evidence Quality:** Validation logs completed for every evaluation
5. **Pattern Confidence:** Recurring findings observed across evaluations

## Schema Change Policy

### To modify schema:

1. **Version bump:** v1 → v2
2. **Document change:** Update this file with new schema
3. **Backward compatibility:** Document how v1 datasets map to v2
4. **Migration guide:** Provide instructions for updating existing datasets

### Breaking changes require:

- Clear deprecation notice
- Migration script if possible
- Documentation of impact
- Approval from review process

## Current Schema Version

**Schema Version:** v1  
**Frozen:** 2026-07-27  
**Next allowed version:** v2 (only for non-breaking clarifications)

## Schema Stability Benefits

1. **Reproducibility:** Datasets remain comparable over time
2. **Consistency:** Metrics calculated the same way across cycles
3. **Trend analysis:** Meaningful longitudinal comparisons
4. **Auditability:** Clear provenance from dataset to report
5. **Tooling:** Scripts can rely on stable schema

---

**Schema maintainer:** Hermes Automation Architect  
**Next review:** After collecting 15+ evaluations