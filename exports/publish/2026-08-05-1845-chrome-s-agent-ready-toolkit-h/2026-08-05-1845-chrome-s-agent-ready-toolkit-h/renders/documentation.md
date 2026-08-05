# Documentation update draft — Chrome's agent-ready toolkit: how the web platform is being reshaped so AI agents can use websites, and what it means for browser automation, anti-detection, and agent infrastructure

Reference-style material compiled from accepted findings. Nothing here is corpus knowledge until it passes validation.

### The agentic web has two stages: agents searching the web and agents using the web. SEO principles still apply while agents only search; when agents interact directly with a website, developers need predictable machine-readable signals and dedicated tooling.

- Sources: https://developer.chrome.com/blog/agent-ready-toolkit
- Evidence: ev-7, ev-16, ev-4
- Status: needs_adjudication · Confidence: None

### WebMCP is a proposed standard that exposes structured tools to AI agents on existing websites, accelerating and simplifying agent interactions without rebuilding the site.

- Sources: https://developer.chrome.com/blog/agent-ready-toolkit
- Evidence: ev-7, ev-16, ev-4
- Status: needs_adjudication · Confidence: None

### Third-party developer tools for Chrome DevTools for agents are experimental and available from version 0.25.0, enabled via the --categoryExperimentalThirdParty command-line flag.

- Sources: https://developer.chrome.com/blog/devtools-for-agents-3p-tools
- Evidence: ev-36, ev-34, ev-61
- Status: needs_adjudication · Confidence: None

### To make a website agent-ready, adopt WebMCP to explicitly expose logic and forms, ensure a sound accessibility tree (semantic HTML, proper ARIA), and optimize layout stability so elements do not move between an agent identifying and interacting with them.

- Sources: https://developer.chrome.com/docs/lighthouse/agentic-browsing/
- Evidence: ev-89, ev-69, ev-67
- Status: needs_adjudication · Confidence: None

### WebMCP supports MCP sampling: the server can request LLM completions through the client, enabling sophisticated agentic behaviors while maintaining security and privacy via human oversight.

- Sources: https://webmcp.dev
- Evidence: ev-107, ev-95, ev-94
- Status: needs_adjudication · Confidence: None

### WebMCP is installed client-side as an MCP server via npx @jason.today/webmcp@latest --mcp (for example in Claude Desktop); MCP clients may need a restart before newly registered tools appear.

- Sources: https://webmcp.dev
- Evidence: ev-107, ev-95, ev-94
- Status: needs_adjudication · Confidence: None

### WebMCP is an open-source JavaScript library that lets any website integrate with the Model Context Protocol, adding a small widget so users can connect to and interact with the page through an LLM or agent.

- Sources: https://webmcp.dev
- Evidence: ev-107, ev-95, ev-94
- Status: needs_adjudication · Confidence: None

### Lighthouse Agentic browsing (available from Chrome M150) is informational and deliberately unbenchmarked: deterministic audits emit pass/fail statuses and warnings plus a fractional pass ratio, with no weighted 0-100 score, because agentic-web standards are still emerging and the focus is actionable signals rather than ranking.

- Sources: https://developer.chrome.com/blog/agent-ready-toolkit, https://developer.chrome.com/docs/lighthouse/agentic-browsing/
- Evidence: (none)
- Status: needs_adjudication · Confidence: None

### AI agents use the accessibility tree as their primary data model: the Agentic Browsing audits verify a machine-critical subset of accessibility checks, including programmatic names and labels on every interactive element, tree integrity (valid roles and parent-child relationships), and visibility of interactive content.

- Sources: https://developer.chrome.com/blog/agent-ready-toolkit, https://developer.chrome.com/docs/lighthouse/agentic-browsing/
- Evidence: (none)
- Status: needs_adjudication · Confidence: None

### Layout stability is an agentic-readiness criterion: Cumulative Layout Shift from ads, images without dimensions, or injected content moves elements between the time an agent identifies them and the time it attempts an interaction, causing misclicks; agentic-audit results also fluctuate with dynamic WebMCP tool registration timing and accessibility-tree variability from DOM changes.

- Sources: https://developer.chrome.com/blog/agent-ready-toolkit, https://developer.chrome.com/docs/lighthouse/agentic-browsing/
- Evidence: (none)
- Status: needs_adjudication · Confidence: None

### Lighthouse checks for llms.txt, a machine-readable summary at the domain root, as an agentic-readiness signal, and verifies WebMCP registration through the CDP WebMCP domain covering both declarative tools defined in HTML and imperative tools defined in JavaScript.

- Sources: https://developer.chrome.com/docs/lighthouse/agentic-browsing/
- Evidence: (none)
- Status: needs_adjudication · Confidence: None

### Chrome DevTools for Agents provides a testing persona that transforms a coding agent into a browsing agent: it can simulate the exact steps an agent would take, invoke lighthouse_audit directly on the active tab for an instant multi-category health check, and screencast how the agent perceives the page, exposing machine-readable signals such as the accessibility tree that may confuse agents.

- Sources: https://developer.chrome.com/blog/agent-ready-toolkit
- Evidence: (none)
- Status: needs_adjudication · Confidence: None

### Modern Web Guidance packages agent-ready best practices and skills, including a webmcp skill that lets a coding agent implement WebMCP tools, so applications are built agent-friendly from the ground up.

- Sources: https://developer.chrome.com/blog/agent-ready-toolkit
- Evidence: (none)
- Status: needs_adjudication · Confidence: None

### Third-party developer tools for Chrome DevTools for agents use an event-based JavaScript API: pages listen for the devtoolstooldiscovery event on the window (dispatched on navigation or page change) and respond with a ToolGroup of tools defined by JSON Schema inputs and execute functions running in the page context; returned DOM elements are automatically mapped to the same UIDs used by the take_snapshot tool.

- Sources: https://developer.chrome.com/blog/devtools-for-agents-3p-tools
- Evidence: (none)
- Status: needs_adjudication · Confidence: None

### Agents invoke third-party tools through list_3p_developer_tools, execute_3p_developer_tool (with DevTools validating parameters against the tool schema) or evaluate_script; the rationale is that application truth lives in framework internals invisible to the DOM, so Angular ships Signal Graph and Dependency Injection Graph tools for agents while React is experimenting with the API.

- Sources: https://developer.chrome.com/blog/devtools-for-agents-3p-tools
- Evidence: (none)
- Status: needs_adjudication · Confidence: None

### WebMCP exposes MCP primitives directly on the page via registerTool, registerPrompt, registerResource and resource templates, plus sampling through the client; tools should be registered immediately after loading webmcp.js because MCP clients may need to be restarted before new tools appear.

- Sources: https://webmcp.dev, https://developer.chrome.com/docs/lighthouse/agentic-browsing/
- Evidence: (none)
- Status: needs_adjudication · Confidence: None

### The Chrome agent-ready toolkit is experimental end to end: Agentic Browsing requires Chrome 150 or later, WebMCP audits require registration for the WebMCP origin trial, third-party developer tools require DevTools for agents 0.25.0+ with an explicit flag, and the experimental flags are documented as unstable.

- Sources: https://developer.chrome.com/blog/agent-ready-toolkit, https://developer.chrome.com/docs/lighthouse/agentic-browsing/, https://developer.chrome.com/blog/devtools-for-agents-3p-tools
- Evidence: (none)
- Status: needs_adjudication · Confidence: None
