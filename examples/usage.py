from playwright.sync_api import sync_playwright
from axe_core_python.sync_playwright import Axe

axe = Axe()

with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.google.com")
    results = axe.run(page)
    browser.close()