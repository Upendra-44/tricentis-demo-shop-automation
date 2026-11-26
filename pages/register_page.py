from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class RegisterPage(BasePage):
    MALE=(By.ID,"gender-male"); FEMALE=(By.ID,"gender-female")
    FIRST=(By.ID,"FirstName"); LAST=(By.ID,"LastName"); EMAIL=(By.ID,"Email")
    PASSWORD=(By.ID,"Password"); CONFIRM=(By.ID,"ConfirmPassword")
    SUBMIT=(By.ID,"register-button"); RESULT=(By.CSS_SELECTOR,".result")
    ERRORS=(By.CSS_SELECTOR,".field-validation-error, .validation-summary-errors")
    def register(self, first, last, email, password, gender="male"):
        self.click(self.MALE if gender.lower()=="male" else self.FEMALE)
        for loc,val in [(self.FIRST,first),(self.LAST,last),(self.EMAIL,email),(self.PASSWORD,password),(self.CONFIRM,password)]: self.type(loc,val)
        self.click(self.SUBMIT)
    def submit_empty(self): self.click(self.SUBMIT)
