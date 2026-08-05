# FAQ draft — Web automation pain points (2026)

## Q1. Multiple independent practitioners report that scraping modern websites requires either paid APIs (Firecrawl/Browserbase) or headless Chrome?

A1. Multiple independent practitioners report that scraping modern websites requires either paid APIs (Firecrawl/Browserbase) or headless Chrome fleets that consume ~1GB of RAM per page and still get blocked by Cloudflare.

  - status: community_signal · confidence: None · method: keyword-density-v0
  - dates: 2026-03-09, 2026-06-12, 2026-08-02
  - source: https://news.ycombinator.com/item?id=49148163
  - source: https://news.ycombinator.com/item?id=48505364
  - source: https://news.ycombinator.com/item?id=47312509
  - evidence: ev-109, ev-110, ev-112
  - review note: Draft was the Draco product pitch itself. The pain-point claim inside it (RAM cost + Cloudflare blocking + the paid-API-vs-fleet dichotomy) is corroborated by the StackScope pitch (ev-110, score 67) in the same thread — two independent occurrences of the same pain point.

## Q2. Practitioners report Playwright and Puppeteer 'fall apart when you need stealth at scale', and that cloud-based automation sends data to thi?

A2. Practitioners report Playwright and Puppeteer 'fall apart when you need stealth at scale', and that cloud-based automation sends data to third parties, motivating self-hosted alternatives.

  - status: community_signal · confidence: None · method: keyword-density-v0
  - dates: 2026-03-09, 2026-06-12, 2026-08-02
  - source: https://news.ycombinator.com/item?id=49148163
  - source: https://news.ycombinator.com/item?id=48505364
  - source: https://news.ycombinator.com/item?id=47312509
  - evidence: ev-109, ev-110, ev-112
  - review note: Owl Browser pitch (score 2 — low). Claim survives as a community_signal but with weak independent corroboration; keep status.

## Q3. Practitioners actively build counter-tooling against browser fingerprinting, which is described as tracking users without cookies.?

A3. Practitioners actively build counter-tooling against browser fingerprinting, which is described as tracking users without cookies.

  - status: community_signal · confidence: None · method: keyword-density-v0
  - dates: 2026-05-29, 2026-07-02, 2026-07-31
  - source: https://news.ycombinator.com/item?id=49124017
  - source: https://news.ycombinator.com/item?id=48326123
  - source: https://news.ycombinator.com/item?id=48768421
  - evidence: ev-115, ev-117, ev-116
  - review note: Privacy Thing pitch (score 20). The underlying claim (fingerprinting = cookie-less tracking, actively fought) is consistent across two independent products in this thread.

## Q4. Practitioners report websites flag accounts when browser-reported geolocation disagrees with the IP's country, and that browsers emit dozens?

A4. Practitioners report websites flag accounts when browser-reported geolocation disagrees with the IP's country, and that browsers emit dozens of fingerprintable signals no single tool covers.

  - status: community_signal · confidence: None · method: keyword-density-v0
  - dates: 2026-05-29, 2026-07-02, 2026-07-31
  - source: https://news.ycombinator.com/item?id=49124017
  - source: https://news.ycombinator.com/item?id=48326123
  - source: https://news.ycombinator.com/item?id=48768421
  - evidence: ev-115, ev-117, ev-116
  - review note: GeoSpoof pitch (score 19). Concrete pain point (geo mismatch flags) plus an independent corroborating claim about the breadth of fingerprint signals (ev-117).

## Q5. Practitioners report that anti-bot defences (Cloudflare, captcha challenges) block scraping use cases, and that official APIs are often miss?

A5. Practitioners report that anti-bot defences (Cloudflare, captcha challenges) block scraping use cases, and that official APIs are often missing, forcing reverse engineering.

  - status: community_signal · confidence: None · method: keyword-density-v0
  - dates: 2023-01-02, 2024-11-20, 2024-12-07
  - source: https://news.ycombinator.com/item?id=42347252
  - source: https://news.ycombinator.com/item?id=34217999
  - source: https://news.ycombinator.com/item?id=42193973
  - evidence: ev-121, ev-123, ev-122
  - review note: xhr.dev pitch (score 15). The pain point (blocked by anti-bot when scraping) is explicit and matches f-10/f-17 independently.

## Q6. Practitioners report Cloudflare 'Under Attack Mode' serves captchas to Tor and other 'bad' IPs that fail roughly 90% of the time — the check?

A6. Practitioners report Cloudflare 'Under Attack Mode' serves captchas to Tor and other 'bad' IPs that fail roughly 90% of the time — the checkbox spins forever — and that this is specific to under-attack-mode sites.

  - status: community_signal · confidence: None · method: keyword-density-v0
  - dates: 2023-01-02, 2024-11-20, 2024-12-07
  - source: https://news.ycombinator.com/item?id=42347252
  - source: https://news.ycombinator.com/item?id=34217999
  - source: https://news.ycombinator.com/item?id=42193973
  - evidence: ev-121, ev-123, ev-122
  - review note: Strongest signal in the session: score 161, concrete, falsifiable, dated 2023-2024. Retain as community_signal. This is the anchor for the Cloudflare-blocking finding.

## Q7. Site operators report bot traffic accounts for a large share of web traffic and that the common response (putting Cloudflare in front) is th?

A7. Site operators report bot traffic accounts for a large share of web traffic and that the common response (putting Cloudflare in front) is the only mitigation they consider, with AI-crawler traffic worsening the problem.

  - status: community_signal · confidence: None · method: keyword-density-v0
  - dates: 2025-01-24, 2025-05-18, 2026-02-22
  - source: https://news.ycombinator.com/item?id=44022039
  - source: https://news.ycombinator.com/item?id=42810527
  - source: https://news.ycombinator.com/item?id=47113242
  - evidence: ev-129, ev-130, ev-126
  - review note: Site-operator perspective (score 12) — the mirror image of the automation-side pain points. Weak frequency but genuinely different perspective; keep as community_signal.

## Q8. Official documentation presents browser automation as a supported, feature-complete practice (Playwright e2e framework, Chrome DevTools), wh?

A8. Official documentation presents browser automation as a supported, feature-complete practice (Playwright e2e framework, Chrome DevTools), while community evidence reports systematic blocking under anti-bot systems: Cloudflare Under-Attack-Mode captchas failing ~90% of the time for Tor/bad IPs (score 161), headless fleets blocked despite ~1GB RAM per page, and tooling explicitly built around evading WAFs and detection (undetected-chromedriver successor). Community experience diverges from official documentation regarding reliability under anti-bot systems.

  - status: needs_adjudication · confidence: None · method: adjudication-synthesis-v0
  - source: https://playwright.dev/docs/intro
  - source: https://developer.chrome.com/docs/devtools
  - source: https://github.com/ultrafunkamsterdam/nodriver
  - source: https://news.ycombinator.com/item?id=34217999
  - source: https://news.ycombinator.com/item?id=49148163
  - review note: Synthesized by the reviewer from the divergence between primary/code evidence and community evidence in this session. Deliberately kept as a draft (needs_adjudication, confidence null) — it does not graduate automatically.
