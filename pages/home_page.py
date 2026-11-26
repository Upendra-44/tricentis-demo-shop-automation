from selenium.webdriver.common.by import By
from config.settings import BASE_URL
from pages.base_page import BasePage
class HomePage(BasePage):
    REGISTER=(By.CSS_SELECTOR,"a.ico-register")
    LOGIN=(By.CSS_SELECTOR,"a.ico-login")
    CART=(By.CSS_SELECTOR,"a.ico-cart")
    SEARCH=(By.ID,"small-searchterms")
    SEARCH_BUTTON=(By.CSS_SELECTOR,"input.button-1.search-box-button")
    FEATURED=(By.LINK_TEXT,"Build your own computer")
    def load(self): self.open(BASE_URL); return self
    def go_register(self): self.click(self.REGISTER)
    def go_login(self): self.click(self.LOGIN)
    def go_cart(self):
        close_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".bar-notification .close")
        if close_buttons:
            close_buttons[0].click()
        self.click(self.CART)
    def search(self, term): self.type(self.SEARCH,term); self.click(self.SEARCH_BUTTON)
    def open_featured(self): self.click(self.FEATURED)
