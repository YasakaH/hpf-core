# Hallucination

## Identity
- id: hallucination
- type: concept
- title: Hallucination
- tags: [machine learning, hallucination, generation, factuality, LLM, grounding, verification]
- entities: [hallucination, fabrication, generation, factuality, grounding, retrieval augmentation, verification]
- concepts: [confidence-calibration, probabilistic-outputs, uncertainty-estimation, benchmark-validity, distribution-shift, model-monitoring]

## Claims
- claim: "Hallucination is the generation of fluent, confident content that is factually incorrect or unsupported — it is a failure mode of generation, not of comprehension."
  certainty: high
  evidence: LLM factuality research
  scope: cross-domain
- claim: "Hallucination is dangerous because it is confidence-correlated — models hallucinate with high stated confidence, defeating naive confidence gating."
  certainty: high
  evidence: Hallucination and calibration research
  scope: cross-domain
- claim: "Hallucination rates are context-dependent — they vary with domain, prompt, knowledge recency, and task type."
  certainty: high
  evidence: Hallucination evaluation literature
  scope: cross-domain
- claim: "Hallucination is partially detectable post-hoc (verification against sources) and partially irreducible (unverifiable claims)."
  certainty: high
  evidence: Grounding and verification research
  scope: cross-domain
- claim: "Hallucination is a distribution property of the model-prompt pair, not a fixed model property — it cannot be permanently eliminated by training alone."
  certainty: high
  evidence: Hallucination research across model generations
  scope: cross-domain

## Relationships
- concept: confidence-calibration
  relationship: exploits
  description: "Hallucination exploits calibration — high stated confidence on false content defeats confidence-based gating."
- concept: probabilistic-outputs
  relationship: masks
  description: "Probabilistic outputs mask hallucination — a plausible distribution over wrong content looks indistinguishable from correct."
- concept: uncertainty-estimation
  relationship: targeted_by
  description: "Uncertainty estimation targets hallucination — detecting when the model does not know is the mitigation path."
- concept: benchmark-validity
  relationship: measured_by
  description: "Hallucination is measured by benchmarks — hallucination metrics inherit benchmark validity limits."
- concept: distribution-shift
  relationship: aggravated_by
  description: "Distribution shift aggravates hallucination — unfamiliar inputs raise fabrication likelihood."
- concept: model-monitoring
  relationship: detected_by
  description: "Model monitoring detects hallucination — production hallucination is a monitoring signal, not just an evaluation metric."

## Tradeoffs
- dimension: factual_strictness_vs_utility
  options:
    strict_refusal:
      value: safety
      rationale: "Refusing or hedging when uncertain prevents fabrication but reduces usefulness."
    always_answer:
      value: utility
      rationale: "Answering always maximizes usefulness but fabricates when knowledge is absent."
  importance: high
- dimension: verification_cost_vs_coverage
  options:
    full_verification:
      value: assurance
      rationale: "Verifying every output against sources is complete but expensive and latency-heavy."
    sampled_verification:
      value: efficiency
      rationale: "Sampling verification is cheap but leaves unverified fabrications in the tail."
  importance: high

## Failure Modes
- name: confident_fabrication
  description: "Model asserts invented facts with high stated confidence — the core hallucination mode and the hardest to gate."
  likelihood: high
  observable_evidence: "Factual errors asserted fluently; confidence on false content matches confidence on true content"
  detection: "Source verification; factual consistency checks; human review on high-stakes outputs"
  recovery: "Grounding via retrieval; verification pipelines; abstention policies on unverifiable claims"
  retryable: true
- name: source_misattribution
  description: "Model attributes correct content to the wrong source — the claim is true but its provenance is fabricated."
  likelihood: medium
  observable_evidence: "Correct statements with invented citations; references that do not contain the cited content"
  detection: "Citation verification; provenance checking against retrieved sources"
  recovery: "Retrieval-grounded citation; cite-only-what-is-provided policy; citation verification checks"
  retryable: true
- name: stale_knowledge_assertion
  description: "Model confidently states outdated facts as current — knowledge recency conflicts with confident delivery."
  likelihood: high
  observable_evidence: "Confident answers contradicting current sources; temporal errors in time-sensitive domains"
  detection: "Recency-aware evaluation; cross-check against current sources; timestamp-aware prompting"
  recovery: "Time-aware retrieval; fresh grounding; uncertainty about recency surfaced explicitly"
  retryable: true

## Observations
- observation: "Hallucination rates correlate with question ambiguity and knowledge recency."
  confidence: high
  source: Hallucination evaluation studies
- observation: "Retrieval augmentation substantially reduces but does not eliminate hallucination."
  confidence: high
  source: RAG research and evaluations
- observation: "Human raters frequently cannot distinguish hallucinated from factual content without external verification."
  confidence: high
  source: Factuality evaluation research

## Constraints
- constraint: "A generative model cannot be fully grounded in evidence it was not trained or provided with."
  type: invariant
  scope: cross-domain
- constraint: "Confidence cannot serve as a reliable hallucination detector — hallucination is confidence-correlated by construction."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Treat any claim the model cannot support from provided sources as suspect."
  rationale: "Unsupported content is where fabrication concentrates; verification is the only reliable gate."
  evidence_level: high
- heuristic: "Prefer abstention or hedging for unverifiable claims in high-stakes contexts."
  rationale: "Honest uncertainty beats confident fabrication when the cost of error is high."
  evidence_level: high
- heuristic: "Verify outputs against sources whenever the cost of error exceeds the cost of checking."
  rationale: "The verification decision is an economic tradeoff between error cost and checking cost."
  evidence_level: high

## Recommendations
- recommendation: "Ground generation in retrieval or verified sources for fact-critical applications."
  context: system_design
  certainty: strong
  rationale: "Grounding converts generation from memory recall into source-constrained composition, sharply reducing fabrication."
- recommendation: "Instrument hallucination detection for high-stakes outputs rather than trusting confidence."
  context: deployment
  certainty: strong
  rationale: "Confidence is correlated with hallucination, making it useless as a gate."
- recommendation: "Report hallucination rates by domain in evaluation, not a single aggregate number."
  context: evaluation
  certainty: strong
  rationale: "Hallucination is context-dependent; aggregate numbers hide the domains where it concentrates."
