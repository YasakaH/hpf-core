# X thread draft — Web automation pain points (2026)

## Thread (one claim per post)

1/9 Thread: Web automation pain points (2026)
2/9 Multiple independent practitioners report that scraping modern websites requires either paid APIs (Firecrawl/Browserbase) or headless Chrome fleets that consume ~1GB of RAM per page and still get blocked by Cloudflare.
3/9 Practitioners report Playwright and Puppeteer 'fall apart when you need stealth at scale', and that cloud-based automation sends data to third parties, motivating self-hosted alternatives.
4/9 Practitioners actively build counter-tooling against browser fingerprinting, which is described as tracking users without cookies.
5/9 Practitioners report websites flag accounts when browser-reported geolocation disagrees with the IP's country, and that browsers emit dozens of fingerprintable signals no single tool covers.
6/9 Practitioners report that anti-bot defences (Cloudflare, captcha challenges) block scraping use cases, and that official APIs are often missing, forcing reverse engineering.
7/9 Practitioners report Cloudflare 'Under Attack Mode' serves captchas to Tor and other 'bad' IPs that fail roughly 90% of the time — the checkbox spins forever — and that this is specific to under-attack-mode sites.
8/9 Site operators report bot traffic accounts for a large share of web traffic and that the common response (putting Cloudflare in front) is the only mitigation they consider, with AI-crawler traffic worsening the problem.
9/9 Official documentation presents browser automation as a supported, feature-complete practice (Playwright e2e framework, Chrome DevTools), while community evidence reports systematic blocking under anti-bot systems: Cloudflare Under-Attack-Mode captch
9/9 Source session: 2026-08-05-0512-web-automation-pain-points-202 — draft findings, confidence null, not validated facts.