# LinkedIn draft — Web automation pain points (2026)

## Post body

Research on: Web automation pain points (2026).
- Multiple independent practitioners report that scraping modern websites requires either paid APIs (Firecrawl/Browserbase) or headless Chrome fleets that consume ~1GB of RAM per page and still get blocked by Cloudflare.
- Practitioners report Playwright and Puppeteer 'fall apart when you need stealth at scale', and that cloud-based automation sends data to third parties, motivating self-hosted alternatives.
- Practitioners actively build counter-tooling against browser fingerprinting, which is described as tracking users without cookies.
- Practitioners report websites flag accounts when browser-reported geolocation disagrees with the IP's country, and that browsers emit dozens of fingerprintable signals no single tool covers.
- Practitioners report that anti-bot defences (Cloudflare, captcha challenges) block scraping use cases, and that official APIs are often missing, forcing reverse engineering.

Claims are draft research findings (confidence null), not established facts.

Source session: 2026-08-05-0512-web-automation-pain-points-202