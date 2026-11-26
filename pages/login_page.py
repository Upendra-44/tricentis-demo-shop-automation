from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class LoginPage(BasePage):
    EMAIL=(By.ID,"Email"); PASSWORD=(By.ID,"Password"); BUTTON=(By.CSS_SELECTOR,"input.button-1.login-button")
    LOGOUT=(By.CSS_SELECTOR,"a.ico-logout"); ERROR=(By.CSS_SELECTOR,".validation-summary-errors")
    def login(self,email,password): self.type(self.EMAIL,email); self.type(self.PASSWORD,password); self.click(self.BUTTON)
    def logged_in(self): return self.visible(self.LOGOUT)
