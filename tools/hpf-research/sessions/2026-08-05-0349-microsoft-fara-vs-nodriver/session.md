# Research session: Microsoft Fara vs nodriver

Goal: Does Microsoft Fara make nodriver obsolete?
Audience: Blog · Depth: standard
Status: draft · id: 2026-08-05-0349-microsoft-fara-vs-nodriver

## Sources
- [evidence-fara-github](https://github.com/microsoft/fara) — imported (2416 chars)
- [evidence-fara-msr](https://www.microsoft.com/en-us/research/blog/fara-7b-an-efficient-agentic-model-for-computer-use/) — imported (1335 chars)
- [evidence-nodriver-pypi](https://pypi.org/project/nodriver/) — imported (1153 chars)
- [r/webscraping community signal (4 comments)](reddit://r/webscraping/comments/nodriver vs playwright undetected 2026) — imported (584 chars)

## Findings (drafts)
- **Fara-7B is Microsoft's first agentic small language model (SLM) designed specifically for computer use. With only 7 billion parameters, Fara-7B is an ultra-compact Computer Use Age…**
  - sources: https://github.com/microsoft/fara
  - status: needs_adjudication · method: keyword-density-v0
- **Fara-7B is trained using a novel synthetic data generation pipeline built on the Magentic-One framework.**
  - sources: https://github.com/microsoft/fara
  - status: needs_adjudication · method: keyword-density-v0
- **The evaluation setup leverages Playwright - a cross-browser automation framework that replicates browser environments - plus an Abstract Web Agent Interface that allows integration…**
  - sources: https://github.com/microsoft/fara
  - status: needs_adjudication · method: keyword-density-v0
- **Source: https://www.microsoft.com/en-us/research/blog/fara-7b-an-efficient-agentic-model-for-computer-use/**
  - sources: https://www.microsoft.com/en-us/research/blog/fara-7b-an-efficient-agentic-model-for-computer-use/
  - status: needs_adjudication · method: keyword-density-v0
- **Microsoft engaged with a trusted third party, Browserbase, to independently verify Fara-7B with human annotators, establishing 62% accuracy of Fara-7B on filtered and re-refreshed …**
  - sources: https://www.microsoft.com/en-us/research/blog/fara-7b-an-efficient-agentic-model-for-computer-use/
  - status: needs_adjudication · method: keyword-density-v0
- **We ask Fara-7B to find and summarize the latest three issues on GitHub microsoft/Magentic-UI. In another demo Fara-7B uses different tools to find relevant information and analyze …**
  - sources: https://www.microsoft.com/en-us/research/blog/fara-7b-an-efficient-agentic-model-for-computer-use/
  - status: needs_adjudication · method: keyword-density-v0
- **Direct communication provides even better resistance against web application firewalls (WAFs), while performance gets a massive boost.**
  - sources: https://pypi.org/project/nodriver/
  - status: needs_adjudication · method: keyword-density-v0
- **nodriver provides next level async webscraping and browser automation library for python with an easy interface. This is the official successor of the Undetected-Chromedriver pytho…**
  - sources: https://pypi.org/project/nodriver/
  - status: needs_adjudication · method: keyword-density-v0
- **nodriver is open-source, an asynchronous Python library that drives Chrome directly over the Chrome DevTools Protocol (CDP), with no Selenium or WebDriver binary in the loop. Inste…**
  - sources: https://pypi.org/project/nodriver/
  - status: needs_adjudication · method: keyword-density-v0
- **Fara is a model that uses browser automation, not a scraping library. Comparing it with nodriver is apples to oranges, they solve different problems.**
  - sources: reddit://r/webscraping/comments/nodriver vs playwright undetected 2026
  - status: community_signal · method: keyword-density-v0
- **Careful with nodriver after Chrome updates - CDP changes have broken it twice this year for us. Pin your Chrome version.**
  - sources: reddit://r/webscraping/comments/nodriver vs playwright undetected 2026
  - status: community_signal · method: keyword-density-v0
- **We moved from Selenium to nodriver because ChromeDriver binary detection was killing us. Direct CDP over websocket is the only thing that passed their WAF.**
  - sources: reddit://r/webscraping/comments/nodriver vs playwright undetected 2026
  - status: community_signal · method: keyword-density-v0

## Evidence
- [ev-1] Fara-7B is Microsoft's first agentic small language model (SLM) designed specifically for computer use. With only 7 billion parameters, Fara-7B is an ultra-compact Computer Use Agent (CUA) that achieves state-of-the-art performance within i… (https://github.com/microsoft/fara)
- [ev-2] Unlike traditional chat models that generate text-based responses, Fara-7B leverages computer interfaces - mouse and keyboard - to perform multi-step tasks on behalf of users. (https://github.com/microsoft/fara)
- [ev-3] The model operates visually by perceiving webpages and taking actions like scrolling, typing, and clicking on directly predicted coordinates. It uses the same modalities as humans to interact with computers - no accessibility trees or separ… (https://github.com/microsoft/fara)
- [ev-4] Fara-7B enables on-device deployment due to its compact 7B parameter size, resulting in reduced latency and improved privacy as user data remains local. It completes tasks efficiently, averaging only about 16 steps per task compared to roug… (https://github.com/microsoft/fara)
- [ev-5] Fara-7B is trained using a novel synthetic data generation pipeline built on the Magentic-One framework. (https://github.com/microsoft/fara)
- [ev-6] The evaluation setup leverages Playwright - a cross-browser automation framework that replicates browser environments - plus an Abstract Web Agent Interface that allows integration of any model from any source, and a Fara-Agent Class refere… (https://github.com/microsoft/fara)
- [ev-7] The repository is MIT licensed. Running the agent requires hosting the model (for example with vLLM on port 5000), cloning the repository, setting up a Python virtual environment, installing the package with pip, and running playwright inst… (https://github.com/microsoft/fara)
- [ev-8] Fara1.5 is a family of frontier computer use agent models (4B, 9B, 27B) available on Microsoft Foundry. All five models operate through an observe-think-act loop: given a screenshot of the browser and the conversation history, the model rea… (https://github.com/microsoft/fara)
- [ev-9] WebTailBench is a new evaluation benchmark focusing on 11 real-world task types. Online agent evaluation results show Fara-7B achieving 73.5% success on one benchmark with 34.1%, 26.2%, and 38.4% on others, results averaged over 3 runs. (https://github.com/microsoft/fara)
- [ev-10] Source: https://www.microsoft.com/en-us/research/blog/fara-7b-an-efficient-agentic-model-for-computer-use/ (https://www.microsoft.com/en-us/research/blog/fara-7b-an-efficient-agentic-model-for-computer-use/)
- [ev-11] We ask Fara-7B to find and summarize the latest three issues on GitHub microsoft/Magentic-UI. In another demo Fara-7B uses different tools to find relevant information and analyze it through Magentic-UI - it finds driving time between two p… (https://www.microsoft.com/en-us/research/blog/fara-7b-an-efficient-agentic-model-for-computer-use/)
- [ev-12] Fara-7B exhibits strong performance compared to existing models across a diverse set of benchmarks, including both existing benchmarks and new evaluations covering useful task segments that are underrepresented in common benchmarks, such as… (https://www.microsoft.com/en-us/research/blog/fara-7b-an-efficient-agentic-model-for-computer-use/)
- [ev-13] While Fara-7B demonstrates strong benchmark results, even against much larger models, it shares many of the limitations of large models, including challenges with accuracy on more complex tasks, mistakes in following instructions, and susce… (https://www.microsoft.com/en-us/research/blog/fara-7b-an-efficient-agentic-model-for-computer-use/)
- [ev-14] Microsoft engaged with a trusted third party, Browserbase, to independently verify Fara-7B with human annotators, establishing 62% accuracy of Fara-7B on filtered and re-refreshed WebVoyager tasks. (https://www.microsoft.com/en-us/research/blog/fara-7b-an-efficient-agentic-model-for-computer-use/)
- [ev-15] nodriver provides next level async webscraping and browser automation library for python with an easy interface. This is the official successor of the Undetected-Chromedriver python package. No more webdriver, no more selenium. (https://pypi.org/project/nodriver/)
- [ev-16] Direct communication provides even better resistance against web application firewalls (WAFs), while performance gets a massive boost. (https://pypi.org/project/nodriver/)
- [ev-17] What makes this package different from other known packages is the optimization to stay undetected for most anti-bot solutions. (https://pypi.org/project/nodriver/)
- [ev-18] Another focus point is usability and quick prototyping, so expect a lot to work as-is, with most method parameters having best practice defaults. Using 1 or 2 lines, this is up and running. (https://pypi.org/project/nodriver/)
- [ev-19] nodriver is open-source, an asynchronous Python library that drives Chrome directly over the Chrome DevTools Protocol (CDP), with no Selenium or WebDriver binary in the loop. Instead of patching a ChromeDriver binary to hide automation mark… (https://pypi.org/project/nodriver/)
- [ev-20] nodriver is undetected by default but Playwright gets flagged by most anti-bot systems these days. Websites increasingly detect automation via CDP fingerprints. (reddit://r/webscraping/comments/nodriver vs playwright undetected 2026)
- [ev-21] We moved from Selenium to nodriver because ChromeDriver binary detection was killing us. Direct CDP over websocket is the only thing that passed their WAF. (reddit://r/webscraping/comments/nodriver vs playwright undetected 2026)
- [ev-22] Careful with nodriver after Chrome updates - CDP changes have broken it twice this year for us. Pin your Chrome version. (reddit://r/webscraping/comments/nodriver vs playwright undetected 2026)
- [ev-23] Fara is a model that uses browser automation, not a scraping library. Comparing it with nodriver is apples to oranges, they solve different problems. (reddit://r/webscraping/comments/nodriver vs playwright undetected 2026)