import pytest
from playwright.sync_api import expect

@pytest.mark.smoke
def test_add_item_updates_badge(logged_in):
    logged_in.add_first_item()
    expect(logged_in.cart_badge).to_have_text("1")

@pytest.mark.regression
def test_add_multiple_items(logged_in):
    logged_in.add_item_by_index(0)
    logged_in.add_item_by_index(1)
    logged_in.add_item_by_index(2)
    expect(logged_in.cart_badge).to_have_text("3")

@pytest.mark.regression
def test_remove_item_clears_badge(logged_in):
    logged_in.add_first_item()
    logged_in.remove_item_by_index(0)
    expect(logged_in.cart_badge).to_have_count(0)

@pytest.mark.regression
def test_cart_page_shows_added_item(page, logged_in):
    logged_in.add_first_item()
    logged_in.open_cart()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(page.locator(".cart_item")).to_have_count(1)