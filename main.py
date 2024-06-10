import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)

    page = browser.new_page()

    page.goto('https://clash.gg', timeout=60000)




    time.sleep(5)



