# HPF Knowledge Report

_Generated 2026-08-03T01:54:26Z from knowledge-export-core-v1 (schema 1.2). Derived projection of the research corpus._

## Contents

1. [Abstract Syntax Tree](#abstract-syntax-tree)
2. [Actuation](#actuation)
3. [Alignment](#alignment)
4. [Anti-Detection Strategy](#anti-detection-strategy)
5. [Artifact Under Analysis](#artifact)
6. [Atomicity](#atomicity)
7. [Attack Surface](#attack-surface)
8. [Attacker Capability](#attacker-capability)
9. [Attribution of Artifacts](#attribution)
10. [Attribution Assessment for Midnight Foundry](#attribution-assessment)
11. [Automation Detection Surface](#automation-detection-surface)
12. [Automation Protocol](#automation-protocol)
13. [Autonomy Decision](#autonomy-decision)
14. [Availability](#availability)
15. [Backpressure](#backpressure)
16. [Backup Recovery](#backup-recovery)
17. [Behavioural Observation of Artifacts](#behavioral-observation)
18. [Belief State](#belief-state)
19. [Benchmark Validity](#benchmark-validity)
20. [Browser Fingerprint](#browser-fingerprint)
21. [Isolated Browser Profiles](#browser-profiles-concept)
22. [Build Systems](#build-systems)
23. [CAP Theorem](#cap-theorem)
24. [Cascading Failure](#cascading-failure)
25. [Chrome DevTools Protocol Mechanics](#cdp-mechanics)
26. [Circuit Breaker](#circuit-breaker)
27. [Closed-Loop Guarantee](#closed-loop-guarantee)
28. [Cluster 1 C2 Infrastructure](#cluster-1-c2-infrastructure)
29. [Cluster 2 Staging Infrastructure](#cluster-2-staging-infrastructure)
30. [Collection Pattern](#collection-pattern)
31. [Compensating Controls](#compensating-controls)
32. [Competing Hypotheses in Artifact Analysis](#competing-hypotheses)
33. [Compiler Correctness](#compiler-correctness)
34. [Compiler Optimization](#compiler-optimization)
35. [Compiler Performance](#compiler-performance)
36. [Concealed Intent of Artifacts](#concealed-intent)
37. [Confidence in Security Judgement](#confidence)
38. [Confidence Calibration](#confidence-calibration)
39. [Confidence Threshold Decision](#confidence-threshold)
40. [Constant Folding](#constant-folding)
41. [Containment Decision on Incomplete Reconstruction](#containment-decision)
42. [Control-Scheduling Interaction](#control-scheduling-interaction)
43. [Cyber-Physical System](#cyber-physical-system)
44. [Data Governance](#data-governance)
45. [Data Integrity](#data-integrity)
46. [Database Indexing](#database-indexing)
47. [Dead Code Elimination](#dead-code-elimination)
48. [Deadline](#deadline)
49. [Debug vs Release Modes](#debug-vs-release-modes)
50. [Defense in Depth](#defense-in-depth)
51. [Deployment Risk](#deployment-risk)
52. [Design Under Concealment](#design-under-concealment)
53. [Detection Decision on Incomplete Reconstruction](#detection-decision)
54. [Disclosure Decision on Incomplete Reconstruction](#disclosure-decision)
55. [Distribution Shift](#distribution-shift)
56. [Drift Detection](#drift-detection)
57. [First-Stage Dropper Family](#dropper)
58. [Earliest-Deadline-First](#earliest-deadline-first)
59. [Epistemic Symmetry Between Analyst and Designer](#epistemic-symmetry)
60. [Equivalence Checking](#equivalence-checking)
61. [Eventual Consistency](#eventual-consistency)
62. [Exfiltration Pattern](#exfiltration-pattern)
63. [Fail-Safe](#fail-safe)
64. [Feedback Control](#feedback-control)
65. [Fixed-Priority Scheduling](#fixed-priority-scheduling)
66. [Formal Verification](#formal-verification)
67. [Generalization](#generalization)
68. [Hallucination](#hallucination)
69. [Hammer-A Variant](#hammer-a-variant)
70. [Hammer-B Variant](#hammer-b-variant)
71. [Hammer Backdoor Family](#hammer-backdoor-family)
72. [Hammer One-Family-vs-Two Classification Dispute](#hammer-classification-dispute)
73. [Hard vs Soft Real-Time](#hard-vs-soft-real-time)
74. [HTTP Protocol](#http-protocol)
75. [Human Evaluation](#human-evaluation)
76. [Idempotency](#idempotency)
77. [Incident Response](#incident-response)
78. [Incomplete Evidence in Security Analysis](#incomplete-evidence)
79. [Index Selection](#index-selection)
80. [Inference from Behaviour](#inference-from-behavior)
81. [Intermediate Representation](#intermediate-representation)
82. [Isolation Levels](#isolation-levels)
83. [Iterative Refinement of Reconstructions](#iterative-refinement)
84. [K7 Overlap Links](#k7-overlap)
85. [Kill Chain](#kill-chain)
86. [Lateral Movement Pattern](#lateral-movement-pattern)
87. [Leader Election](#leader-election)
88. [Likelihood of Security Events](#likelihood)
89. [Metric Selection](#metric-selection)
90. [Midnight Foundry Intrusion Campaign](#midnight-foundry-campaign)
91. [Model Monitoring](#model-monitoring)
92. [Network Failure Propagation](#network-failure-propagation)
93. [Network Partition Recovery](#network-partition-recovery)
94. [Normalization](#normalization)
95. [Observable Evidence from Artifacts](#observable-evidence)
96. [Open Analytical Questions for Midnight Foundry](#open-analytical-questions)
97. [Optimization Pass](#optimization-pass)
98. [Optimization Tradeoffs](#optimization-tradeoffs)
99. [Overfitting](#overfitting)
100. [Overload Handling](#overload-handling)
101. [Per-Victim Operational Separation Pattern](#per-victim-operational-separation)
102. [Perception Uncertainty](#perception-uncertainty)
103. [Persistence Pattern](#persistence-pattern)
104. [Physical State](#physical-state)
105. [Priority Inversion](#priority-inversion)
106. [Probabilistic Outputs](#probabilistic-outputs)
107. [Procurement-Aware Targeting Pattern](#procurement-aware-targeting)
108. [Program Semantics](#program-semantics)
109. [Proxy Infrastructure](#proxy-infrastructure)
110. [Query Optimization](#query-optimization)
111. [Query Planning](#query-planning)
112. [Quorum](#quorum)
113. [Raft Consensus](#raft-consensus)
114. [Rate-Monotonic Analysis](#rate-monotonic-analysis)
115. [Real-Time Guarantee](#real-time-guarantee)
116. [Real-Time System](#real-time-system)
117. [Real-Time Throughput Tradeoff](#real-time-throughput-tradeoff)
118. [Reconstruction Confidence](#reconstruction-confidence)
119. [Relational Model](#relational-model)
120. [Replication](#replication)
121. [Residual Risk](#residual-risk)
122. [Resource Arbitration](#resource-arbitration)
123. [Retraining Decisions](#retraining-decisions)
124. [Retry Storm Amplification](#retry-storm-amplification)
125. [Risk Acceptance](#risk-acceptance)
126. [Rivet Credential and Data Stealer](#rivet-stealer)
127. [Rolling Deployment](#rolling-deployment)
128. [Safety Case](#safety-case)
129. [Saga Pattern](#saga-pattern)
130. [Schedulability Analysis](#schedulability-analysis)
131. [Scheduling Policy](#scheduling-policy)
132. [Schema Design](#schema-design)
133. [Schema Migration](#schema-migration)
134. [Sensing](#sensing)
135. [Sensor Fusion](#sensor-fusion)
136. [Spearphishing Initial Access Pattern](#spearphishing-initial-access)
137. [Split Brain](#split-brain)
138. [Stability](#stability)
139. [State Estimation](#state-estimation)
140. [Strong Consistency](#strong-consistency)
141. [Surface Ambiguity of Artifacts](#surface-ambiguity)
142. [Task Scheduling](#task-scheduling)
143. [TCP and TLS Connection Foundation](#tcp-tls-foundation)
144. [Temporal Isolation](#temporal-isolation)
145. [Threat Actor](#threat-actor)
146. [Threat Detection](#threat-detection)
147. [Training Data](#training-data)
148. [Transaction Failures](#transaction-failures)
149. [Transactions](#transactions)
150. [Type Safety](#type-safety)
151. [Type System](#type-system)
152. [Unassigned Hosts](#unassigned-hosts)
153. [Uncertainty Estimation](#uncertainty-estimation)
154. [Aerospace Defense Supply-Chain Victim Set](#victim-set)
155. [Vulnerability Management](#vulnerability-management)
156. [Watchdog Timer](#watchdog-timer)
157. [Worst-Case Execution Time](#worst-case-execution-time)
158. [Zero Trust Architecture](#zero-trust)

## Abstract Syntax Tree (`abstract-syntax-tree`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/abstract-syntax-tree.md`

### Claims

- "An abstract syntax tree is the structured representation of source code — a tree of syntax nodes produced by a parser, discarding non-essential surface syntax." _(certainty: high)_
- "The AST is defined by the grammar — node structure, precedence, and associativity all derive from the language's grammar." _(certainty: high)_
- "ASTs are the transformation substrate — optimizations and lowering operate on the AST or structures derived from it." _(certainty: high)_
- "AST nodes carry identity and position — source location, lexical context, and ancestry determine what transformations are valid at a node." _(certainty: high)_
- "An AST is an abstraction over parse trees — it drops punctuation and grouping details while preserving the structure that matters for semantics." _(certainty: high)_

### Relationships

- **annotated_by** → `type-system`
- **lowered_from** → `intermediate-representation`
- **expresses** → `program-semantics`
- **operates_on** → `compiler-optimization`
- **enables** → `constant-folding`
- **enables** → `dead-code-elimination`

### Constraints

- "AST structure must be derivable from the grammar — tree shape that contradicts the grammar produces untrustworthy tooling and transformations."
- "Transformation validity is bound to tree position — a rewrite that ignores node ancestry or scope can change program meaning."

### Recommendations

- "Define the AST directly from the grammar and validate structure against it."
- "Carry source position through every lowering and transformation stage."
- "Fuzz and conformance-test the parser independently of the rest of the pipeline."

## Actuation (`actuation`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/actuation.md`

### Claims

- "Actuation is the action end of the loop — decisions become physical commands that change the world." _(certainty: high)_
- "An actuator command is the consequence of a decision about a belief — action under an incomplete world model, never under direct knowledge." _(certainty: high)_
- "Repeated physical commands are not harmless — actuation inherits the idempotency discipline of distributed systems." _(certainty: high)_
- "Actuation failure is physical — the consequence is in the world, and the failure mode must carry its physical effect." _(certainty: high)_
- "The Epistemic Chain closes at actuation — reality acts back on the next observation, making the loop the unit of knowledge, not the object." _(certainty: high)_

### Relationships

- **serves** → `cyber-physical-system`
- **changes** → `physical-state`
- **analogous_to** → `idempotency`
- **mitigated_by** → `retry-pattern`
- **executed_under** → `real-time-system`

### Constraints

- "An actuator command is valid only under its timing and idempotency conditions — duplicate or late actuation is a failure."
- "Action is taken on belief, never on direct knowledge — the epistemic gap is closed by verification, not eliminated."

### Recommendations

- "Represent actuation as the action destination of the decision — a command is a consequence, not a construct."
- "Apply the idempotency discipline to every physical command."
- "Close the loop with verification — treat the world's response as the evidence for the command."

## Alignment (`alignment`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/alignment.md`

### Claims

- "Alignment is the correspondence between a system's objectives and the intended objectives — a property evaluated through evidence, not a value object." _(certainty: high)_
- "Alignment is multi-objective — it requires trading off competing objectives (helpfulness vs safety, capability vs constraint)." _(certainty: high)_
- "Alignment is inferred from evaluated behaviour, never from declared intent." _(certainty: high)_
- "Alignment failures are specification failures — the system optimizes what it was trained to optimize, including misspecified objectives." _(certainty: high)_
- "Alignment requires continuous re-assessment — behaviour drift and objective change invalidate prior alignment evidence." _(certainty: high)_

### Relationships

- **grounded_in** → `human-evaluation`
- **measured_by** → `benchmark-validity`
- **expressed_through** → `metric-selection`
- **shaped_by** → `training-data`
- **destabilized_by** → `distribution-shift`
- **informs** → `risk-acceptance`

### Constraints

- "A system optimizes its training objective — misspecification in the objective propagates into behaviour."
- "Alignment claims are valid only under the conditions they were evaluated under."

### Recommendations

- "Express alignment as explicit objective tradeoffs with stated weights and evaluation instruments."
- "Evaluate alignment on behaviour, never on declared intent."
- "Treat alignment as a continuous process with re-evaluation triggers, not a one-time property."

## Anti-Detection Strategy (`anti-detection-strategy`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/anti-detection-strategy.md`

### Claims

- "IP reputation is the single highest-weight signal for most commercial anti-bot services (Cloudflare, Datadome, Akamai). A clean residential proxy with minimal JS patching outperforms perfect JS/TLS patches on a flagged IP." _(certainty: high)_
- "Patching `navigator.webdriver` alone provides negligible protection against sophisticated anti-bot services — they check multiple signals and detect patching inconsistencies." _(certainty: high)_
- "Behavioural simulation (mouse movement, typing patterns, scrolling) is not confirmed to be deployed in production anti-bot services. Its effectiveness for anti-detection is theoretical." _(certainty: medium)_
- "No anti-detection strategy provides permanent protection. The arms race between automation and detection services requires continuous maintenance — a fixed strategy will degrade in effectiveness within 3-9 months." _(certainty: high)_

### Relationships

- **modifies** → `automation-detection-surface`
- **manipulates** → `browser-fingerprint`
- **constrained_by** → `automation-protocol`
- **profile_strategy** → `browser-profile`
- **timing_dependent** → `browser-session-lifecycle`

### Constraints

- "JS property patches must execute before any page script; `Page.addScriptToEvaluateOnNewDocument` provides this but only for CDP — WebDriver has no equivalent pre-load injection mechanism."
- "TLS fingerprint cannot be modified from within the browser JavaScript context; requires external proxy or custom browser build."
- "Headless mode (even `--headless=new`) exposes some detectable differences from headed Chrome — no single Chrome flag eliminates all detection signals."
- "Community stealth libraries update on their maintainer's schedule, not yours. Version pinning prevents unexpected changes but also prevents receiving security/detection updates."
- "Anti-bot services A/B test detection thresholds. A strategy that works for 90% of sessions may fail for 10% if your session falls into a test group with stricter detection."

### Recommendations

- "Implement layered anti-detection with at least JS property patching (layer 1), protocol flag manipulation (layer 2), and infrastructure (layer 5) for any production deployment."
- "Use residential proxies (not datacenter) for high-value targets. The cost is justified by the significantly lower detection rate."
- "Do not implement custom behavioural simulation (mouse movement, typing) for production anti-detection without first confirming it is actually deployed on your target site."
- "Schedule quarterly anti-detection strategy reviews. Detection signal half-life is 3-9 months; quarterly reviews enable proactive maintenance before degradation impacts operations."
- "Test anti-detection strategy weekly against the actual target site. Detection service changes can happen at any time and may not be announced."

## Artifact Under Analysis (`artifact`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/artifact.md`

### Claims

- "An artifact is a manufactured object whose provenance is suspect or unknown — a binary, firmware image, or captured device presented to analysis without a trusted account of what it is." _(certainty: high)_
- "The artifact presents itself through two channels only: its observable surface and its behaviour — everything else about it is inference." _(certainty: high)_
- "Artifacts of adversarial origin are deliberately separated from their own description — the thing itself is present; the account of what it does is withheld." _(certainty: high)_
- "The artifact's true purpose is a property the analyst does not directly access — it exists in the design intent of an absent creator." _(certainty: high)_
- "An artifact is evidence — its legal and operational significance depends on preserved provenance, not on the analyst's reading of it." _(certainty: high)_

### Relationships

- **constrained_by** → `incomplete-evidence`
- **describes** → `attacker-capability`
- **challenges** → `threat-detection`
- **requires** → `confidence`
- **informs** → `incident-response`

### Constraints

- "The observable surface is not the semantics — an artifact's appearance never certifies what it does."
- "Every claim about an artifact carries a provenance condition — claims without capture context are unqualified."

### Recommendations

- "Separate the artifact from the account of it — record what is observed and what is inferred distinctly."
- "Preserve provenance at capture time — the artifact's history is evidence about the artifact."
- "Keep the surface/semantics distinction explicit in every analysis record."

## Atomicity (`atomicity`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/atomicity.md`

### Claims

- "Atomicity is the guarantee that a transaction applies fully or not at all — no partial states are observable." _(certainty: high)_
- "Atomicity is a scoped guarantee — it holds for the transaction boundary, not for work outside it." _(certainty: high)_
- "Atomicity is implemented through write-ahead logging — durability of the intent log makes rollback and recovery possible." _(certainty: high)_
- "Atomicity converts crash exposure into a recovery procedure — the guarantee is about observable outcome, not about the failure event itself." _(certainty: high)_
- "Atomicity's value is compositional — multi-step operations become testable units; partial failure becomes a contradiction, not a case." _(certainty: high)_

### Relationships

- **defines** → `transactions`
- **protects** → `data-integrity`
- **contained_by** → `transaction-failures`
- **preserves** → `relational-model`
- **required_by** → `schema-migration`

### Constraints

- "A transaction's effects are either fully observable or not at all — partial visibility is a correctness failure."
- "Atomicity holds within the transaction boundary — work outside the boundary has no claim to the guarantee."

### Recommendations

- "Treat atomicity as a scoped guarantee — state what is inside the boundary."
- "Rehearse crash recovery with integrity verification."
- "Use sagas or compensation when atomicity is unachievable across boundaries — explicitly."

## Attack Surface (`attack-surface`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/attack-surface.md`

### Claims

- "The attack surface is the set of all points where an attacker can enter or extract data from a system — every network service, interface, endpoint, and input channel." _(certainty: high)_
- "Attack surface is a function of what is exposed, not what is known — unmanaged and shadow assets are part of the surface whether or not they are inventoried." _(certainty: high)_
- "Attack surface reduction is one of the highest-value defensive strategies — every eliminated entry point eliminates an entire class of attack." _(certainty: high)_
- "The attack surface expands faster than it contracts — new features, integrations, and cloud resources routinely outpace removal of legacy exposure." _(certainty: high)_
- "Attack surface and vulnerability are distinct — a large surface with no exploitable vulnerabilities presents less risk than a small surface with one critical flaw." _(certainty: high)_

### Relationships

- **multiplied_by** → `attacker-capability`
- **targeted_by** → `threat-actor`
- **entry_point** → `kill-chain`
- **informs** → `vulnerability-management`
- **reduces** → `zero-trust`

### Constraints

- "The attack surface can never be fully enumerated — completeness of surface knowledge is asymptotic, not attainable."
- "Every connected component contributes to the surface — unmanaged components still contribute whether or not they are known."

### Recommendations

- "Run continuous asset discovery and treat inventory drift as a security finding, not an operational nuisance."
- "Require explicit network exposure approval for every new service — default should be non-exposed."
- "Audit attack surface reduction opportunities quarterly — removing legacy exposure is cheaper than defending it."

## Attacker Capability (`attacker-capability`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/attacker-capability.md`

### Claims

- "Attacker capability describes what an adversary is able to do — their skills, tools, resources, and access — independently of whether they choose to attack." _(certainty: high)_
- "Capability is distinct from intent — a highly capable actor with no intent poses no immediate threat, while intent without capability produces no successful attacks." _(certainty: high)_
- "Capability levels span a wide spectrum — from untargeted commodity attacks using automated tooling to sophisticated state-sponsored operations with custom exploits." _(certainty: high)_
- "Capability is observable through behaviour, not just claims — capabilities manifest in TTPs (tactics, techniques, procedures) that can be detected and attributed." _(certainty: high)_
- "Capability is not static — it increases through tooling commoditisation, knowledge sharing, and the reuse of previously exploited vulnerabilities." _(certainty: high)_

### Relationships

- **characterises** → `threat-actor`
- **interacts_with** → `attack-surface`
- **enables** → `kill-chain`
- **drives** → `likelihood`
- **informs** → `risk-acceptance`

### Constraints

- "Capability without a path to the attack surface produces no exploit — capability assessment must be paired with attack-surface analysis."
- "Capability assessments are time-bound — an assessment is valid only until tooling or knowledge advances change the baseline."

### Recommendations

- "Base capability assessments on observed TTPs and intelligence, not on assumed actor sophistication."
- "Pair every capability assessment with attack-surface analysis — capability alone does not constitute a threat."
- "Review capability baselines quarterly against exploit commoditisation and CVE exploitation trends."

## Attribution of Artifacts (`attribution`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/attribution.md`

### Claims

- "Attribution is the claim about the artifact's origin — who or what built it — and it is an inference over the whole evidence chain, never an observation." _(certainty: high)_
- "Attribution stands at the analysis's furthest inferential reach — origin is inferred from intent, inferred from the artifact, inferred from behaviour, observed." _(certainty: high)_
- "Attribution carries the highest stakes and the lowest evidence — it decides response, and its evidence is the thinnest in the chain." _(certainty: high)_
- "Attribution carries no evidence of its own — the origin claim carries confidence like any other, and the chain is its only evidence." _(certainty: high)_
- "Attribution is strengthened by the evidence chain, never by the verdict — a confident attribution is a confidence in a long derived claim, not a fact." _(certainty: high)_

### Relationships

- **informed_by** → `concealed-intent`
- **describes** → `threat-actor`
- **qualified_by** → `reconstruction-confidence`
- **constrained_by** → `incomplete-evidence`
- **applies_to** → `artifact`

### Constraints

- "Attribution is a claim about origin, never a fact — the verdict is a qualified derived claim and is always revisable."
- "Attribution requires the evidence chain, not the verdict — an origin claim without its chain is an assertion."

### Recommendations

- "Build every attribution from its evidence chain — origin claims cite their bases."
- "Never raise an attribution claim without its evidence chain."
- "Treat every attribution as revisable — record what evidence would change it."

## Attribution Assessment for Midnight Foundry (`attribution-assessment`)

| Field | Value |
|---|---|
| kind | decision |
| domain | threat-analysis |
| research_cycle | "015" |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/attribution-assessment.md`

### Claims

- "The leading hypothesis attributes the activity to a state-affiliated group, supported by language artifacts in Hammer-B, operational hours aligned with UTC+8, procurement-linked targeting, and the dismissal of the K7 link by some analysts." _(certainty: medium)_
- "The competing hypothesis holds that the intrusions are contract work by a professional group possibly related to K7, supported by the infrastructure overlap, operational cleanliness, and the shared tooling comment string." _(certainty: medium)_
- "Both hypotheses remain open; the evidence is insufficient to choose between them with confidence." _(certainty: high)_

### Relationships

- **linked_to** → `midnight-foundry-campaign`
- **linked_to** → `k7-overlap`
- **linked_to** → `hammer-b-variant`
- **constrained_by** → `open-analytical-questions`

### Constraints

- "The assessment records both hypotheses and their evidence; it does not resolve them."

### Recommendations

- "Keep both attribution hypotheses open in tracking systems, each with its supporting evidence listed."
- "Record what evidence would move each hypothesis before acting on either."

## Automation Detection Surface (`automation-detection-surface`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/automation-detection-surface.md`

### Claims

- "The most reliable detection signals are not single properties but inconsistencies between multiple properties." _(certainty: high)_
- "TLS fingerprint (JA3/JA3S) manipulation is the highest-friction anti-detection technique because it requires controlling the TCP/TLS stack, which most automation frameworks delegate to the operating system." _(certainty: high)_
- "Detection surface signals have a half-life of 3-9 months before anti-bot services adapt to new stealth patches." _(certainty: medium)_
- "Behavioural detection (mouse movement, scrolling, typing patterns) is not widely deployed in production anti-bot services; its effectiveness is unconfirmed." _(certainty: medium)_

### Relationships

- **composes** → `browser-fingerprint`
- **modifies** → `anti-detection-strategy`
- **determines** → `automation-protocol`
- **amplifies** → `browser-profile`
- **varies_with** → `browser-session-lifecycle`

### Constraints

- "JavaScript property patches must execute before any page script runs; CDP `Page.addScriptToEvaluateOnNewDocument` provides this guarantee but adds measurable latency before pages can begin loading."
- "TLS and HTTP/2 fingerprints cannot be modified from JavaScript; they require external proxy or custom browser build."
- "Behavioural simulation cannot fully replicate human behaviour; fractal complexity of natural movement exceeds current simulation capabilities."
- "Anti-bot services continuously discover new detection signals; no patching strategy provides permanent effectiveness."

### Recommendations

- "Implement layered anti-detection: patch at least JS properties (layer 1), protocol flags (layer 2), and environment consistency (layer 3) for any production deployment."
- "Use residential proxies for high-value automation targets. IP reputation is the highest-weight single signal for most anti-bot services."
- "Do not rely on behavioural simulation (mouse movement, typing patterns) as a primary anti-detection strategy — its effectiveness in production anti-bot services is unconfirmed."
- "Schedule quarterly stealth patch reviews. Detection signal half-life is 3-9 months; quarterly reviews catch decay before it impacts production."

## Automation Protocol (`automation-protocol`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/automation-protocol.md`

### Claims

- "CDP is a JSON-RPC protocol over WebSocket that exposes every internal Chromium debugging primitive." _(certainty: high)_
- "WebDriver Classic is a W3C-standardised HTTP API that abstracts browser internals behind a session model." _(certainty: high)_
- "WebDriver BiDi combines the standardisation of WebDriver with the streaming capability of CDP using JSON-RPC over WebSocket." _(certainty: high)_
- "BiDi's script module provides execution world isolation — automation scripts and page scripts run in separate JavaScript contexts." _(certainty: medium)_
- "Protocol migration is trending toward standardised protocols (BiDi) but CDP will remain relevant for legacy systems and Chromium-specific features." _(certainty: medium)_

### Relationships

- **defines** → `browser-session-lifecycle`
- **determines** → `automation-detection-surface`
- **influences** → `browser-readiness-model`
- **specialises** → `cdp-mechanics`
- **specialises** → `webdriver-classic`
- **specialises** → `webdriver-bidi`

### Constraints

- "One protocol connection per browser process."
- "Protocol version must match browser version within compatibility window."
- "Network-level protocol metadata (WebSocket upgrade headers) is observable by the page."

### Recommendations

- "Select protocol based on capability requirements first, then detection sensitivity."
- "Build protocol-agnostic automation where possible to enable future migration."

## Autonomy Decision (`autonomy-decision`)

| Field | Value |
|---|---|
| kind | decision |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/autonomy-decision.md`

### Claims

- "An autonomy decision is a decision under an incomplete world model — generating options, not choosing among predefined ones." _(certainty: high)_
- "Action generation is option creation under uncertainty — the decision structure extends to open action spaces without a new construct." _(certainty: high)_
- "The autonomy decision is the Epistemic Chain's decision node — belief informs the decision, the decision informs actuation." _(certainty: high)_
- "Autonomy is posture, not property — the degree of autonomy is chosen per context, exactly as hard/soft posture is chosen." _(certainty: high)_
- "Autonomy decisions are valid only under stated conditions — the world model's conditions bound the decision's claims." _(certainty: high)_

### Relationships

- **constrained_by** → `belief-state`
- **informs** → `actuation`
- **constrained_by** → `safety-case`
- **analogous_to** → `risk-acceptance`
- **analogous_to** → `scheduling-policy`

### Constraints

- "Autonomy is decision under an incomplete model — the model's confidence bounds the decision's claims."
- "Every autonomous action is an action on belief — verification closes the gap, and the envelope bounds the action."

### Recommendations

- "Represent autonomy as decision objects in open action spaces — generation is part of the decision, not a construct."
- "Bound autonomous action by the verified envelope."
- "Audit the generated option set, not only the chosen action."

## Availability (`availability`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/availability.md`

### Claims

- "Availability is the proportion of time a system remains operational and able to serve requests, typically measured as a percentage of uptime." _(certainty: high)_
- "Availability is not binary — a system can be available for reads but not writes, available at degraded performance, or available for only a subset of clients." _(certainty: high)_
- "High availability (HA) is achieved through redundancy — multiple instances that can serve requests when one fails." _(certainty: high)_
- "Increasing availability by one 'nine' (99.9% to 99.99%) typically requires an order of magnitude increase in architectural complexity." _(certainty: high)_
- "Availability and consistency are traded off during partitions — CAP theorem formally captures this constraint." _(certainty: high)_
- "Degraded availability (serving requests with higher latency or reduced functionality) is preferable to total unavailability for most user-facing systems." _(certainty: high)_

### Relationships

- **constrained_by** → `cap-theorem`
- **enables** → `eventual-consistency`
- **limits** → `strong-consistency`
- **affects** → `quorum`
- **protects** → `backpressure`
- **protects** → `circuit-breaker`

### Constraints

- "System availability cannot exceed the availability of its least redundant component — availability is constrained by the weakest link."
- "Increasing availability past 99.99% requires redundancy at every layer (compute, network, storage, power, data centre region)."

### Recommendations

- "Define availability SLOs in terms of user-visible behaviour, not infrastructure metrics — '99.9% of requests succeed with latency under 500ms' is more meaningful than '99.9% uptime'."
- "Implement graceful degradation as a first-class architectural requirement, not an afterthought — define what the system does at each saturation level."
- "Test availability boundaries through chaos engineering — validate that redundancy and failover mechanisms work under realistic failure conditions."

## Backpressure (`backpressure`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/backpressure.md`

### Claims

- "Backpressure is the mechanism by which a downstream component signals its capacity to upstream components, creating a feedback loop that prevents overload." _(certainty: high)_
- "Backpressure propagates capacity information against the direction of data flow — downstream saturation is communicated upstream so upstream can reduce its emission rate." _(certainty: high)_
- "Without backpressure, a downstream component can be overwhelmed by upstream production that exceeds its processing capacity." _(certainty: high)_
- "Backpressure can be implemented at multiple levels: TCP receive window (transport), gRPC flow control (RPC), message queue credits (application)." _(certainty: high)_
- "Backpressure is distinct from load shedding — backpressure reduces upstream emission; load shedding drops excess requests at the current level." _(certainty: high)_

### Relationships

- **prevents** → `cascading-failure`
- **reduces** → `retry-storm-amplification`
- **complementary_to** → `circuit-breaker`
- **interacts_with** → `quorum`

### Constraints

- "Backpressure cannot increase total system capacity — it can only distribute load within existing capacity constraints."
- "Backpressure propagation has latency — a downstream overload can persist for one propagation cycle before the upstream responds."

### Recommendations

- "Implement explicit backpressure at every asynchronous boundary in the system — implicit backpressure (TCP) only covers transport-level flow."
- "Monitor backpressure signals as leading indicators of saturation — backpressure activation precedes circuit-breaker activation."
- "Test backpressure behaviour under load patterns that exceed capacity — validate that signals propagate correctly and upstreams honour them."

## Backup Recovery (`backup-recovery`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/backup-recovery.md`

### Claims

- "Backup recovery is the discipline of restoring data to a defined point after loss — a recovery capability, not a storage practice." _(certainty: high)_
- "RPO and RTO are the recovery contract — how much data loss is acceptable and how fast recovery must be." _(certainty: high)_
- "Backup validity is derivation — a backup is valid if it faithfully represents the source at its snapshot point." _(certainty: high)_
- "An untested backup is a claim — restorability is only established by actually restoring." _(certainty: high)_
- "Recovery is the proof of the system's failure tolerance — every other guarantee is exercised at recovery time." _(certainty: high)_

### Relationships

- **restores** → `data-integrity`
- **supported_by** → `atomicity`
- **guards** → `schema-migration`
- **governed_by** → `data-governance`
- **analogous_to** → `build-systems`

### Constraints

- "Backup validity is a derivation claim — a backup is valid only if it faithfully represents its source at snapshot."
- "Recovery must meet the stated contract — RPO/RTO violations are operational failures, not details."

### Recommendations

- "Verify restorability continuously, not at incident time."
- "Define RPO/RTO explicitly and review them as the contract changes."
- "Practice incident-time recovery in realistic environments."

## Behavioural Observation of Artifacts (`behavioral-observation`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/behavioral-observation.md`

### Claims

- "Behavioural observation is the record of what an artifact does when executed or engaged — the action sequence is the analyst's primary window on the artifact." _(certainty: high)_
- "Behaviour is observed, not read — an execution trace is a sequence of recorded actions, and interpretation of the sequence is a separate step." _(certainty: high)_
- "Observed behaviour is conditional — the same artifact behaves differently across environments, inputs, and conditions of observation." _(certainty: high)_
- "Observation changes the observed — an artifact aware of being watched may behave differently than one that is not." _(certainty: high)_
- "A behavioural record is a sequence of recorded actions — individual events compose into the behaviour." _(certainty: high)_

### Relationships

- **describes** → `artifact`
- **produces** → `observable-evidence`
- **feeds** → `threat-detection`
- **constrained_by** → `perception-uncertainty`
- **subject_to** → `incomplete-evidence`

### Constraints

- "A behavioural record is valid only under its observation conditions — environment, instrumentation, and inputs are part of the record."
- "Observation does not exhaust behaviour — unobserved phases are unknown, not absent."

### Recommendations

- "Record behaviour at event granularity — a trace is a sequence of atomic actions."
- "Cross-check behaviour across observation conditions before drawing conclusions."
- "Qualify every behavioural claim by its capture conditions."

## Belief State (`belief-state`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/belief-state.md`

### Claims

- "A belief state is the system's internal model of the world — a distribution over possible states, expressed as claims qualified by confidence." _(certainty: high)_
- "Belief is composition, not ontology — a belief state is a set of qualified observations combined through a model, never a new knowledge type." _(certainty: high)_
- "The epistemic gap lives inside the belief — belief is about the model, never about reality directly." _(certainty: high)_
- "Confidence is the qualification that carries distance — the same structure as uncertainty (007) and probabilistic outputs (008)." _(certainty: high)_
- "A belief state is valid only under the observations and model that produced it — stale or mismatched beliefs invalidate decisions." _(certainty: high)_

### Relationships

- **produced_by** → `state-estimation`
- **informs** → `actuation`
- **analogous_to** → `probabilistic-outputs`
- **describes** → `physical-state`
- **constrained_by** → `incomplete-evidence`

### Constraints

- "A belief is valid only under the observations and model that produced it — overconfidence is a failure of qualification, not of perception."
- "Decisions act on belief, never on reality directly — the epistemic gap is structural, closed only by verification."

### Recommendations

- "Represent belief as qualified observation composition, never as a belief construct."
- "Treat overconfidence as the belief failure mode to manage."
- "Update belief on new observation — the loop closes at the next sensing."

## Benchmark Validity (`benchmark-validity`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/benchmark-validity.md`

### Claims

- "A benchmark is a measurement instrument — its score is evidence about the model only within the benchmark's scope." _(certainty: high)_
- "Benchmark scores are upper bounds on demonstrated performance, not ground truth about capability." _(certainty: high)_
- "Benchmark contamination — benchmark content in training data — inflates scores and invalidates the measurement." _(certainty: high)_
- "Benchmark validity decays — benchmarks saturate as models train on them and their ability to discriminate capability diminishes." _(certainty: high)_
- "Benchmarks are proxies for capability — they measure proxy tasks and inherit the proxy's blind spots." _(certainty: high)_

### Relationships

- **estimates** → `generalization`
- **contaminated_by** → `training-data`
- **measures** → `hallucination`
- **governed_by** → `metric-selection`
- **complements** → `human-evaluation`
- **evaluates** → `alignment`

### Constraints

- "A benchmark score is evidence only within the benchmark's stated scope."
- "A benchmark whose content has entered training data can no longer measure the model."

### Recommendations

- "Treat benchmarks as measurement instruments with stated scope, not as capability verdicts."
- "Keep benchmark content out of training data by exclusion list and audit."
- "Complement static benchmarks with task-matched, fresh evaluation at deployment time."

## Browser Fingerprint (`browser-fingerprint`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/browser-fingerprint.md`

### Claims

- "Canvas fingerprint has 4-6 bits of entropy and is the most commonly collected fingerprint dimension across anti-bot services." _(certainty: high)_
- "WebGL fingerprint has 12-15 bits of entropy, making it the single highest-entropy dimension. It is tied to physical GPU hardware and cannot be changed without changing hardware or using GPU virtualization." _(certainty: high)_
- "Fresh profiles on cloud VMs (no dedicated GPU) produce near-identical fingerprints because they share SwiftShader software rendering, default screen resolution, and minimal font sets." _(certainty: high)_
- "Fingerprint entropy decreases in homogeneous environments (cloud VMs, containers), providing crowd anonymity but reducing the effectiveness of fingerprint-based session blocking." _(certainty: medium)_
- "Audio fingerprint provides an independent detection dimension that is harder to patch consistently than canvas or WebGL." _(certainty: medium)_

### Relationships

- **derived_from** → `automation-detection-surface`
- **targeted_by** → `anti-detection-strategy`
- **amplified_by** → `browser-profile`
- **persists_via** → `browser-storage`
- **established_at** → `browser-session-lifecycle`

### Constraints

- "WebGL fingerprint is tied to physical GPU hardware; software-only fingerprint manipulation cannot change the GPU-specific values returned by the driver."
- "Canvas fingerprint varies between operating systems, GPU drivers, and browser versions. A fingerprint generated on one system will not match another, even with identical browser configuration."
- "Font enumeration returns the OS-installed font set. In headless Linux environments, this is typically 30-100 fonts vs 200-500+ on a normal desktop, creating a detectable mismatch."
- "Headless mode (pre-112) reports `navigator.gpu` as absent and WebGL renderer as SwiftShader. `--headless=new` reduces but does not eliminate these differences."
- "Fingerprint dimension values can change with browser updates, OS updates, GPU driver updates, or hardware changes. No single dimension is fully stable across time."

### Recommendations

- "Use fresh profile per session to break cross-session fingerprint linking as the primary anti-detection mechanism."
- "In cloud automation environments, introduce per-instance viewport and timezone variation to avoid fingerprint collision blocking."
- "Do not rely solely on canvas fingerprint for cross-session identification — WebGL + canvas + font enumeration provides more reliable identification across software updates."
- "Patch audio fingerprint alongside canvas and WebGL — it is an independent detection dimension that is commonly collected but less commonly patched."

## Isolated Browser Profiles (`browser-profiles-concept`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/browser-profiles-concept.md`

### Claims

- "A browser profile is an isolated storage directory containing all persistent browser state." _(certainty: high)_
- "Profiles are fully isolated from each other; one profile cannot access another's data." _(certainty: high)_
- "Fresh profiles eliminate storage-based tracking; clearing cookies alone leaves IndexedDB and Cache API data intact." _(certainty: high)_
- "IndexedDB-based supercookies can survive cookie clear operations." _(certainty: medium)_

### Relationships

- **contains** → `browser-session-lifecycle`
- **contains** → `browser-storage`
- **influences** → `memory-pressure`
- **influences** → `anti-detection-principle`
- **influences** → `navigation-lifecycle`

### Constraints

- "Only one browser instance can use a profile at a time."
- "Chrome for Testing terminates when all CDP sessions disconnect; full Chrome persists with the profile."
- "Profile format may change between browser versions, requiring migration."
- "Cross-origin iframe storage within a profile is isolated per origin."

### Recommendations

- "Use fresh profiles per session for production automation."
- "Use persistent profiles only when authentication state must survive sessions."
- "Use Playwright browser contexts for automatic per-session profile isolation."
- "Implement profile age monitoring if using persistent profiles."

## Build Systems (`build-systems`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/build-systems.md`

### Claims

- "A build system derives artifacts from sources through a dependency graph — the graph defines what must rebuild when anything changes." _(certainty: high)_
- "Artifact validity is the core correctness property — an artifact is valid if and only if it was derived from the current sources and toolchain state." _(certainty: high)_
- "Incremental builds are caching over the dependency graph — correctness requires invalidation to match the dependency relation exactly." _(certainty: high)_
- "The dependency graph is an engineering artifact with its own failure modes — missing edges produce stale artifacts; extra edges produce rebuild storms." _(certainty: high)_
- "Build reproducibility depends on hermeticity — builds that consume ambient state (time, network, environment) cannot be reproduced or trusted." _(certainty: high)_

### Relationships

- **constrains** → `compiler-performance`
- **executes** → `optimization-tradeoffs`
- **produces** → `debug-vs-release-modes`
- **invokes** → `compiler-optimization`

### Constraints

- "Artifact validity is defined by derivation — an artifact is valid only if derived from current sources and toolchain state."
- "Invalidation must match the dependency relation exactly — over-invalidation wastes builds; under-invalidation ships stale artifacts."

### Recommendations

- "Derive invalidation from the declared dependency graph, and test the graph."
- "Make builds hermetic — pin toolchains and eliminate ambient-state dependence."
- "Compare incremental and clean builds as a routine check."

## CAP Theorem (`cap-theorem`)

| Field | Value |
|---|---|
| kind | principle |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/cap-theorem.md`

### Claims

- "CAP theorem states that a distributed data store can simultaneously provide at most two of three guarantees: Consistency, Availability, and Partition Tolerance." _(certainty: high)_
- "During a network partition, a distributed system must choose between consistency (return an error or timeout) and availability (return potentially stale data)." _(certainty: high)_
- "CAP theorem is often misinterpreted as 'choose 2 of 3 at all times' — the choice only applies during partitions; outside partitions, all three can be provided." _(certainty: high)_
- "Partition Tolerance is not a choice — distributed systems over a network must tolerate partitions because networks can fail." _(certainty: high)_
- "The real CAP trade-off is not 'pick two' but 'how to behave during a partition': reduce consistency or reduce availability." _(certainty: high)_
- "CAP applies to state, not computation — stateless services are not constrained by CAP." _(certainty: high)_

### Relationships

- **explains** → `eventual-consistency`
- **explains** → `strong-consistency`
- **frames** → `availability`
- **constrains** → `quorum`
- **relevant_to** → `network-partition-recovery`

### Constraints

- "During a network partition, a distributed system must sacrifice either consistency or availability — this is provable, not a design preference."
- "Outside of a partition, a distributed system can provide all three properties — CAP is a partition-specific constraint, not a universal one."

### Recommendations

- "Treat CAP as a partition-specific design constraint, not a universal property selection — the 'choose two' framing is misleading."
- "Document partition behaviour explicitly in architecture decisions — how the system behaves during a partition is a design choice, not an accident of implementation."
- "Validate CAP assumptions through partition testing (network fault injection) before production deployment."

## Cascading Failure (`cascading-failure`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/cascading-failure.md`

### Claims

- "A cascading failure is a failure that propagates through a system as each component's failure increases the load on remaining components." _(certainty: high)_
- "Cascading failures follow a characteristic pattern: initial failure → load redistribution → remaining components exceed capacity → secondary failures." _(certainty: high)_
- "The propagation speed of a cascading failure depends on the coupling between components — tightly coupled systems fail faster." _(certainty: high)_
- "Cascading failures are not caused by the initial failure alone — they require overload of the remaining capacity to propagate." _(certainty: high)_
- "Cascading failures can be arrested if the remaining capacity can absorb the redistributed load or if load shedding is activated in time." _(certainty: high)_

### Relationships

- **triggers** → `retry-storm-amplification`
- **similar_to** → `network-failure-propagation`
- **prevents** → `circuit-breaker`
- **prevents** → `backpressure`
- **worsens** → `split-brain`

### Constraints

- "Total system capacity is always less than the sum of component capacities during a cascade — redistributed load has overhead."
- "A cascading failure cannot be stopped without either adding capacity or reducing load — one of these must happen before the cascade completes."

### Recommendations

- "Implement automatic load shedding at 80% of component capacity — waiting for 100% risks uncontrolled cascade."
- "Map cascade boundaries explicitly — document which component failures can propagate to which dependent components."
- "Test cascade scenarios under production-like load — idle-system cascade behaviour differs significantly from loaded-system behaviour."

## Chrome DevTools Protocol Mechanics (`cdp-mechanics`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/cdp-mechanics.md`

### Claims

- "CDP uses JSON-RPC 2.0 over WebSocket with a command model of method/params/id and an event model of server-push method/params." _(certainty: high)_
- "CDP exposes approximately 30 domains covering debugging, rendering, network, input, storage, and profiling." _(certainty: high)_
- "CDP target model enables multi-tab control over a single WebSocket connection via Target.attachToTarget and Target.createTarget." _(certainty: high)_
- "CDP session model uses targetId routing — each command targets a specific tab or worker within the browser." _(certainty: high)_
- "CDP detection signals include navigator.webdriver, chrome.app.isInstalled, WebSocket upgrade header, and /json endpoint presence." _(certainty: high)_

### Relationships

- **specialises** → `automation-protocol`
- **exposes** → `automation-detection-surface`
- **controls** → `browser-session-lifecycle`
- **contrasts_with** → `webdriver-classic`

### Constraints

- "CDP is Chromium-only; no other browser engine implements it."
- "CDP version is tied to Chromium release version; breaking changes occur per release."

### Recommendations

- "Use CDP directly only when WebDriver BiDi does not provide required capability."
- "Pin Chromium version in production CDP automation to prevent protocol version mismatch."

## Circuit Breaker (`circuit-breaker`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/circuit-breaker.md`

### Claims

- "A circuit breaker is a resilience pattern that detects failures and prevents calls to a failing component until it is likely to recover." _(certainty: high)_
- "Circuit breakers operate in three states: closed (normal operation), open (failing fast), and half-open (testing recovery)." _(certainty: high)_
- "The transition from open to half-open occurs after a cooldown period — a single probe request tests whether the downstream component has recovered." _(certainty: high)_
- "Circuit breakers prevent cascading failures by failing fast instead of waiting for timeouts — this preserves thread and connection pool capacity." _(certainty: high)_
- "Circuit breakers are complementary to retry — retries handle transient failures; circuit breakers handle sustained failures." _(certainty: high)_

### Relationships

- **prevents** → `cascading-failure`
- **prevents** → `retry-storm-amplification`
- **complementary_to** → `backpressure`
- **interacts_with** → `rolling-deployment`
- **protects** → `availability`
- **similar_to** → `raft-consensus`

### Constraints

- "A circuit breaker cannot distinguish between a downstream failure and increased latency — both count toward the failure threshold."
- "Circuit breaker state is local to each caller — different callers may have different circuit states for the same downstream component."

### Recommendations

- "Deploy circuit breakers at every synchronous dependency boundary — any component that calls another component synchronously should be protected."
- "Instrument circuit breaker state as a observable metric with alerts on state transitions — open circuit breaker is an operational event."
- "Test circuit breaker behaviour under realistic failure patterns — circuit breakers configured in isolation behave differently under cascading conditions."

## Closed-Loop Guarantee (`closed-loop-guarantee`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/closed-loop-guarantee.md`

### Claims

- "A closed-loop guarantee is the scoped claim that the loop holds its specified behaviour under stated conditions — the fifth guarantee object." _(certainty: high)_
- "The guarantee structure is unchanged: scoped claim + invariants + failure modes + verification evidence — joining type-safety (009), data-integrity (010), atomicity (010), and real-time-guarantee (011)." _(certainty: high)_
- "The guarantee is valid only under its conditions — plant model, envelope, measurement quality, and timing bound the claim." _(certainty: high)_
- "The guarantee is verified, not assumed — stability analysis, simulation, and test are the evidence." _(certainty: high)_
- "The guarantee-object motif reaches n=5 across five engineering categories — composition, not coincidence." _(certainty: high)_

### Relationships

- **guaranteed_by** → `feedback-control`
- **depends_on** → `stability`
- **analogous_to** → `type-safety`
- **analogous_to** → `data-integrity`
- **analogous_to** → `real-time-guarantee`

### Constraints

- "The closed-loop guarantee is valid only under its stated conditions — envelope and model bound it."
- "A guarantee without verification evidence is a claim, not a guarantee."

### Recommendations

- "Represent the closed-loop guarantee as scoped claim + invariants + failure modes + verification evidence."
- "State the envelope with the guarantee."
- "Re-verify the guarantee when the plant model or envelope changes."

## Cluster 1 C2 Infrastructure (`cluster-1-c2-infrastructure`)

| Field | Value |
|---|---|
| kind | concept |
| domain | threat-analysis |
| research_cycle | "015" |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/cluster-1-c2-infrastructure.md`

### Claims

- "Cluster 1 is the primary C2 cluster: five domains registered through a privacy service with hosting in two providers, and four VPS endpoints, plus relays, DNS glue, lure infrastructure, and one suspected host from the appendix." _(certainty: high)_
- "Hammer variants phone home to Cluster 1 sinks; each victim observed a different callback domain." _(certainty: high)_
- "One appendix host (telemetry-12) is a suspected C2 with no confirmed callback." _(certainty: high)_

### Relationships

- **part_of** → `midnight-foundry-campaign`
- **linked_to** → `hammer-backdoor-family`
- **linked_to** → `unassigned-hosts`
- **linked_to** → `per-victim-operational-separation`

### Constraints

- "Cluster 1 claims cover the assigned hosts only; staging and unassigned hosts are separate objects."

## Cluster 2 Staging Infrastructure (`cluster-2-staging-infrastructure`)

| Field | Value |
|---|---|
| kind | concept |
| domain | threat-analysis |
| research_cycle | "015" |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/cluster-2-staging-infrastructure.md`

### Claims

- "Cluster 2 is the staging cluster: two file-staging hosts and three VPS endpoints used for exfil staging and module hosting, plus appendix module and archival hosts." _(certainty: high)_
- "The module host is the only cross-victim infrastructure overlap observed: it served Hammer-B modules to both Victim B and Victim D." _(certainty: high)_
- "One Cluster 2 VPS sits in an IP range previously used by K7 infrastructure — the single strongest piece of evidence in the competing-hypothesis debate." _(certainty: high)_

### Relationships

- **part_of** → `midnight-foundry-campaign`
- **linked_to** → `hammer-b-variant`
- **linked_to** → `exfiltration-pattern`
- **linked_to** → `k7-overlap`

### Constraints

- "Cluster 2 claims cover the staging hosts only; the C2 cluster is a separate object."

## Collection Pattern (`collection-pattern`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | threat-analysis |
| research_cycle | "015" |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/collection-pattern.md`

### Claims

- "Collection focused on engineering workstations, CAD files, and sensor-test data, with the Rivet stealer the only custom collection tool, on Victim C." _(certainty: high)_
- "The collection focus is consistent with programmatic rather than opportunistic collection — a reading the source records, not a demonstrated fact." _(certainty: medium)_
- "Collection activity was consistent with persistent collection; no confirmed operational impact resulted." _(certainty: high)_

### Relationships

- **part_of** → `midnight-foundry-campaign`
- **linked_to** → `rivet-stealer`
- **linked_to** → `exfiltration-pattern`

### Constraints

- "The pattern records the observed collection focus; intent readings are labeled as interpretations."

### Recommendations

- "Record collection targets (workstation class, file classes) as observables independent of any intent assessment."

## Compensating Controls (`compensating-controls`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/compensating-controls.md`

### Claims

- "A compensating control is an alternative control that reduces risk to an acceptable level when the required primary control cannot be implemented." _(certainty: high)_
- "Compensation is valid only when the alternative control demonstrably achieves an equivalent or better risk reduction — intent alone is insufficient." _(certainty: high)_
- "Compensating controls are accepted on the basis of effectiveness evidence, not equivalence of mechanism — the risk outcome must match, not the control type." _(certainty: high)_
- "Compensation is distinct from acceptance — compensation actively reduces risk via an alternative; acceptance tolerates the residual without an alternative." _(certainty: high)_
- "Compensating controls are most defensible when paired with enhanced detection and monitoring of the compensated risk." _(certainty: high)_

### Relationships

- **distinguishes_from** → `risk-acceptance`
- **reduces** → `residual-risk`
- **contributes_to** → `defense-in-depth`
- **applies_to** → `vulnerability-management`
- **enhances** → `threat-detection`

### Constraints

- "Compensation without effectiveness evidence is not compensation — it is a claim."
- "Compensation cannot reduce risk below what the compensated exposure allows — some residual always remains."

### Recommendations

- "Document the risk-reduction evidence for every compensating control — the alternative must demonstrate outcome equivalence."
- "Pair compensation with enhanced monitoring of the compensated risk — monitoring is both the control and the early warning."
- "Reclassify claimed compensations without evidence as risk acceptance — honest classification improves governance."

## Competing Hypotheses in Artifact Analysis (`competing-hypotheses`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/competing-hypotheses.md`

### Claims

- "The same evidence supports multiple reconstructions of the artifact — competing hypotheses are the normal state of analysis, not its failure." _(certainty: high)_
- "A hypothesis is a reading of the artifact evaluated against evidence — multiple readings of the same record are the normal state of analysis." _(certainty: high)_
- "Hypotheses are the analyst's reading set, not properties of the artifact — the artifact is one object; the plurality lives in the analyst's knowledge." _(certainty: high)_
- "Resolution comes from discriminative evidence — evidence that distinguishes between readings — not from more confidence in any single one." _(certainty: high)_
- "An unbounded reading set is a failure of discipline, not of evidence — hypothesis proliferation is managed, not suffered." _(certainty: high)_

### Relationships

- **based_on** → `observable-evidence`
- **describes** → `artifact`
- **resolves** → `surface-ambiguity`
- **alternative_to** → `inference-from-behavior`
- **constrained_by** → `incomplete-evidence`
- **informed_by** → `likelihood`

### Constraints

- "A hypothesis is a reading, never a fact — the reading set is structure over evidence, and the artifact is not changed by how it is read."
- "Resolution requires discriminative evidence — eliminating a candidate is an evidence act, not a confidence act."

### Recommendations

- "Evaluate new evidence against the reading set, not within it."
- "Prune the reading set by discriminative testability."
- "Weight evidence by discriminative force, not by support for the favourite."

## Compiler Correctness (`compiler-correctness`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/compiler-correctness.md`

### Claims

- "Compiler correctness is semantic preservation — the compiler is correct if every program it compiles behaves per the source's semantics." _(certainty: high)_
- "Miscompilation is the correctness failure mode — a compiler defect that produces wrong behaviour for correct source, distinct from rejecting valid input." _(certainty: high)_
- "Compiler correctness is never established by testing alone — the input space is unbounded and the failure modes are rare and input-specific." _(certainty: high)_
- "Correctness evidence accumulates from multiple channels — differential testing, conformance suites, formal verification, and real-world volume." _(certainty: high)_
- "Correctness is relative to a stated observation model — the compiler preserves the observable behaviour the language defines, not unspecified behaviour." _(certainty: high)_

### Relationships

- **preserves** → `program-semantics`
- **constrains** → `intermediate-representation`
- **must_preserve** → `type-safety`
- **supported_by** → `formal-verification`
- **verified_by** → `equivalence-checking`
- **depends_on** → `optimization-pass`
- **affected_by** → `debug-vs-release-modes`

### Constraints

- "The compiler must preserve the source's defined behaviour — divergence is a correctness failure regardless of how rarely it triggers."
- "Correctness claims are valid under the language's observation model — unspecified behaviour is outside the preservation obligation."

### Recommendations

- "Run differential testing continuously across optimization levels and releases."
- "Formalize the observation model the compiler is allowed to change."
- "Verify high-value transformations with equivalence checking before release."

## Compiler Optimization (`compiler-optimization`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/compiler-optimization.md`

### Claims

- "A compiler optimization is a transformation of a program's representation that preserves observable semantics while improving a target cost (speed, size, energy)." _(certainty: high)_
- "Optimization correctness is semantic preservation — a transformation that changes program meaning is a miscompilation, not an optimization." _(certainty: high)_
- "Every optimization has enabling conditions — a transformation is valid only when its preconditions (analysis results, dominance, liveness, constancy) hold." _(certainty: high)_
- "Optimizations trade target costs against each other and against compilation time — speed, size, and build time are competing objectives." _(certainty: high)_
- "Optimization validity is relative to the observation model — transformations legal under input-output equivalence may be illegal under stricter behavioural observation." _(certainty: high)_

### Relationships

- **operates_on** → `abstract-syntax-tree`
- **operates_on** → `intermediate-representation`
- **preserves** → `program-semantics`
- **organized_as** → `optimization-pass`
- **includes** → `constant-folding`
- **includes** → `dead-code-elimination`
- **verified_by** → `equivalence-checking`
- **driven_by** → `compiler-performance`

### Constraints

- "Every optimization must preserve observable semantics — meaning change is a correctness failure, not a feature."
- "A transformation is valid only where its enabling conditions hold — applying it elsewhere is unsound by construction."

### Recommendations

- "State the enabling conditions of every transformation and gate its application on them."
- "Treat each optimization as a hypothesis — test it differentially against unoptimized output."
- "Define the observation model the optimizer is allowed to change, and document it."

## Compiler Performance (`compiler-performance`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/compiler-performance.md`

### Claims

- "Compiler performance has two axes — the quality of the generated code and the cost of compilation itself (time, memory)." _(certainty: high)_
- "Generated-code performance is measured by benchmarks — the instruments define what 'fast' means, and benchmark validity bounds the measurement." _(certainty: high)_
- "Performance is a distribution, not a point — benchmark noise, hardware variation, and input dependence make single-number claims misleading." _(certainty: high)_
- "Optimizations trade axes against each other — faster generated code can cost compile time, binary size, or debuggability." _(certainty: high)_
- "Performance regressions are detectable only with disciplined measurement — without baselines and noise control, regressions hide in the noise." _(certainty: high)_

### Relationships

- **driven_by** → `compiler-optimization`
- **informed_by** → `optimization-tradeoffs`
- **constrained_by** → `build-systems`
- **affected_by** → `optimization-pass`
- **differentiated_by** → `debug-vs-release-modes`

### Constraints

- "Performance claims are valid only within the benchmark's validity — the instrument bounds the claim."
- "Optimization must not trade correctness for performance — a faster miscompilation is still a miscompilation."

### Recommendations

- "Maintain continuous benchmark baselines with noise controls."
- "Validate performance changes against diverse real workloads, not just benchmarks."
- "Never accept a correctness risk for a benchmark gain."

## Concealed Intent of Artifacts (`concealed-intent`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/concealed-intent.md`

### Claims

- "The artifact's intent is the creator's design state — why the artifact is shaped this way — and it is withheld by design, never presented with the artifact." _(certainty: high)_
- "Intent is accessed only through the artifact — every claim about the creator's purpose is an inference through the object, never a direct observation." _(certainty: high)_
- "Intent claims stand furthest removed from direct observation — an inference about a creator's state, inferred from an artifact, inferred from behaviour, observed." _(certainty: high)_
- "Intent is reconstructed from the artifact's form — the purpose is read from the object's sacrifices, choices, and structure, never from a direct account." _(certainty: high)_
- "The intent claim is the weakest-evidenced and highest-stakes claim in the analysis — it decides response, and its evidence is the thinnest." _(certainty: high)_

### Relationships

- **grounded_in** → `artifact`
- **derived_from** → `inference-from-behavior`
- **constrained_by** → `design-under-concealment`
- **informs** → `attribution`
- **describes** → `threat-actor`

### Constraints

- "The creator's intent is accessed only through the artifact — intent claims are inferences, never direct observations."
- "An intent claim is derived and marked as derived — purpose treated as a fact is the corruption the analysis is most vulnerable to."

### Recommendations

- "Record alternative design states alongside the claimed intent."
- "Qualify intent claims by their full evidence chain."
- "Treat intent claims as derived, always — never as facts about the artifact."

## Confidence in Security Judgement (`confidence`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/confidence.md`

### Claims

- "Confidence is a property of a security judgement, not of the system being judged — it qualifies the quality of the evidence and reasoning behind a claim." _(certainty: high)_
- "Confidence can be high even when certainty is low — a well-evidenced probabilistic judgement can carry high confidence in its own reliability." _(certainty: high)_
- "Confidence degrades with evidence quality, evidence age, and conflicting signals — stale intelligence produces lower confidence conclusions." _(certainty: high)_
- "Security decisions made without expressed confidence levels mask the true uncertainty of the underlying judgement." _(certainty: high)_
- "Confidence is not transferable between contexts — high confidence in one environment does not imply high confidence in a different deployment." _(certainty: high)_

### Relationships

- **qualifies** → `likelihood`
- **limited_by** → `incomplete-evidence`
- **informs** → `risk-acceptance`
- **affects** → `threat-detection`

### Constraints

- "Confidence cannot exceed the quality of the underlying evidence — high confidence on weak evidence is a contradiction, not a judgement."
- "Confidence is always time-bound — evidence ages, environments change, and confidence must decay accordingly."

### Recommendations

- "Include an explicit confidence statement with rationale in every security risk assessment."
- "Audit confidence calibration quarterly — compare expressed confidence against actual outcomes."
- "Act on high-impact low-confidence threats with reversible, low-cost mitigations rather than ignoring them."

## Confidence Calibration (`confidence-calibration`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/confidence-calibration.md`

### Claims

- "Confidence calibration is the alignment between a model's stated confidence and its observed accuracy — a calibrated model is accurate in proportion to its confidence." _(certainty: high)_
- "Calibration is measurable independently of accuracy (expected calibration error, reliability diagrams) and degrades independently of raw accuracy." _(certainty: high)_
- "Calibration is fragile across distribution shifts — a model calibrated on its training distribution is often miscalibrated elsewhere." _(certainty: high)_
- "Calibration and accuracy are independent properties — an accurate model can be poorly calibrated and vice versa." _(certainty: high)_
- "Calibration loss is typically invisible in aggregate metrics — average accuracy can remain high while per-prediction confidence is systematically wrong." _(certainty: high)_

### Relationships

- **qualified_by** → `likelihood`
- **validates** → `uncertainty-estimation`
- **evaluates** → `probabilistic-outputs`
- **mitigates** → `hallucination`
- **depends_on** → `generalization`
- **degraded_by** → `distribution-shift`

### Constraints

- "A model cannot be calibrated on distributions it has never seen — calibration is distribution-bound."
- "Calibration cannot be inferred from accuracy — the two must be measured separately."

### Recommendations

- "Report calibration metrics alongside accuracy for any confidence-scored model."
- "Re-calibrate after deployment whenever the input distribution changes."
- "Set decision thresholds from calibration curves, not from point accuracy."

## Confidence Threshold Decision (`confidence-threshold`)

| Field | Value |
|---|---|
| kind | decision |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/confidence-threshold.md`

### Claims

- "The confidence threshold decision is where the reconstruction's confidence becomes a decision rule — the qualification is operationalised into a cut-off for action." _(certainty: high)_
- "The threshold is a decision, not a property of confidence — confidence measures the chain; the threshold says what the organisation will act on." _(certainty: high)_
- "The threshold inherits the asymmetry of the domain — under concealment, the cost of the two error directions is never equal, and the threshold prices it." _(certainty: high)_
- "The threshold is qualified by the same evidence chain as the decisions it governs — a threshold is only as honest as the calibration behind it." _(certainty: high)_
- "The threshold prices the error asymmetry — under concealment, the two error directions never cost the same." _(certainty: high)_

### Relationships

- **operates_on** → `reconstruction-confidence`
- **governs** → `detection-decision`
- **informed_by** → `competing-hypotheses`
- **applies_to** → `confidence`
- **calibrates** → `likelihood`

### Constraints

- "A threshold is a decision, never a property of confidence — the qualification measures, the organisation cuts."
- "The threshold prices the error asymmetry of concealment — symmetric thresholds on concealed artifacts are mispriced."

### Recommendations

- "Hold the threshold for a decision window; revise on calibration evidence."
- "Record the chain's calibration ceiling with every threshold."

## Constant Folding (`constant-folding`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/constant-folding.md`

### Claims

- "Constant folding is the compile-time evaluation of constant expressions — replacing a computable expression with its value." _(certainty: high)_
- "Folding preserves semantics only when the operands are truly constant under the language's rules — value-dependent effects break the precondition." _(certainty: high)_
- "Folding interacts with undefined and implementation-defined behaviour — integer overflow, division by zero, and rounding rules decide what folding is legal." _(certainty: high)_
- "Folding is the simplest transformation — no control flow, no liveness, just value computation — making it the canonical test case for transformation correctness." _(certainty: high)_
- "Folding shifts work from runtime to compile time — the tradeoff is compile-time cost against the runtime value of the eliminated computation." _(certainty: high)_

### Relationships

- **instance_of** → `compiler-optimization`
- **operates_on** → `abstract-syntax-tree`
- **preserves** → `program-semantics`
- **verifiable_by** → `equivalence-checking`
- **bounded_by** → `compiler-correctness`

### Constraints

- "Folding is legal only for verified constant operands under well-defined semantics — any other fold is a miscompilation."
- "The folded value must equal the evaluated expression under the language's rules — standards compliance bounds folding."

### Recommendations

- "Fold only expressions verified constant by analysis and well-defined by the language standard."
- "Differential-test folding against unoptimized evaluation on edge cases."
- "Cap folding work per expression to bound pathological compile time."

## Containment Decision on Incomplete Reconstruction (`containment-decision`)

| Field | Value |
|---|---|
| kind | decision |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/containment-decision.md`

### Claims

- "The containment decision is whether and how far to isolate the artifact — a decision taken while the reconstruction is still open." _(certainty: high)_
- "Containment is decided before the reconstruction is complete — the point of containment is to act while the artifact's reach is still unknown." _(certainty: high)_
- "Containment decisions are qualified by the reconstruction's confidence and bounded by its gaps — the unknown reach is part of the decision's evidence." _(certainty: high)_
- "Containment is a decision about unknown reach — what isolation cannot see is what isolation must bound." _(certainty: high)_
- "Containment can be staged — the decision is not binary; isolation depth is chosen against the reconstruction's openness." _(certainty: high)_

### Relationships

- **triggered_by** → `detection-decision`
- **informed_by** → `concealed-intent`
- **qualified_by** → `reconstruction-confidence`
- **constrained_by** → `incomplete-evidence`
- **serves** → `incident-response`

### Constraints

- "Containment inherits the reconstruction's qualification — a containment call cannot be more certain than the reach claim it bounds."
- "Containment is staged by confidence — isolation depth is chosen against the openness of the reconstruction, and is revisable as it closes."

### Recommendations

- "Record the unknown reach explicitly before choosing isolation depth."
- "Set isolation scope from the unknown reach's bound, not the known reach."
- "Stage containment and revise as the reconstruction closes."

## Control-Scheduling Interaction (`control-scheduling-interaction`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/control-scheduling-interaction.md`

### Claims

- "The control-scheduling interaction is where temporal guarantees (011) meet physical control (012) — the loop's correctness depends on when computations complete." _(certainty: high)_
- "Sampling jitter and delay are temporal constraints on the loop — the 011 deadline structure applied inside the control cycle." _(certainty: high)_
- "The interaction is a composition pattern — scheduling constrains control timing, control demands scheduling service, neither is a new construct." _(certainty: high)_
- "The interaction's failure is temporal — jitter, missed periods, and delayed actuation degrade the loop before the logic fails." _(certainty: high)_
- "Temporal constraint density rises at this tier — the interaction tier is the temporal-epistemic junction, reconnecting 012 to the 011 signal." _(certainty: high)_

### Relationships

- **afflicts** → `feedback-control`
- **analogous_to** → `task-scheduling`
- **constrained_by** → `deadline`
- **supports** → `closed-loop-guarantee`
- **serves** → `cyber-physical-system`

### Constraints

- "The control loop's temporal behaviour is a stated condition on its guarantees — jitter and delay bound the claim."
- "A loop whose timing conditions are unstated has no guarantee."

### Recommendations

- "Represent the interaction as relationships between the control and scheduling corpora — no interaction construct."
- "Declare the loop's timing conditions with the guarantee."
- "Monitor jitter as a first-class disturbance."

## Cyber-Physical System (`cyber-physical-system`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/cyber-physical-system.md`

### Claims

- "A cyber-physical system is a system whose correctness depends on continuous interaction with an external physical world — sensing, computation, and actuation in one loop." _(certainty: high)_
- "The physical plant is part of the system: the boundary between computer and world is architectural, not epistemic — no new knowledge type separates them." _(certainty: high)_
- "Correctness in a cyber-physical system is a claim about behaviour in the physical world, bound by stated conditions about dynamics, environment, and timing." _(certainty: high)_
- "The system's knowledge about the world is always indirect — internal belief is derived from sensors through models, never observed directly." _(certainty: high)_
- "Cyber-physical guarantees are the unification-hypothesis test at the physical pole — valid if stated conditions hold, exactly as knowledge (008), actions (009), data (010), and completion (011) are." _(certainty: high)_

### Relationships

- **requires** → `physical-state`
- **requires** → `sensing`
- **requires** → `actuation`
- **analogous_to** → `real-time-system`
- **analogous_to** → `schema-design`

### Constraints

- "Internal belief about the world is valid only under its model's stated conditions — model mismatch invalidates decisions, not the schema."
- "Every physical action is taken on a belief, never on direct knowledge of reality — the epistemic gap is closed by verification, not eliminated."

### Recommendations

- "Express dynamics as constraints on state evolution, not as a continuous-state category."
- "Treat every internal belief as an observation of a model, qualified by confidence."
- "Verify against the physical world — the model is a claim, the world is the evidence."

## Data Governance (`data-governance`)

| Field | Value |
|---|---|
| kind | decision |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/data-governance.md`

### Claims

- "Data governance is the decision structure for data value and risk — what is kept, who sees it, and how it is traced." _(certainty: high)_
- "Retention is a policy decision — what data is kept and for how long, balancing value against risk and cost." _(certainty: high)_
- "Access scope is a security boundary decision — who may read and modify data, expressed as constraints." _(certainty: high)_
- "Lineage is an observation — the derivation chain of data — not a new primitive; it was resolved in Cycle 008 for training-data." _(certainty: high)_
- "Governance is a decision object, not a concept — it varies with retention requirement, access scope, lineage traceability, and compliance cost." _(certainty: high)_

### Relationships

- **protects** → `data-integrity`
- **constrains** → `schema-migration`
- **directs** → `backup-recovery`
- **analogous_to** → `training-data`

### Constraints

- "Governance decisions are bound by stated factors — retention, access, lineage, and cost requirements are the validity conditions."
- "Lineage is an observation with a traceability obligation — a derivation chain must be answerable or its absence known."

### Recommendations

- "Make governance a decided policy, not an accident of practice."
- "Track lineage as a first-class observation."
- "Re-decide the four factors as the data changes."

## Data Integrity (`data-integrity`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/data-integrity.md`

### Claims

- "Data integrity is the guarantee that data conforms to its defining rules — integrity rules are invariants the data must satisfy at all times." _(certainty: high)_
- "Integrity is enforced by the schema, not the application — schema-enforced rules are verifiable and universal; application-enforced rules are optional." _(certainty: high)_
- "Entity integrity (keys exist and are unique) and referential integrity (references resolve) are the foundational integrity classes." _(certainty: high)_
- "Integrity failures are correctness failures with a trace — orphaned references, duplicate identity, and constraint violations signal model or process defects." _(certainty: high)_
- "Integrity guarantees are scoped — the schema's rules define what integrity means for this data; rules outside the schema are outside the guarantee." _(certainty: high)_

### Relationships

- **guaranteed_by** → `relational-model`
- **shaped_by** → `schema-design`
- **reinforced_by** → `normalization`
- **protected_by** → `transactions`
- **threatened_by** → `schema-migration`
- **audited_by** → `data-governance`

### Constraints

- "Data must conform to its integrity rules at all times — a rule violated even once is a correctness failure."
- "Integrity guarantees are scoped to the schema — rules not in the schema are not part of the guarantee."

### Recommendations

- "Express integrity rules as schema constraints with enforcement."
- "Audit integrity continuously, not at migrations only."
- "Re-verify integrity after every migration and bulk load."

## Database Indexing (`database-indexing`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/database-indexing.md`

### Claims

- "An index is a maintained copy of data in a different ordering — a redundant structure that exists to accelerate access." _(certainty: high)_
- "An index is a structure with a tradeoff contract — reads are accelerated at the price of write cost and storage." _(certainty: high)_
- "Index correctness is coherence — the index must reflect the data it indexes; incoherent indexes return wrong results." _(certainty: high)_
- "Index structures are access-path mechanisms, not knowledge types — a B-tree is an ordering discipline, not a new category of information." _(certainty: high)_
- "The right index structure is workload-shaped — range queries favor ordered structures; point lookups favor hashes." _(certainty: high)_

### Relationships

- **selected_by** → `index-selection`
- **enables** → `query-planning`
- **serves** → `relational-model`
- **informed_by** → `schema-design`
- **exploited_by** → `query-optimization`

### Constraints

- "An index must remain coherent with its data — divergence is a correctness failure, not a performance issue."
- "Every index is a maintained copy — maintenance obligations are part of the structure's contract."

### Recommendations

- "Choose index structures by access-path demand."
- "Verify index coherence after maintenance events."
- "Monitor index bloat as a storage and performance signal."

## Dead Code Elimination (`dead-code-elimination`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/dead-code-elimination.md`

### Claims

- "Dead code is code that cannot affect observable behaviour — unreachable code, unused results, and redundant computation." _(certainty: high)_
- "Dead code elimination removes dead code from the program — a transformation that shrinks the program without changing its observable behaviour." _(certainty: high)_
- "Elimination correctness depends on liveness analysis — code is removed only when analysis proves it cannot be observed." _(certainty: high)_
- "Liveness analysis results are observations, not guarantees — an analysis bug that marks live code dead produces a miscompilation." _(certainty: high)_
- "Elimination must respect the observation model — side effects, volatile access, and external observability make code live even when its result is unused." _(certainty: high)_

### Relationships

- **instance_of** → `compiler-optimization`
- **operates_on** → `abstract-syntax-tree`
- **preserves** → `program-semantics`
- **verifiable_by** → `equivalence-checking`
- **improves** → `compiler-performance`

### Constraints

- "Code may be eliminated only when analysis proves it unobservable — elimination without proof is a miscompilation."
- "The observation model bounds elimination — external observability (side effects, volatile, I/O) makes code live."

### Recommendations

- "Base elimination decisions on explicit liveness and reachability evidence."
- "Model external observability explicitly before designing elimination."
- "Differential-test elimination across optimization levels on observability-heavy programs."

## Deadline (`deadline`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/deadline.md`

### Claims

- "A deadline is a timing requirement on completion — a boundary that separates valid from invalid results." _(certainty: high)_
- "A deadline is a constraint whose content happens to mention time — not a new evidence kind." _(certainty: high)_
- "A deadline miss is a correctness failure — the result is invalid regardless of its logical content." _(certainty: high)_
- "Deadline validity is the unification-hypothesis test at the temporal pole — completion <= T is a validity condition on the result, exactly as schema validity is on data." _(certainty: high)_
- "Deadlines vary in strength — hard deadlines make misses failures; soft deadlines tolerate misses with bounded degradation." _(certainty: high)_

### Relationships

- **constrains** → `real-time-system`
- **guides** → `task-scheduling`
- **compared_with** → `worst-case-execution-time`
- **analogous_to** → `transactions`
- **analogous_to** → `backup-recovery`

### Constraints

- "A result produced after its deadline is invalid — temporal correctness is a validity condition."
- "Deadline validity is bound by stated conditions — load, timing, and environment assumptions qualify the deadline."

### Recommendations

- "Model a deadline as a constraint on completion — never as a temporal primitive."
- "Treat deadline misses as correctness failures, not quality issues."
- "Bind deadlines by their stated conditions and audit them."

## Debug vs Release Modes (`debug-vs-release-modes`)

| Field | Value |
|---|---|
| kind | decision |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/debug-vs-release-modes.md`

### Claims

- "Debug and release are different build postures — debug optimizes for diagnosability, release for delivered performance." _(certainty: high)_
- "The modes differ in behaviour, not just speed — assertion removal, optimization legality, and debug-info presence change observable behaviour." _(certainty: high)_
- "Assertion removal is a correctness hazard — behaviour checked in debug builds is unguarded in release, making release-only failures possible." _(certainty: high)_
- "The behaviour gap between modes is a knowledge gap — code validated in debug mode is a different program in release mode." _(certainty: high)_
- "Mode divergence is a decision, not an accident — the gap can be deliberately widened or narrowed per the product's risk profile." _(certainty: high)_

### Relationships

- **configured_by** → `compiler-optimization`
- **instantiates** → `optimization-tradeoffs`
- **produced_by** → `build-systems`
- **affected_by** → `compiler-correctness`
- **differentiates** → `compiler-performance`

### Constraints

- "Each mode is a distinct program — debug and release builds must be validated separately."
- "Assertion removal must not delete behaviour the program depends on — guards are code, and their removal is a code change."

### Recommendations

- "Define the behaviour contract of each mode explicitly — what is optimized, what is removed, what is retained."
- "Keep critical assertions in release."
- "Run release-mode tests in the release configuration as part of the release process."

## Defense in Depth (`defense-in-depth`)

| Field | Value |
|---|---|
| kind | principle |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/defense-in-depth.md`

### Claims

- "Defense in depth is the strategy of layering independent security controls so that the failure of any single control does not compromise the system." _(certainty: high)_
- "Layered controls assume each layer will fail eventually — the design question is what remains secure when any given layer fails." _(certainty: high)_
- "Effective layering requires independence — layers that share a common failure mode provide the appearance of depth without its resilience." _(certainty: high)_
- "Depth is measured by the number of independent control failures required for compromise, not by the number of controls present." _(certainty: high)_
- "Defense in depth extends beyond prevention — detection, response, and recovery layers are as important as access-control layers." _(certainty: high)_

### Relationships

- **complements** → `attack-surface`
- **resists** → `kill-chain`
- **includes** → `threat-detection`
- **includes** → `incident-response`
- **extends** → `zero-trust`
- **reduces_need** → `risk-acceptance`

### Constraints

- "Layers sharing a dependency are a single layer — depth is defined by independent failure paths, not control count."
- "No layer count provides absolute security — depth bounds the probability of compromise; it does not eliminate it."

### Recommendations

- "Document layer independence assumptions and test them with failure injection exercises."
- "Include prevention, detection, and response layers in every depth design — depth that stops at prevention fails silently."
- "Audit effective depth annually — count independent failure paths, not controls."

## Deployment Risk (`deployment-risk`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/deployment-risk.md`

### Claims

- "Deployment risk is the exposure created by putting a model into production — failure likelihood and impact, under validity conditions." _(certainty: high)_
- "Deployment risk is reducible by evidence — validation, monitoring, rollback, and staged rollout convert unknown risk into managed risk." _(certainty: high)_
- "Deployment risk changes over time — drift, context change, and model updates alter the risk profile after deployment." _(certainty: high)_
- "Deployment risk is partially residual — acceptable residual risk is a decision, informed by monitoring and response capability." _(certainty: high)_
- "Deployment risk composes with existing risk knowledge — model risk is a case of the risk-acceptance structure, not a new kind of risk." _(certainty: high)_

### Relationships

- **informs** → `risk-acceptance`
- **reduced_by** → `model-monitoring`
- **modifies** → `retraining-decisions`
- **increased_by** → `distribution-shift`
- **quantified_by** → `uncertainty-estimation`
- **assessed_by** → `benchmark-validity`

### Constraints

- "Deployment risk cannot be reduced beyond the coverage of validation and monitoring evidence."
- "Accepted risk must be revisited when conditions change — acceptance expires with its conditions."

### Recommendations

- "Stage rollouts with canary segments and measured outcomes between stages."
- "Require monitoring and a verified rollback path before any production deployment."
- "Re-assess accepted residual risk whenever context or model conditions change."

## Design Under Concealment (`design-under-concealment`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/design-under-concealment.md`

### Claims

- "Concealment is an engineering parameter of the artifact's design — every design decision under concealment serves the artefact's secrecy as well as its function." _(certainty: high)_
- "The design anticipates being read — concealment design treats the analyst as an adversary and shapes the artifact accordingly." _(certainty: high)_
- "Concealment is visible only as its effects — the design state of the creator is never presented, only the shape the concealment produced." _(certainty: high)_
- "Concealment shapes the observable surface — the ambiguity the analyst sees is often a designed property, not an accident of capture." _(certainty: high)_
- "Concealment has a cost — secrecy trades against function, performance, and robustness, and the trade is visible in the artifact's shape." _(certainty: high)_

### Relationships

- **shapes** → `artifact`
- **amplifies** → `surface-ambiguity`
- **explains** → `concealed-intent`
- **expresses** → `attacker-capability`
- **subject_to** → `incomplete-evidence`

### Constraints

- "Concealment is a design property of the artifact, visible only as its effects — the design state is never presented."
- "Every surface convenience is a design decision — the convenient reading competes with the concealment hypothesis."

### Recommendations

- "Analyse the secrecy trade for every artifact feature, not just the artifact as a whole."
- "Analyse the secrecy trade explicitly for every artifact."
- "Keep the concealment hypothesis in every reading set."

## Detection Decision on Incomplete Reconstruction (`detection-decision`)

| Field | Value |
|---|---|
| kind | decision |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/detection-decision.md`

### Claims

- "The detection decision is whether the reconstruction supports acting on the artifact — a decision taken on claims whose ground truth is still withheld." _(certainty: high)_
- "Detection decisions are made under incomplete reconstruction — the reading set is open, the intent claim is derived, and the decision is made anyway." _(certainty: high)_
- "The decision is qualified by the reconstruction's confidence — the decision-maker inherits the evidence chain's qualification, and the decision inherits the chain's limits." _(certainty: high)_
- "The detection decision prices what the reconstruction does not know — the decision's condition is openness, not completeness." _(certainty: high)_
- "False negatives and false positives are asymmetric under concealment — the artifact was designed against detection, and the decision must price that design." _(certainty: high)_

### Relationships

- **qualified_by** → `reconstruction-confidence`
- **informed_by** → `competing-hypotheses`
- **constrained_by** → `incomplete-evidence`
- **serves** → `threat-detection`
- **applies_to** → `artifact`

### Constraints

- "A detection decision inherits its evidence chain's qualification — the decision cannot be more certain than the reconstruction it stands on."
- "The concealment design is part of the detection decision's evidence — the artifact was designed against being caught, and the decision prices it."

### Recommendations

- "Record the reconstruction's openness with every detection call."
- "Attach the evidence chain's qualification to every detection decision."
- "Time-box reconstruction against the decision window."

## Disclosure Decision on Incomplete Reconstruction (`disclosure-decision`)

| Field | Value |
|---|---|
| kind | decision |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/disclosure-decision.md`

### Claims

- "The disclosure decision is whether, what, and to whom to reveal about the artifact — a decision taken on a reconstruction that is still open." _(certainty: high)_
- "Disclosure is irreversible — once revealed, the reconstruction's claims leave the analyst's control, and the decision prices that." _(certainty: high)_
- "Disclosure decisions are qualified by the reconstruction's confidence — what is disclosed carries the chain's qualification, and the disclosure carries its limits." _(certainty: high)_
- "Disclosure decisions are made on open reconstructions — what is revealed inherits what the analysis still does not know." _(certainty: high)_
- "The disclosure decision is the point where the analysis's epistemic limits become public — the reader of the disclosure inherits the chain's openness." _(certainty: high)_

### Relationships

- **informed_by** → `attribution`
- **informed_by** → `concealed-intent`
- **qualified_by** → `reconstruction-confidence`
- **constrained_by** → `competing-hypotheses`
- **serves** → `risk-acceptance`

### Constraints

- "A disclosure inherits its chain's qualification — what is revealed carries the reconstruction's openness, and the reader is told so."
- "Disclosure is irreversible — the decision prices the loss of control, and nothing disclosed is treated as revisable."

### Recommendations

- "Carry the reconstruction's confidence into the disclosure text."
- "Carry the chain's qualification into every disclosure."
- "Price irreversibility explicitly in every disclosure decision."

## Distribution Shift (`distribution-shift`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/distribution-shift.md`

### Claims

- "Distribution shift is the divergence between the input distribution a model was trained on and the distribution it operates on — the primary cause of model decay." _(certainty: high)_
- "Shift invalidates evidence about a model — observations, calibration, and generalization claims all decay as the distribution moves." _(certainty: high)_
- "Covariate shift (input change) and concept drift (input-output mapping change) demand different responses — misclassifying the shift type misdirects remediation." _(certainty: high)_
- "Shift is detectable from monitoring data before it causes visible failures — drift metrics lead degradation." _(certainty: high)_
- "Shift is partially correctable by retraining, but retraining on shifted data without validation risks learning new failure modes." _(certainty: high)_

### Relationships

- **deviates_from** → `training-data`
- **limits** → `generalization`
- **degrades** → `confidence-calibration`
- **degrades** → `uncertainty-estimation`
- **detected_by** → `model-monitoring`
- **triggers** → `retraining-decisions`

### Constraints

- "Model validity is bound to its training distribution — shift invalidates model evidence until re-validated."
- "Shift must be verified and typed before remediation — untyped shift response is a guess."

### Recommendations

- "Instrument drift monitoring with a fixed reference distribution and alert thresholds."
- "Diagnose shift type (covariate vs concept) before triggering remediation."
- "Treat every shift-triggered retraining as an experiment — validate against fresh data before deployment."

## Drift Detection (`drift-detection`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/drift-detection.md`

### Claims

- "Drift detection is the practice of measuring divergence between a reference and current distribution — it converts 'the world changed' into measurable evidence." _(certainty: high)_
- "Drift detection must distinguish signal from routine fluctuation — statistical tests require severity thresholds to mean anything." _(certainty: high)_
- "Drift detection is only useful when tied to response — detection without a decision channel is noise." _(certainty: high)_
- "Detection methods trade sensitivity against noise tolerance — no method detects all real shift without some false alarms." _(certainty: high)_
- "Drift detection evidence decays — thresholds and reference windows age as the world moves." _(certainty: high)_

### Relationships

- **measures** → `distribution-shift`
- **composes** → `model-monitoring`
- **triggers** → `retraining-decisions`
- **protects** → `confidence-calibration`
- **references** → `training-data`
- **guards** → `generalization`

### Constraints

- "Drift detection is only meaningful against a fixed reference — a moving baseline cannot detect change."
- "Detection without response capacity is noise — the detector and the decision channel must be designed together."

### Recommendations

- "Detect drift at decision-relevant granularity — segments, not just global distributions."
- "Pair every drift detector with a response workflow — detection without response is noise."
- "Renew the reference distribution deliberately on verified regime change, never on routine fluctuation."

## First-Stage Dropper Family (`dropper`)

| Field | Value |
|---|---|
| kind | concept |
| domain | threat-analysis |
| research_cycle | "015" |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/dropper.md`

### Claims

- "The droppers are small, single-use first-stage loader binaries: unique per victim, compiled per campaign, and never reused." _(certainty: high)_
- "The shared download logic across all four victims is the droppers' only identifying artifact; they contain no other identifying artifacts." _(certainty: high)_
- "The droppers stage the Hammer backdoor family after execution." _(certainty: high)_

### Relationships

- **delivered_by** → `spearphishing-initial-access`
- **installed_by** → `hammer-backdoor-family`
- **linked_to** → `per-victim-operational-separation`
- **part_of** → `midnight-foundry-campaign`

### Constraints

- "Dropper-specific claims are limited to the loader stage; lure mechanics and the backdoor payload belong to their own objects."

## Earliest-Deadline-First (`earliest-deadline-first`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/earliest-deadline-first.md`

### Claims

- "Earliest-deadline-first is a scheduling policy that orders tasks by deadline — the earliest deadline executes first." _(certainty: high)_
- "EDF is optimal among dynamic policies — if any policy can schedule a task set, EDF can — the optimality claim." _(certainty: high)_
- "The optimality claim is bound by stated conditions — preemptive, uniprocessor assumptions qualify the guarantee." _(certainty: high)_
- "EDF's deadline ordering is a constraint — the schedule must respect the ordering, exactly as priority ordering constrains fixed-priority scheduling." _(certainty: high)_
- "EDF is one realization of the scheduling-policy decision — optimality is the decision's content, not a new construct." _(certainty: high)_

### Relationships

- **realizes** → `scheduling-policy`
- **orders_by** → `deadline`
- **allocates_within** → `task-scheduling`
- **analogous_to** → `leader-election`
- **analogous_to** → `quorum`

### Constraints

- "Deadline ordering is an invariant — the schedule must respect the deadline ordering under EDF."
- "The optimality claim is valid only under its stated conditions — preemptive, uniprocessor assumptions."

### Recommendations

- "Model EDF as a policy decision with an ordering constraint."
- "Verify the optimality conditions before relying on the claim."
- "Plan for overload despite optimality."

## Epistemic Symmetry Between Analyst and Designer (`epistemic-symmetry`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/epistemic-symmetry.md`

### Claims

- "The analyst and the designer model each other — the designer anticipated the analyst, and the analyst reconstructs the designer; the artifact is the intersection of two analyses." _(certainty: high)_
- "The symmetry is structural — the two parties model each other through the artifact, and the artifact is where both models meet." _(certainty: high)_
- "The analysis closes onto itself in this domain — the creator's reality is itself only accessible as a claim, and the analyst's position matches the modelled system's." _(certainty: high)_
- "The designer's anticipation shapes the artifact's surface — the ambiguity the analyst reads is the designer's prediction of reading." _(certainty: high)_
- "Symmetry awareness is a qualification, not a paralysis — the analyst models the designer without modelling the model of the model." _(certainty: high)_

### Relationships

- **grounded_in** → `artifact`
- **explains** → `concealed-intent`
- **complicates** → `attribution`
- **explains** → `surface-ambiguity`
- **analogous_to** → `belief-state`

### Constraints

- "The artifact is the intersection of two analyses — the designer's anticipation and the analyst's reconstruction — and the intersection is where both are grounded."
- "The mutual model is one level deep — the designer's anticipation and the analyst's reconstruction are the only layers, and the artifact bounds them."

### Recommendations

- "Record the mutual model explicitly — who anticipated what — in every analysis."
- "Review the analyst↔designer loop explicitly at each analysis milestone."

## Equivalence Checking (`equivalence-checking`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/equivalence-checking.md`

### Claims

- "Equivalence checking is the mechanical comparison of two programs — determining whether their observable behaviour matches under a stated observation model." _(certainty: high)_
- "Equivalence is a relation defined over semantics, not syntax — two differently-shaped programs can be equivalent; two similar ones may not be." _(certainty: high)_
- "Equivalence is always relative to an observation model — equivalence under input-output behaviour is not equivalence under full behavioural observation." _(certainty: high)_
- "Equivalence checking is the verification channel for transformations — before/after comparison is how optimization correctness is mechanically established." _(certainty: high)_
- "A checker can be wrong in both directions — false positives (claiming equivalence where behaviour differs) and false negatives (rejecting true equivalence) are distinct failure classes." _(certainty: high)_

### Relationships

- **based_on** → `program-semantics`
- **verifies** → `compiler-optimization`
- **verifies** → `compiler-correctness`
- **used_by** → `formal-verification`
- **verifies** → `constant-folding`
- **verifies** → `dead-code-elimination`

### Constraints

- "Equivalence verdicts are valid only under a stated observation model — an unstated model makes every verdict untestable."
- "A checker must never claim equivalence falsely — false positives violate the verification contract."

### Recommendations

- "Define the equivalence relation and its observation model explicitly."
- "Prefer unsoundness-by-silence over false claims — reject rather than wrongly accept."
- "Re-verify checked transformations when the observation model changes."

## Eventual Consistency (`eventual-consistency`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/eventual-consistency.md`

### Claims

- "Eventual consistency guarantees that if no new writes are made to a data item, all replicas will eventually return the same value." _(certainty: high)_
- "Eventual consistency does not guarantee when convergence will occur — the window of inconsistency is unbounded." _(certainty: high)_
- "Eventual consistency allows stale reads — a read may return an older value if the replica has not yet received the latest write." _(certainty: high)_
- "Eventual consistency maintains availability during partitions — all replicas accept writes regardless of partition state." _(certainty: high)_
- "Conflict resolution is required when multiple replicas accept concurrent writes — last-write-wins (LWW) is the most common strategy." _(certainty: high)_
- "Eventual consistency is not a single model — read-after-write, monotonic reads, and causal consistency are stronger forms that bound inconsistency." _(certainty: high)_

### Relationships

- **realises** → `cap-theorem`
- **contrasts_with** → `strong-consistency`
- **provides** → `availability`
- **may_use** → `quorum`
- **requires** → `network-partition-recovery`

### Constraints

- "Eventual consistency provides no upper bound on staleness unless explicitly bounded by configuration or application logic."
- "Concurrent writes to the same key in different partitions will always produce conflicts that require resolution."

### Recommendations

- "Never deploy eventually consistent systems without staleness monitoring — if you cannot measure staleness, you cannot reason about correctness."
- "Use per-request consistency hints — allow reads to request stronger consistency when needed without making it the default."
- "Test conflict resolution logic under concurrent write patterns that exceed expected production load."

## Exfiltration Pattern (`exfiltration-pattern`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | threat-analysis |
| research_cycle | "015" |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/exfiltration-pattern.md`

### Claims

- "On Victims A, B, and D, files were compressed into encrypted archives, uploaded to the staging host, and retrieved over FTP sessions originating from a single external IP per victim." _(certainty: high)_
- "Exfiltration occurred in small batches over weeks — behavior consistent with an attempt to stay under data-volume thresholds, a reading the source records rather than proves." _(certainty: medium)_
- "Victim C's exfiltration channel was interrupted before completion, and the Rivet stealer's collected data was not recovered." _(certainty: high)_

### Relationships

- **part_of** → `midnight-foundry-campaign`
- **linked_to** → `cluster-2-staging-infrastructure`
- **linked_to** → `collection-pattern`

### Constraints

- "The pattern records the observed channel behavior; volume-threshold intent is a labeled reading."

### Recommendations

- "Track exfiltration completeness per victim rather than as a campaign-wide status."

## Fail-Safe (`fail-safe`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/fail-safe.md`

### Claims

- "Fail-safe is the posture a system takes under failure — a degraded-but-valid state, chosen by design, not a new construct." _(certainty: high)_
- "A fail-safe posture is a mode-divergence result — the same pattern as debug-vs-release (009) and hard-vs-soft (011): the system changes posture by decision." _(certainty: high)_
- "Fail-safe validity is conditional — the degraded state is valid under its stated conditions (the failure), and its own claims hold under those conditions." _(certainty: high)_
- "The fail-safe structure is failure modes + postures + recovery relationships — composition of existing destinations." _(certainty: high)_
- "Fail-safe is not safety — it is the bounded response to failure: the system remains valid, degraded, under stated conditions." _(certainty: high)_

### Relationships

- **serves** → `cyber-physical-system`
- **supports** → `safety-case`
- **analogous_to** → `hard-vs-soft-real-time`
- **analogous_to** → `debug-vs-release-modes`
- **constrains** → `actuation`

### Constraints

- "The degraded posture is valid under its stated conditions — its own validity conditions hold in failure."
- "Fail-safe is bounded response to failure — the posture must be verified, not assumed."

### Recommendations

- "Represent fail-safe as failure modes + postures + recovery relationships."
- "Verify the degraded state under its failure conditions."
- "Track degraded duration as an operating signal."

## Feedback Control (`feedback-control`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/feedback-control.md`

### Claims

- "Feedback control is the closed-loop structure — observation, comparison against a reference, and corrective action, repeated." _(certainty: high)_
- "The error signal is an observation of divergence — the difference between belief and reference, qualified by measurement uncertainty." _(certainty: high)_
- "A controller is a relationship structure — the mapping from observed error to corrective command — not a new knowledge type." _(certainty: high)_
- "The closed loop is the unit of cyber-physical knowledge — each cycle senses, compares, acts, and observes again." _(certainty: high)_
- "Feedback control is valid only under its stated conditions — plant model, measurement quality, and timing bound the loop's correctness." _(certainty: high)_

### Relationships

- **serves** → `cyber-physical-system`
- **directs** → `actuation`
- **evaluated_through** → `belief-state`
- **analogous_to** → `model-monitoring`
- **constrained_by** → `deadline`

### Constraints

- "The closed loop is valid only under its stated conditions — plant model, measurement quality, and timing bound the loop's correctness."
- "Every cycle of the loop acts on qualified belief — the epistemic gap is never closed by the loop, only managed within its conditions."

### Recommendations

- "Represent feedback control as a relationship structure over observation and action — no controller construct."
- "Treat the error signal as qualified observation of divergence."
- "State the loop's timing conditions with the loop."

## Fixed-Priority Scheduling (`fixed-priority-scheduling`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/fixed-priority-scheduling.md`

### Claims

- "Fixed-priority scheduling is a pattern — tasks carry static priorities and the highest-priority ready task executes." _(certainty: high)_
- "Priority is a constraint plus a relationship — priority ordering constrains the schedule; priority assignment relates tasks to the policy." _(certainty: high)_
- "The pattern's validity is bound by stated conditions — priority assignment, preemption rules, and workload assumptions qualify the guarantee." _(certainty: high)_
- "Fixed-priority scheduling is one realization of the scheduling-policy decision — the pattern instantiates the decision object." _(certainty: high)_
- "Rate-monotonic analysis verifies the pattern — feasibility is a claim established by analysis, not assumed by the policy." _(certainty: high)_

### Relationships

- **realizes** → `scheduling-policy`
- **allocates_within** → `task-scheduling`
- **serves** → `deadline`
- **verified_by** → `rate-monotonic-analysis`
- **analogous_to** → `leader-election`

### Constraints

- "Priority ordering is an invariant — the schedule must respect the assigned priority order."
- "The pattern's guarantee is valid only under stated conditions — priority assignment, preemption rules, and workload assumptions."

### Recommendations

- "Model priority as constraint plus relationship, not a construct."
- "Verify fixed-priority feasibility with rate-monotonic analysis."
- "Apply priority inheritance when resources are shared."

## Formal Verification (`formal-verification`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/formal-verification.md`

### Claims

- "Formal verification is the machine-checked establishment of a property — a proof artifact whose every step is checked by a machine." _(certainty: high)_
- "A proof is an artifact of evidence — proof obligations, specifications, and machine-checked derivations are the evidence structure, not a new knowledge kind." _(certainty: high)_
- "Verification is bounded by specification correctness — a verified system is correct only with respect to what the specification states (garbage in, verified garbage out)." _(certainty: high)_
- "Machine-checked proofs are the strongest evidence engineering has — they eliminate the possibility of proof error, not the possibility of specification error." _(certainty: high)_
- "Verification cost scales with system complexity — verification investment is a decision about which properties deserve proof." _(certainty: high)_

### Relationships

- **verifies** → `compiler-correctness`
- **verifies** → `type-safety`
- **uses** → `equivalence-checking`
- **requires** → `program-semantics`
- **verifies** → `type-system`

### Constraints

- "A verified property holds only under the stated assumptions and specification — verification does not transcend its own inputs."
- "Proofs must be machine-checked to count as verification — human proof checking reintroduces exactly the error class being eliminated."

### Recommendations

- "Verify only with machine-checked proofs."
- "Review specifications as carefully as code."
- "Choose verification targets by failure cost, not by proof convenience."

## Generalization (`generalization`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/generalization.md`

### Claims

- "Generalization is the ability to perform on unseen data from the same distribution — it is a property inferred from observations, not a mechanism." _(certainty: high)_
- "Generalization cannot be directly measured — it is estimated from held-out evaluation, which is itself evidence subject to validity conditions." _(certainty: high)_
- "Generalization claims are distribution-bound — a model that generalizes within its training distribution may not generalize across distribution shift." _(certainty: high)_
- "Generalization trades against memorization — capacity beyond what the data supports is absorbed as memorization of noise." _(certainty: high)_
- "Apparent generalization can be an artifact of evaluation design — leakage, overlapping splits, and contamination inflate generalization estimates." _(certainty: high)_

### Relationships

- **learned_from** → `training-data`
- **contrasts_with** → `overfitting`
- **limited_by** → `distribution-shift`
- **measured_by** → `benchmark-validity`
- **affects** → `confidence-calibration`
- **interacts_with** → `uncertainty-estimation`

### Constraints

- "Generalization cannot be directly measured — only estimated, under validity conditions that must be stated."
- "Generalization claims are valid only within the training distribution."

### Recommendations

- "Report generalization estimates with their validity conditions — distribution, data source, and evaluation design."
- "Validate generalization on fresh production-like data before deployment, not only on held-out splits."
- "Bound deployment scope to the distribution where generalization was demonstrated."

## Hallucination (`hallucination`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/hallucination.md`

### Claims

- "Hallucination is the generation of fluent, confident content that is factually incorrect or unsupported — it is a failure mode of generation, not of comprehension." _(certainty: high)_
- "Hallucination is dangerous because it is confidence-correlated — models hallucinate with high stated confidence, defeating naive confidence gating." _(certainty: high)_
- "Hallucination rates are context-dependent — they vary with domain, prompt, knowledge recency, and task type." _(certainty: high)_
- "Hallucination is partially detectable post-hoc (verification against sources) and partially irreducible (unverifiable claims)." _(certainty: high)_
- "Hallucination is a distribution property of the model-prompt pair, not a fixed model property — it cannot be permanently eliminated by training alone." _(certainty: high)_

### Relationships

- **exploits** → `confidence-calibration`
- **masks** → `probabilistic-outputs`
- **targeted_by** → `uncertainty-estimation`
- **measured_by** → `benchmark-validity`
- **aggravated_by** → `distribution-shift`
- **detected_by** → `model-monitoring`

### Constraints

- "A generative model cannot be fully grounded in evidence it was not trained or provided with."
- "Confidence cannot serve as a reliable hallucination detector — hallucination is confidence-correlated by construction."

### Recommendations

- "Ground generation in retrieval or verified sources for fact-critical applications."
- "Instrument hallucination detection for high-stakes outputs rather than trusting confidence."
- "Report hallucination rates by domain in evaluation, not a single aggregate number."

## Hammer-A Variant (`hammer-a-variant`)

| Field | Value |
|---|---|
| kind | concept |
| domain | threat-analysis |
| research_cycle | "015" |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/hammer-a-variant.md`

### Claims

- "Hammer-A was observed on Victims A and C and compiled with a particular toolchain." _(certainty: high)_
- "Hammer-A uses HTTP POST callbacks and persists via service registration." _(certainty: high)_
- "Hammer-A has no module loader; the loader and encryption layer of Hammer-B have no equivalent in A." _(certainty: high)_

### Relationships

- **part_of** → `hammer-backdoor-family`
- **observed_on** → `victim-set`
- **linked_to** → `hammer-classification-dispute`

## Hammer-B Variant (`hammer-b-variant`)

| Field | Value |
|---|---|
| kind | concept |
| domain | threat-analysis |
| research_cycle | "015" |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/hammer-b-variant.md`

### Claims

- "Hammer-B was observed on Victims B and D: the same core as Hammer-A with encrypted HTTPS callbacks and an added in-memory module loader." _(certainty: high)_
- "The loader retrieves additional modules in-memory from the campaign's module host." _(certainty: high)_
- "Two malformed code comments in Hammer-B are consistent with a specific East Asian language family — a reading recorded as attribution input, not a demonstrated fact." _(certainty: medium)_

### Relationships

- **part_of** → `hammer-backdoor-family`
- **observed_on** → `victim-set`
- **loads_from** → `cluster-2-staging-infrastructure`
- **linked_to** → `attribution-assessment`

## Hammer Backdoor Family (`hammer-backdoor-family`)

| Field | Value |
|---|---|
| kind | concept |
| domain | threat-analysis |
| research_cycle | "015" |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/hammer-backdoor-family.md`

### Claims

- "Hammer is a backdoor observed on all four victims: it registers as a service, collects host information, polls a C2 domain at fixed intervals, and supports a small command set." _(certainty: high)_
- "Hammer-A and Hammer-B share the core logic and C2 protocol framing that unify the builds." _(certainty: high)_
- "Whether Hammer is one family or two is contested: the loader and encryption layer of Hammer-B are functionally distinct, and B's module system has no equivalent in A." _(certainty: high)_
- "The malware repository holds the builds as two artifacts with a shared lineage note — a provisional handling, not a resolution." _(certainty: high)_

### Relationships

- **installed_by** → `dropper`
- **observed_on** → `victim-set`
- **phones_home_to** → `cluster-1-c2-infrastructure`
- **linked_to** → `persistence-pattern`
- **linked_to** → `hammer-classification-dispute`
- **part_of** → `midnight-foundry-campaign`

### Constraints

- "Family-level claims cover the shared core only; variant-specific capability claims are carried by the variant objects."
- "The family object does not resolve the one-family-vs-two classification."

## Hammer One-Family-vs-Two Classification Dispute (`hammer-classification-dispute`)

| Field | Value |
|---|---|
| kind | decision |
| domain | threat-analysis |
| research_cycle | "015" |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/hammer-classification-dispute.md`

### Claims

- "The one-family reading holds that Hammer-A and Hammer-B are two builds of one family because the core logic and C2 protocol framing are shared." _(certainty: high)_
- "The two-family reading holds that the loader and encryption layer are functionally distinct capabilities, and B's module system has no equivalent in A." _(certainty: high)_
- "The evidence is insufficient to choose between the readings; the classification remains open." _(certainty: high)_
- "The repository's handling — two artifacts with a shared lineage note — is a provisional decision that preserves both readings." _(certainty: high)_

### Relationships

- **linked_to** → `hammer-backdoor-family`
- **linked_to** → `hammer-a-variant`
- **linked_to** → `hammer-b-variant`
- **linked_to** → `open-analytical-questions`

### Constraints

- "The dispute object records both readings; it does not resolve them."

### Recommendations

- "Keep the family count open in tracking systems and record which reading each downstream claim assumes."

## Hard vs Soft Real-Time (`hard-vs-soft-real-time`)

| Field | Value |
|---|---|
| kind | decision |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/hard-vs-soft-real-time.md`

### Claims

- "Hard vs soft real-time is a behavioural decision — the choice of what a deadline miss means — not a property of the system." _(certainty: high)_
- "Hard real-time treats a miss as a failure; soft real-time treats it as degradation — the same system can change posture by decision." _(certainty: high)_
- "The decision is structurally identical to debug-vs-release-modes — a posture choice with distinct behaviour contracts — the Cycle 009 cross-domain link." _(certainty: high)_
- "The posture decision carries four factors — miss_consequence, timing_strictness, workload_variability, and degradation_policy — the decision-object pattern at 4." _(certainty: high)_
- "Each posture is a distinct guarantee contract — hard and soft modes are different promises, and validation must be per-mode." _(certainty: high)_

### Relationships

- **decides** → `real-time-guarantee`
- **interprets** → `deadline`
- **informs** → `scheduling-policy`
- **analogous_to** → `debug-vs-release-modes`
- **analogous_to** → `optimization-tradeoffs`

### Constraints

- "The posture defines the miss meaning — a hard system's miss is a failure, a soft system's is degradation."
- "Each posture's guarantee is valid under its own contract — cross-mode promises are invalid."

### Recommendations

- "Treat hard vs soft as a decision with stated factors."
- "State the miss meaning explicitly with the contract."
- "Validate per-mode."

## HTTP Protocol (`http-protocol`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/http-protocol.md`

### Claims

- "HTTP/1.1 uses one TCP connection per request — parallelism requires multiple concurrent connections (typically 6-8 per origin)." _(certainty: high)_
- "HTTP/2 multiplexes multiple streams over a single TCP connection, eliminating connection-level head-of-line blocking at the HTTP layer." _(certainty: high)_
- "HTTP/2 stream multiplexing still experiences head-of-line blocking at the TCP layer — one lost packet affects all streams." _(certainty: high)_
- "HTTP method idempotency determines retry safety — GET, HEAD, PUT, DELETE are idempotent; POST and PATCH are not." _(certainty: high)_
- "HTTP 429 (Too Many Requests) indicates rate limiting — retry without backoff amplifies the problem." _(certainty: high)_

### Relationships

- **runs_over** → `tcp-tls-foundation`
- **traverses** → `proxy-infrastructure`
- **triggers** → `network-failure-propagation`
- **distinct_from** → `automation-protocol`
- **contributes_to** → `automation-detection-surface`

### Constraints

- "HTTP request cannot be sent before TCP connection is established and TLS handshake (if HTTPS) is complete."
- "Idempotent methods (GET, HEAD, PUT, DELETE) produce the same server state regardless of how many times they are executed."

### Recommendations

- "Implement rate limit detection with automatic backoff at the HTTP client layer."
- "Distinguish transient server errors (503, 504) from permanent ones (500, 502 persistent) in retry logic."

## Human Evaluation (`human-evaluation`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/human-evaluation.md`

### Claims

- "Human evaluation is evidence about quality derived from human judgement — disagreement between raters is data, not noise." _(certainty: high)_
- "Human judgement is variable — inter-rater agreement must be measured for human evaluation results to be interpretable." _(certainty: high)_
- "Human evaluation is the reference for qualities automated metrics cannot measure — fluency, preference, harm." _(certainty: high)_
- "Human evaluation is expensive and difficult to reproduce — reproducibility limits its evidentiary strength." _(certainty: high)_
- "Subjective judgement is structured evidence — preference, disagreement, and confidence are expressible as qualified observations and decision factors, not as a separate evidence type." _(certainty: high)_

### Relationships

- **complements** → `benchmark-validity`
- **evaluates** → `alignment`
- **informs** → `metric-selection`
- **verifies** → `hallucination`
- **biased_by** → `training-data`
- **validates** → `generalization`

### Constraints

- "Human evaluation is evidence about the evaluators as much as about the system evaluated."
- "Disagreement must be measured for human evaluation results to be interpretable."

### Recommendations

- "Report inter-rater agreement with every human evaluation result."
- "Use preference-based protocols for qualities with low absolute-rating reliability."
- "Recruit raters matching the deployment population and document the composition."

## Idempotency (`idempotency`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/idempotency.md`

### Claims

- "An idempotent operation produces the same result regardless of how many times it is applied — retrying an idempotent operation is safe." _(certainty: high)_
- "Idempotency is the foundation of safe retry — without idempotency, retrying a failed operation can produce duplicate side effects." _(certainty: high)_
- "Idempotency keys (unique operation identifiers) enable exactly-once processing in at-least-once delivery systems." _(certainty: high)_
- "Natural idempotency (operation is inherently repeatable) is preferable to enforced idempotency (deduplication logic) because it has no overhead." _(certainty: high)_
- "Idempotency does not imply no side effects — it implies the same result and side effects for repeated identical requests." _(certainty: high)_

### Relationships

- **enables_safe_retry** → `retry-storm-amplification`
- **complementary_to** → `circuit-breaker`
- **requires** → `saga-pattern`
- **interacts_with** → `eventual-consistency`

### Constraints

- "An operation that produced side effects before failure cannot be made idempotent without deduplication — the first application already occurred."
- "Idempotency keys have a finite lifetime — once the key retention period expires, duplicate detection is no longer possible."

### Recommendations

- "Require idempotency keys for all mutating API operations as an architectural standard."
- "Verify idempotency through chaos engineering — inject failures after partial operation completion and confirm retry produces correct state."
- "Include idempotency key in all retry logging to enable deduplication analysis during incident investigation."

## Incident Response (`incident-response`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/incident-response.md`

### Claims

- "Incident response is the disciplined process of detecting, containing, eradicating, and recovering from security incidents — defined phases, not improvisation." _(certainty: high)_
- "Response quality is determined before the incident — preparation (plans, runbooks, trained teams, exercised scenarios) is the strongest predictor of outcome." _(certainty: high)_
- "Time is the critical resource — faster containment directly reduces attacker dwell time and realised damage." _(certainty: high)_
- "Incidents are investigated under incomplete evidence — responders must act on partial information while evidence collection continues." _(certainty: high)_
- "Post-incident review converts incidents into learning — without review, the organisation repeats the same response mistakes." _(certainty: high)_

### Relationships

- **triggered_by** → `threat-detection`
- **position_aware** → `kill-chain`
- **operates_under** → `incomplete-evidence`
- **responds_to** → `threat-actor`
- **final_layer** → `defense-in-depth`
- **informs** → `risk-acceptance`

### Constraints

- "Response decisions are made under incomplete evidence — waiting for complete understanding forfeits the time advantage."
- "Eradication cannot be declared complete without persistence hunting — absence of observed footholds is not absence of footholds."

### Recommendations

- "Pre-approve containment actions so responders do not wait for escalation during an active incident."
- "Hunt for persistence before declaring recovery — assume incomplete eradication until validated."
- "Track dwell time as a core response metric and review trends quarterly."

## Incomplete Evidence in Security Analysis (`incomplete-evidence`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/incomplete-evidence.md`

### Claims

- "Security analysis almost always operates on incomplete evidence — full observability of an attacker's behaviour is the exception, not the rule." _(certainty: high)_
- "The distinction between known unknowns (identified gaps) and unknown unknowns (unimagined gaps) determines how evidence gaps should be managed." _(certainty: high)_
- "Evidence gaps are asymmetric in impact — missing evidence of attack is not evidence of no attack." _(certainty: high)_
- "Incomplete evidence biases analysis toward visible threats — what is measured is weighted higher than what is not measured." _(certainty: high)_
- "The cost of closing an evidence gap must be weighed against the cost of acting on incomplete evidence — evidence perfection is rarely affordable." _(certainty: high)_

### Relationships

- **reduces** → `confidence`
- **widens** → `likelihood`
- **blinds** → `threat-detection`
- **distorts** → `vulnerability-management`
- **complicates** → `risk-acceptance`

### Constraints

- "Evidence absence cannot be used as evidence of security — 'no evidence of compromise' is a finding about coverage, not about compromise."
- "Every analysis carries an unquantified component of unknown unknowns — claims of complete evidence are necessarily false."

### Recommendations

- "Record confidence degradation explicitly when evidence is incomplete — a finding without confidence is an assumption."
- "Conduct periodic red team exercises specifically to discover unknown unknowns — not just to test known defences."
- "When accepting risk on incomplete evidence, document what additional evidence would change the acceptance decision."

## Index Selection (`index-selection`)

| Field | Value |
|---|---|
| kind | decision |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/index-selection.md`

### Claims

- "Index selection is the decision of which indexes to maintain — every index trades read speed against write cost and storage." _(certainty: high)_
- "The right index set is workload-dependent — queries define value; unused indexes are pure cost." _(certainty: high)_
- "Index value is a function of selectivity — an index that rarely narrows the result set is not worth its write tax." _(certainty: high)_
- "Index selection is an ongoing decision — workload change invalidates index decisions as it invalidates schema decisions." _(certainty: high)_
- "Index governance is redundancy governance — every index is a maintained copy, and unmaintained copies decay." _(certainty: high)_

### Relationships

- **selects_among** → `database-indexing`
- **constrains** → `query-planning`
- **shaped_by** → `query-optimization`
- **serves** → `relational-model`
- **influenced_by** → `schema-design`

### Constraints

- "Every index is a maintained copy — an index without governance is redundancy without a control."
- "Index decisions are workload-scoped — an index justified by one workload is unjustified by another."

### Recommendations

- "Measure index usage and drop what is unused."
- "Base index selection on workload evidence, not intuition."
- "Govern indexes with the same lifecycle as schema."

## Inference from Behaviour (`inference-from-behavior`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/inference-from-behavior.md`

### Claims

- "Inferring what the artifact does from what it is observed doing is an inference step — behaviour is evidence, and the step from evidence to function is never given by the evidence itself." _(certainty: high)_
- "The inference is a claim about the artifact one inference beyond the observation it is built on." _(certainty: high)_
- "Every behavioural inference is conditional — it holds only under the observation conditions that produced its evidence." _(certainty: high)_
- "The same behaviour supports multiple inferences — behavioural evidence underdetermines function, exactly as the surface does." _(certainty: high)_
- "Inference quality is a function of evidence, not of fluency — a smooth reading is not a grounded reading." _(certainty: high)_

### Relationships

- **derived_from** → `behavioral-observation`
- **describes** → `artifact`
- **constrained_by** → `surface-ambiguity`
- **based_on** → `observable-evidence`
- **analogous_to** → `belief-state`
- **subject_to** → `perception-uncertainty`

### Constraints

- "A behavioural inference is valid only under the observation it is derived from — the reading inherits the trace's conditions."
- "The inference never closes the surface/semantics gap by itself — a reading is a claim, not a fact."

### Recommendations

- "Mark every behaviour→function reading as derived — the reading stands one step beyond its observation."
- "Ground every reading in its observation and record the conditions."
- "Keep the reading set open until evidence discriminates."

## Intermediate Representation (`intermediate-representation`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/intermediate-representation.md`

### Claims

- "An intermediate representation is a representation of a program between source and machine code — designed to make analysis and transformation tractable." _(certainty: high)_
- "IRs are nested — compilers lower through multiple representation levels, each closer to machine semantics than the last." _(certainty: high)_
- "IR choice determines which optimizations are possible — a representation that hides information makes that information unoptimizable." _(certainty: high)_
- "Lowering must preserve program semantics — each representation transition is a transformation with the same correctness obligation as an optimization." _(certainty: high)_
- "The final IR is the substrate for code generation — machine-level decisions (register allocation, scheduling, instruction selection) operate on it." _(certainty: high)_

### Relationships

- **lowered_from** → `abstract-syntax-tree`
- **preserves** → `program-semantics`
- **substrate_for** → `compiler-optimization`
- **organizes** → `optimization-pass`
- **constrained_by** → `compiler-correctness`

### Constraints

- "Every lowering step must preserve program semantics — the IR is a representation of the program, not a new program."
- "Representation must retain the information later stages depend on — information discarded at one level cannot be recovered at a lower one."

### Recommendations

- "Design the IR ladder deliberately — each level's contract, not its data structures, is the architecture."
- "Never drop information without a recorded decision that no later stage needs it."
- "Treat lowering steps with the same verification discipline as optimizations."

## Isolation Levels (`isolation-levels`)

| Field | Value |
|---|---|
| kind | decision |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/isolation-levels.md`

### Claims

- "Isolation levels define which concurrency anomalies a transaction system permits — each level is a contract about what concurrent behaviour can be observed." _(certainty: high)_
- "The anomaly taxonomy (dirty reads, non-repeatable reads, phantoms) is the constraint structure of concurrency — anomalies are constraint violations, not events." _(certainty: high)_
- "Serializable isolation eliminates all anomalies at the cost of concurrency — every weaker level trades correctness for throughput." _(certainty: high)_
- "Isolation selection is a decision with cost consequences — the chosen level determines which application bugs are possible." _(certainty: high)_
- "Application expectations often exceed the configured level — 'consistency bugs' are usually isolation-mismatch bugs." _(certainty: high)_

### Relationships

- **scopes** → `transactions`
- **determines** → `transaction-failures`
- **conditioned_by** → `data-integrity`
- **independent_of** → `atomicity`

### Constraints

- "Correctness claims are scoped to the isolation level — behaviour verified at one level is not guaranteed at another."
- "Anomalies permitted by the configured level are not defects — they are the contract."

### Recommendations

- "Choose isolation levels by anomaly tolerance with recorded rationale."
- "Document permitted anomalies for each workload."
- "Test concurrency behaviour at production isolation levels."

## Iterative Refinement of Reconstructions (`iterative-refinement`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/iterative-refinement.md`

### Claims

- "Reconstruction knowledge revises itself as evidence accumulates — the reading of the artifact changes when the record changes." _(certainty: high)_
- "Refinement is the reading changing as the record changes — the revised reading stands on the new record, not on the old." _(certainty: high)_
- "Each revision carries its own qualification — the refined reading is a new claim about the artifact with its own evidence and confidence, not an edit of the old one." _(certainty: high)_
- "Refinement is convergent when discriminative evidence arrives — the reading set narrows because evidence decides, not because the analyst settles." _(certainty: high)_
- "Revision without new evidence is churn — a refined reading must cite what changed in the record, or it is not refinement." _(certainty: high)_

### Relationships

- **driven_by** → `observable-evidence`
- **evolves** → `competing-hypotheses`
- **improves** → `inference-from-behavior`
- **characterises** → `artifact`
- **subject_to** → `incomplete-evidence`

### Constraints

- "A revision is valid only under the evidence that motivated it — refinement without a record delta is churn."
- "Refinement approaches the withheld truth but never closes it — the artifact's hidden semantics are reached by convergence, not by arrival."

### Recommendations

- "Anchor every revised reading to the record delta that motivated it."
- "Require a cited evidence delta for every refined reading."
- "Instrument convergence — record why the reading set closed."

## K7 Overlap Links (`k7-overlap`)

| Field | Value |
|---|---|
| kind | concept |
| domain | threat-analysis |
| research_cycle | "015" |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/k7-overlap.md`

### Claims

- "K7 is an unrelated financially motivated cluster that has never been linked to state-sponsored activity." _(certainty: high)_
- "Two links between Midnight Foundry and K7 are observed: the byte-identical code-signing string in Rivet, and one Cluster 2 VPS endpoint in an IP range previously used by K7 infrastructure." _(certainty: high)_
- "No other link between Midnight Foundry and K7 has been found." _(certainty: high)_
- "The infrastructure overlap is the strongest piece of evidence in the competing-hypothesis debate." _(certainty: high)_

### Relationships

- **linked_to** → `rivet-stealer`
- **linked_to** → `cluster-2-staging-infrastructure`
- **linked_to** → `attribution-assessment`
- **linked_to** → `open-analytical-questions`

### Constraints

- "Overlap claims are restricted to the two observed links; no claim here asserts a relationship between the actors themselves."

## Kill Chain (`kill-chain`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/kill-chain.md`

### Claims

- "The kill chain models an attack as a sequence of stages — from initial reconnaissance through delivery and exploitation to actions on objectives." _(certainty: high)_
- "Kill-chain stage progression is not linear — attackers can loop stages, skip stages, and combine them, making stage detection valuable but not deterministic." _(certainty: high)_
- "Detection and response value increases the earlier in the chain an attack is interrupted — each earlier stage prevents all subsequent stages." _(certainty: high)_
- "Kill chains are increasingly automated — commodity tooling executes multiple stages autonomously, compressing chain duration dramatically." _(certainty: high)_
- "The kill chain is adversary-observable — defenders can infer stage progression from observable artefacts (phishing emails, C2 traffic, lateral movement)." _(certainty: high)_

### Relationships

- **determines_progression** → `attacker-capability`
- **executes** → `threat-actor`
- **entered_through** → `attack-surface`
- **informs** → `threat-detection`
- **guided_by** → `incident-response`

### Constraints

- "Reconnaissance is not reliably detectable — defenders should not depend on detecting pre-intrusion surveillance."
- "Chain progression is observable only through artefacts — undetectable stages remain black boxes regardless of the model."

### Recommendations

- "Maintain a kill-chain coverage map that ties every stage to concrete detection capability and owners."
- "Prioritise detection and response at the earliest feasible stages — target delivery and initial access before C2."
- "Rehearse response per kill-chain stage — the response playbook should differ by where the chain is interrupted."

## Lateral Movement Pattern (`lateral-movement-pattern`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | threat-analysis |
| research_cycle | "015" |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/lateral-movement-pattern.md`

### Claims

- "RDP was the primary lateral movement mechanism, with credentials obtained via Mimikatz usage observed once (Victim A) and password-spraying against local admin accounts (Victim C)." _(certainty: high)_
- "Living-off-the-land binaries (PowerShell, WMIC, sc.exe) were used for enumeration; no custom tooling was observed in lateral movement except the Rivet stealer on Victim C." _(certainty: high)_
- "No domain-wide compromise was observed at any victim; the operators appeared to work within specific engineering workstations and file shares." _(certainty: high)_

### Relationships

- **part_of** → `midnight-foundry-campaign`
- **linked_to** → `rivet-stealer`

### Constraints

- "Movement claims are scoped to the observed per-victim behavior; no claim asserts domain-wide activity."

## Leader Election (`leader-election`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/leader-election.md`

### Claims

- "Leader election selects a single node to coordinate decisions in a distributed system — without it, competing nodes cannot converge." _(certainty: high)_
- "In Raft, leader election uses a request-vote mechanism: candidates request votes from all nodes and win if they receive a quorum." _(certainty: high)_
- "Every leader election is associated with a strictly increasing term number — terms act as a logical clock for leadership epoch." _(certainty: high)_
- "Nodes vote for at most one candidate per term on a first-come-first-served basis." _(certainty: high)_
- "Heartbeats maintain leader authority — followers reset their election timeout on receiving a heartbeat from the current leader." _(certainty: high)_
- "Election timeout is randomised across nodes (typically 150-300ms) to reduce the probability of simultaneous candidate announcements." _(certainty: high)_
- "A leader continuously asserts authority through periodic heartbeats — silence triggers a new election." _(certainty: high)_
- "Split-brain — the condition where two nodes both believe they are leader — is prevented by quorum-based election." _(certainty: high)_

### Relationships

- **requires** → `quorum`
- **part_of** → `raft-consensus`
- **prevents** → `split-brain`
- **affects** → `network-partition-recovery`
- **triggers** → `cascading-failure`

### Constraints

- "At most one leader can exist per term — this is enforced by the quorum requirement, not by mutual exclusion."
- "A candidate cannot vote for itself and must request votes from other nodes — a leader cannot be elected without external agreement."
- "Election timeout must be greater than heartbeat interval to prevent premature elections."
- "Clock skew between nodes must be bounded — excessive skew breaks timeout-based election logic."

### Recommendations

- "Never deploy a single-leader distributed system without monitoring the election rate."
- "Set up pre-emptive alerts at 1 election event — the first election may indicate a pattern."
- "Test leader election under load before production deployment — election timeouts behave differently under resource contention."

## Likelihood of Security Events (`likelihood`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/likelihood.md`

### Claims

- "Likelihood is the estimated probability or frequency of a security event occurring, typically expressed as a category (rare, unlikely, possible, likely, almost certain) or a probability range." _(certainty: high)_
- "Likelihood estimation in security is fundamentally different from probability in engineered systems — it involves an intelligent adversary actively attempting to influence outcomes." _(certainty: high)_
- "Adversarial likelihood estimates are conditional — the likelihood of an attack depends on attacker motivation, capability, and opportunity, not just system vulnerability." _(certainty: high)_
- "Likelihood estimates degrade with uncertainty about attacker behaviour — incomplete threat intelligence widens the confidence interval on any estimate." _(certainty: high)_
- "Likelihood and impact are independent dimensions of risk — a low-likelihood event can have catastrophic impact and still warrant mitigation." _(certainty: high)_

### Relationships

- **qualified_by** → `confidence`
- **degraded_by** → `incomplete-evidence`
- **informs** → `risk-acceptance`
- **informs** → `threat-detection`
- **informs** → `vulnerability-management`

### Constraints

- "Adversarial likelihood is conditional on attacker variables (motivation, capability, opportunity) — unconditional likelihood statements are not well-defined."
- "Likelihood cannot be zero for any plausible attack path — zero likelihood statements contradict adversarial reasoning."

### Recommendations

- "Never present likelihood without both a basis (historical, analytical, or adversarial) and a confidence level."
- "Treat novel attack likelihood as non-zero — maintain mitigations proportional to impact regardless of historical frequency."
- "Separate accidental-failure likelihood from adversarial likelihood in risk registers — they require different estimation methods."

## Metric Selection (`metric-selection`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/metric-selection.md`

### Claims

- "Metric choice determines what an evaluation demonstrates — different metrics measure different properties of the same predictions." _(certainty: high)_
- "Metrics are not interchangeable — accuracy, precision, recall, calibration, and coverage answer different questions about the same model." _(certainty: high)_
- "Metric selection is a decision under tradeoffs — the choice encodes which error type the evaluator finds costlier." _(certainty: high)_
- "Aggregate metrics hide per-segment structure — a good average can mask systematically failing segments." _(certainty: high)_
- "The metric must match the deployment loss — a mismatch between evaluation metric and real cost produces harmful optimization." _(certainty: high)_

### Relationships

- **composes** → `benchmark-validity`
- **estimates** → `generalization`
- **evaluates** → `confidence-calibration`
- **masks** → `distribution-shift`
- **contrasts_with** → `human-evaluation`
- **expresses_objectives** → `alignment`

### Constraints

- "A metric is evidence only about the property it measures."
- "Evaluation must not be tuned to the metric — optimizing the measurement corrupts the measurement."

### Recommendations

- "Define evaluation metrics from the deployment objective and the cost of each error type."
- "Report segment-level performance alongside every aggregate metric."
- "Document the rationale for every selected metric, including what it excludes."

## Midnight Foundry Intrusion Campaign (`midnight-foundry-campaign`)

| Field | Value |
|---|---|
| kind | concept |
| domain | threat-analysis |
| research_cycle | "015" |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/midnight-foundry-campaign.md`

### Claims

- "Midnight Foundry is the working designation for a cluster of intrusions observed between January and October of the reporting year against four aerospace and defense contractors in three countries." _(certainty: high)_
- "The intrusions combine spearphishing, custom backdoors, lateral movement over RDP, and staged exfiltration, with professionally separated operations across victims." _(certainty: high)_
- "Whether Midnight Foundry is one campaign, several intrusion sets, or two operational phases is an open question the source material does not resolve." _(certainty: medium)_
- "No operational impact has been confirmed at any victim; the observed activity was consistent with persistent collection." _(certainty: high)_

### Relationships

- **part_of** → `victim-set`
- **part_of** → `per-victim-operational-separation`
- **linked_to** → `attribution-assessment`
- **part_of** → `open-analytical-questions`

### Constraints

- "Campaign-level claims are restricted to umbrella-level facts; per-victim and per-tool detail is carried by the objects that own it."
- "The campaign object records the open boundary question; it does not resolve it."

## Model Monitoring (`model-monitoring`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/model-monitoring.md`

### Claims

- "Model monitoring is the continuous observation of deployed model behaviour and its context — it is the evidence channel that keeps deployed knowledge valid." _(certainty: high)_
- "Monitoring detects degradation signals (performance, distribution, input anomalies) before users experience failure." _(certainty: high)_
- "Monitoring is bounded by what is instrumented — unobserved dimensions degrade silently." _(certainty: high)_
- "Monitoring produces evidence for decisions (retraining, rollback, escalation) — its value is realized in the decisions it informs." _(certainty: high)_
- "Monitoring is itself a system with failure modes — missing telemetry, alert fatigue, and stale thresholds degrade it silently." _(certainty: high)_

### Relationships

- **detects** → `distribution-shift`
- **tracks** → `confidence-calibration`
- **validates** → `uncertainty-estimation`
- **informs** → `retraining-decisions`
- **reduces** → `deployment-risk`
- **detects** → `hallucination`

### Constraints

- "A deployed model's validity cannot be assessed beyond what is monitored."
- "Monitoring evidence is only as fresh as the last valid observation — stale telemetry is not evidence."

### Recommendations

- "Instrument distribution, performance, and business outcome dimensions jointly."
- "Refresh thresholds and references whenever the model is retrained or redeployed."
- "Make monitoring feed an explicit decision channel — alerts must map to actions."

## Network Failure Propagation (`network-failure-propagation`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/network-failure-propagation.md`

### Claims

- "Network failures propagate upward through layers — a TCP timeout becomes an HTTP timeout which becomes an application failure." _(certainty: high)_
- "Connection pool exhaustion at any layer (client, proxy, server) causes cascading failures as queued requests accumulate and time out." _(certainty: high)_
- "Retry storms — coordinated retry from many clients after a transient failure — can cause sustained overload worse than the original failure." _(certainty: high)_
- "Circuit breakers prevent cascading failures by stopping retries to a failing dependency after a threshold of failures." _(certainty: high)_
- "Exponential backoff with jitter is the most effective retry strategy for avoiding retry storms." _(certainty: high)_
- "Congestion collapse occurs when retransmissions consume more bandwidth than data, reducing effective throughput to near zero." _(certainty: high)_

### Relationships

- **originates_from** → `tcp-tls-foundation`
- **manifests_as** → `http-protocol`
- **amplifies** → `proxy-infrastructure`
- **mitigates** → `retry-pattern`
- **informs** → `health-check-pattern`

### Constraints

- "TCP congestion control reduces send window on packet loss — this is automatic and unavoidable at the transport layer."
- "Circuit breaker open state prevents all requests to a failing dependency until the cooldown period expires."

### Recommendations

- "Implement exponential backoff with jitter as the default retry strategy for all network operations."
- "Monitor connection pool depth and TIME_WAIT count as capacity metrics — not just CPU and memory."
- "Use short request timeouts (5-10s) with retry rather than long timeouts (30-60s) without — fail fast, retry smart."

## Network Partition Recovery (`network-partition-recovery`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/network-partition-recovery.md`

### Claims

- "Network partition recovery is the process of detecting that a partition has resolved, reconnecting separated nodes, and reconciling any state that diverged during the partition." _(certainty: high)_
- "The duration of a partition directly affects recovery complexity — longer partitions produce more divergent state and higher reconciliation cost." _(certainty: high)_
- "Recovery from a partition requires three phases: detection (partition healed), stabilisation (nodes rejoin safely), and reconciliation (divergent state resolved)." _(certainty: high)_
- "In quorum-based systems, recovery is simpler because the minority partition could not make progress — only the majority side has authoritative state." _(certainty: high)_
- "In availability-preferring systems, recovery requires conflict resolution because both partitions accepted writes." _(certainty: high)_

### Relationships

- **resolves** → `split-brain`
- **simplifies** → `raft-consensus`
- **determines** → `cap-theorem`
- **requires** → `eventual-consistency`
- **affects** → `quorum`
- **risk_during** → `cascading-failure`

### Constraints

- "Recovery cannot begin until partition detection is confirmed — premature recovery attempts fail or cause oscillation."
- "Reconciliation is bounded by the size of divergent state — longer partitions produce more divergence and longer recovery."

### Recommendations

- "Define and document partition recovery procedures before deployment — designing recovery under incident pressure produces incorrect procedures."
- "Automate partition detection but require operator approval for recovery initiation in systems with manual reconciliation requirements."
- "Run partition recovery drills quarterly — recovery procedures that are never exercised will fail when first attempted under incident conditions."

## Normalization (`normalization`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/normalization.md`

### Claims

- "Normalization is the disciplined evaluation of schema structure against normal forms — each form eliminates a class of redundancy and its update anomalies." _(certainty: high)_
- "Normal forms are constraints on structure — they define what counts as well-formed relations, not as a separate design vocabulary." _(certainty: high)_
- "Normalization eliminates anomalies — redundancy, update anomalies, and deletion anomalies — by distributing facts across correctly structured relations." _(certainty: high)_
- "Denormalization is a deliberate tradeoff, not an accident — reintroducing redundancy for query performance requires compensating discipline." _(certainty: high)_
- "The value of normalization degrades past the point of diminishing returns — beyond a practical form, purity costs complexity without integrity gain." _(certainty: high)_

### Relationships

- **evaluates** → `relational-model`
- **guides** → `schema-design`
- **reinforces** → `data-integrity`
- **shapes** → `query-optimization`
- **complicates** → `schema-migration`

### Constraints

- "Every redundant fact requires a compensating control — denormalization without discipline is corruption in waiting."
- "Normal forms are structural constraints — a relation that violates its declared form is structurally unsound."

### Recommendations

- "Apply normal forms as checkable criteria, not as ideology."
- "Pair every denormalization with a consistency control."
- "Revisit normalization decisions when workloads change."

## Observable Evidence from Artifacts (`observable-evidence`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/observable-evidence.md`

### Claims

- "Observable evidence is the recorded signal the artifact yields — bytes, strings, hashes, timestamps, event sequences, and files touched, as captured." _(certainty: high)_
- "Evidence records observation, not meaning — the same evidence record supports multiple interpretations, and interpretation is a separate step." _(certainty: high)_
- "Evidence is qualified by its provenance — who captured it, how, when, and what was done to it between capture and analysis." _(certainty: high)_
- "The absence of recorded evidence is not evidence about the artifact — a clean capture is a statement about the capture, not about the artifact's behaviour." _(certainty: high)_
- "Evidence quality varies with capture conditions — contaminated, incomplete, or selection-biased captures degrade every claim built on them." _(certainty: high)_

### Relationships

- **produced_by** → `behavioral-observation`
- **originates_from** → `artifact`
- **qualified_by** → `confidence`
- **subject_to** → `incomplete-evidence`
- **informs** → `likelihood`
- **feeds** → `threat-detection`

### Constraints

- "Observable evidence records observation, not meaning — meaning is inference, never part of the record."
- "A clean capture is evidence about the capture, not about the artifact — absence of signal is not absence of behaviour."

### Recommendations

- "Treat provenance as part of the evidence — capture context qualifies every claim built on the record."
- "Preserve a pristine working copy and analyse the copy."
- "Record capture selection explicitly — what the capture could see is part of every conclusion built on it."

## Open Analytical Questions for Midnight Foundry (`open-analytical-questions`)

| Field | Value |
|---|---|
| kind | decision |
| domain | threat-analysis |
| research_cycle | "015" |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/open-analytical-questions.md`

### Claims

- "The source lists five open analytical questions: one campaign or several intrusion sets; Hammer one family or two; unassigned-host membership; K7 overlap significance; and lure-content sourcing as possible evidence of a separate access." _(certainty: high)_
- "None of the five questions is resolved by the source material; each carries attached analyst disagreement." _(certainty: high)_
- "The open questions matter for how the activity is organized in knowledge bases and tracking systems." _(certainty: high)_

### Relationships

- **part_of** → `midnight-foundry-campaign`
- **linked_to** → `hammer-classification-dispute`
- **linked_to** → `unassigned-hosts`
- **linked_to** → `k7-overlap`
- **linked_to** → `spearphishing-initial-access`
- **linked_to** → `attribution-assessment`

### Constraints

- "The object records the questions as open; it resolves none of them."

### Recommendations

- "Represent each open question at the object whose boundary it contests, and consolidate them as a campaign-level open-question list."

## Optimization Pass (`optimization-pass`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/optimization-pass.md`

### Claims

- "An optimization pass is a single unit of transformation — a well-scoped rewrite over a program representation, reusable across programs." _(certainty: high)_
- "Passes are composed into pipelines — a sequence of passes whose combined effect is the optimization outcome." _(certainty: high)_
- "Pass ordering matters — the output of one pass changes what later passes can do, and the best order is not always obvious." _(certainty: high)_
- "Many passes are fixed-point computations — they must run until no further improvement occurs, with guaranteed termination." _(certainty: high)_
- "A pass pipeline is correct only if every constituent pass preserves semantics — pipeline correctness is the composition of per-pass correctness." _(certainty: high)_

### Relationships

- **composed_of** → `compiler-optimization`
- **operates_on** → `intermediate-representation`
- **preserves** → `program-semantics`
- **affects** → `compiler-performance`
- **constrained_by** → `compiler-correctness`

### Constraints

- "Pipeline correctness is the composition of per-pass correctness — one unsound pass invalidates the pipeline."
- "Fixed-point passes must terminate — a pass that cannot converge is a pipeline defect regardless of its quality."

### Recommendations

- "Document each pass's contract — its assumptions, what it canonicalizes, and what it requires from its input."
- "Run passes to fixed points deliberately, with termination guarantees."
- "Test pipelines differentially, including pass-order variants."

## Optimization Tradeoffs (`optimization-tradeoffs`)

| Field | Value |
|---|---|
| kind | decision |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/optimization-tradeoffs.md`

### Claims

- "Optimization is a decision problem — every optimization posture trades generated-code quality against compile time, binary size, and debuggability." _(certainty: high)_
- "The optimization posture is chosen per context — release builds optimize differently from debug builds, and shipping contexts weight the axes differently." _(certainty: high)_
- "Tradeoffs are explicit when chosen, implicit when defaulted — an unexamined default still makes a tradeoff, just an unaudited one." _(certainty: high)_
- "Debuggability is the tradeoff dimension most often ignored — optimized builds that users must debug become a correctness-equivalent cost." _(certainty: high)_
- "Tradeoff decisions are reversible only when measurement exists — without performance and compile-time tracking, decisions cannot be audited or rolled back rationally." _(certainty: high)_

### Relationships

- **decides_over** → `compiler-optimization`
- **shapes** → `compiler-performance`
- **configures** → `build-systems`
- **defines** → `debug-vs-release-modes`
- **bounded_by** → `equivalence-checking`

### Constraints

- "Every optimization posture is a tradeoff — choosing 'default' chooses a tradeoff, not a way to avoid one."
- "Posture changes require measurement — a tradeoff decision without evidence is reversible only by accident."

### Recommendations

- "Make optimization posture an explicit decision with a recorded owner and evidence."
- "Measure before changing posture."
- "Never let debug/release divergence become a debugging tax on production issues."

## Overfitting (`overfitting`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/overfitting.md`

### Claims

- "Overfitting is the absorption of noise from training data — the model fits patterns that exist in the sample but not in the distribution." _(certainty: high)_
- "The train-validation gap is the primary observable signal — growing gap with training progress indicates overfitting." _(certainty: high)_
- "Overfitting risk increases with capacity relative to information in the data — excess capacity has nowhere to go but noise." _(certainty: high)_
- "Overfitting is mitigated by regularization, data volume, and early stopping — each trades expressiveness for stability." _(certainty: high)_
- "Overfitting is undetectable from training performance alone — training error approaching zero is consistent with either excellent fit or total memorization." _(certainty: high)_

### Relationships

- **degrades** → `generalization`
- **depends_on** → `training-data`
- **masked_by** → `benchmark-validity`
- **interacts_with** → `uncertainty-estimation`
- **detected_by** → `model-monitoring`
- **worsens_with** → `distribution-shift`

### Constraints

- "Training performance is not evidence of deployment performance."
- "Evaluation data must never influence training, tuning, or model selection."

### Recommendations

- "Monitor the train-validation gap as a training-time quality gate."
- "Enforce evaluation-set separation as an invariant across the entire pipeline, including tuning."
- "Validate final models on a fresh holdout never touched during development."

## Overload Handling (`overload-handling`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/overload-handling.md`

### Claims

- "Overload handling is the discipline of responding when demand exceeds capacity — admission and shedding are the mechanisms." _(certainty: high)_
- "Overload is a condition of the system under demand, not a new knowledge kind — the response is constraints on admission and shedding." _(certainty: high)_
- "Admission control bounds what enters the system — a constraint on acceptance — while load shedding bounds what continues under saturation." _(certainty: high)_
- "Overload handling is structurally identical to backpressure and circuit-breaking — the bounded-response family — the Cycle 006 cross-domain link." _(certainty: high)_
- "Shedding priority is a decision — what to drop under overload is a policy choice, not an accident." _(certainty: high)_

### Relationships

- **protects** → `real-time-system`
- **coordinates_with** → `scheduling-policy`
- **prevents** → `cascading-failure`
- **analogous_to** → `backpressure`
- **analogous_to** → `circuit-breaker`

### Constraints

- "Admission is bounded — the system must not accept beyond its capacity under the guarantee."
- "Shedding follows priority — the wrong-work shed is a priority violation."

### Recommendations

- "Model overload handling as constraints on admission and shedding."
- "Decide the shedding order explicitly."
- "Practice overload response in realistic drills."

## Per-Victim Operational Separation Pattern (`per-victim-operational-separation`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | threat-analysis |
| research_cycle | "015" |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/per-victim-operational-separation.md`

### Claims

- "The intrusions are professionally separated: distinct command-and-control infrastructure per victim, fresh spearphishing lures per company, and minimal tool overlap between victim networks." _(certainty: high)_
- "Per-victim separation has exactly one observed exception: the module host served Hammer-B modules to both Victim B and Victim D." _(certainty: high)_
- "The separation profile is an observed pattern of the intrusions; the source does not establish that it was deliberate." _(certainty: medium)_

### Relationships

- **part_of** → `midnight-foundry-campaign`
- **linked_to** → `spearphishing-initial-access`
- **linked_to** → `dropper`
- **linked_to** → `cluster-1-c2-infrastructure`
- **linked_to** → `cluster-2-staging-infrastructure`

### Constraints

- "Separation claims are restricted to the observed profile; operator intent is not asserted."

### Recommendations

- "Record the per-victim separation and its single exception as one observable profile."

## Perception Uncertainty (`perception-uncertainty`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/perception-uncertainty.md`

### Claims

- "Perception uncertainty is the qualification of observations at epistemic distance — confidence metadata over the chain from sensor to belief." _(certainty: high)_
- "Uncertainty in perception is the same structure as uncertainty everywhere — the 007/008 qualification model applies unchanged." _(certainty: high)_
- "Perception is inference, and inference carries its uncertainty — the interpretation is a claim, qualified by confidence, never a fact." _(certainty: high)_
- "Uncertainty is not a failure of perception — it is the correct description of indirect observation." _(certainty: high)_
- "Perception claims are valid only under stated conditions — environment, sensor state, and model bound the interpretation." _(certainty: high)_

### Relationships

- **afflicts** → `belief-state`
- **constrained_by** → `sensing`
- **analogous_to** → `confidence-calibration`
- **analogous_to** → `uncertainty-estimation`
- **constrained_by** → `incomplete-evidence`

### Constraints

- "Calibration is the honesty of the belief — overconfidence is a qualification failure, not a perception failure."
- "Uncertainty is metadata about the observation chain — it describes the distance, it does not remove it."

### Recommendations

- "Represent perception uncertainty as qualification of observation — confidence metadata, not a perception construct."
- "Audit calibration, and treat overconfidence as the priority failure mode."
- "Hold ambiguity until the evidence resolves it."

## Persistence Pattern (`persistence-pattern`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | threat-analysis |
| research_cycle | "015" |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/persistence-pattern.md`

### Claims

- "Persistence on non-domain workstations used scheduled tasks and WMI event subscriptions." _(certainty: high)_
- "Persistence on servers used service registration for the Hammer backdoor." _(certainty: high)_

### Relationships

- **part_of** → `midnight-foundry-campaign`
- **linked_to** → `hammer-backdoor-family`

### Constraints

- "Persistence claims cover the documented mechanisms only; movement and collection are separate objects."

## Physical State (`physical-state`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/physical-state.md`

### Claims

- "State is a snapshot of a system's condition at a point in time — a set of claims about the system, not a new knowledge type." _(certainty: high)_
- "A differential equation is a constraint governing state evolution — dynamics bind how state may change, exactly as invariants bind data." _(certainty: high)_
- "State is never directly known in a cyber-physical system — it is always estimated from observations through a model." _(certainty: high)_
- "A state representation is a model of the world under stated conditions — the same structure as a schema." _(certainty: high)_
- "Continuous evolution is expressible as constraint relationships over discrete observations — continuity is mathematics, not ontology." _(certainty: high)_

### Relationships

- **describes** → `cyber-physical-system`
- **evaluated_through** → `sensing`
- **analogous_to** → `schema-design`
- **constrained_by** → `deadline`
- **informs** → `actuation`

### Constraints

- "State evolution is governed by stated dynamics — the constraint set is the model, not a continuous primitive."
- "A state claim is valid only for its stated instant and model — staleness or model change invalidates it."

### Recommendations

- "Model continuous dynamics as constraint relationships over state, not as a continuous category."
- "Qualify every state claim with its estimation confidence."
- "Reject decisions on stale state."

## Priority Inversion (`priority-inversion`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/priority-inversion.md`

### Claims

- "Priority inversion is a blocking failure — a low-priority task holds a resource a high-priority task needs, inverting the priority order." _(certainty: high)_
- "Priority inversion is a failure mode of the priority ordering invariant — the schedule violates the ordering it promises." _(certainty: high)_
- "Priority inversion is bounded — with priority inheritance or priority ceiling, blocking is bounded by the critical section, not by arbitrary delay." _(certainty: high)_
- "Priority inversion resolves as failure mode + constraint (priority ordering) + mitigation pattern (priority inheritance) — no concurrency-failure primitive." _(certainty: high)_
- "Priority inversion is the strongest test of contention under guarantees — time + resources + competing tasks + blocking all at once." _(certainty: high)_

### Relationships

- **afflicts** → `fixed-priority-scheduling`
- **challenges** → `scheduling-policy`
- **threatens** → `deadline`
- **emerges_in** → `task-scheduling`
- **analogous_to** → `split-brain`

### Constraints

- "Priority ordering is an invariant — the schedule must respect the priority order."
- "Blocking must be bounded — unbounded priority inversion violates the guarantee."

### Recommendations

- "Model priority inversion as a failure mode with constraint and mitigation."
- "Apply priority inheritance or ceiling when sharing resources."
- "Monitor for inversion chains under load."

## Probabilistic Outputs (`probabilistic-outputs`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/probabilistic-outputs.md`

### Claims

- "Probabilistic outputs express a model's belief distribution over outcomes rather than a single point prediction." _(certainty: high)_
- "Probabilistic outputs are only as useful as their calibration — an uncalibrated probability is a ranking, not a probability." _(certainty: high)_
- "Probabilistic outputs enable downstream decisions that point predictions do not — abstention, risk-based thresholds, and uncertainty-aware routing." _(certainty: high)_
- "Probability output formats (softmax, logits, ensembles, native probability models) differ in how faithfully they represent underlying uncertainty." _(certainty: high)_
- "Probabilistic outputs compound — downstream decisions inherit the calibration of upstream probability estimates." _(certainty: high)_

### Relationships

- **requires** → `confidence-calibration`
- **enabled_by** → `uncertainty-estimation`
- **mitigates** → `hallucination`
- **expresses** → `likelihood`
- **informs** → `risk-acceptance`
- **informs** → `retraining-decisions`

### Constraints

- "A probability output is only meaningful relative to the distribution it was learned from."
- "Decision thresholds must be set from calibrated probabilities, not raw output scores."

### Recommendations

- "Prefer calibrated probability models for any decision pipeline that consumes confidence."
- "Gate high-stakes automation on calibrated confidence thresholds."
- "Record the calibration state of every probability source feeding a pipeline."

## Procurement-Aware Targeting Pattern (`procurement-aware-targeting`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | threat-analysis |
| research_cycle | "015" |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/procurement-aware-targeting.md`

### Claims

- "In all four compromises, access was obtained within two weeks of the victim becoming part of a funded procurement program visible in public procurement notices." _(certainty: high)_
- "The lure content references real procurement documents that would be visible only to someone with prior access to the procurement process or to the relevant procurement feeds." _(certainty: high)_
- "The sourcing of the procurement-aware lure content is unexplained; it may imply a separate, earlier compromise of a procurement entity that has never been observed." _(certainty: low)_
- "The procurement-linked timing is consistent with state collection priorities, but the source records this as an analytical reading, not a demonstrated fact." _(certainty: medium)_

### Relationships

- **linked_to** → `victim-set`
- **linked_to** → `spearphishing-initial-access`
- **linked_to** → `attribution-assessment`

### Constraints

- "The timing correlation is an observed pattern, not evidence of intent."

### Recommendations

- "Track procurement-linked timing as a targeting observable, distinct from any attribution reading built on it."

## Program Semantics (`program-semantics`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/program-semantics.md`

### Claims

- "Program semantics is the meaning of a program — the behaviour it exhibits when executed, independent of its representation." _(certainty: high)_
- "Semantics is the correctness yardstick — every transformation, lowering, and code-generation step is judged against semantic preservation." _(certainty: high)_
- "Semantics is defined by formal models — operational and denotational semantics give meaning a checkable form instead of an informal gloss." _(certainty: high)_
- "Semantic equivalence is relative to a chosen notion of observable behaviour — two programs equivalent under one observation model may differ under another." _(certainty: high)_
- "Formalizing semantics is a modelling act with its own failure modes — the model can misrepresent the language it claims to define." _(certainty: high)_

### Relationships

- **expressed_by** → `abstract-syntax-tree`
- **preserved_through** → `intermediate-representation`
- **judged_by** → `compiler-optimization`
- **based_on** → `equivalence-checking`
- **anchored_in** → `compiler-correctness`

### Constraints

- "Meaning is invariant under representation — the same program in different forms has the same semantics."
- "Correctness claims are valid only under a stated observation model — unstated observation assumptions make equivalence claims untestable."

### Recommendations

- "Write the semantics down in a checkable form before designing transformations."
- "Define correctness against an explicit observation model and document the behavioural boundary it permits."
- "Validate the semantic model against real program behaviour continuously."

## Proxy Infrastructure (`proxy-infrastructure`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/proxy-infrastructure.md`

### Claims

- "Forward proxies relay client requests to targets, masking the client's IP address and altering the client's network fingerprint." _(certainty: high)_
- "Residential proxies hosted on ISP connections have better IP reputation than datacenter proxies but are slower and less reliable." _(certainty: high)_
- "Proxies that terminate TLS and re-encrypt change the TLS fingerprint from the client's to the proxy's." _(certainty: high)_
- "Transparent proxies intercept traffic without explicit client configuration, detectable by the target server via proxy headers or connection properties." _(certainty: medium)_
- "Connection pool exhaustion at the proxy causes downstream retry storms as clients retry failed requests." _(certainty: high)_

### Relationships

- **terminates** → `tcp-tls-foundation`
- **forwards** → `http-protocol`
- **introduces** → `network-failure-propagation`
- **affects** → `automation-detection-surface`
- **influenced_by** → `retry-pattern`

### Constraints

- "Proxy cannot relay UDP traffic unless it supports SOCKS5 or a tunnelling protocol."
- "Transparent proxy interception requires the client traffic to pass through the proxy's network path."

### Recommendations

- "Use residential proxies for any automation where IP reputation is a significant detection risk."
- "Implement proxy rotation with health checking and circuit breaker patterns."
- "Test proxy TLS fingerprint before deploying — residential proxy networks may alter the fingerprint unexpectedly."

## Query Optimization (`query-optimization`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/query-optimization.md`

### Claims

- "Query optimization is the transformation of a query into an equivalent form with lower execution cost — the result relation is the correctness contract." _(certainty: high)_
- "Optimization correctness is logical equivalence — a rewrite that changes the result relation is a miscompilation of the query." _(certainty: high)_
- "Query rewrites are judged against the relational observation model — two query forms are equivalent when they produce the same relation under the model's semantics." _(certainty: high)_
- "Every rewrite has enabling conditions — equivalence holds only where the rewrite's preconditions (semantics of operators, data independence, NULL handling) hold." _(certainty: high)_
- "Query optimization is the same epistemic structure as compiler optimization — a transformation of representation that preserves meaning." _(certainty: high)_

### Relationships

- **performs** → `query-planning`
- **bounded_by** → `equivalence-checking`
- **preserves** → `relational-model`
- **analogous_to** → `compiler-optimization`
- **shaped_by** → `index-selection`

### Constraints

- "Every rewrite must preserve the result relation — semantic change is a correctness failure."
- "Rewrites are legal only where their enabling conditions hold — equivalence is conditional, not universal."

### Recommendations

- "Gate rewrites on their enabling conditions."
- "Differential-test query optimization against unoptimized execution."
- "Treat optimizer correctness with compiler correctness discipline."

## Query Planning (`query-planning`)

| Field | Value |
|---|---|
| kind | decision |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/query-planning.md`

### Claims

- "Query planning is the decision of how to execute a declarative query — the planner chooses join order, access paths, and algorithms under a cost model." _(certainty: high)_
- "Plan quality is bounded by statistics quality — the planner decides on evidence, and unreliable statistics produce unreliable plans." _(certainty: high)_
- "Planner choices trade plan quality against planning cost — exhaustive search is impossible for complex queries." _(certainty: high)_
- "The planner's output is a recommendation, not a guarantee — plans are hypotheses about cost that runtime evidence can falsify." _(certainty: high)_
- "Plan stability is a correctness-adjacent property — plan changes alter performance without altering results, and destabilized plans become operational incidents." _(certainty: high)_

### Relationships

- **operates_upon** → `relational-model`
- **performed_by** → `query-optimization`
- **dependent_on** → `index-selection`
- **bounded_by** → `database-indexing`
- **bounded_by** → `equivalence-checking`

### Constraints

- "Plan choice is bounded by correctness — no plan may return a different result than the query's semantics require."
- "Plan decisions are bounded by evidence — decisions without statistics are guesses."

### Recommendations

- "Maintain statistics freshness as an operational duty."
- "Monitor plan stability and treat flips as incidents."
- "Verify plans against runtime evidence periodically."

## Quorum (`quorum`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/quorum.md`

### Claims

- "A quorum is the minimum number of nodes that must agree on a value for a distributed system to make progress." _(certainty: high)_
- "A simple majority quorum requires more than N/2 nodes, where N is the total number of nodes." _(certainty: high)_
- "Quorum intersection property — any two quorums must share at least one node — ensures consistency across reads and writes." _(certainty: high)_
- "Read and write quorums can be configured independently as long as they intersect." _(certainty: high)_
- "Without a quorum, the system cannot make progress — writes fail, elections stall, and state cannot be advanced." _(certainty: high)_
- "Larger quorums increase fault tolerance but reduce availability because more nodes must respond." _(certainty: high)_
- "A system cannot simultaneously tolerate N node failures and require (N+1)-node quorums — these constraints are incompatible." _(certainty: high)_

### Relationships

- **required_by** → `leader-election`
- **required_by** → `raft-consensus`
- **affects** → `network-partition-recovery`
- **contrasts_with** → `eventual-consistency`

### Constraints

- "A system with quorum size Q can tolerate at most (N - Q) simultaneous failures."
- "Read and write quorums must satisfy R + W > N to guarantee read-after-write consistency."

### Recommendations

- "Always verify quorum intersection property when configuring read and write quorums independently."
- "Set monitoring alerts at 2 * quorum_size available nodes, not at quorum_size."
- "Use odd-numbered clusters (3, 5, 7) to maximise the fault-tolerance-to-node ratio."

## Raft Consensus (`raft-consensus`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/raft-consensus.md`

### Claims

- "Raft is a consensus algorithm that ensures all non-faulty nodes agree on the same sequence of log entries." _(certainty: high)_
- "Raft operates through three core subsystems: leader election, log replication, and safety guarantees." _(certainty: high)_
- "Log entries flow from leader to followers — the leader accepts client requests and appends them to its local log before replicating." _(certainty: high)_
- "A log entry is committed when the leader has replicated it to a quorum of nodes — committed entries are durable and applied in order." _(certainty: high)_
- "Raft guarantees that committed entries are never lost and are applied in the same order on all nodes." _(certainty: high)_
- "Raft restricts log writing to a single leader per term — only the leader decides what entries to append." _(certainty: high)_
- "The Raft safety property guarantees that if two logs contain the same entry at the same index, all prior entries are identical." _(certainty: high)_
- "Raft's election restriction ensures a candidate can only win an election if its log is at least as up-to-date as a quorum of nodes — this prevents a stale leader from overwriting committed entries." _(certainty: high)_

### Relationships

- **requires** → `quorum`
- **includes** → `leader-election`
- **prevents** → `split-brain`
- **survives** → `network-partition-recovery`
- **vulnerable_to** → `cascading-failure`
- **similar_to** → `circuit-breaker`

### Constraints

- "Only one leader may exist per term — enforced by quorum-based election, not by mutual exclusion primitives."
- "Committed entries are never lost — once an entry reaches quorum, it is durable regardless of subsequent leader changes."
- "Log entries are committed in order — entry at index I is committed only after all entries with lower index are committed."
- "A candidate cannot become leader unless its log is at least as up-to-date as a quorum of nodes."

### Recommendations

- "Always run Raft clusters in odd-numbered configurations (3, 5, or 7 nodes)."
- "Implement leader-based read isolation at the application level to guarantee linearisable reads."
- "Pre-allocate and monitor disk space for Raft logs to prevent unbounded-growth-induced failures."
- "Test Raft cluster behaviour under network latency variation during pre-production validation."

## Rate-Monotonic Analysis (`rate-monotonic-analysis`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/rate-monotonic-analysis.md`

### Claims

- "Rate-monotonic analysis is a feasibility test — a claim about whether a task set meets its deadlines under fixed-priority scheduling." _(certainty: high)_
- "The utilization bound is the analysis core — a sufficient condition expressed as a constraint on total utilization." _(certainty: high)_
- "The analysis is a claim with evidence and conditions — the bound holds under periodic, independent, deadline-equals-period assumptions." _(certainty: high)_
- "The analysis result is an observation about feasibility, not a guarantee about runtime — runtime evidence can diverge from the bound's assumptions." _(certainty: high)_
- "Rate-monotonic analysis is structurally identical to equivalence checking — a mechanical verification that makes a property claim — the Cycle 009 cross-domain link." _(certainty: high)_

### Relationships

- **verifies** → `fixed-priority-scheduling`
- **consumes** → `worst-case-execution-time`
- **bounded_by** → `deadline`
- **analogous_to** → `equivalence-checking`
- **analogous_to** → `benchmark-validity`

### Constraints

- "The bound is valid only under its stated conditions — periodic, independent tasks with deadline equal to period."
- "The analysis result is bound by its inputs — a bad WCET propagates into a false feasibility claim."

### Recommendations

- "Treat feasibility analysis as a claim with evidence and conditions."
- "Cross-check the bound against the actual task model."
- "Propagate WCET confidence into the analysis result."

## Real-Time Guarantee (`real-time-guarantee`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/real-time-guarantee.md`

### Claims

- "A real-time guarantee is a scoped claim — a statement that timing requirements will be met under stated conditions." _(certainty: high)_
- "The guarantee's validity is bound by its conditions — deadline, load, and model assumptions qualify the claim." _(certainty: high)_
- "A real-time guarantee is the fourth guarantee object — joining type-safety (009), data-integrity (010), and atomicity (010) — the guarantee-object motif at n=4." _(certainty: high)_
- "The guarantee is established by analysis and verified by runtime — it is a claim with evidence, not an observation." _(certainty: high)_
- "Temporal correctness is not a separate kind of correctness — it is logical correctness plus a validity condition on completion." _(certainty: high)_

### Relationships

- **bounded_by** → `deadline`
- **established_by** → `schedulability-analysis`
- **rests_on** → `worst-case-execution-time`
- **analogous_to** → `type-safety`
- **analogous_to** → `data-integrity`

### Constraints

- "A real-time guarantee is valid only under its stated conditions — deadline, load, and model assumptions bound the claim."
- "A guarantee outside its scope is a false promise — scope precision is part of the claim."

### Recommendations

- "Model real-time guarantees as scoped claims with conditions."
- "Verify the guarantee's conditions continuously."
- "Keep the guarantee-object pattern as the fourth instantiation."

## Real-Time System (`real-time-system`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/real-time-system.md`

### Claims

- "A real-time system is a system whose correctness depends on the time at which results are produced — not only on what is produced." _(certainty: high)_
- "A deadline is a validity condition on completion — a result produced after its deadline is invalid regardless of its content." _(certainty: high)_
- "Real-time correctness decomposes into logical correctness plus temporal correctness — the temporal part is carried by constraints." _(certainty: high)_
- "Guarantees in a real-time system are claims about future behaviour — valid only under stated conditions about load, timing, and environment." _(certainty: high)_
- "Real-time guarantees are the unification-hypothesis test at the temporal pole — a guarantee is valid if its stated conditions hold, exactly as knowledge (008), transformations (009), and data (010) are." _(certainty: high)_

### Relationships

- **constrained_by** → `deadline`
- **requires** → `task-scheduling`
- **evaluated_through** → `worst-case-execution-time`
- **affected_by** → `deployment-risk`
- **analogous_to** → `build-systems`

### Constraints

- "A result produced after its deadline is invalid — temporal correctness is a validity condition, not a quality preference."
- "A real-time guarantee is valid only under its stated conditions — load, timing, and environment assumptions bound the claim."

### Recommendations

- "Express deadlines as constraints on completion, not as a special temporal category."
- "Treat timing analyses as observations with confidence, not promises."
- "Audit guarantee assumptions as the system changes."

## Real-Time Throughput Tradeoff (`real-time-throughput-tradeoff`)

| Field | Value |
|---|---|
| kind | decision |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/real-time-throughput-tradeoff.md`

### Claims

- "The real-time throughput tradeoff is a decision — how much throughput to trade for timing guarantee — not a property of the system." _(certainty: high)_
- "Timing and throughput are in tension — headroom for guarantees costs throughput; throughput pressure erodes guarantees." _(certainty: high)_
- "The decision carries four factors — timing_sensitivity, throughput_target, resource_budget, and deadline_margin — the decision-object pattern at 4." _(certainty: high)_
- "The decision is structurally identical to optimization-tradeoffs — a performance posture decision — the Cycle 009 cross-domain link." _(certainty: high)_
- "Throughput is measured; the guarantee is claimed — the two live in different evidence layers, so the tradeoff is between an observation and a claim." _(certainty: high)_

### Relationships

- **trades_against** → `real-time-guarantee`
- **preserves** → `deadline`
- **depends_on** → `hard-vs-soft-real-time`
- **analogous_to** → `optimization-tradeoffs`
- **analogous_to** → `compiler-performance`

### Constraints

- "The guarantee is valid only with its margin — a margin below its stated bound invalidates the claim."
- "The tradeoff must be decided — an undecided tradeoff is a drift in progress."

### Recommendations

- "Treat the tradeoff as a decision with stated factors."
- "Monitor margin as a first-class signal."
- "Keep throughput measurement separate from guarantee claims."

## Reconstruction Confidence (`reconstruction-confidence`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/reconstruction-confidence.md`

### Claims

- "Confidence in a reconstruction is confidence attached to an interpretation of an inference — the claim in the analysis furthest removed from direct observation." _(certainty: high)_
- "Confidence in a reading must reflect the inference's distance, not the analyst's fluency — the longer the evidential chain, the harder honest confidence must work." _(certainty: high)_
- "Confidence in a reading and confidence in an observation are anchored differently — conflating them is the analysis's characteristic corruption." _(certainty: high)_
- "The object of confidence in a reconstruction is the reading, never the artifact's hidden nature — the analyst is confident about a claim, and the claim is about the artifact." _(certainty: high)_
- "Overconfidence is the reconstruction's characteristic failure — fluency is the analyst's most convincing substitute for evidence." _(certainty: high)_

### Relationships

- **anchored_in** → `confidence`
- **qualifies** → `inference-from-behavior`
- **applies_to** → `competing-hypotheses`
- **analogous_to** → `belief-state`
- **analogous_to** → `probabilistic-outputs`

### Constraints

- "Confidence qualifies the claim it is attached to — the object of reconstruction confidence is the reading, never the artifact's hidden nature."
- "Fluency is not confidence — confidence is calibrated to evidence strength, and a reading's smoothness is never grounds for it."

### Recommendations

- "Record reconstruction confidence in the same form as any claim confidence — a reading gets no special scale."
- "Record confidence destination explicitly — say what the confidence is about."
- "Calibrate interpretation-anchored confidence against evidence strength before acting on it."

## Relational Model (`relational-model`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/relational-model.md`

### Claims

- "The relational model represents data as relations — sets of tuples over named attributes — with keys defining identity and integrity rules bounding validity." _(certainty: high)_
- "The model separates logical structure from physical storage — queries are written against the logical schema, independent of how data is laid out." _(certainty: high)_
- "Keys are the identity mechanism — primary keys define what a tuple is, foreign keys define what references it." _(certainty: high)_
- "The model's vocabulary — entities and relationships — coincides with knowledge-graph vocabulary because both model structured reality; the coincidence is the model's power, not an accident." _(certainty: high)_
- "Set semantics give the model its mathematical base — relation operations (selection, projection, join) are closed and composable." _(certainty: high)_

### Relationships

- **governs** → `schema-design`
- **enables** → `data-integrity`
- **rationalized_by** → `normalization`
- **manipulated_by** → `transactions`
- **operated_upon_by** → `query-planning`
- **preserves** → `query-optimization`

### Constraints

- "Every tuple must satisfy the model's integrity rules — a relation that violates its constraints is not valid data."
- "Keys must be stable and unique — identity that changes or duplicates is identity failure."

### Recommendations

- "Model identity explicitly — keys are the load-bearing design decision."
- "Validate the model against reality before building on it."
- "Maintain the logical/physical separation as an invariant."

## Replication (`replication`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/replication.md`

### Claims

- "Replication is the maintenance of multiple copies of data across nodes — a redundancy pattern with consistency obligations." _(certainty: high)_
- "Replica semantics are defined by the consistency model — the model states what divergence is permitted between copies." _(certainty: high)_
- "Replication trades availability and latency against consistency — the tradeoff shape is chosen, not discovered." _(certainty: high)_
- "Replication lag is an observable condition — stale reads are the cost of asynchronous propagation and must be part of the contract." _(certainty: high)_
- "Replication failure modes are divergence and split-brain — copies disagree, or the system splits into isolated writers." _(certainty: high)_

### Relationships

- **constrained_by** → `strong-consistency`
- **allows** → `eventual-consistency`
- **subject_to** → `split-brain`
- **supports** → `transactions`
- **complicates** → `atomicity`

### Constraints

- "Replica semantics are bound by the consistency model — divergence beyond the model's terms is a failure."
- "Every replica is a maintained copy — replication without monitoring is divergence in progress."

### Recommendations

- "Document the consistency model as the replication contract."
- "Monitor lag against consumer expectations."
- "Enforce quorum to prevent split-brain."

## Residual Risk (`residual-risk`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/residual-risk.md`

### Claims

- "Residual risk is the risk that remains after risk treatment — mitigation reduces risk but rarely eliminates it." _(certainty: high)_
- "Residual risk is the only risk that materially exists — inherent risk is a theoretical pre-mitigation quantity that no organisation actually operates under." _(certainty: high)_
- "Residual risk is frequently unmeasured — organisations track mitigated risks and accepted risks but rarely the difference between them." _(certainty: high)_
- "Residual risk is the true input to risk acceptance — acceptance decisions address residual risk, not inherent risk." _(certainty: high)_
- "Residual risk is time-variant — controls degrade, threats evolve, and the residual risk profile changes between assessments." _(certainty: high)_

### Relationships

- **addresses** → `risk-acceptance`
- **reduces** → `compensating-controls`
- **reduces** → `defense-in-depth`
- **quantified_by** → `likelihood`
- **required** → `confidence`

### Constraints

- "Residual risk cannot be zero for any system of interest to an adversary — some exposure always remains."
- "Residual risk is bounded below by assessment error — the true residual cannot be known more precisely than the assessment allows."

### Recommendations

- "Require a residual risk estimate with confidence for every mitigated finding."
- "Link residual risk updates to control health and threat intelligence — residual changes when controls or threats change."
- "Distinguish inherent and residual in all risk reporting — conflation misleads governance."

## Resource Arbitration (`resource-arbitration`)

| Field | Value |
|---|---|
| kind | decision |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/resource-arbitration.md`

### Claims

- "Resource arbitration is the allocation decision under contention — bus, memory, and compute shared under physical constraints." _(certainty: high)_
- "Arbitration is the fourth appearance of the structure — consensus (006), locking (010), scheduling (011), arbitration (012): contenders + selection rule + allocation + guarantee." _(certainty: high)_
- "Arbitration is graph topology, not a construct — the allocation discipline is a decision structure, exactly as resolved in 011." _(certainty: high)_
- "Arbitration validity is conditional — the allocation is valid under its stated contention and priority conditions." _(certainty: high)_
- "The arbitration candidate is re-tested at n=4 but not promoted — the five acceptance criteria must survive further cycles." _(certainty: high)_

### Relationships

- **serves** → `cyber-physical-system`
- **analogous_to** → `raft-consensus`
- **analogous_to** → `scheduling-policy`
- **analogous_to** → `isolation-levels`
- **constrained_by** → `deadline`

### Constraints

- "The allocation is valid under its stated conditions — contention and priority conditions bound the decision."
- "Arbitration is topology, not construct — the discipline must remain an optional composition of existing primitives."

### Recommendations

- "Represent arbitration as a decision object — contenders, selection rule, allocation, and guarantee as structure."
- "State the contention conditions with the allocation rule."
- "Monitor starvation, not only throughput."

## Retraining Decisions (`retraining-decisions`)

| Field | Value |
|---|---|
| kind | decision |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/retraining-decisions.md`

### Claims

- "Retraining is an intervention on a live system — it carries regression risk and must be decided, not scheduled by default." _(certainty: high)_
- "Retraining should be triggered by evidence (verified shift, degraded performance, new data) rather than by calendar or habit." _(certainty: high)_
- "Retraining is a feedback operation — the system updates its own behaviour from new observations." _(certainty: high)_
- "Retraining outcomes must be validated before deployment — the retrained model is a hypothesis until evaluated on fresh data." _(certainty: high)_
- "Retraining frequency trades freshness against stability — too frequent amplifies noise; too rare compounds staleness." _(certainty: high)_

### Relationships

- **triggered_by** → `distribution-shift`
- **informed_by** → `model-monitoring`
- **triggered_by** → `drift-detection`
- **acts_on** → `training-data`
- **modifies** → `deployment-risk`
- **revalidates** → `generalization`

### Constraints

- "A retrained model is unvalidated until evaluated on fresh data — release without validation is an untested claim."
- "Retraining on unverified shift risks learning new failure modes."

### Recommendations

- "Gate retraining on verified triggers and document the evidence for each update."
- "Validate every retrained model against a fresh holdout before deployment."
- "Treat each retraining as an experiment with measured outcomes and rollback capability."

## Retry Storm Amplification (`retry-storm-amplification`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/retry-storm-amplification.md`

### Claims

- "A retry storm occurs when many clients retry failed operations simultaneously, amplifying load beyond what the recovering system can handle." _(certainty: high)_
- "Retry storms transform transient failures into sustained overload — the initial trigger resolves but the retry-induced load keeps the system saturated." _(certainty: high)_
- "Without jitter, clients using exponential backoff synchronise naturally — identical backoff schedules produce coordinated retry waves." _(certainty: high)_
- "Fixed-interval retries without backoff guarantee overload on recovery — all clients retry simultaneously at the same interval." _(certainty: high)_
- "A retry storm can sustain itself: overload causes failures, failures trigger retries, retries maintain overload." _(certainty: high)_

### Relationships

- **triggers** → `cascading-failure`
- **similar_to** → `network-failure-propagation`
- **prevents** → `circuit-breaker`
- **reduces** → `backpressure`
- **vulnerable_to** → `leader-election`

### Constraints

- "Retry amplification is bounded by the ratio of retry interval to recovery time — faster retries produce more amplification."
- "Without coordination, N clients with identical retry policy produce N-fold load amplification on every retry wave."

### Recommendations

- "Set a maximum retry limit of 3 attempts with exponential backoff (base 1s, max 30s) as the organisation-wide default."
- "Instrument every retry with a unique identifier that survives across retry attempts for observability."
- "Never use fixed-interval retries in distributed systems — they guarantee thundering herd on recovery."

## Risk Acceptance (`risk-acceptance`)

| Field | Value |
|---|---|
| kind | decision |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/risk-acceptance.md`

### Claims

- "Risk acceptance is the formal decision to tolerate a known risk rather than mitigate or avoid it — it is an explicit governance act, not an implicit condition." _(certainty: high)_
- "Risk acceptance has no objectively correct answer — the right decision depends on business context, evidence quality, priorities, and constraints." _(certainty: high)_
- "Risk acceptance requires both likelihood and impact assessment — accepting a risk without estimating its dimensions is not a decision, it is an omission." _(certainty: high)_
- "Risk acceptance must be time-bound and revisitable — the conditions that justified acceptance (threat landscape, evidence, business context) change." _(certainty: high)_
- "Formal risk acceptance reduces organisational surprise — an accepted risk that materialises is an expected outcome, not an undiscovered failure." _(certainty: high)_

### Relationships

- **requires** → `likelihood`
- **requires** → `confidence`
- **addresses** → `residual-risk`
- **complicates** → `incomplete-evidence`
- **may_support** → `compensating-controls`
- **triggers** → `vulnerability-management`

### Constraints

- "Acceptance without likelihood, impact, and confidence assessment is not a decision — it is an omission that transfers risk to whoever discovers it later."
- "Acceptance validity is bounded by the stability of its conditions — conditions change, and acceptance must be re-evaluated."

### Recommendations

- "Formalise risk acceptance as a governance act with named owner, time window, and documented assessment."
- "Re-review every acceptance when threat intelligence indicates a material change in likelihood."
- "Pair acceptance with compensating controls whenever partial mitigation is possible."

## Rivet Credential and Data Stealer (`rivet-stealer`)

| Field | Value |
|---|---|
| kind | concept |
| domain | threat-analysis |
| research_cycle | "015" |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/rivet-stealer.md`

### Claims

- "Rivet is a credential and data stealer observed on Victim C only, harvesting browser credentials, clipboard contents, and documents matching file-name patterns." _(certainty: high)_
- "Rivet's code contains a code-signing comment string byte-identical to a string in tooling used two years earlier by the unrelated financially motivated cluster K7." _(certainty: high)_
- "Whether the string indicates shared tool lineage, shared authors, or stolen or borrowed code is unknown." _(certainty: medium)_
- "Rivet's collected data was not recovered because Victim C's exfiltration channel was interrupted." _(certainty: high)_

### Relationships

- **observed_on** → `victim-set`
- **linked_to** → `k7-overlap`
- **part_of** → `collection-pattern`

### Constraints

- "The Rivet object records the string match; the lineage interpretation is carried as an open question, not a fact."

## Rolling Deployment (`rolling-deployment`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/rolling-deployment.md`

### Claims

- "Rolling deployment updates nodes incrementally rather than simultaneously, maintaining system availability throughout the deployment." _(certainty: high)_
- "The batch size in a rolling deployment determines the trade-off between deployment speed and risk — larger batches deploy faster but increase blast radius." _(certainty: high)_
- "Rolling deployments require the system to support mixed versions during the deployment window — old and new versions must be interoperable." _(certainty: high)_
- "Automated rollback is a critical component of rolling deployment — if the new version fails, the deployment system must revert the updated nodes." _(certainty: high)_
- "Rolling deployment cannot protect against data format or schema changes that are incompatible between versions." _(certainty: high)_

### Relationships

- **preserves** → `availability`
- **interacts_with** → `circuit-breaker`
- **interacts_with** → `backpressure`
- **risk_during** → `cascading-failure`

### Constraints

- "Rolling deployment cannot update all nodes faster than the system's capacity to absorb node removals — removing too many nodes simultaneously reduces capacity below demand."
- "Version interoperability must be maintained for the duration of the deployment window — incompatible changes require different deployment strategies."

### Recommendations

- "Automate rollback testing in the deployment pipeline — every deployment candidate should have a verified rollback path."
- "Monitor cross-node interaction failures specifically during rolling deployments — per-node health checks are insufficient."
- "Always deploy with a canary batch first — update a single node or small percentage before committing to the full rollout."

## Safety Case (`safety-case`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/safety-case.md`

### Claims

- "A safety case is an artifact of evidence — claim + evidence + argument structure, exactly as a proof is an artifact of evidence." _(certainty: high)_
- "The safety case is the sixth verification-family member — claim + evidence + constraints, joining equivalence-checking, formal-verification, benchmark-validity, schedulability-analysis, and stability." _(certainty: high)_
- "The argument is a relationship structure — evidence links to claims through stated conditions, not a new evidence type." _(certainty: high)_
- "A safety case is valid only under its stated conditions — environment, configuration, and assumptions bound the claim." _(certainty: high)_
- "Certification standards are constraint sets over evidence — the case demonstrates the claim, it does not construct it." _(certainty: high)_

### Relationships

- **serves** → `cyber-physical-system`
- **supports** → `closed-loop-guarantee`
- **analogous_to** → `formal-verification`
- **analogous_to** → `stability`
- **constrains** → `autonomy-decision`

### Constraints

- "A safety case demonstrates a claim under stated conditions — it verifies, it does not construct."
- "An argument without evidence is an assertion, not a case."

### Recommendations

- "Represent the safety case as claim + evidence + constraints — the argument is a relationship structure."
- "Regenerate the case when the system changes."
- "Treat certification standards as constraint sets over evidence, not as authority."

## Saga Pattern (`saga-pattern`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/saga-pattern.md`

### Claims

- "A saga is a sequence of local transactions where each step has a compensating transaction that can undo its effects." _(certainty: high)_
- "Sagas avoid distributed transactions (two-phase commit) by breaking multi-step operations into independently committable steps." _(certainty: high)_
- "If a step in a saga fails, the compensating transactions for all completed steps are executed to maintain overall consistency." _(certainty: high)_
- "Sagas provide eventual consistency — during execution, intermediate states are visible to other components before the saga completes." _(certainty: high)_
- "There are two saga implementation models: choreography (each service publishes events that trigger the next step) and orchestration (a central coordinator manages the sequence)." _(certainty: high)_
- "Compensation logic must be idempotent — a compensating transaction may be executed multiple times in failure scenarios." _(certainty: high)_

### Relationships

- **requires** → `idempotency`
- **relies_on** → `eventual-consistency`
- **vulnerable_to** → `cascading-failure`
- **complementary_to** → `circuit-breaker`

### Constraints

- "A saga cannot provide atomicity — intermediate states are visible to other components during execution."
- "Compensation must be idempotent — a compensating transaction may be executed multiple times for the same saga step."

### Recommendations

- "Always design compensation logic before implementing forward logic — if you cannot compensate, you cannot safely execute the saga."
- "Monitor saga execution and compensation metrics separately — compensation rate is a leading indicator of system health."
- "Test saga compensation under realistic failure patterns — compensation that works in isolation may fail when multiple compensations execute concurrently."

## Schedulability Analysis (`schedulability-analysis`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/schedulability-analysis.md`

### Claims

- "Schedulability analysis is the discipline of establishing feasibility — whether a task set can meet its deadlines under a policy." _(certainty: high)_
- "Schedulability is a property claim — established through analysis under a task model, valid only under that model's conditions." _(certainty: high)_
- "The analysis is evidence for a guarantee, not the guarantee itself — runtime conditions can diverge from the model." _(certainty: high)_
- "Schedulability analysis is the generalized form of rate-monotonic analysis — a family of feasibility tests, not a new construct." _(certainty: high)_
- "The analysis is structurally analogous to formal verification — mechanical property establishment under a stated model — the Cycle 009 cross-domain link." _(certainty: high)_

### Relationships

- **generalizes** → `rate-monotonic-analysis`
- **consumes** → `worst-case-execution-time`
- **establishes** → `real-time-guarantee`
- **evaluated_against** → `deadline`
- **analogous_to** → `formal-verification`

### Constraints

- "A schedulability claim is valid only under its task model's conditions — periodicity, independence, and timing assumptions bound it."
- "The analysis inherits its inputs' confidence — a bad WCET propagates into a false feasibility claim."

### Recommendations

- "Treat feasibility as a claim bound by its model, not a fact."
- "Re-run analysis when the system changes."
- "Carry WCET confidence through the analysis."

## Scheduling Policy (`scheduling-policy`)

| Field | Value |
|---|---|
| kind | decision |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/scheduling-policy.md`

### Claims

- "A scheduling policy is the decision of how execution time is allocated among tasks — the choice of the allocation rule." _(certainty: high)_
- "Policy selection is a decision, not a discovery — the same task set can be scheduled under different policies with different guarantee outcomes." _(certainty: high)_
- "A policy's validity is bound by stated conditions — workload, priorities, and preemption assumptions qualify the guarantee it provides." _(certainty: high)_
- "A scheduling policy is structurally identical to every other decision object — it varies with deadline_priority, utilization_target, task_criticality, and preemption_allowance." _(certainty: high)_
- "Policy is the allocation rule; scheduling is the discipline; the two are not separate knowledge kinds." _(certainty: high)_

### Relationships

- **guides** → `task-scheduling`
- **serves** → `deadline`
- **realized_by** → `fixed-priority-scheduling`
- **alternative_to** → `earliest-deadline-first`
- **analogous_to** → `isolation-levels`

### Constraints

- "A policy's guarantee is valid only under its stated conditions — workload, priority, and preemption assumptions bound the claim."
- "A policy must remain feasible — a policy that cannot meet its task set's deadlines is invalid under those conditions."

### Recommendations

- "Treat policy selection as a decision with stated factors."
- "Verify feasibility after choosing the policy."
- "Document the policy's conditions with the decision."

## Schema Design (`schema-design`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/schema-design.md`

### Claims

- "A schema is a claim about the world — what exists, what properties it has, and what constraints hold over it." _(certainty: high)_
- "Schema design is a modelling act with correctness obligations — a schema that misrepresents its domain produces data that cannot represent real states." _(certainty: high)_
- "Schema decisions trade expressiveness against integrity — permissive schemas accept more data but weaken guarantees; strict schemas enforce more but reject more." _(certainty: high)_
- "A schema is never finished — domain understanding evolves, and the schema must evolve with it under migration discipline." _(certainty: high)_
- "The schema is the contract between data producers and consumers — every query and every write is interpreted against it." _(certainty: high)_

### Relationships

- **instantiates** → `relational-model`
- **shapes** → `data-integrity`
- **guided_by** → `normalization`
- **evolves** → `schema-migration`
- **bounded_by** → `query-optimization`
- **constrained_by** → `data-governance`

### Constraints

- "The schema must faithfully represent its domain — a schema that misrepresents reality invalidates every query's interpretation."
- "Integrity rules belong in the schema — validation scattered in application code is integrity without a contract."

### Recommendations

- "Treat the schema as a contract — version it, document it, and change it under migration discipline."
- "Move integrity into schema constraints wherever possible."
- "Review the schema against its domain periodically."

## Schema Migration (`schema-migration`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/schema-migration.md`

### Claims

- "Schema migration is a disciplined schema change — a versioned transition with validity conditions, not an edit." _(certainty: high)_
- "A schema version's validity is bound to stated conditions — the data, consumers, and operations that version supports." _(certainty: high)_
- "Migrations carry correctness obligations — data must be transformed faithfully, and the post-migration schema must satisfy the new contract." _(certainty: high)_
- "The schema is a contract — migration breaks contracts unless consumers move in step, making additive migration the default discipline." _(certainty: high)_
- "Migration validity is the artifact-validity pattern applied to data — a migrated schema is valid if derived from its predecessor under the migration's conditions." _(certainty: high)_

### Relationships

- **evolves** → `schema-design`
- **must_preserve** → `data-integrity`
- **executed_under** → `transactions`
- **analogous_to** → `build-systems`
- **affected_by** → `query-optimization`

### Constraints

- "A schema version's validity is bound to its stated conditions — use outside those conditions is unsupported."
- "Migration must preserve data — a migration that loses or corrupts data is a correctness failure."

### Recommendations

- "Treat migration as a versioned, rehearsed, verified operation."
- "Keep consumers moving with additive defaults and coordinated breaking changes."
- "Verify post-migration integrity and schema validity explicitly."

## Sensing (`sensing`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/sensing.md`

### Claims

- "A sensor is the source of observation — its output is the first evidence about the physical world, always qualified by noise and calibration." _(certainty: high)_
- "Sensing is observation at its epistemic limit — the sensor never reports reality, only a measurement of it under stated conditions." _(certainty: high)_
- "Sensor uncertainty is qualification of observation — noise and drift are confidence metadata, not a new evidence type." _(certainty: high)_
- "Sensing is the base of the Epistemic Chain — every claim about the physical world derives from observations that begin here." _(certainty: high)_
- "A measurement is valid only under stated conditions — calibration, environment, and the sensor model bound the observation." _(certainty: high)_

### Relationships

- **serves** → `cyber-physical-system`
- **informs** → `physical-state`
- **analogous_to** → `model-monitoring`
- **affected_by** → `deployment-risk`
- **constrained_by** → `deadline`

### Constraints

- "A measurement is valid only under its sensor model and calibration — unstated drift invalidates it."
- "Observation never touches reality directly — every claim about the world carries the epistemic gap from sensor to belief."

### Recommendations

- "Represent sensor output as qualified observation — the measurement is evidence with confidence, not a fact."
- "Track calibration drift as a failure mode, not an adjustment."
- "Bound every claim about the world with the sensing conditions it rests on."

## Sensor Fusion (`sensor-fusion`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/sensor-fusion.md`

### Claims

- "Sensor fusion is combining observations from multiple sources into a single belief — the agreement structure of redundant observation." _(certainty: high)_
- "Independent observation chains constrain each other — agreement is evidence, disagreement is a calibration or model signal." _(certainty: high)_
- "Fusion reduces uncertainty at a given epistemic distance by combining independent evidence chains — the number of inferential layers is unchanged; the qualification carried through them tightens." _(certainty: high)_
- "Fusion is a composition pattern over observations — no fusion primitive." _(certainty: high)_
- "A fused belief is valid only when the source models' stated conditions hold — a faulty source model corrupts the fusion." _(certainty: high)_

### Relationships

- **serves** → `cyber-physical-system`
- **produces** → `belief-state`
- **evaluates** → `sensing`
- **analogous_to** → `quorum`
- **analogous_to** → `model-monitoring`

### Constraints

- "A fused belief is valid only when its source models hold — correlated errors defeat fusion, whatever the agreement."
- "Independence is the precondition of agreement — correlated sources are one source."

### Recommendations

- "Model fusion as composition over observations — sources constrain each other through relationships."
- "Track source independence as an operating condition."
- "Verify fused belief against reality on a schedule."

## Spearphishing Initial Access Pattern (`spearphishing-initial-access`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | threat-analysis |
| research_cycle | "015" |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/spearphishing-initial-access.md`

### Claims

- "All four intrusions began with spearphishing, in two lure styles: a PDF request-for-quote exploiting a now-patched reader vulnerability (Victims A and B) and a macro-enabled Word security questionnaire (Victims C and D)." _(certainty: high)_
- "Lures were individually tailored per company — different templates, different prime-contractor personas, different sender infrastructure — with the sender domain spoofed via lookalike registrations." _(certainty: high)_
- "The lures share one underlying behavior: they download the same first-stage dropper family across all four victims." _(certainty: high)_
- "Lure content references real procurement documents whose sourcing is unexplained." _(certainty: high)_

### Relationships

- **linked_to** → `victim-set`
- **linked_to** → `dropper`
- **linked_to** → `procurement-aware-targeting`
- **linked_to** → `per-victim-operational-separation`

### Constraints

- "The pattern describes access mechanics; loader internals belong to the dropper object."

### Recommendations

- "Track the two lure styles and their per-company variants as distinct observables."
- "Attribute the unexplained lure sourcing to a separate potential access only as a hypothesis."

## Split Brain (`split-brain`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/split-brain.md`

### Claims

- "Split brain occurs when a distributed system continues operating in two or more disconnected partitions, with each partition independently modifying state." _(certainty: high)_
- "Split brain is prevented by requiring quorum for writes — the minority partition cannot make progress because it cannot form quorum." _(certainty: high)_
- "Systems without quorum-based write coordination (asynchronous replication, multi-master) are vulnerable to split brain during network partitions." _(certainty: high)_
- "Split brain produces divergent state that requires reconciliation or manual resolution when partitions rejoin." _(certainty: high)_
- "The duration of a split brain condition correlates with the volume of divergent state — longer partitions produce more divergence." _(certainty: high)_

### Relationships

- **prevents** → `quorum`
- **vulnerable_to** → `leader-election`
- **causes** → `network-partition-recovery`
- **avoids** → `raft-consensus`
- **worsens** → `cascading-failure`

### Constraints

- "In a system with N nodes, any partition with fewer than (N/2 + 1) nodes cannot make progress under quorum-based consistency."
- "Split brain reconciliation requires a total order of operations across partitions — without it, conflict resolution is ambiguous."

### Recommendations

- "Never deploy a distributed system without testing split brain behaviour under controlled partition conditions."
- "Implement cross-datacenter quorum awareness to prevent split brain across geo-distributed deployments."
- "Audit split brain detection and reconciliation procedures during each major deployment cycle."

## Stability (`stability`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/stability.md`

### Claims

- "Stability is the closed-loop correctness property — bounded response to bounded disturbance over time." _(certainty: high)_
- "Stability is demonstrated, not claimed — analysis (Lyapunov conditions), simulation, and test provide the evidence." _(certainty: high)_
- "A stability condition is a constraint — boundedness and convergence are invariants governing state evolution." _(certainty: high)_
- "Stability claims are valid under stated conditions — the plant model and operating envelope bound the claim, exactly as all verification claims." _(certainty: high)_
- "Stability joins the verification family — claim + evidence + constraints, where verification does not become ontology." _(certainty: high)_

### Relationships

- **constrains** → `feedback-control`
- **supports** → `closed-loop-guarantee`
- **analogous_to** → `formal-verification`
- **analogous_to** → `schedulability-analysis`
- **governs** → `physical-state`

### Constraints

- "Stability is a claim under stated conditions — the plant model and operating envelope bound it."
- "A stability demonstration is an artifact of evidence — it verifies, it does not construct."

### Recommendations

- "Represent stability as claim + constraints + evidence — never as a stability construct."
- "Bound every stability claim with its operating envelope."
- "Re-verify stability when the plant model changes."

## State Estimation (`state-estimation`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/state-estimation.md`

### Claims

- "State estimation is inference of a system's state from observations through a model — a claim built from qualified observations under stated conditions." _(certainty: high)_
- "An estimator is a relationship structure — observations flow into belief through a model — not a new knowledge type." _(certainty: high)_
- "The estimate is an observation of the model, qualified by its confidence — the epistemic chain at work: reality → sensor → model → belief." _(certainty: high)_
- "An estimate is a hypothesis about state, exactly as a plan is a hypothesis about cost — runtime evidence can falsify it." _(certainty: high)_
- "An estimate is valid only under its model's stated conditions — model mismatch invalidates the belief, exactly as schema mismatch invalidates data." _(certainty: high)_

### Relationships

- **produces** → `belief-state`
- **evaluated_through** → `sensing`
- **analogous_to** → `query-planning`
- **describes** → `physical-state`
- **constrained_by** → `deadline`

### Constraints

- "An estimate is valid only under its model's stated conditions — divergence invalidates the belief."
- "The estimate is never the state — belief and reality remain separated by the model, and the separation is carried by qualification."

### Recommendations

- "Represent estimation as claim + qualified observations + constraints, not as an estimator construct."
- "Treat the estimate as a hypothesis that runtime evidence can falsify."
- "Widen uncertainty before acting on distant belief."

## Strong Consistency (`strong-consistency`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/strong-consistency.md`

### Claims

- "Strong consistency guarantees that every read returns the most recent write — all nodes agree on the order of operations." _(certainty: high)_
- "Linearisable consistency is the strongest form of strong consistency — operations appear to execute atomically at a single point between invocation and response." _(certainty: high)_
- "Strong consistency requires coordination between nodes — typically through quorum-based writes or consensus protocols." _(certainty: high)_
- "Strong consistency increases read and write latency because operations must wait for coordination to complete." _(certainty: high)_
- "Strong consistency reduces availability during partitions because the minority partition cannot serve writes." _(certainty: high)_
- "Strong consistency is not a single property — linearisability, sequential consistency, and causal consistency are distinct models with different guarantees." _(certainty: high)_

### Relationships

- **constrained_by** → `cap-theorem`
- **contrasts_with** → `eventual-consistency`
- **requires** → `quorum`
- **provides** → `raft-consensus`
- **trades_off_against** → `availability`

### Constraints

- "Strongly consistent reads require quorum intersection (R + W > N) or leader-based reads — otherwise consistency is not guaranteed."
- "Strong consistency cannot be maintained during a network partition — the system must either stall (unavailable) or relax consistency."

### Recommendations

- "Default to strong consistency for system-of-record data; relax only when performance requirements cannot otherwise be met."
- "Instrument consistency verification at the application layer — do not rely solely on the data store's consistency claims."
- "Document the chosen consistency model and its limitations explicitly — future maintainers need to know what guarantees they can rely on."

## Surface Ambiguity of Artifacts (`surface-ambiguity`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/surface-ambiguity.md`

### Claims

- "The observable surface of an artifact is ambiguous — the same surface is compatible with multiple candidate purposes, and the surface alone does not decide between them." _(certainty: high)_
- "Ambiguity at the surface is often designed — concealment produces surfaces engineered to support plausible innocent readings." _(certainty: high)_
- "Ambiguity is not resolved by more observation alone — additional surface evidence narrows, but the gap between surface and semantics is structural." _(certainty: high)_
- "Ambiguity is a property of the surface as perceived — the artifact is a single object; the plurality of readings lives in the evidence, not in the artifact." _(certainty: high)_
- "Premature commitment is the characteristic response to ambiguity — analysis that fixes one reading early trades correctness for closure." _(certainty: high)_

### Relationships

- **characterises** → `artifact`
- **constrained_by** → `observable-evidence`
- **amplified_by** → `incomplete-evidence`
- **reduces** → `confidence`
- **blinds** → `threat-detection`

### Constraints

- "The observable surface does not determine semantics — identical surfaces can serve different purposes, and this gap is structural."
- "A claim grounded in the surface alone is a qualified observation, never a conclusion — surface-derived certainty is false certainty."

### Recommendations

- "Treat the surface/semantics gap as structural — the gap is not closed by looking harder at the surface."
- "Record candidate readings explicitly with the evidence that supports each."
- "Require behavioural confirmation before a reading becomes a claim."

## Task Scheduling (`task-scheduling`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/task-scheduling.md`

### Claims

- "Task scheduling is the discipline of allocating execution time to tasks so that timing requirements are satisfied." _(certainty: high)_
- "A schedule is an allocation of time to tasks — a plan whose outcome is bound by deadlines." _(certainty: high)_
- "Scheduling resolves as relationships plus constraints — task-to-time allocation expressed as graph edges with timing bounds — not a distinct construct." _(certainty: high)_
- "Scheduling feasibility is a claim about the schedule under stated conditions — load and timing assumptions qualify it." _(certainty: high)_
- "Scheduling is the discipline; the policy is the decision — policy selection is the Tier 2 decision object, not a new knowledge kind." _(certainty: high)_

### Relationships

- **serves** → `deadline`
- **operates_within** → `real-time-system`
- **consumes** → `worst-case-execution-time`
- **analogous_to** → `quorum`
- **analogous_to** → `backpressure`

### Constraints

- "A schedule is valid only if all tasks meet their deadlines under the policy and its stated conditions."
- "Scheduling guarantees are bound by load and timing assumptions — unstated conditions void the allocation's validity."

### Recommendations

- "Model scheduling as relationships plus constraints, not a scheduling construct."
- "Keep the schedule's conditions explicit and audited."
- "Choose the policy deliberately; re-verify when load changes."

## TCP and TLS Connection Foundation (`tcp-tls-foundation`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/tcp-tls-foundation.md`

### Claims

- "TCP provides reliable, ordered, error-checked delivery of a byte stream — every browser automation connection depends on it." _(certainty: high)_
- "Ephemeral port exhaustion occurs when rapid connections cycling exceeds the available port range (~28K-64K on Linux)." _(certainty: high)_
- "TIME_WAIT accumulation blocks port reuse for 60 seconds (2*MSL) after client-initiated close, contributing to port exhaustion." _(certainty: high)_
- "The TLS ClientHello produces an observable fingerprint (JA3) that differs between browser TLS stacks and automation TLS libraries." _(certainty: high)_
- "Nagle's algorithm adds latency to small messages by buffering them — CDP commands are small JSON messages and are affected." _(certainty: high)_
- "TLS 1.3 reduces handshake latency to 1-RTT (or 0-RTT with session resumption) compared to TLS 1.2's 2-RTT." _(certainty: high)_

### Relationships

- **underlies** → `http-protocol`
- **interacts_with** → `proxy-infrastructure`
- **source_of** → `network-failure-propagation`
- **transports** → `automation-protocol`
- **contributes_to** → `automation-detection-surface`

### Constraints

- "TCP connection established during SYN-SYN-ACK handshake — no data flows before completion."
- "TLS handshake must complete before application data flows over HTTPS."

### Recommendations

- "Set TCP_NODELAY on CDP client sockets to minimise command latency."
- "Use connection pooling and SO_REUSEADDR to manage TCP connection resources at scale."
- "Profile and match browser TLS fingerprint when operating in detection-sensitive environments."

## Temporal Isolation (`temporal-isolation`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/temporal-isolation.md`

### Claims

- "Temporal isolation is the discipline of keeping one task's timing behaviour from breaking another's guarantee." _(certainty: high)_
- "Temporal isolation is an invariant — each task's guarantee holds independently of others' behaviour." _(certainty: high)_
- "Isolation is enforced by budget and partition constraints, not by a new construct — execution budgets bound each task's impact." _(certainty: high)_
- "Temporal isolation is the real-time form of isolation — the same guarantee-separation structure as consistency isolation in databases." _(certainty: high)_
- "Temporal isolation is a pattern — a reusable enforcement discipline, not a knowledge kind." _(certainty: high)_

### Relationships

- **protects** → `real-time-guarantee`
- **structures** → `task-scheduling`
- **supported_by** → `scheduling-policy`
- **analogous_to** → `isolation-levels`
- **analogous_to** → `strong-consistency`

### Constraints

- "Each task's guarantee must hold independently — temporal isolation is an invariant."
- "Execution budgets bound each task's impact — an unbudgeted task can break isolation."

### Recommendations

- "Model temporal isolation as a pattern with budget constraints."
- "Enforce budgets at the partition boundary."
- "Test isolation under worst-case interference."

## Threat Actor (`threat-actor`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/threat-actor.md`

### Claims

- "A threat actor is an entity that poses a security threat — ranging from individual criminals and insiders to organised groups and state-sponsored units." _(certainty: high)_
- "Threat actors are classified by motivation (financial, espionage, ideology, disruption), capability, and access — these determine their threat profile." _(certainty: high)_
- "Actor attribution is probabilistic, not certain — most attributions carry confidence levels and are frequently contested." _(certainty: high)_
- "Actor behaviour evolves — groups disband, rebrand, share tooling, and change targets, making actor identity less stable than tooling signatures." _(certainty: high)_
- "Insider threats form a distinct actor category — their access advantage compensates for typically lower technical capability." _(certainty: high)_

### Relationships

- **has** → `attacker-capability`
- **executes** → `kill-chain`
- **targets** → `attack-surface`
- **determines** → `likelihood`
- **informs** → `risk-acceptance`

### Constraints

- "Attribution is always probabilistic — no actor identity is ever established with certainty."
- "Actor capability cannot exceed what tooling and knowledge currently enable — actor models are bounded by the capability floor."

### Recommendations

- "Never base critical defence decisions on attribution alone — pair attribution with behaviour-based detection."
- "Maintain an explicit insider-threat actor model with privileged access monitoring."
- "Document confidence levels on every actor attribution and revisit them when counter-evidence appears."

## Threat Detection (`threat-detection`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/threat-detection.md`

### Claims

- "Threat detection is the practice of observing system and user behaviour to identify malicious activity — it is a continuous capability, not a tool." _(certainty: high)_
- "Detection value is bounded by telemetry — no detection can see what is not observed; coverage gaps are detection gaps." _(certainty: high)_
- "Detection precision and recall trade off — precision optimising reduces alert noise but misses attacks; recall optimising catches attacks but floods analysts." _(certainty: high)_
- "Detection quality is measured by outcome — detection without response is noise; the metric is prevented or contained damage, not alert count." _(certainty: high)_
- "Detection effectiveness decays — new attack techniques, tooling changes, and environment drift age detection rules." _(certainty: high)_

### Relationships

- **designed_against** → `kill-chain`
- **limited_by** → `incomplete-evidence`
- **carries** → `confidence`
- **triggers** → `incident-response`
- **tracked_against** → `attacker-capability`
- **behaviour_based** → `threat-actor`

### Constraints

- "Detection cannot observe what telemetry does not capture — coverage is the ceiling of detection capability."
- "Detection without response capacity is noise — the pipeline is only as strong as the slowest stage."

### Recommendations

- "Instrument telemetry proportional to the attack surface — every high-risk surface should have corresponding visibility."
- "Refresh detection coverage against current TTPs on a continuous basis — detect behaviour, not just signatures."
- "Review alert precision quarterly and retire noisy detections — alert fatigue is a detection failure mode."

## Training Data (`training-data`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/training-data.md`

### Claims

- "Training data bounds model capability — a model cannot exceed the information content of its training data, regardless of architecture." _(certainty: high)_
- "Training data distribution defines the model's validity domain — the model is only as reliable as the match between training distribution and deployment distribution." _(certainty: high)_
- "Data quality dominates architecture in determining model performance — clean representative data improves models more than model changes." _(certainty: high)_
- "Data lineage matters — without provenance, data errors, leakage, and biases cannot be traced, diagnosed, or corrected." _(certainty: high)_
- "Training data is a live system input — models retrained on evolving data inherit both its improvements and its degradations." _(certainty: high)_

### Relationships

- **defines_baseline** → `distribution-shift`
- **bounds** → `generalization`
- **facilitated_by** → `overfitting`
- **informs** → `uncertainty-estimation`
- **risks_contamination** → `benchmark-validity`
- **source_of** → `retraining-decisions`

### Constraints

- "A model cannot exceed the information content of its training data."
- "Evaluation data must never influence training — separation is an invariant, not a preference."

### Recommendations

- "Document data lineage for every training run — sources, transformations, and exclusions."
- "Enforce evaluation-data separation as a pipeline invariant, with contamination checks."
- "Measure and report the distribution match between training data and live deployment data."

## Transaction Failures (`transaction-failures`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/transaction-failures.md`

### Claims

- "Transaction failures are a normal class of concurrency outcomes — deadlock, abort, and lost updates are expected failure modes, not exceptional bugs." _(certainty: high)_
- "Deadlock is a cycle in resource waiting — detection and victim selection are the standard resolution." _(certainty: high)_
- "Lost updates are silent failures — the system reports success while discarding work — making them the most dangerous transaction failure class." _(certainty: high)_
- "Retry is the recovery mechanism for retryable failures — retrying non-retryable failures (lost updates, constraint violations) amplifies the problem." _(certainty: high)_
- "Failure classification precedes recovery — a transaction must know whether its failure is retryable before choosing a response." _(certainty: high)_

### Relationships

- **afflict** → `transactions`
- **contained_by** → `atomicity`
- **caused_by** → `isolation-levels`
- **preserved_by** → `data-integrity`
- **mitigated_by** → `retry-pattern`

### Constraints

- "Recovery must be preceded by failure classification — retrying without classification amplifies damage."
- "Retryable failures are bounded — unbounded retry is an amplifier, not a recovery."

### Recommendations

- "Explicitly classify transaction failures as retryable or terminal."
- "Retry deadlocks and aborts with bounded backoff and idempotence."
- "Detect lost updates with version checks or conditional writes."

## Transactions (`transactions`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/transactions.md`

### Claims

- "A transaction is a unit of work — a bounded set of operations that either applies fully or not at all." _(certainty: high)_
- "ACID is the transaction's contract — atomicity, consistency, isolation, and durability are the guarantees a transaction system provides." _(certainty: high)_
- "A transaction is a unit of work with constraints on its outcome, not on its duration — temporal extent is an implementation detail." _(certainty: high)_
- "Transactions manage concurrency — isolation levels trade consistency guarantees against throughput." _(certainty: high)_
- "The transaction boundary is a correctness decision — too coarse deadlocks and blocks; too fine breaks atomicity." _(certainty: high)_

### Relationships

- **guaranteed_by** → `atomicity`
- **scoped_by** → `isolation-levels`
- **subject_to** → `transaction-failures`
- **protects** → `data-integrity`
- **manipulates** → `relational-model`
- **executes_under** → `schema-migration`

### Constraints

- "A transaction applies fully or not at all — partial application is a correctness failure, not a performance concern."
- "The transaction's guarantees are scoped by its isolation level — behaviour valid at one level may be invalid at another."

### Recommendations

- "Design the transaction boundary deliberately — it is the unit of correctness."
- "Choose isolation levels by anomaly tolerance, documented per workload."
- "Detect deadlocks and retry transactionally — with backoff and idempotence."

## Type Safety (`type-safety`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/type-safety.md`

### Claims

- "Type safety is a language guarantee: well-typed programs cannot exhibit the runtime failure classes the safety theorem covers." _(certainty: high)_
- "Type safety decomposes into progress and preservation — a well-typed program either steps to a well-typed program or is a value, and no type error is reachable." _(certainty: high)_
- "Type safety is a property of the type system and the runtime together — the guarantee holds only where both halves are sound." _(certainty: high)_
- "The guarantee is scoped — unsafe constructs, dynamic escapes, and runtime boundaries are outside the safety claim." _(certainty: high)_
- "Type safety is enforced at compile time — the type checker rejects ill-typed programs before they can run." _(certainty: high)_

### Relationships

- **guaranteed_by** → `type-system`
- **defined_over** → `program-semantics`
- **must_preserve** → `compiler-correctness`
- **verifiable_by** → `formal-verification`
- **bounded_by** → `equivalence-checking`
- **enabled_by** → `dead-code-elimination`

### Constraints

- "The safety guarantee is scoped — unsafe constructs and runtime boundaries are outside it by definition."
- "Compile-time rejection must be decidable — the checker must decide well-typedness without executing the program."

### Recommendations

- "Define the safety theorem, its proof strategy, and its scope as a first-class artifact."
- "Keep escape hatches small, visible, and audited."
- "Test optimizations against the guarantee's boundary, not just its happy path."

## Type System (`type-system`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/type-system.md`

### Claims

- "A type system is a set of formal rules assigning types to program terms — the rules determine which programs are well-typed." _(certainty: high)_
- "Type checking is decidable static analysis — the checker decides well-typedness without executing the program." _(certainty: high)_
- "A sound type system guarantees that well-typed programs cannot exhibit the runtime failure classes its safety theorem covers." _(certainty: high)_
- "Type rules trade expressiveness against checking power — richer type systems detect more classes of errors but complicate the checker and the language." _(certainty: high)_
- "Type system soundness holds only within its stated scope — unsafe constructs, dynamic escapes, and untrusted annotations can pierce the guarantee." _(certainty: high)_

### Relationships

- **annotates** → `abstract-syntax-tree`
- **guarantees** → `type-safety`
- **constrains** → `program-semantics`
- **must_preserve** → `compiler-correctness`
- **verified_by** → `formal-verification`
- **relied_upon_by** → `equivalence-checking`

### Constraints

- "Type rules are invariants — every rule must hold for every program, or the system's guarantee is void."
- "Type safety holds only within the typed core — unsafe constructs and runtime escapes are outside the guarantee."

### Recommendations

- "Define the type system's safety claim explicitly, including its scope and escape hatches."
- "Test the checker against the type rules, including negative tests for forbidden programs."
- "Track unsoundness reports as correctness failures, not feature requests."

## Unassigned Hosts (`unassigned-hosts`)

| Field | Value |
|---|---|
| kind | concept |
| domain | threat-analysis |
| research_cycle | "015" |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/unassigned-hosts.md`

### Claims

- "Two hosts (skunk-09 and skunk-10) share SSL certificate reuse with Cluster 1 but have an unknown active role." _(certainty: high)_
- "Analysts disagree on whether the unassigned hosts belong to the campaign at all." _(certainty: high)_

### Relationships

- **linked_to** → `cluster-1-c2-infrastructure`
- **part_of** → `midnight-foundry-campaign`
- **linked_to** → `open-analytical-questions`

### Constraints

- "The object records the observed reuse and the disputed membership; it does not assign the hosts."

## Uncertainty Estimation (`uncertainty-estimation`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/uncertainty-estimation.md`

### Claims

- "Uncertainty estimation quantifies what a model does not know — distinguishing aleatoric (irreducible data noise) from epistemic (reducible model ignorance) uncertainty." _(certainty: high)_
- "Uncertainty estimates are only useful when calibrated and validated against the true failure rate." _(certainty: high)_
- "Epistemic uncertainty is actionable — it identifies where more data, better features, or different architecture would help." _(certainty: high)_
- "Aleatoric uncertainty sets a floor on achievable predictive accuracy — no model can reduce irreducible noise." _(certainty: high)_
- "Uncertainty estimates decay in validity as the input distribution shifts from training." _(certainty: high)_

### Relationships

- **validated_by** → `confidence-calibration`
- **produces** → `probabilistic-outputs`
- **mitigates** → `hallucination`
- **quantifies** → `likelihood`
- **degrades_with** → `distribution-shift`
- **informs** → `retraining-decisions`

### Constraints

- "Uncertainty estimates are only meaningful to the extent they are calibrated to realized outcomes."
- "Epistemic uncertainty can be reduced by data; aleatoric cannot — the two must be distinguished for action."

### Recommendations

- "Distinguish aleatoric from epistemic uncertainty in any uncertainty reporting."
- "Gate automation on validated uncertainty estimates, not raw model confidence."
- "Re-estimate uncertainty after distribution shifts — old estimates are stale evidence."

## Aerospace Defense Supply-Chain Victim Set (`victim-set`)

| Field | Value |
|---|---|
| kind | concept |
| domain | threat-analysis |
| research_cycle | "015" |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/victim-set.md`

### Claims

- "The four victims are mid-sized aerospace or defense suppliers in three regions: aircraft subassemblies (North America), avionics (Europe), propulsion components (North America), and sensor systems (East Asia)." _(certainty: high)_
- "All four are secondary suppliers in larger defense supply chains, and each was compromised within two weeks of becoming part of a funded procurement program." _(certainty: high)_
- "Compromise timeframes ran January through October, with each victim's first access two weeks before its first observed C2 contact." _(certainty: high)_
- "No confirmed operational impact; the observed activity at each victim was consistent with persistent collection." _(certainty: high)_

### Relationships

- **part_of** → `midnight-foundry-campaign`
- **linked_to** → `procurement-aware-targeting`

### Constraints

- "Shared victimology claims are asserted at the set level only; nothing in this object attributes means of access or tooling to specific victims."

## Vulnerability Management (`vulnerability-management`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/vulnerability-management.md`

### Claims

- "Vulnerability management is the continuous process of discovering, prioritising, and remediating vulnerabilities — it is a cycle, not an event." _(certainty: high)_
- "Vulnerability management is bounded by asset discovery — unmanaged assets cannot be scanned, assessed, or remediated." _(certainty: high)_
- "Prioritisation by severity alone is insufficient — exploitability, exposure, and asset criticality determine actual risk." _(certainty: high)_
- "Time to remediation is the key metric — the vulnerability window (discovery to remediation) is the period of exploitability." _(certainty: high)_
- "Not all vulnerabilities can be remediated within acceptable time — un-remediable findings become candidates for compensation or acceptance." _(certainty: high)_

### Relationships

- **scoped_by** → `attack-surface`
- **prioritised_by** → `likelihood`
- **triggers** → `risk-acceptance`
- **exploit_leveraged** → `attacker-capability`
- **bridges** → `compensating-controls`
- **complements** → `threat-detection`

### Constraints

- "Vulnerability management cannot assess what it cannot discover — asset discovery is a prerequisite, not an optimisation."
- "The vulnerability window is bounded below by remediation velocity — patch testing and deployment take time."

### Recommendations

- "Run continuous asset discovery and treat inventory drift as a critical finding."
- "Weight prioritisation by exploitability, exposure, and asset criticality — not severity alone."
- "Track time-to-remediation as the programme's core metric and report it to governance."

## Watchdog Timer (`watchdog-timer`)

| Field | Value |
|---|---|
| kind | pattern |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/watchdog-timer.md`

### Claims

- "A watchdog timer is a failure-detection pattern — a timing sentinel that detects when a system stops making progress." _(certainty: high)_
- "The watchdog detects stalls by deadline, not by inspection — a bounded expectation of progress is the detection mechanism." _(certainty: high)_
- "A watchdog is a pattern with timeout constraints and reset discipline — the detection bound is a constraint, not a construct." _(certainty: high)_
- "Watchdog detection is the temporal form of health checking — a bounded liveness expectation, analogous to health-check-pattern." _(certainty: high)_
- "The watchdog's value is bounded reaction time — detection without a bounded response is a false promise." _(certainty: high)_

### Relationships

- **guards** → `real-time-system`
- **enforces** → `hard-vs-soft-real-time`
- **analogous_to** → `incident-response`
- **analogous_to** → `health-check-pattern`
- **complements** → `retry-pattern`

### Constraints

- "The watchdog timeout is a validity condition on progress — a system that exceeds it is presumed stalled."
- "Reset must be independent of progress — a task must not reset its own watchdog."

### Recommendations

- "Model the watchdog as a pattern with timeout constraints."
- "Enforce reset independence."
- "Pair detection with a bounded response."

## Worst-Case Execution Time (`worst-case-execution-time`)

| Field | Value |
|---|---|
| kind | concept |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/worst-case-execution-time.md`

### Claims

- "WCET is an estimate of the longest execution time a task can exhibit — a claim about the future, not a measured fact." _(certainty: high)_
- "WCET is an observation with confidence, not a guarantee — underestimation is the characteristic failure." _(certainty: high)_
- "WCET validity is bound by stated conditions — architecture, inputs, and analysis assumptions qualify the bound." _(certainty: high)_
- "A WCET estimate is a hypothesis about execution that runtime evidence can falsify — the query-planning finding applied to timing." _(certainty: high)_
- "The bound's usefulness depends on its confidence — a safe over-approximation and a tight approximation differ in certainty, not kind." _(certainty: high)_

### Relationships

- **bounded_by** → `deadline`
- **feeds** → `schedulability-analysis`
- **analogous_to** → `benchmark-validity`
- **analogous_to** → `query-planning`
- **underpins** → `real-time-system`

### Constraints

- "WCET validity is bound by stated conditions — architecture, inputs, and analysis assumptions qualify the estimate."
- "A guarantee built on an unstated or drifted WCET assumption is invalid — the estimate's conditions must hold."

### Recommendations

- "State WCET conditions explicitly with the estimate."
- "Treat a passed feasibility check as evidence, not proof."
- "Re-validate WCET when the system changes."

## Zero Trust Architecture (`zero-trust`)

| Field | Value |
|---|---|
| kind | principle |
| domain | — |
| research_cycle | — |
| origin | hpf |
| authority | hpf_experiment |
| status | observed |

Source: `domain/knowledge/zero-trust.md`

### Claims

- "Zero trust is an architecture principle: no entity is trusted by virtue of network position — every access request is verified regardless of origin." _(certainty: high)_
- "Zero trust replaces perimeter trust with identity-based, per-request verification — the network no longer implies trust." _(certainty: high)_
- "Zero trust is a journey of architecture changes, not a product — it reorients identity, device, network, workload, and data security." _(certainty: high)_
- "Zero trust assumes breach — the architecture is designed for the reality that attackers are already inside." _(certainty: high)_
- "Zero trust reduces lateral movement — segmented access limits how far a compromised identity can travel." _(certainty: high)_

### Relationships

- **reduces** → `attack-surface`
- **extends** → `defense-in-depth`
- **depends_on** → `threat-detection`
- **supports** → `incident-response`
- **resists** → `threat-actor`
- **changes** → `risk-acceptance`

### Constraints

- "Zero trust cannot eliminate trust — it relocates and bounds it — identity, device, and policy trust remain."
- "Zero trust effectiveness is bounded by identity quality — weak identity undermines every verification."

### Recommendations

- "Implement zero trust incrementally, identity-first — transformation is architectural, not a product purchase."
- "Harden the identity provider as the highest-value target — phishing-resistant MFA, privileged access isolation, and monitoring."
- "Measure zero trust by architecture change and containment outcomes, not by vendor adoption labels."

---

Report covers 158 valid objects. Invalid objects export metadata and errors only and are excluded here by design.
