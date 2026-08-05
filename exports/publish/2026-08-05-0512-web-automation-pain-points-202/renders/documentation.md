# Documentation update draft — Web automation pain points (2026)

Reference-style material compiled from accepted findings. Nothing here is corpus knowledge until it passes validation.

### Multiple independent practitioners report that scraping modern websites requires either paid APIs (Firecrawl/Browserbase) or headless Chrome fleets that consume ~1GB of RAM per page and still get blocked by Cloudflare.

- Sources: https://news.ycombinator.com/item?id=49148163, https://news.ycombinator.com/item?id=48505364, https://news.ycombinator.com/item?id=47312509
- Dates: 2026-03-09, 2026-06-12, 2026-08-02
- Evidence: ev-109, ev-110, ev-112
- Status: community_signal · Confidence: None

### Practitioners report Playwright and Puppeteer 'fall apart when you need stealth at scale', and that cloud-based automation sends data to third parties, motivating self-hosted alternatives.

- Sources: https://news.ycombinator.com/item?id=49148163, https://news.ycombinator.com/item?id=48505364, https://news.ycombinator.com/item?id=47312509
- Dates: 2026-03-09, 2026-06-12, 2026-08-02
- Evidence: ev-109, ev-110, ev-112
- Status: community_signal · Confidence: None

### Practitioners actively build counter-tooling against browser fingerprinting, which is described as tracking users without cookies.

- Sources: https://news.ycombinator.com/item?id=49124017, https://news.ycombinator.com/item?id=48326123, https://news.ycombinator.com/item?id=48768421
- Dates: 2026-05-29, 2026-07-02, 2026-07-31
- Evidence: ev-115, ev-117, ev-116
- Status: community_signal · Confidence: None

### Practitioners report websites flag accounts when browser-reported geolocation disagrees with the IP's country, and that browsers emit dozens of fingerprintable signals no single tool covers.

- Sources: https://news.ycombinator.com/item?id=49124017, https://news.ycombinator.com/item?id=48326123, https://news.ycombinator.com/item?id=48768421
- Dates: 2026-05-29, 2026-07-02, 2026-07-31
- Evidence: ev-115, ev-117, ev-116
- Status: community_signal · Confidence: None

### Practitioners report that anti-bot defences (Cloudflare, captcha challenges) block scraping use cases, and that official APIs are often missing, forcing reverse engineering.

- Sources: https://news.ycombinator.com/item?id=42347252, https://news.ycombinator.com/item?id=34217999, https://news.ycombinator.com/item?id=42193973
- Dates: 2023-01-02, 2024-11-20, 2024-12-07
- Evidence: ev-121, ev-123, ev-122
- Status: community_signal · Confidence: None

### Practitioners report Cloudflare 'Under Attack Mode' serves captchas to Tor and other 'bad' IPs that fail roughly 90% of the time — the checkbox spins forever — and that this is specific to under-attack-mode sites.

- Sources: https://news.ycombinator.com/item?id=42347252, https://news.ycombinator.com/item?id=34217999, https://news.ycombinator.com/item?id=42193973
- Dates: 2023-01-02, 2024-11-20, 2024-12-07
- Evidence: ev-121, ev-123, ev-122
- Status: community_signal · Confidence: None

### Site operators report bot traffic accounts for a large share of web traffic and that the common response (putting Cloudflare in front) is the only mitigation they consider, with AI-crawler traffic worsening the problem.

- Sources: https://news.ycombinator.com/item?id=44022039, https://news.ycombinator.com/item?id=42810527, https://news.ycombinator.com/item?id=47113242
- Dates: 2025-01-24, 2025-05-18, 2026-02-22
- Evidence: ev-129, ev-130, ev-126
- Status: community_signal · Confidence: None

### Official documentation presents browser automation as a supported, feature-complete practice (Playwright e2e framework, Chrome DevTools), while community evidence reports systematic blocking under anti-bot systems: Cloudflare Under-Attack-Mode captchas failing ~90% of the time for Tor/bad IPs (score 161), headless fleets blocked despite ~1GB RAM per page, and tooling explicitly built around evading WAFs and detection (undetected-chromedriver successor). Community experience diverges from official documentation regarding reliability under anti-bot systems.

- Sources: https://playwright.dev/docs/intro, https://developer.chrome.com/docs/devtools, https://github.com/ultrafunkamsterdam/nodriver, https://news.ycombinator.com/item?id=34217999, https://news.ycombinator.com/item?id=49148163
- Evidence: (none)
- Status: needs_adjudication · Confidence: None
