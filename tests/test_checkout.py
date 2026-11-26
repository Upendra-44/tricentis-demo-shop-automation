import pytest
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
@pytest.mark.regression
def test_checkout_terms_are_shown_from_cart(driver):
    home=HomePage(driver).load(); home.open_featured(); ProductPage(driver).add_to_cart(); home.go_cart()
    checkout=CheckoutPage(driver); assert checkout.visible(checkout.TERMS)
