import pytest
from pages.home_page import HomePage
@pytest.mark.smoke
def test_home_page_loads(driver):
    HomePage(driver).load()
    assert "Demo Web Shop" in driver.title
@pytest.mark.smoke
def test_home_navigation_links_are_visible(driver):
    page=HomePage(driver).load()
    assert page.visible(page.REGISTER) and page.visible(page.LOGIN) and page.visible(page.CART)
