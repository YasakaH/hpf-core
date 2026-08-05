# Research session: Web automation pain points (2026)

Goal: What are the recurring practitioner pain points in browser automation in 2026, and what do official sources say?
Audience: Blog · Depth: deep
Status: draft · id: 2026-08-05-0455-web-automation-pain-points-202

## Sources
- [playwright.dev](https://playwright.dev/docs/intro) — fetched (5348 chars)
- [github.com](https://github.com/nodriver) — fetched (4176 chars)
- [developer.chrome.com](https://developer.chrome.com/docs/devtools) — fetched (17320 chars)
- [r/hacker-news community signal (6 comments)](reddit://r/hacker-news/comments/playwright detection bot) — imported (12225 chars)
- [r/hacker-news community signal (5 comments)](reddit://r/hacker-news/comments/browser fingerprinting) — imported (8739 chars)
- [r/hacker-news community signal (6 comments)](reddit://r/hacker-news/comments/web scraping blocked captcha) — imported (17801 chars)
- [r/hacker-news community signal (6 comments)](reddit://r/hacker-news/comments/Cloudflare blocking bots) — imported (9341 chars)

## Findings (drafts)
- **Playwright Test is an end-to-end test framework for modern web apps. It bundles test runner, assertions, isolation, parallelization and rich tooling. Playwright supports Chromium, …**
  - sources: https://playwright.dev/docs/intro
  - status: needs_adjudication · method: keyword-density-v0
- **By default tests run headless in parallel across Chromium, Firefox and WebKit (configurable in playwright.config). Output and aggregated results display in the terminal.**
  - sources: https://playwright.dev/docs/intro
  - status: needs_adjudication · method: keyword-density-v0
- **Playwright Test
Agents
Annotations
Command line
Configuration
Configuration (use)
Emulation
Fixtures
Global setup and teardown
Parallelism
Parameterize tests
Projects
Reporters
Ret…**
  - sources: https://playwright.dev/docs/intro
  - status: needs_adjudication · method: keyword-density-v0
- **PROGRAMS
Security Lab
Maintainer Community
Accelerator
GitHub Stars
Archive Program**
  - sources: https://github.com/nodriver
  - status: needs_adjudication · method: keyword-density-v0
- **EXPLORE BY TYPE
Customer stories
Events & webinars
Ebooks & reports
Business insights
GitHub Skills**
  - sources: https://github.com/nodriver
  - status: needs_adjudication · method: keyword-density-v0
- **BY INDUSTRY
Healthcare
Financial services
Manufacturing
Government
View all industries
View all solutions**
  - sources: https://github.com/nodriver
  - status: needs_adjudication · method: keyword-density-v0
- **Learn about the new performance insights, the power of Lighthouse directly in the DevTools Performance panel.**
  - sources: https://developer.chrome.com/docs/devtools
  - status: needs_adjudication · method: keyword-density-v0
- **Learn about all the features in the Performance panel: how to record a performance trace, how to view and analyze the trace, and more.**
  - sources: https://developer.chrome.com/docs/devtools
  - status: needs_adjudication · method: keyword-density-v0
- **A wide range of tools to help you measure and optimize different aspects of your runtime performance: the Performance panel, Lighthouse, and more.**
  - sources: https://developer.chrome.com/docs/devtools
  - status: needs_adjudication · method: keyword-density-v0
- **Scraping modern websites has become a massive headache. You basically have two choices: pay for an expensive API like Firecrawl&#x2F;Browserbase, or run a fleet of headless Chrome …**
  - sources: reddit://r/hacker-news/comments/playwright detection bot
  - status: community_signal · method: keyword-density-v0
- **Hey all, I built StackScope, a crawler&#x2F;catalogue that looks at new product launches and shows what they were built with.<p>It watches launches from Product Hunt, Show HN, and …**
  - sources: reddit://r/hacker-news/comments/playwright detection bot
  - status: community_signal · method: keyword-density-v0
- **I&#x27;ve been working on browser automation infrastructure for a while and kept hitting the same ceiling: Playwright and Puppeteer are great for scripting but fall apart when you …**
  - sources: reddit://r/hacker-news/comments/playwright detection bot
  - status: community_signal · method: keyword-density-v0
- **Hello Hacker News! I’m Tomasz, creator of Privacy Thing, a browser extension for Firefox and Chromium-based browsers. I’ve just released its Preview version.<p>Privacy Thing aims t…**
  - sources: reddit://r/hacker-news/comments/browser fingerprinting
  - status: community_signal · method: keyword-density-v0
- **The premise is web pages have two readers, people and the AI reading for people. Web pages can now be written more for the AI and less for people. It’s a companion to an earlier pa…**
  - sources: reddit://r/hacker-news/comments/browser fingerprinting
  - status: community_signal · method: keyword-density-v0
- **Hello HN,<p>I started building GeoSpoof after I noticed my IP says one country, but the browser still hands sites my real location. Websites were flagging me because of this discre…**
  - sources: reddit://r/hacker-news/comments/browser fingerprinting
  - status: community_signal · method: keyword-density-v0
- **Hey HN! I’m John from xhr.dev (<a href="https:&#x2F;&#x2F;xhr.dev" rel="nofollow">https:&#x2F;&#x2F;xhr.dev</a>). At xhr.dev, I’m building tools
for reverse engineering websites, a…**
  - sources: reddit://r/hacker-news/comments/web scraping blocked captcha
  - status: community_signal · method: keyword-density-v0
- **Right now if anyone tries to load a Cloudflared website over Tor or any &quot;bad&quot; IP, they get a captcha which breaks something like 90% of the time. It seems to only be &quo…**
  - sources: reddit://r/hacker-news/comments/web scraping blocked captcha
  - status: community_signal · method: keyword-density-v0
- **I&#x27;ve launched the new product, xhr.dev (<a href="https:&#x2F;&#x2F;xhr.dev&#x2F;" rel="nofollow">https:&#x2F;&#x2F;xhr.dev&#x2F;</a>)<p>The initial product is a 1 line code in…**
  - sources: reddit://r/hacker-news/comments/web scraping blocked captcha
  - status: community_signal · method: keyword-density-v0
- **Following up on earlier thread about what setup to use for main email account. Consensus appeared to be &#x27;Get a custom domain (e.g. with Cloudflare) and use it with e.g. Fastma…**
  - sources: reddit://r/hacker-news/comments/Cloudflare blocking bots
  - status: community_signal · method: keyword-density-v0
- **Bots account for just a ridiculous amount of web traffic, tying up resources and bandwidth, and the go to response to this is...basically nothing.  You can maybe throw Cloudflare i…**
  - sources: reddit://r/hacker-news/comments/Cloudflare blocking bots
  - status: community_signal · method: keyword-density-v0
- **Hi HN,<p>This weekend I built seafruit.pages.dev  to privately share any webpage with my LLM. More sites are (rightfully) blocking AI crawlers but as a reader with the page already…**
  - sources: reddit://r/hacker-news/comments/Cloudflare blocking bots
  - status: community_signal · method: keyword-density-v0

## Evidence
- [ev-1] Getting Started
Installation
Writing tests
Generating tests
Running and debugging tests
Trace viewer
Setting up CI
VS Code
Release notes
Canary releases (https://playwright.dev/docs/intro)
- [ev-2] Playwright Test
Agents
Annotations
Command line
Configuration
Configuration (use)
Emulation
Fixtures
Global setup and teardown
Parallelism
Parameterize tests
Projects
Reporters
Retries
Sharding
Timeouts
TypeScript
UI Mode
Web server (https://playwright.dev/docs/intro)
- [ev-3] Guides
Library
Accessibility testing
Actions
Assertions
API testing
Authentication
Auto-waiting
Best Practices
Browsers
Chrome extensions
Clock
Component testing
Debugging Tests
Dialogs
Downloads
Evaluating JavaScript
Events
Extensibility
F… (https://playwright.dev/docs/intro)
- [ev-4] Playwright Test is an end-to-end test framework for modern web apps. It bundles test runner, assertions, isolation, parallelization and rich tooling. Playwright supports Chromium, WebKit and Firefox on Windows, Linux and macOS, locally or i… (https://playwright.dev/docs/intro)
- [ev-5] The command below either initializes a new project or adds Playwright to an existing one. (https://playwright.dev/docs/intro)
- [ev-6] The playwright.config centralizes configuration: target browsers, timeouts, retries, projects, reporters and more. In existing projects dependencies are added to your current package.json. (https://playwright.dev/docs/intro)
- [ev-7] By default tests run headless in parallel across Chromium, Firefox and WebKit (configurable in playwright.config). Output and aggregated results display in the terminal. (https://playwright.dev/docs/intro)
- [ev-8] After a test run, the HTML Reporter provides a dashboard filterable by the browser, passed, failed, skipped, flaky and more. Click a test to inspect errors, attachments and steps. It auto-opens only when failures occur; open manually with t… (https://playwright.dev/docs/intro)
- [ev-9] Run tests with UI Mode for watch mode, live step view, time travel debugging and more. (https://playwright.dev/docs/intro)
- [ev-10] See the detailed guide on UI Mode for watch filters, step details and trace integration. (https://playwright.dev/docs/intro)
- [ev-11] Introduction
Installing Playwright
Using npm, yarn or pnpm
Using the VS Code Extension
What's Installed
Running the Example Test
HTML Test Reports
Running the Example Test in UI Mode
Updating Playwright
System requirements
What's next (https://playwright.dev/docs/intro)
- [ev-12] BY INDUSTRY
Healthcare
Financial services
Manufacturing
Government
View all industries
View all solutions (https://github.com/nodriver)
- [ev-13] EXPLORE BY TYPE
Customer stories
Events & webinars
Ebooks & reports
Business insights
GitHub Skills (https://github.com/nodriver)
- [ev-14] SUPPORT & SERVICES
Documentation
Customer support
Community forum
Trust center
Partners
View all resources (https://github.com/nodriver)
- [ev-15] PROGRAMS
Security Lab
Maintainer Community
Accelerator
GitHub Stars
Archive Program (https://github.com/nodriver)
- [ev-16] You signed in with another tab or window. Reload to refresh your session.
 You signed out in another tab or window. Reload to refresh your session.
 You switched accounts on another tab or window. Reload to refresh your session. (https://github.com/nodriver)
- [ev-17] Prevent this user from interacting with your repositories and sending you notifications.
 Learn more about blocking users. (https://github.com/nodriver)
- [ev-18] Maximum 250 characters. Please don’t include any personal information such as legal names or email addresses. Markdown is supported. This note will only be visible to you. (https://github.com/nodriver)
- [ev-19] Contact GitHub support about this user’s behavior.
 Learn more about reporting abuse. (https://github.com/nodriver)
- [ev-20] Learn how Chrome works, participate in origin trials, and build with Chrome everywhere. (https://developer.chrome.com/docs/devtools)
- [ev-21] Chrome DevTools is a set of web developer tools built directly into the Google Chrome browser. DevTools lets you edit pages on-the-fly and diagnose problems quickly, which helps you build better websites, faster. (https://developer.chrome.com/docs/devtools)
- [ev-22] Explore how AI innovations in DevTools let you do more, faster. Use DevTools for agents to connect the power of DevTools to your favorite coding agents. (https://developer.chrome.com/docs/devtools)
- [ev-23] Let Gemini help you analyze and improve your website's styling, network, sources, and performance. Get help with console errors, and code suggestions in the Console and Sources panels. (https://developer.chrome.com/docs/devtools)
- [ev-24] Give your coding agents the same trusted tools you use to inspect network activity, record traces, and troubleshoot web applications, within your AI workflow. (https://developer.chrome.com/docs/devtools)
- [ev-25] Connect the Chrome DevTools MCP (Model Context Protocol) server to your tool of choice: Antigravity, Claude Code, Cline, Copilot, and more. (https://developer.chrome.com/docs/devtools)
- [ev-26] Learn how to inspect resources loaded by your page and edit them from your browser. (https://developer.chrome.com/docs/devtools)
- [ev-27] Explore our monthly video series taking you through common debugging scenarios in DevTools in a playful way. (https://developer.chrome.com/docs/devtools)
- [ev-28] Chrome DevTools for agents lets your agent verify responsive layouts, test location-aware APIs, and simulate varied CPU or network speeds. (https://developer.chrome.com/docs/devtools)
- [ev-29] Lighthouse in Chrome DevTools for agents lets your coding agent evaluate website quality by performing live health checks for accessibility, SEO, best practices, and agentic browsing. (https://developer.chrome.com/docs/devtools)
- [ev-30] Get a tour through the updated Performance panel, showing you how to measure Core Web Vitals (LCP, CLS, INP) and how to get tailored advice from Gemini. (https://developer.chrome.com/docs/devtools)
- [ev-31] Set sail with DevTools and become a debugging pirate! Discover techniques for emulating focus styles, testing forms with autofill, and resolving backend errors with network overrides. (https://developer.chrome.com/docs/devtools)
- [ev-32] A wide range of tools to help you measure and optimize different aspects of your runtime performance: the Performance panel, Lighthouse, and more. (https://developer.chrome.com/docs/devtools)
- [ev-33] Learn about all the features in the Performance panel: how to record a performance trace, how to view and analyze the trace, and more. (https://developer.chrome.com/docs/devtools)
- [ev-34] Learn about new DevTools features like CPU throttling calibration to help you base your performance debugging decisions on data from the real world (https://developer.chrome.com/docs/devtools)
- [ev-35] Learn about the new performance insights, the power of Lighthouse directly in the DevTools Performance panel. (https://developer.chrome.com/docs/devtools)
- [ev-36] Learn about all the features in the Sources panel: how to view and edit files, debug JavaScript, and set up a workspace. (https://developer.chrome.com/docs/devtools)
- [ev-37] Workspace lets you to save changes that you make within DevTools to source code that's stored on your computer. Learn how to set up a workspace in your own projects. (https://developer.chrome.com/docs/devtools)
- [ev-38] Learn about all the features in the Network panel: inspect response and request bodies, overwrite headers, and more. (https://developer.chrome.com/docs/devtools)
- [ev-39] Find memory issues that affect page performance, including memory leaks, and more. (https://developer.chrome.com/docs/devtools)
- [ev-40] [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too … (https://developer.chrome.com/docs/devtools)
- [ev-41] Scraping modern websites has become a massive headache. You basically have two choices: pay for an expensive API like Firecrawl&#x2F;Browserbase, or run a fleet of headless Chrome instances that eat 1GB of RAM per page and still get blocked… (reddit://r/hacker-news/comments/playwright detection bot)
- [ev-42] Hey all, I built StackScope, a crawler&#x2F;catalogue that looks at new product launches and shows what they were built with.<p>It watches launches from Product Hunt, Show HN, and PeerPush, then crawls the public site behind each one. The g… (reddit://r/hacker-news/comments/playwright detection bot)
- [ev-43] Libretto (<a href="https:&#x2F;&#x2F;libretto.sh" rel="nofollow">https:&#x2F;&#x2F;libretto.sh</a>) is a Skill+CLI that makes it easy for your coding agent to generate deterministic browser automations and debug existing ones. Key shift is … (reddit://r/hacker-news/comments/playwright detection bot)
- [ev-44] I&#x27;ve been working on browser automation infrastructure for a while and kept hitting the same ceiling: Playwright and Puppeteer are great for scripting but fall apart when you need stealth at scale. Cloud-based solutions like Browserbas… (reddit://r/hacker-news/comments/playwright detection bot)
- [ev-45] Hi HN,<p>I’m the creator of StageWright (and the open-source playwright-smart-reporter).<p>I’ve been frustrated by the &quot;black box&quot; nature of E2E test failures. Standard reporters tell you that a test failed, but they don&#x27;t he… (reddit://r/hacker-news/comments/playwright detection bot)
- [ev-46] Just shipped v2.0 of my browser fingerprinting lib.<p>The big change: I split collectors into &quot;stable&quot; (14) and &quot;unstable&quot; (5). Stable ones like canvas, webgl, fonts go into the hash. Unstable ones like battery level, ne… (reddit://r/hacker-news/comments/playwright detection bot)
- [ev-47] Hello Hacker News! I’m Tomasz, creator of Privacy Thing, a browser extension for Firefox and Chromium-based browsers. I’ve just released its Preview version.<p>Privacy Thing aims to reduce browser fingerprinting—the tracking of users withou… (reddit://r/hacker-news/comments/browser fingerprinting)
- [ev-48] Hello HN,<p>I started building GeoSpoof after I noticed my IP says one country, but the browser still hands sites my real location. Websites were flagging me because of this discrepancy. I searched for a good geolocation spoofer, only to go… (reddit://r/hacker-news/comments/browser fingerprinting)
- [ev-49] The premise is web pages have two readers, people and the AI reading for people. Web pages can now be written more for the AI and less for people. It’s a companion to an earlier page about browser fingerprinting. 
(<a href="https:&#x2F;&#x2… (reddit://r/hacker-news/comments/browser fingerprinting)
- [ev-50] I&#x27;ve been scraping 241 UK council planning portals – 2.6M decisions so far<p>UK planning data is technically public. In practice it&#x27;s locked behind 400+ different council portals, some still running bespoke ASP.NET that looks like… (reddit://r/hacker-news/comments/browser fingerprinting)
- [ev-51] If you frequently work on data collection, account management, or automation tasks, CAPTCHA is an unavoidable topic. Those constantly popping up image verifications, rotating CAPTCHAs, and pages requiring you to click &quot;I&#x27;m human&q… (reddit://r/hacker-news/comments/web scraping blocked captcha)
- [ev-52] Hey HN!<p>Excited to share a project we&#x27;ve been working on called Hyperbrowser. It’s a tool that makes scaling headless browsers ridiculously easy. It allows you to spin up hundreds of browser sessions in secure, isolated environments,… (reddit://r/hacker-news/comments/web scraping blocked captcha)
- [ev-53] Hey HN! I’m John from xhr.dev (<a href="https:&#x2F;&#x2F;xhr.dev" rel="nofollow">https:&#x2F;&#x2F;xhr.dev</a>). At xhr.dev, I’m building tools
for reverse engineering websites, and our initial product is a one-line code
integration that e… (reddit://r/hacker-news/comments/web scraping blocked captcha)
- [ev-54] I&#x27;ve launched the new product, xhr.dev (<a href="https:&#x2F;&#x2F;xhr.dev&#x2F;" rel="nofollow">https:&#x2F;&#x2F;xhr.dev&#x2F;</a>)<p>The initial product is a 1 line code integration that does bot detection avoidance via a forward pr… (reddit://r/hacker-news/comments/web scraping blocked captcha)
- [ev-55] Right now if anyone tries to load a Cloudflared website over Tor or any &quot;bad&quot; IP, they get a captcha which breaks something like 90% of the time. It seems to only be &quot;under attack mode&quot; websites, by the fact that only a … (reddit://r/hacker-news/comments/web scraping blocked captcha)
- [ev-56] This is the text contained in http://blog.mocality.co.ke/2012/01/13/google-what-were-you-thinking/blog as written by Mocality CEO
You can follow the blog link to read the full story(of which I propose since it is of better quality) but just… (reddit://r/hacker-news/comments/web scraping blocked captcha)
- [ev-57] Ask HN: Do you use Cloudflare bot protection? If so, why do you use it? Did you stress test your servers and determine that you need bot blocking? Have you considered alternatives like anubis? (reddit://r/hacker-news/comments/Cloudflare blocking bots)
- [ev-58] Hi HN,<p>This weekend I built seafruit.pages.dev  to privately share any webpage with my LLM. More sites are (rightfully) blocking AI crawlers but as a reader with the page already open, it&#x27;s frustrating that my AI assistant can&#x27;t… (reddit://r/hacker-news/comments/Cloudflare blocking bots)
- [ev-59] Hey HN,<p>I&#x27;m Daniel, solo dev from Germany. I built ClawHosters (<a href="https:&#x2F;&#x2F;clawhosters.com" rel="nofollow">https:&#x2F;&#x2F;clawhosters.com</a>), a managed hosting platform for OpenClaw, the open-source AI agent fram… (reddit://r/hacker-news/comments/Cloudflare blocking bots)
- [ev-60] Dear HN crowd,
Turnstile is making my life absolutely miserable. Since a year ago or so, I can no longer pass any challenge on my phone. I use the Firefox ESR system package on Linux (PureOS Byzantium). Whenever Turnstile gives me a checkbo… (reddit://r/hacker-news/comments/Cloudflare blocking bots)
- [ev-61] Following up on earlier thread about what setup to use for main email account. Consensus appeared to be &#x27;Get a custom domain (e.g. with Cloudflare) and use it with e.g. Fastmail&#x27;. The plan is to then make that email address the co… (reddit://r/hacker-news/comments/Cloudflare blocking bots)
- [ev-62] Bots account for just a ridiculous amount of web traffic, tying up resources and bandwidth, and the go to response to this is...basically nothing.  You can maybe throw Cloudflare in front of your site, and that&#x27;s it.<p>Within the last … (reddit://r/hacker-news/comments/Cloudflare blocking bots)