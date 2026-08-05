# Documentation update draft — Cloudflare OS and the Agent Access Model: implications for AI browser agents, browser automation, anti-detection, and secure agent infrastructure

Reference-style material compiled from accepted findings. Nothing here is corpus knowledge until it passes validation.

### Apps built in Cloudflare OS are instantiated from blueprints: the shared app's code is copied, but each new instance starts with independent SQLite data, conversation history, credentials, and connected resources, so teams can modify their own copies with AI instead of filing feature requests.

- Sources: https://blog.cloudflare.com/cloudflare-os/
- Evidence: ev-6, ev-16, ev-12
- Status: needs_adjudication · Confidence: None

### Cloudflare OS mediates agent and app access to systems of record through Gatekeepers, a security and governance framework that applies guardrails to agents and apps, and supports existing organizational MCP servers via MCP Server Portals.

- Sources: https://blog.cloudflare.com/cloudflare-os/
- Evidence: ev-6, ev-16, ev-12
- Status: needs_adjudication · Confidence: None

### Cloudflare OS is model-agnostic: it works with many major AI model providers and self-hosted models, and AI Gateway provides routing and spend control so expensive models are not used for routine tasks.

- Sources: https://github.com/cloudflare/cloudflare-os
- Evidence: ev-70, ev-64, ev-71
- Status: needs_adjudication · Confidence: None

### Cloudflare OS treats AI agents as principals distinct from users: agents are accountable to a human user while holding their own restricted permissions, and they do work by writing and executing code under those permissions.

- Sources: https://github.com/cloudflare/cloudflare-os
- Evidence: ev-70, ev-64, ev-71
- Status: needs_adjudication · Confidence: None

### Cloudflare reports that due to the tightly-integrated and simplified platform, the Cloudflare OS coding agent performs better and faster with fewer tokens than a general-purpose coding agent using the same underlying models (vendor-reported claim, not independently measured).

- Sources: https://github.com/cloudflare/cloudflare-os
- Evidence: ev-70, ev-64, ev-71
- Status: needs_adjudication · Confidence: None

### Cloudflare's Agents SDK provides a durable agent runtime - durable identity, state, connections, scheduling, and recoverable execution - with built-in Browser, Sandbox, AI Search, MCP, and Payments tools.

- Sources: https://developers.cloudflare.com/agents/
- Evidence: ev-100, ev-101, ev-110
- Status: needs_adjudication · Confidence: None

### The Cloudflare Agents SDK entry path is a three-command starter template (npx create-cloudflare agents-starter) that runs with no API keys, using Workers AI as the default model provider.

- Sources: https://developers.cloudflare.com/agents/
- Evidence: ev-100, ev-101, ev-110
- Status: needs_adjudication · Confidence: None

### The Agent Access Model (AAM) proposes five components that live outside the model and outside the request path: an Identity Broker, an Access Engine, a Mediation Layer, a Trust Ratchet, and an append-only Agent Activity Log; the guarantee that prompt text confers no credentials or authority depends on execution and traffic being unable to bypass mediation and on the shared control plane failing closed.

- Sources: https://blog.cloudflare.com/the-agent-access-model/
- Evidence: (none)
- Status: needs_adjudication · Confidence: None

### AAM's core stance is capability reduction over smarter decisions: make the agent's capability smaller so there is less to judge, and enforce access at the harness mediating tool calls and the network layer mediating packets, because inferred intent is shapeable through injected content - 'a boundary you can talk your way past is not a boundary.'

- Sources: https://blog.cloudflare.com/the-agent-access-model/
- Evidence: (none)
- Status: needs_adjudication · Confidence: None

### AAM replaces static long-lived grants with task-scoped capability ceilings: at task dispatch the Access Engine intersects the approved task template with the initiating principal's authority (e.g. a ten-minute ceiling naming the approved APIs, reads, and outputs), and the Identity Broker exchanges the service's broad identity for a task-scoped credential within that ceiling.

- Sources: https://blog.cloudflare.com/the-agent-access-model/
- Evidence: (none)
- Status: needs_adjudication · Confidence: None

### AAM names multiplayer access control as an unsolved problem: authority composed across actor chains, shared context, and caching - an answer computed under Alice's authority and reused for Bob is an authorization bug, not a performance optimization - with cited work reporting 15.8-50.9% privacy violation rates and up to 26.7% leakage in simulated enterprise workflows.

- Sources: https://blog.cloudflare.com/the-agent-access-model/
- Evidence: (none)
- Status: needs_adjudication · Confidence: None

### Browser Run was rebuilt on Cloudflare Containers: 60 browsers per minute via the Workers binding, up to 120 concurrent browsers, and a recently launched /crawl endpoint - a capacity and concurrency jump driven by AI agent request volumes outgrowing the shared Browser Isolation infrastructure.

- Sources: https://blog.cloudflare.com/browser-run-containers/
- Evidence: (none)
- Status: needs_adjudication · Confidence: None

### Cloudflare OS is open source (Apache-2.0) and runs inside the organization's own Cloudflare account, so organizations own what they build on it and are not locked into a closed vendor platform; it was originally built to run Cloudflare's own workforce.

- Sources: https://blog.cloudflare.com/cloudflare-os/, https://github.com/cloudflare/cloudflare-os
- Evidence: (none)
- Status: needs_adjudication · Confidence: None

### Strategic position: Cloudflare now spans both sides of the browser-automation equation - the anti-bot/bot-management network business and a governed agent-execution platform (Cloudflare OS, Agents SDK, Browser Run) - so the same vendor that gates browser-automation traffic also sells the infrastructure for governed browser agents; the synthesis question for the browser automation ecosystem is how Gatekeepers-style governance and anti-detection tooling will interact.

- Sources: https://blog.cloudflare.com/the-agent-access-model/, https://blog.cloudflare.com/cloudflare-os/, https://blog.cloudflare.com/browser-run-containers/
- Evidence: (none)
- Status: needs_adjudication · Confidence: None
