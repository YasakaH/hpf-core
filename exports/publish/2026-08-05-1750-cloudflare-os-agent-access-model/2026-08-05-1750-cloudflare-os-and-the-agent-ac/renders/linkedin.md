# LinkedIn draft — Cloudflare OS and the Agent Access Model: implications for AI browser agents, browser automation, anti-detection, and secure agent infrastructure

## Post body

Research on: Cloudflare OS and the Agent Access Model: implications for AI browser agents, browser automation, anti-detection, and secure agent infrastructure.
- Apps built in Cloudflare OS are instantiated from blueprints: the shared app's code is copied, but each new instance starts with independent SQLite data, conversation history, credentials, and connected resources, so teams can modify their own copies with AI instead of filing feature requests.
- Cloudflare OS mediates agent and app access to systems of record through Gatekeepers, a security and governance framework that applies guardrails to agents and apps, and supports existing organizational MCP servers via MCP Server Portals.
- Cloudflare OS is model-agnostic: it works with many major AI model providers and self-hosted models, and AI Gateway provides routing and spend control so expensive models are not used for routine tasks.
- Cloudflare OS treats AI agents as principals distinct from users: agents are accountable to a human user while holding their own restricted permissions, and they do work by writing and executing code under those permissions.
- Cloudflare reports that due to the tightly-integrated and simplified platform, the Cloudflare OS coding agent performs better and faster with fewer tokens than a general-purpose coding agent using the same underlying models (vendor-reported claim, not independently measured).

Claims are draft research findings (confidence null), not established facts.

Source session: 2026-08-05-1750-cloudflare-os-and-the-agent-ac