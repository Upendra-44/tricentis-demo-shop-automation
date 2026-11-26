from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProductPage(BasePage):
    TITLE = (By.CSS_SELECTOR, ".product-name h1")
    ADD = (By.CSS_SELECTOR, "input[id^='add-to-cart-button-']")
    NOTICE = (By.CSS_SELECTOR, ".bar-notification")

    def title(self):
        return self.text(self.TITLE)

    def add_to_cart(self):
        # Build-your-own-computer requires an HDD selection. Select the first
        # option only for radio groups that do not already have a selection.
        radio_groups = {}
        for radio in self.driver.find_elements(By.CSS_SELECTOR, ".attributes input[type='radio']"):
            radio_groups.setdefault(radio.get_attribute("name"), []).append(radio)

        for radios in radio_groups.values():
            if not any(radio.is_selected() for radio in radios):
                radios[0].click()

        self.click(self.ADD)
        notice = WebDriverWait(self.driver, self.wait._timeout).until(
            EC.visibility_of_element_located(self.NOTICE)
        )

        if "added" not in notice.text.lower():
            raise AssertionError(f"Product was not added to cart: {notice.text.strip()}")
