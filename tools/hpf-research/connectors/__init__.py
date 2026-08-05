"""HPF evidence connectors.

Evidence classes (the planner picks which classes a research request needs):

    primary       official docs, RFCs, specifications
    code          GitHub, GitLab repositories
    community     practitioner signal: Reddit (Devvit CLI), HN, Stack Overflow
    scientific    papers, preprints
    operational   benchmarks, telemetry, release notes

A connector gathers evidence for one class and emits structured payloads.
Community output is SIGNAL, never truth: findings derived from it are labeled
`community_signal` and go through normal validation before any corpus
admission.
"""

EVIDENCE_CLASSES = (
    "primary",
    "code",
    "community",
    "scientific",
    "operational",
)


def plan_evidence_classes(topic: str, depth: str, keywords: list) -> dict:
    """Mechanical planner rules: recommend evidence classes per topic.

    Returns a dict of class -> weight ('high'|'low'|'skip') with a reason.
    """
    t = topic.lower()
    rules = {
        "primary": ("high", "official documentation anchors any topic"),
        "code": ("high", "repositories show implementation reality"),
        "community": ("high", "practitioner pain points are core signal for tooling topics")
            if any(k in t for k in ("automation", "scraping", "scrape", "crawl", "tool", "framework", "library", "cli", "driver", "dev", "python", "agent", "browser", "bot", "cdp"))
            else ("low", "community weight low outside developer-tooling topics"),
        "scientific": ("high", "benchmarks and papers matter when the topic names a model or method")
            if any(k in t for k in ("model", "paper", "benchmark", "research", "fara", "gpt", "llm", "agent"))
            else ("low", "scientific weight low unless the topic is model/research-focused"),
        "operational": ("high", "operational evidence for performance/robustness topics")
            if any(k in t for k in ("performance", "robust", "reliab", "latency", "scal", "production"))
            else ("low", "operational weight low unless performance is central"),
    }
    if depth == "deep":
        for k in rules:
            if rules[k][0] != "skip":
                rules[k] = ("high", rules[k][1])
    return rules
