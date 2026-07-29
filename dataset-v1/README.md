# Operational Validation Dataset v1

## Purpose

Collect evidence from real persona usage to validate the CORE behavioural architecture.

## Structure

```
dataset-v1/
├── evaluations/
│   ├── principal-engineer/
│   │   ├── evaluation-001.md
│   │   ├── evaluation-002.md
│   │   └── ...
│   ├── staff-engineer/
│   ├── product-manager/
│   ├── ux-designer/
│   └── security-engineer/
│
├── metrics/
│   ├── capability-usage.json
│   ├── lifecycle-coverage.json
│   ├── failure-modes.json
│   └── taxonomy-summary.json
│
└── reports/
    └── operational-validation-report-v1.md
```

## Data Model

### Evaluation Log (evaluations/{persona}/{evaluation-id}.md)
- Persona details
- Scenario executed
- Lifecycle stages observed
- Capability documents referenced
- Observations (friction points, bottlenecks)
- Classification (architecture, behaviour, evidence, usability)

### Metrics (metrics/*.json)
- Aggregated statistics
- Cross-persona patterns
- Usage frequencies
- Failure mode analysis

### Report (reports/operational-validation-report-v1.md)
- Derived from dataset
- Descriptive observations only
- No recommendations until gates are met

## Quality Gates

See quality-gates.md for exit criteria before generating reports.

## Next Steps

1. Execute scenarios for each persona
2. Fill validation logs with actual observations
3. Run metrics calculation script
4. Verify quality gates
5. Generate report only if gates are met

---
**Dataset Version:** v1  
**Generated:** 2026-07-27