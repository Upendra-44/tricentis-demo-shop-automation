import pytest
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
@pytest.mark.smoke
def test_featured_product_can_be_added_to_cart(driver):
    home=HomePage(driver).load(); home.open_featured(); product=ProductPage(driver)
    assert "computer" in product.title().lower(); product.add_to_cart()
    assert product.visible(product.NOTICE)
@pytest.mark.regression
def test_cart_contains_added_product(driver):
    home=HomePage(driver).load(); home.open_featured(); ProductPage(driver).add_to_cart(); home.go_cart()
    assert CartPage(driver).row_count()>0
