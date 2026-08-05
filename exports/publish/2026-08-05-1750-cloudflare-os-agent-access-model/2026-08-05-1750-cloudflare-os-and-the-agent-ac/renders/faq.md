# FAQ draft — Cloudflare OS and the Agent Access Model: implications for AI browser agents, browser automation, anti-detection, and secure agent infrastructure

## Q1. Apps built in Cloudflare OS are instantiated from blueprints: the shared app's code is copied, but each new instance starts with independent?

A1. Apps built in Cloudflare OS are instantiated from blueprints: the shared app's code is copied, but each new instance starts with independent SQLite data, conversation history, credentials, and connected resources, so teams can modify their own copies with AI instead of filing feature requests.

  - status: needs_adjudication · confidence: None · method: keyword-density-v0
  - source: https://blog.cloudflare.com/cloudflare-os/
  - evidence: ev-6, ev-16, ev-12
  - review note: extracted excerpt restated as a claim; grounded ev-16

## Q2. Cloudflare OS mediates agent and app access to systems of record through Gatekeepers, a security and governance framework that applies guard?

A2. Cloudflare OS mediates agent and app access to systems of record through Gatekeepers, a security and governance framework that applies guardrails to agents and apps, and supports existing organizational MCP servers via MCP Server Portals.

  - status: needs_adjudication · confidence: None · method: keyword-density-v0
  - source: https://blog.cloudflare.com/cloudflare-os/
  - evidence: ev-6, ev-16, ev-12
  - review note: excerpt restated; grounded ev-12, ev-30

## Q3. Cloudflare OS is model-agnostic: it works with many major AI model providers and self-hosted models, and AI Gateway provides routing and spe?

A3. Cloudflare OS is model-agnostic: it works with many major AI model providers and self-hosted models, and AI Gateway provides routing and spend control so expensive models are not used for routine tasks.

  - status: needs_adjudication · confidence: None · method: keyword-density-v0
  - source: https://github.com/cloudflare/cloudflare-os
  - evidence: ev-70, ev-64, ev-71
  - review note: excerpt + ev-17

## Q4. Cloudflare OS treats AI agents as principals distinct from users: agents are accountable to a human user while holding their own restricted ?

A4. Cloudflare OS treats AI agents as principals distinct from users: agents are accountable to a human user while holding their own restricted permissions, and they do work by writing and executing code under those permissions.

  - status: needs_adjudication · confidence: None · method: keyword-density-v0
  - source: https://github.com/cloudflare/cloudflare-os
  - evidence: ev-70, ev-64, ev-71
  - review note: excerpt restated; ev-8, ev-30

## Q5. Cloudflare reports that due to the tightly-integrated and simplified platform, the Cloudflare OS coding agent performs better and faster wit?

A5. Cloudflare reports that due to the tightly-integrated and simplified platform, the Cloudflare OS coding agent performs better and faster with fewer tokens than a general-purpose coding agent using the same underlying models (vendor-reported claim, not independently measured).

  - status: needs_adjudication · confidence: None · method: keyword-density-v0
  - source: https://github.com/cloudflare/cloudflare-os
  - evidence: ev-70, ev-64, ev-71
  - review note: vendor claim kept with explicit attribution

## Q6. Cloudflare's Agents SDK provides a durable agent runtime - durable identity, state, connections, scheduling, and recoverable execution - wit?

A6. Cloudflare's Agents SDK provides a durable agent runtime - durable identity, state, connections, scheduling, and recoverable execution - with built-in Browser, Sandbox, AI Search, MCP, and Payments tools.

  - status: needs_adjudication · confidence: None · method: keyword-density-v0
  - source: https://developers.cloudflare.com/agents/
  - evidence: ev-100, ev-101, ev-110
  - review note: excerpt restated; ev-101, ev-105

## Q7. The Cloudflare Agents SDK entry path is a three-command starter template (npx create-cloudflare agents-starter) that runs with no API keys, ?

A7. The Cloudflare Agents SDK entry path is a three-command starter template (npx create-cloudflare agents-starter) that runs with no API keys, using Workers AI as the default model provider.

  - status: needs_adjudication · confidence: None · method: keyword-density-v0
  - source: https://developers.cloudflare.com/agents/
  - evidence: ev-100, ev-101, ev-110
  - review note: excerpt restated

## Q8. The Agent Access Model (AAM) proposes five components that live outside the model and outside the request path: an Identity Broker, an Acces?

A8. The Agent Access Model (AAM) proposes five components that live outside the model and outside the request path: an Identity Broker, an Access Engine, a Mediation Layer, a Trust Ratchet, and an append-only Agent Activity Log; the guarantee that prompt text confers no credentials or authority depends on execution and traffic being unable to bypass mediation and on the shared control plane failing closed.

  - status: needs_adjudication · confidence: None · method: adjudication-v0
  - source: https://blog.cloudflare.com/the-agent-access-model/
  - review note: reviewer synthesis from the AAM post; the post's body was under-extracted into the evidence layer (see friction log)

## Q9. AAM's core stance is capability reduction over smarter decisions: make the agent's capability smaller so there is less to judge, and enforce?

A9. AAM's core stance is capability reduction over smarter decisions: make the agent's capability smaller so there is less to judge, and enforce access at the harness mediating tool calls and the network layer mediating packets, because inferred intent is shapeable through injected content - 'a boundary you can talk your way past is not a boundary.'

  - status: needs_adjudication · confidence: None · method: adjudication-v0
  - source: https://blog.cloudflare.com/the-agent-access-model/
  - review note: reviewer synthesis from the AAM post

## Q10. AAM replaces static long-lived grants with task-scoped capability ceilings: at task dispatch the Access Engine intersects the approved task ?

A10. AAM replaces static long-lived grants with task-scoped capability ceilings: at task dispatch the Access Engine intersects the approved task template with the initiating principal's authority (e.g. a ten-minute ceiling naming the approved APIs, reads, and outputs), and the Identity Broker exchanges the service's broad identity for a task-scoped credential within that ceiling.

  - status: needs_adjudication · confidence: None · method: adjudication-v0
  - source: https://blog.cloudflare.com/the-agent-access-model/
  - review note: reviewer synthesis from the AAM post's worked example

## Q11. AAM names multiplayer access control as an unsolved problem: authority composed across actor chains, shared context, and caching - an answer?

A11. AAM names multiplayer access control as an unsolved problem: authority composed across actor chains, shared context, and caching - an answer computed under Alice's authority and reused for Bob is an authorization bug, not a performance optimization - with cited work reporting 15.8-50.9% privacy violation rates and up to 26.7% leakage in simulated enterprise workflows.

  - status: needs_adjudication · confidence: None · method: adjudication-v0
  - source: https://blog.cloudflare.com/the-agent-access-model/
  - review note: reviewer synthesis from the AAM post; open-problem status is the post's own framing

## Q12. Browser Run was rebuilt on Cloudflare Containers: 60 browsers per minute via the Workers binding, up to 120 concurrent browsers, and a recen?

A12. Browser Run was rebuilt on Cloudflare Containers: 60 browsers per minute via the Workers binding, up to 120 concurrent browsers, and a recently launched /crawl endpoint - a capacity and concurrency jump driven by AI agent request volumes outgrowing the shared Browser Isolation infrastructure.

  - status: needs_adjudication · confidence: None · method: adjudication-v0
  - source: https://blog.cloudflare.com/browser-run-containers/
  - review note: reviewer synthesis; grounded ev-119, ev-120

## Q13. Cloudflare OS is open source (Apache-2.0) and runs inside the organization's own Cloudflare account, so organizations own what they build on?

A13. Cloudflare OS is open source (Apache-2.0) and runs inside the organization's own Cloudflare account, so organizations own what they build on it and are not locked into a closed vendor platform; it was originally built to run Cloudflare's own workforce.

  - status: needs_adjudication · confidence: None · method: adjudication-v0
  - source: https://blog.cloudflare.com/cloudflare-os/
  - source: https://github.com/cloudflare/cloudflare-os
  - review note: reviewer synthesis; grounded ev-24

## Q14. Strategic position: Cloudflare now spans both sides of the browser-automation equation - the anti-bot/bot-management network business and a ?

A14. Strategic position: Cloudflare now spans both sides of the browser-automation equation - the anti-bot/bot-management network business and a governed agent-execution platform (Cloudflare OS, Agents SDK, Browser Run) - so the same vendor that gates browser-automation traffic also sells the infrastructure for governed browser agents; the synthesis question for the browser automation ecosystem is how Gatekeepers-style governance and anti-detection tooling will interact.

  - status: needs_adjudication · confidence: None · method: adjudication-v0
  - source: https://blog.cloudflare.com/the-agent-access-model/
  - source: https://blog.cloudflare.com/cloudflare-os/
  - source: https://blog.cloudflare.com/browser-run-containers/
  - review note: reviewer synthesis from session goal's implications dimension; flagged for maturity review
