# Research session: Why nodriver sessions die overnight and how production systems prevent it

Goal: Document why persisted browser automation sessions fail between runs (cookie expiry, token invalidation, profile corruption, OS restart, lock contention) and which recovery/health-check/re-authentication patterns production systems use. Research for article 3: Why Your nodriver Session Dies Overnight (and How Production Systems Prevent It).
Audience: Blog · Depth: standard
Status: draft · id: 2026-08-05-0649-why-nodriver-sessions-die-over

## Sources
- [github.com](https://github.com/ultrafunkamsterdam/nodriver) — fetched (14414 chars)
- [https://stackoverflow.com/questions/tagged/nodriver](https://stackoverflow.com/questions/tagged/nodriver) — failed (0 chars)
- [github.com](https://github.com/ultrafunkamsterdam/nodriver/issues?q=session) — fetched (3494 chars)

## Findings (drafts)
- **tab = await driver.get("https://twitter.com")**
  - sources: https://github.com/ultrafunkamsterdam/nodriver
  - status: needs_adjudication · method: keyword-density-v0
- **browser = await nodriver.start() page = await browser.get('https://www.nowsecure.nl')**
  - sources: https://github.com/ultrafunkamsterdam/nodriver
  - status: needs_adjudication · method: keyword-density-v0
- **for p in (page, page2, page3): await p.bring_to_front() await p.scroll_down(200) await p # wait for events to be processed await p.reload() if p != page3: await p.close()**
  - sources: https://github.com/ultrafunkamsterdam/nodriver
  - status: needs_adjudication · method: keyword-density-v0
- **You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another …**
  - sources: https://github.com/ultrafunkamsterdam/nodriver/issues?q=session
  - status: needs_adjudication · method: keyword-density-v0
- **No results Try adjusting your search filters.**
  - sources: https://github.com/ultrafunkamsterdam/nodriver/issues?q=session
  - status: needs_adjudication · method: keyword-density-v0
- **You can’t perform that action at this time.**
  - sources: https://github.com/ultrafunkamsterdam/nodriver/issues?q=session
  - status: needs_adjudication · method: keyword-density-v0

## Evidence
- [ev-1] You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-2] This is the official successor of the Undetected-Chromedriver python package. (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-3] Direct communication provides even better resistance against web applicatinon firewalls (WAF’s), while performance gets a massive boost. This module is, contrary to undetected-chromedriver, fully asynchronous. (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-4] What makes this package different from other known packages, is the optimization to stay undetected for most anti-bot solutions. (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-5] Another focus point is usability and quick prototyping, so expect a lot to work -as is- , with most method parameters having best practice defaults. Using 1 or 2 lines, this is up and running, providing best practice config by default. It c… (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-6] While usability and convenience is important. It’s also easy to fully customizable everything using the entire array of CDP domains, methods and events available. (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-7] smart and performant element lookup, by selector or text, including iframe content. this could also be used as wait condition for a element to appear, since it will retry for the duration of until found. so an await tab.select('body') could… (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-8] utility function to convert a running undetected_chromedriver.Chrome instance to a nodriver.Browser instance and contintue from there (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-9] Parts are rewritten to use flat connections in the protocol. Why? - iframes are included in most operations. - tab got a new method: await tab.get_frames() which will return Iframes that are inspectable. - find() will include iframes, so yo… (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-10] Since this required quite some rewriting, please test thoroughly, especially if you run large projects. (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-11] finds the checkbox and click it successfully this only works when NOT in expert mode. currently built-in english only requires opencv-python package to be installed (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-12] tab.bypass_insecure_connection_warning() (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-13] convenience method, for insecure page warning. for example when a certificate is invalid. (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-14] callback may accept a single argument (event), or 2 arguments (event, tab). (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-15] does some hacking for more experienced users. It disables web security and origin-trials, as well as ensures shadow-roots are always open. This makes you more detectable though! (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-16] you need chrome (or some chromium based browser) installed preferably in the default location on the machine where you use this package. (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-17] when running on a headless machine, like AWS or any other environment where no display is present, it's best to use some Xvfb tool, to emulate a screen. alternatively this package can be used in headless mode. (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-18] The aim of this project (just like undetected-chromedriver, somewhere long ago) is to keep it short and simple, so you can quickly open an editor or interactive session, type or paste a few lines and off you go. (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-19] browser = await uc.start() page = await browser.get('https://www.nowsecure.nl') (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-20] if __name__ == '__main__': # since asyncio.run never worked (for me) uc.loop().run_until_complete(main()) (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-21] browser = await start( headless=False, user_data_dir="/path/to/existing/profile", # by specifying it, it won't be automatically cleaned up when finished browser_executable_path="/path/to/some/other/browser", browser_args=['--some-browser-ar… (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-22] config = Config() config.headless = False config.user_data_dir="/path/to/existing/profile", # by specifying it, it won't be automatically cleaned up when finished config.browser_executable_path="/path/to/some/other/browser", config.browser_… (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-23] browser = await nodriver.start() page = await browser.get('https://www.nowsecure.nl') (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-24] await page.save_screenshot() await page.get_content() await page.scroll_down(150) elems = await page.select_all('*[src]') (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-25] page2 = await browser.get('https://twitter.com', new_tab=True) page3 = await browser.get('https://github.com/ultrafunkamsterdam/nodriver', new_window=True) (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-26] for p in (page, page2, page3): await p.bring_to_front() await p.scroll_down(200) await p # wait for events to be processed await p.reload() if p != page3: await p.close() (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-27] # since asyncio.run never worked (for me) uc.loop().run_until_complete(main()) (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-28] A more concrete example, which can be found in the ./example/ folder, shows a script to create a twitter account (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-29] async def main(): driver = await uc.start() (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-30] tab = await driver.get("https://twitter.com") (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-31] # wait for text to appear instead of a static number of seconds to wait # this does not always work as expected, due to speed. print('finding the "create account" button') create_account = await tab.find("create account", best_match=True) (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-32] print('"create account" => click') await create_account.click() (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-33] print("finding the email input field") email = await tab.select("input[type=email]") (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-34] # sometimes, email field is not shown, because phone is being asked instead # when this occurs, find the small text which says "use email instead" if not email: use_mail_instead = await tab.find("use email instead") # and click it await use… (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-35] # now find the email field again email = await tab.select("input[type=email]") (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-36] randstr = lambda k: "".join(random.choices(string.ascii_letters, k=k)) (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-37] # send keys to email field print('filling in the "email" input field') await email.send_keys("".join([randstr(8), "@", randstr(8), ".com"])) (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-38] # find the name input field print("finding the name input field") name = await tab.select("input[type=text]") (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-39] # again, send random text print('filling in the "name" input field') await name.send_keys(randstr(8)) (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-40] # since there are 3 select fields on the tab, we can use unpacking # to assign each field print('finding the "month" , "day" and "year" fields in 1 go') sel_month, sel_day, sel_year = await tab.select_all("select") (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-41] # await sel_month.focus() print('filling in the "month" input field') await sel_month.send_keys(months[random.randint(0, 11)].title()) (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-42] # await sel_day.focus() # i don't want to bother with month-lengths and leap years print('filling in the "day" input field') await sel_day.send_keys(str(random.randint(0, 28))) (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-43] # await sel_year.focus() # i don't want to bother with age restrictions print('filling in the "year" input field') await sel_year.send_keys(str(random.randint(1980, 2005))) (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-44] # let's handle the cookie nag as well cookie_bar_accept = await tab.find("accept all", best_match=True) if cookie_bar_accept: await cookie_bar_accept.click() (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-45] next_btn = await tab.find(text="next", best_match=True) # for btn in reversed(next_btns): await next_btn.mouse_click() (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-46] print("sleeping 2 seconds") await tab.sleep(2) # visually see what part we're actually in (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-47] print('finding "next" button') next_btn = await tab.find(text="next", best_match=True) print('clicking "next" button') await next_btn.mouse_click() (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-48] # just wait for some button, before we continue await tab.select("[role=button]") (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-49] print('finding "sign up" button') sign_up_btn = await tab.find("Sign up", best_match=True) # we need the second one print('clicking "sign up" button') await sign_up_btn.click() (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-50] print('the rest of the "implementation" is out of scope') # further implementation outside of scope await tab.sleep(10) driver.stop() (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-51] if __name__ == "__main__": # since asyncio.run never worked (for me) # i use uc.loop().run_until_complete(main()) (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-52] About Successor of Undetected-Chromedriver. Providing a blazing fast framework for web automation, webscraping, bots and any other creative ideas which are normally hindered by annoying anti bot systems like Captcha / CloudFlare / Imperva /… (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-53] You can’t perform that action at this time. (https://github.com/ultrafunkamsterdam/nodriver)
- [ev-54] You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. (https://github.com/ultrafunkamsterdam/nodriver/issues?q=session)
- [ev-55] No results Try adjusting your search filters. (https://github.com/ultrafunkamsterdam/nodriver/issues?q=session)
- [ev-56] You can’t perform that action at this time. (https://github.com/ultrafunkamsterdam/nodriver/issues?q=session)