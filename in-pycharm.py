import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)

    page = browser.new_page()

    page.goto('https://southeast-thisisourdomain.securerc.co.uk/onlineleasing/ourdomain-amsterdam-south-east/floorplans.aspx?_gl=1*7381pr*_gcl_au*Nzc5Mjk0MTAuMTcxOTIzNTIyMw..*_ga*NTgxNzMwNTcuMTcxOTIzNTIxMA..*_ga_XH6TT97W71*MTcxOTIzNTIwOS4xLjEuMTcxOTIzNTMyNy4wLjAuMA..', timeout=0)




    # time.sleep(57)