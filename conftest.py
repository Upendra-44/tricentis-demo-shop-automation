import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.settings import HEADLESS

@pytest.fixture
def driver():
    options=Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    if HEADLESS: options.add_argument("--headless=new"); options.add_argument("--window-size=1920,1080")
    browser=webdriver.Chrome(options=options)
    browser.implicitly_wait(0)
    browser.set_page_load_timeout(35)
    try: yield browser
    finally: browser.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome=yield
    report=outcome.get_result()
    if report.when=="call" and report.failed:
        browser=item.funcargs.get("driver")
        if browser:
            os.makedirs("screenshots",exist_ok=True)
            name="".join(c if c.isalnum() or c in "-_" else "_" for c in item.nodeid)
            browser.save_screenshot(os.path.join("screenshots",name+".png"))
