from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class SearchPage(BasePage):
    BOX=(By.ID,"small-searchterms"); BUTTON=(By.CSS_SELECTOR,"input.button-1.search-box-button"); TITLES=(By.CSS_SELECTOR,".product-title a")
    def search(self,term): self.type(self.BOX,term); self.click(self.BUTTON)
    def names(self): return [e.text.strip() for e in self.driver.find_elements(*self.TITLES)]
