import time
import random
from playwright.async_api import async_playwright

p = await async_playwright().start()
browser = await p.chromium.launch_persistent_context(headless=False, user_data_dir="userDir")
page = await browser.new_page()

await page.goto("https://www.facebook.com/")
time.sleep(6)

# open marketplace in facebook
await page.goto("https://www.facebook.com/marketplace/create/item")