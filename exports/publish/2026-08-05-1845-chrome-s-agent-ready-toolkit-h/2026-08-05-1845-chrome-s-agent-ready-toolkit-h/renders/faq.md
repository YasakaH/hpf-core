# FAQ draft — Chrome's agent-ready toolkit: how the web platform is being reshaped so AI agents can use websites, and what it means for browser automation, anti-detection, and agent infrastructure

## Q1. The agentic web has two stages: agents searching the web and agents using the web. SEO principles still apply while agents only search; when?

A1. The agentic web has two stages: agents searching the web and agents using the web. SEO principles still apply while agents only search; when agents interact directly with a website, developers need predictable machine-readable signals and dedicated tooling.

  - status: needs_adjudication · confidence: None · method: keyword-density-v0
  - source: https://developer.chrome.com/blog/agent-ready-toolkit
  - evidence: ev-7, ev-16, ev-4
  - review note: restatement sharpened into the two-stage model with the search-vs-use distinction

## Q2. WebMCP is a proposed standard that exposes structured tools to AI agents on existing websites, accelerating and simplifying agent interactio?

A2. WebMCP is a proposed standard that exposes structured tools to AI agents on existing websites, accelerating and simplifying agent interactions without rebuilding the site.

  - status: needs_adjudication · confidence: None · method: keyword-density-v0
  - source: https://developer.chrome.com/blog/agent-ready-toolkit
  - evidence: ev-7, ev-16, ev-4
  - review note: restatement; dropped the doc-pointer noise

## Q3. Third-party developer tools for Chrome DevTools for agents are experimental and available from version 0.25.0, enabled via the --categoryExp?

A3. Third-party developer tools for Chrome DevTools for agents are experimental and available from version 0.25.0, enabled via the --categoryExperimentalThirdParty command-line flag.

  - status: needs_adjudication · confidence: None · method: keyword-density-v0
  - source: https://developer.chrome.com/blog/devtools-for-agents-3p-tools
  - evidence: ev-36, ev-34, ev-61
  - review note: restatement of the availability condition

## Q4. To make a website agent-ready, adopt WebMCP to explicitly expose logic and forms, ensure a sound accessibility tree (semantic HTML, proper A?

A4. To make a website agent-ready, adopt WebMCP to explicitly expose logic and forms, ensure a sound accessibility tree (semantic HTML, proper ARIA), and optimize layout stability so elements do not move between an agent identifying and interacting with them.

  - status: needs_adjudication · confidence: None · method: keyword-density-v0
  - source: https://developer.chrome.com/docs/lighthouse/agentic-browsing/
  - evidence: ev-89, ev-69, ev-67
  - review note: prescription synthesized from the docs' recommendations (ev-89, ev-90, ev-91)

## Q5. WebMCP supports MCP sampling: the server can request LLM completions through the client, enabling sophisticated agentic behaviors while main?

A5. WebMCP supports MCP sampling: the server can request LLM completions through the client, enabling sophisticated agentic behaviors while maintaining security and privacy via human oversight.

  - status: needs_adjudication · confidence: None · method: keyword-density-v0
  - source: https://webmcp.dev
  - evidence: ev-107, ev-95, ev-94
  - review note: restatement, trim the implementation block

## Q6. WebMCP is installed client-side as an MCP server via npx @jason.today/webmcp@latest --mcp (for example in Claude Desktop); MCP clients may n?

A6. WebMCP is installed client-side as an MCP server via npx @jason.today/webmcp@latest --mcp (for example in Claude Desktop); MCP clients may need a restart before newly registered tools appear.

  - status: needs_adjudication · confidence: None · method: keyword-density-v0
  - source: https://webmcp.dev
  - evidence: ev-107, ev-95, ev-94
  - review note: config block restated as an installation claim

## Q7. WebMCP is an open-source JavaScript library that lets any website integrate with the Model Context Protocol, adding a small widget so users ?

A7. WebMCP is an open-source JavaScript library that lets any website integrate with the Model Context Protocol, adding a small widget so users can connect to and interact with the page through an LLM or agent.

  - status: needs_adjudication · confidence: None · method: keyword-density-v0
  - source: https://webmcp.dev
  - evidence: ev-107, ev-95, ev-94
  - review note: restatement, keep the library/widget identity

## Q8. Lighthouse Agentic browsing (available from Chrome M150) is informational and deliberately unbenchmarked: deterministic audits emit pass/fai?

A8. Lighthouse Agentic browsing (available from Chrome M150) is informational and deliberately unbenchmarked: deterministic audits emit pass/fail statuses and warnings plus a fractional pass ratio, with no weighted 0-100 score, because agentic-web standards are still emerging and the focus is actionable signals rather than ranking.

  - status: needs_adjudication · confidence: None · method: adjudication-synthesis-v0
  - source: https://developer.chrome.com/blog/agent-ready-toolkit
  - source: https://developer.chrome.com/docs/lighthouse/agentic-browsing/
  - review note: synthesized from ev-10, ev-14, ev-73, ev-75, ev-76

## Q9. AI agents use the accessibility tree as their primary data model: the Agentic Browsing audits verify a machine-critical subset of accessibil?

A9. AI agents use the accessibility tree as their primary data model: the Agentic Browsing audits verify a machine-critical subset of accessibility checks, including programmatic names and labels on every interactive element, tree integrity (valid roles and parent-child relationships), and visibility of interactive content.

  - status: needs_adjudication · confidence: None · method: adjudication-synthesis-v0
  - source: https://developer.chrome.com/blog/agent-ready-toolkit
  - source: https://developer.chrome.com/docs/lighthouse/agentic-browsing/
  - review note: synthesized from ev-11, ev-84, ev-85, ev-86

## Q10. Layout stability is an agentic-readiness criterion: Cumulative Layout Shift from ads, images without dimensions, or injected content moves e?

A10. Layout stability is an agentic-readiness criterion: Cumulative Layout Shift from ads, images without dimensions, or injected content moves elements between the time an agent identifies them and the time it attempts an interaction, causing misclicks; agentic-audit results also fluctuate with dynamic WebMCP tool registration timing and accessibility-tree variability from DOM changes.

  - status: needs_adjudication · confidence: None · method: adjudication-synthesis-v0
  - source: https://developer.chrome.com/blog/agent-ready-toolkit
  - source: https://developer.chrome.com/docs/lighthouse/agentic-browsing/
  - review note: synthesized from ev-12, ev-78, ev-79, ev-80, ev-87

## Q11. Lighthouse checks for llms.txt, a machine-readable summary at the domain root, as an agentic-readiness signal, and verifies WebMCP registrat?

A11. Lighthouse checks for llms.txt, a machine-readable summary at the domain root, as an agentic-readiness signal, and verifies WebMCP registration through the CDP WebMCP domain covering both declarative tools defined in HTML and imperative tools defined in JavaScript.

  - status: needs_adjudication · confidence: None · method: adjudication-synthesis-v0
  - source: https://developer.chrome.com/docs/lighthouse/agentic-browsing/
  - review note: synthesized from ev-88, ev-82

## Q12. Chrome DevTools for Agents provides a testing persona that transforms a coding agent into a browsing agent: it can simulate the exact steps ?

A12. Chrome DevTools for Agents provides a testing persona that transforms a coding agent into a browsing agent: it can simulate the exact steps an agent would take, invoke lighthouse_audit directly on the active tab for an instant multi-category health check, and screencast how the agent perceives the page, exposing machine-readable signals such as the accessibility tree that may confuse agents.

  - status: needs_adjudication · confidence: None · method: adjudication-synthesis-v0
  - source: https://developer.chrome.com/blog/agent-ready-toolkit
  - review note: synthesized from ev-18, ev-19, ev-20, ev-21

## Q13. Modern Web Guidance packages agent-ready best practices and skills, including a webmcp skill that lets a coding agent implement WebMCP tools?

A13. Modern Web Guidance packages agent-ready best practices and skills, including a webmcp skill that lets a coding agent implement WebMCP tools, so applications are built agent-friendly from the ground up.

  - status: needs_adjudication · confidence: None · method: adjudication-synthesis-v0
  - source: https://developer.chrome.com/blog/agent-ready-toolkit
  - review note: synthesized from ev-17

## Q14. Third-party developer tools for Chrome DevTools for agents use an event-based JavaScript API: pages listen for the devtoolstooldiscovery eve?

A14. Third-party developer tools for Chrome DevTools for agents use an event-based JavaScript API: pages listen for the devtoolstooldiscovery event on the window (dispatched on navigation or page change) and respond with a ToolGroup of tools defined by JSON Schema inputs and execute functions running in the page context; returned DOM elements are automatically mapped to the same UIDs used by the take_snapshot tool.

  - status: needs_adjudication · confidence: None · method: adjudication-synthesis-v0
  - source: https://developer.chrome.com/blog/devtools-for-agents-3p-tools
  - review note: synthesized from ev-44, ev-45, ev-46, ev-47, ev-48, ev-49, ev-50

## Q15. Agents invoke third-party tools through list_3p_developer_tools, execute_3p_developer_tool (with DevTools validating parameters against the ?

A15. Agents invoke third-party tools through list_3p_developer_tools, execute_3p_developer_tool (with DevTools validating parameters against the tool schema) or evaluate_script; the rationale is that application truth lives in framework internals invisible to the DOM, so Angular ships Signal Graph and Dependency Injection Graph tools for agents while React is experimenting with the API.

  - status: needs_adjudication · confidence: None · method: adjudication-synthesis-v0
  - source: https://developer.chrome.com/blog/devtools-for-agents-3p-tools
  - review note: synthesized from ev-40, ev-41, ev-51, ev-52, ev-53, ev-57, ev-58, ev-60

## Q16. WebMCP exposes MCP primitives directly on the page via registerTool, registerPrompt, registerResource and resource templates, plus sampling ?

A16. WebMCP exposes MCP primitives directly on the page via registerTool, registerPrompt, registerResource and resource templates, plus sampling through the client; tools should be registered immediately after loading webmcp.js because MCP clients may need to be restarted before new tools appear.

  - status: needs_adjudication · confidence: None · method: adjudication-synthesis-v0
  - source: https://webmcp.dev
  - source: https://developer.chrome.com/docs/lighthouse/agentic-browsing/
  - review note: synthesized from ev-98, ev-100, ev-101, ev-103, ev-105, ev-107

## Q17. The Chrome agent-ready toolkit is experimental end to end: Agentic Browsing requires Chrome 150 or later, WebMCP audits require registration?

A17. The Chrome agent-ready toolkit is experimental end to end: Agentic Browsing requires Chrome 150 or later, WebMCP audits require registration for the WebMCP origin trial, third-party developer tools require DevTools for agents 0.25.0+ with an explicit flag, and the experimental flags are documented as unstable.

  - status: needs_adjudication · confidence: None · method: adjudication-synthesis-v0
  - source: https://developer.chrome.com/blog/agent-ready-toolkit
  - source: https://developer.chrome.com/docs/lighthouse/agentic-browsing/
  - source: https://developer.chrome.com/blog/devtools-for-agents-3p-tools
  - review note: synthesized from ev-24, ev-26, ev-61, ev-71
