import pytest
from pages.home_page import HomePage
from pages.search_page import SearchPage
@pytest.mark.smoke
def test_search_known_keyword(driver):
    HomePage(driver).load(); page=SearchPage(driver); page.search("computer")
    assert page.names()
@pytest.mark.regression
def test_search_partial_keyword(driver):
    HomePage(driver).load(); page=SearchPage(driver); page.search("comp")
    assert page.names()
@pytest.mark.regression
def test_search_unlikely_keyword_returns_no_products(driver):
    HomePage(driver).load(); page=SearchPage(driver); page.search("zzqvnotaproduct")
    assert not page.names()
