import pytest
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from utils.helpers import unique_email
@pytest.mark.regression
def test_registration_page_opens(driver):
    HomePage(driver).load().go_register()
    assert "register" in driver.current_url.lower()
    assert RegisterPage(driver).visible(RegisterPage.EMAIL)
@pytest.mark.regression
def test_register_new_user(driver):
    HomePage(driver).load().go_register()
    page=RegisterPage(driver); page.register("Automation","Tester",unique_email(),"Test@12345")
    assert page.visible(page.RESULT)
    assert "completed" in page.text(page.RESULT).lower()
@pytest.mark.regression
def test_empty_registration_shows_validation(driver):
    HomePage(driver).load().go_register(); page=RegisterPage(driver); page.submit_empty()
    assert page.visible(page.ERRORS)
