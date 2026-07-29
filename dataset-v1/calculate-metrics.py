#!/usr/bin/env python3
"""
Calculate metrics from Operational Validation Dataset v1
"""

import json
from pathlib import Path
from collections import defaultdict, Counter

dataset_dir = Path("E:/Hermes Projects/personas/dataset-v1")
evaluations_dir = dataset_dir / "evaluations"
metrics_dir = dataset_dir / "metrics"

metrics_dir.mkdir(exist_ok=True)

# Initialize metrics
capability_usage = Counter()
lifecycle_stage_usage = Counter()
failure_modes = []
taxonomy_classification = Counter()

# Process each evaluation
for persona_dir in evaluations_dir.iterdir():
    if persona_dir.is_dir():
        for eval_file in persona_dir.glob("*.md"):
            content = eval_file.read_text(encoding='utf-8')
            
            # Extract capability usage
            if "PLANNING_FRAMEWORK" in content:
                capability_usage["PLANNING_FRAMEWORK"] += 1
            if "DECISION_FRAMEWORK" in content:
                capability_usage["DECISION_FRAMEWORK"] += 1
            if "UNCERTAINTY_HANDLING" in content:
                capability_usage["UNCERTAINTY_HANDLING"] += 1
            if "VERIFICATION_PATTERNS" in content:
                capability_usage["VERIFICATION_PATTERNS"] += 1
            if "EXECUTION_WORKFLOW" in content:
                capability_usage["EXECUTION_WORKFLOW"] += 1
            if "CONTINUOUS_IMPROVEMENT" in content:
                capability_usage["CONTINUOUS_IMPROVEMENT"] += 1
            
            # Extract lifecycle stage usage
            if "- [X] Understand" in content or "- [x] Understand" in content:
                lifecycle_stage_usage["Understand"] += 1
            if "- [X] Plan" in content or "- [x] Plan" in content:
                lifecycle_stage_usage["Plan"] += 1
            if "- [X] Validate" in content or "- [x] Validate" in content:
                lifecycle_stage_usage["Validate"] += 1
            if "- [X] Execute" in content or "- [x] Execute" in content:
                lifecycle_stage_usage["Execute"] += 1
            if "- [X] Verify" in content or "- [x] Verify" in content:
                lifecycle_stage_usage["Verify"] += 1
            if "- [X] Reflect" in content or "- [x] Reflect" in content:
                lifecycle_stage_usage["Reflect"] += 1
            
            # Extract failure modes
            if "Friction Points:" in content:
                friction_section = content.split("Friction Points:")[1].split("Performance Bottlenecks:")[0]
                if "[X]" in friction_section or "[x]" in friction_section:
                    failure_modes.append({
                        "persona": persona_dir.name,
                        "evaluation": eval_file.name,
                        "friction": friction_section.strip()
                    })
            
            # Extract taxonomy classification
            if "Classification" in content:
                classification_section = content.split("Classification")[1]
                if "Architecture" in classification_section:
                    taxonomy_classification["Architecture"] += 1
                if "Behaviour" in classification_section:
                    taxonomy_classification["Behaviour"] += 1
                if "Evidence" in classification_section:
                    taxonomy_classification["Evidence"] += 1
                if "Usability" in classification_section:
                    taxonomy_classification["Usability"] += 1

# Write metrics to JSON
metrics = {
    "capability_usage": dict(capability_usage),
    "lifecycle_stage_usage": dict(lifecycle_stage_usage),
    "failure_modes": failure_modes,
    "taxonomy_classification": dict(taxonomy_classification),
    "total_evaluations": sum(1 for _ in evaluations_dir.rglob("*.md")),
    "dataset_version": "v1",
    "generated_at": "2026-07-27"
}

with open(metrics_dir / "capability-usage.json", "w") as f:
    json.dump(metrics["capability_usage"], f, indent=2)

with open(metrics_dir / "lifecycle-coverage.json", "w") as f:
    json.dump(metrics["lifecycle_stage_usage"], f, indent=2)

with open(metrics_dir / "failure-modes.json", "w") as f:
    json.dump(metrics["failure_modes"], f, indent=2)

with open(metrics_dir / "taxonomy-summary.json", "w") as f:
    json.dump(metrics["taxonomy_classification"], f, indent=2)

with open(metrics_dir / "dataset-summary.json", "w") as f:
    json.dump({
        "total_evaluations": metrics["total_evaluations"],
        "dataset_version": metrics["dataset_version"],
        "generated_at": metrics["generated_at"],
        "metrics_files": [
            "capability-usage.json",
            "lifecycle-coverage.json",
            "failure-modes.json",
            "taxonomy-summary.json"
        ]
    }, f, indent=2)

print("Metrics calculated and saved to dataset-v1/metrics/")
print(f"Evaluations processed: {metrics['total_evaluations']}")
print(f"Capabilities tracked: {len(metrics['capability_usage'])}")
print(f"Lifecycle stages tracked: {len(metrics['lifecycle_stage_usage'])}")