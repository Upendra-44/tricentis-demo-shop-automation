from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class CartPage(BasePage):
    TITLE=(By.CSS_SELECTOR,".page-title h1"); ROWS=(By.CSS_SELECTOR,"table.cart tbody tr")
    def row_count(self): return len(self.driver.find_elements(*self.ROWS))
