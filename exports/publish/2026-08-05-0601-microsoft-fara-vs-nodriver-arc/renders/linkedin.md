# LinkedIn draft — Microsoft Fara vs Nodriver: architecture, capabilities, and future of AI browser automation

## Post body

Research on: Microsoft Fara vs Nodriver: architecture, capabilities, and future of AI browser automation.
- All three models are available on Microsoft Foundry: Fara1.5-4B, Fara1.5-9B, and Fara1.5-27B.
- Microsoft Fara1.5 is a computer use agent (CUA) model for web browsers from Microsoft Research AI Frontiers — a family of native computer use agents at three scales (Fara1.5-4B/9B/27B) built on Qwen3.5 — not a browser automation framework.
- Fara1.5 is trained to pause and ask the user at critical points before continuing — agent-level consent behavior that driver-level tools do not implement.
- Community signal: browser-harness SDKs for AI agents are emerging (e.g., Browser Tools SDK open-sourced July 2026 — a TypeScript package giving AI agents a production-ready real-browser harness).
- Community signal: practitioners building browser automation at scale orchestrate around interchangeable drivers — one HN post (2026-03-02) names Playwright, Selenium, and Nodriver as backends under an orchestration layer built for proxy rotation, fingerprinting, and job queues.

Claims are draft research findings (confidence null), not established facts.

Source session: 2026-08-05-0601-microsoft-fara-vs-nodriver-arc