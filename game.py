from playwright.sync_api import sync_playwright
import requests

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://leetcode.com/accounts/login/")

    input("Login manually and press Enter...")

    cookies = context.cookies()

    s = requests.Session()

    for c in cookies:
        s.cookies.set(c["name"], c["value"])

    headers = {
        "User-Agent": page.evaluate("navigator.userAgent"),
        "Referer": "https://leetcode.com/contest/weekly-contest-458/ranking/",
        "Origin": "https://leetcode.com",
    }

    url = "https://leetcode.com/contest/api/ranking/weekly-contest-458/?pagination=1&region=global"

    r = s.get(url, headers=headers)

    print(r.status_code)
    print(r.text[:500])

    browser.close()