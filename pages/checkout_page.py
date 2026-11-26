from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class CheckoutPage(BasePage):
    TERMS=(By.ID,"termsofservice"); CHECKOUT=(By.ID,"checkout"); GUEST=(By.CSS_SELECTOR,"input.button-1.checkout-as-guest-button")
    def continue_checkout(self):
        cb=self.find(self.TERMS)
        if not cb.is_selected(): cb.click()
        self.click(self.CHECKOUT)
