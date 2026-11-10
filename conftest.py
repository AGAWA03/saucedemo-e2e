import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.open()
    return lp

@pytest.fixture
def logged_in(page, login_page):
    login_page.login("standard_user", "secret_sauce")
    return InventoryPage(page)

@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)