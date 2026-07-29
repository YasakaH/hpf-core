# Book Series Strategy — Frozen

## Purpose

This document freezes the book series direction described in the LongShot conversation (2026-07-27). It is independent of the HPF platform. Changes to this plan should be governed separately.

## The Series

Three books. Three different perspectives on the same ecosystem. Not volumes — perspectives.

### Book 1 — Browser Automation Engineering

**Purpose**: Why browsers became execution environments for AI.

**Audience**: Engineers moving from scripting to production systems.

**What it establishes**: The architectural shift from "browser as UI tester" to "browser as agent execution environment." Foundations, protocols (CDP, WebDriver), session models, detection economics.

**Credential it builds**: Technical authority. This is the book that demonstrates deep browser engineering knowledge.

### Book 2 — Production Browser Agent Infrastructure

**Purpose**: How companies build reliable browser-agent infrastructure.

**Audience**: Senior engineers and architects designing automation platforms.

**What it covers**: Distributed session management, proxy architecture, fingerprint rotation, health monitoring, scaling patterns, operational runbooks.

**Credential it builds**: Production expertise. This is the book that shows you've operated at scale.

### Book 3 — Browser UX Engineering / Agent-Ready Web

**Purpose**: The novel thesis — accessible web = agent API.

**Audience**: Web developers, platform teams, browser engineers.

**What it covers**: How to design web interfaces that are natively consumable by AI agents. The inverse of Browser Automation Engineering — instead of adapting agents to broken web APIs, teach the web to expose clean agent interfaces.

**Credential it builds**: Differentiated thought leadership. This is the novel contribution.

## Design Decisions

1. **No publication order frozen yet.** Book 1 and Book 2 have clearer markets. Book 3 is the most novel but needs research validation before committing to lead with it.
2. **Research dossiers precede books.** Domains are researched independently of any book schedule. Research → HPF knowledge objects → books.
3. **HPF is not the book.** HPF owns the reusable knowledge layer. Each book consumes HPF knowledge objects but arranges and narrates them independently.
4. **Cross-book object sharing.** A knowledge object (e.g., "session-lifecycle-concept") can appear in all three books with different narrative framing.

## Research Domains (Evergreen)

These domains are researched continuously. Results feed into HPF knowledge objects, which feed into all books.

- Browser Perception (how sites detect automation)
- Browser Architecture (CDP, WebDriver, process model)
- Browser Economics (detection arms race, CAPTCHA economics)
- Browser Infrastructure (proxy architectures, session management)
- Browser Security (isolation, sandboxing, fingerprinting)
- Browser Memory (state management, cache, persistence)
- Browser State Machines (navigation lifecycle, readiness)
- Browser Intelligence (agent decision-making, planning)
- Browser UX Engineering (accessible-from-design agent APIs)
- Protocols (HTTP, WebSocket, CDP, WebDriver BiDi)
- Distributed Systems (multi-instance coordination, queues)

## Three-Book Knowledge Map (Conceptual)

```
                    ┌──────────────────────┐
                    │  HPF Knowledge Base   │
                    │  (14+ objects, owned  │
                    │   by the platform)    │
                    └──────┬───────────┬────┘
                           │           │
              ┌────────────┘           └────────────┐
              │                                     │
     ┌────────▼────────┐                  ┌─────────▼─────────┐
     │  Book 1 Frame   │                  │  Book 2 Frame     │
     │  "Engineering"  │                  │  "Infrastructure" │
     │                 │                  │                   │
     │ Foundations     │                  │ Production patterns│
     │ Protocols       │                  │ Scaling           │
     │ Session models  │                  │ Operations        │
     │ Detection 101   │                  │ Reliability       │
     └─────────────────┘                  └───────────────────┘
                           │
                           │
              ┌────────────┘
              │
     ┌────────▼────────┐
     │  Book 3 Frame   │
     │  "UX Engineer"  │
     │                 │
     │ Accessible APIs │
     │ Agent-ready DOM │
     │ Design patterns │
     │ Future web      │
     └─────────────────┘
```

## Governance

- This document is frozen. Changes require a governance review.
- Book order will be decided after research dossiers reach maturity.
- HPF and the book series are separate governance tracks. Changes to one do not imply changes to the other.

---

*Frozen: 2026-07-29*
*Source: LongShot conversation 1785309527487*
