import pytest
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from utils.helpers import unique_email
def make_user(driver):
    email=unique_email(); HomePage(driver).load().go_register()
    RegisterPage(driver).register("Test","User",email,"Test@12345")
    return email
@pytest.mark.regression
def test_login_page_opens(driver):
    HomePage(driver).load().go_login(); assert "login" in driver.current_url.lower()
@pytest.mark.regression
def test_valid_login(driver):
    email=make_user(driver); login=LoginPage(driver)
    if login.logged_in(): driver.find_element(*login.LOGOUT).click()
    HomePage(driver).load().go_login(); login.login(email,"Test@12345")
    assert login.logged_in()
@pytest.mark.regression
@pytest.mark.parametrize("email,password",[("wrong.user@example.com","Wrong@12345"),("","")])
def test_invalid_login_shows_error(driver,email,password):
    HomePage(driver).load().go_login(); login=LoginPage(driver); login.login(email,password)
    assert login.visible(login.ERROR)
