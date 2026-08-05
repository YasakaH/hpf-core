# Documentation update draft — Microsoft Fara vs Nodriver: architecture, capabilities, and future of AI browser automation

Reference-style material compiled from accepted findings. Nothing here is corpus knowledge until it passes validation.

### All three models are available on Microsoft Foundry: Fara1.5-4B, Fara1.5-9B, and Fara1.5-27B.

- Sources: https://github.com/microsoft/fara
- Evidence: ev-9, ev-11, ev-34
- Status: needs_adjudication · Confidence: None

### Microsoft Fara1.5 is a computer use agent (CUA) model for web browsers from Microsoft Research AI Frontiers — a family of native computer use agents at three scales (Fara1.5-4B/9B/27B) built on Qwen3.5 — not a browser automation framework.

- Sources: https://huggingface.co/microsoft/Fara1.5-9B/blob/main/README.md
- Evidence: ev-316, ev-283, ev-299
- Status: needs_adjudication · Confidence: None

### Fara1.5 is trained to pause and ask the user at critical points before continuing — agent-level consent behavior that driver-level tools do not implement.

- Sources: https://huggingface.co/microsoft/Fara1.5-9B/blob/main/README.md
- Evidence: ev-316, ev-283, ev-299
- Status: needs_adjudication · Confidence: None

### Community signal: browser-harness SDKs for AI agents are emerging (e.g., Browser Tools SDK open-sourced July 2026 — a TypeScript package giving AI agents a production-ready real-browser harness).

- Sources: https://news.ycombinator.com/item?id=48998262, https://news.ycombinator.com/item?id=49178393, https://news.ycombinator.com/item?id=48886547
- Dates: 2026-07-13, 2026-07-21, 2026-08-05
- Evidence: ev-320, ev-318, ev-321
- Status: community_signal · Confidence: None

### Community signal: practitioners building browser automation at scale orchestrate around interchangeable drivers — one HN post (2026-03-02) names Playwright, Selenium, and Nodriver as backends under an orchestration layer built for proxy rotation, fingerprinting, and job queues.

- Sources: https://news.ycombinator.com/item?id=47218198, https://news.ycombinator.com/item?id=47758203, https://news.ycombinator.com/item?id=45362134
- Dates: 2025-09-24, 2026-03-02, 2026-04-13
- Evidence: ev-329, ev-327, ev-330
- Status: community_signal · Confidence: None

### Fara and Nodriver occupy different abstraction layers of the browser automation stack: Fara is a vision-first AI computer-use layer (a model that observes screenshots and emits actions, executed through a browser harness), while Nodriver is a low-level CDP browser driver (successor of undetected-chromedriver, direct CDP protocol, anti-bot/WAF resistance focus). Fara complements rather than replaces drivers.

- Sources: https://github.com/microsoft/fara, https://github.com/ultrafunkamsterdam/nodriver, https://huggingface.co/microsoft/Fara1.5-9B/blob/main/README.md
- Evidence: (none)
- Status: needs_adjudication · Confidence: None

### Fara's execution model is vision-first: it sees the browser through screenshots, not the DOM or accessibility tree, and predicts pixel-grounded click and drag targets directly — no separate grounding model needed.

- Sources: https://huggingface.co/microsoft/Fara1.5-9B/blob/main/README.md
- Evidence: (none)
- Status: needs_adjudication · Confidence: None

### Fara1.5 is explicitly a research preview, not a production framework: Microsoft recommends sandboxed execution, monitoring, and avoiding sensitive data or high-risk domains; the model is intended to run only with the microsoft/fara harness or Magentic-Lite.

- Sources: https://github.com/microsoft/fara, https://huggingface.co/microsoft/Fara1.5-9B/blob/main/README.md
- Evidence: (none)
- Status: needs_adjudication · Confidence: None

### Technology maturity asymmetry: Nodriver is a community-maintained driver project (official successor of undetected-chromedriver, fully asynchronous, active iteration documented in README) while Fara is a vendor-backed model family (Microsoft Research AI Frontiers, released 2026-07-22, weights on Hugging Face, hosted on Microsoft Foundry, MIT license) at research-preview maturity.

- Sources: https://github.com/microsoft/fara, https://github.com/ultrafunkamsterdam/nodriver, https://huggingface.co/microsoft/Fara1.5-9B/blob/main/README.md
- Evidence: (none)
- Status: needs_adjudication · Confidence: None

### Fara emits structured tool calls (click, type, scroll, visit URL, web search, terminate) that a browser harness must execute: the model does not drive a browser by itself — the microsoft/fara CLI and Magentic-Lite execute actions in a sandboxed browser and feed screenshots back.

- Sources: https://huggingface.co/microsoft/Fara1.5-9B/blob/main/README.md
- Evidence: (none)
- Status: needs_adjudication · Confidence: None
