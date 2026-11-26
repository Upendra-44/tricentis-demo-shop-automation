from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.settings import EXPLICIT_WAIT

class BasePage:
    def __init__(self, driver, timeout=EXPLICIT_WAIT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    def open(self, url): self.driver.get(url)
    def find(self, locator): return self.wait.until(EC.visibility_of_element_located(locator))
    def clickable(self, locator): return self.wait.until(EC.element_to_be_clickable(locator))
    def click(self, locator): self.clickable(locator).click()
    def type(self, locator, value, clear=True):
        el=self.find(locator)
        if clear: el.clear()
        el.send_keys(value)
    def text(self, locator): return self.find(locator).text.strip()
    def visible(self, locator, timeout=3):
        try: WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)); return True
        except TimeoutException: return False
