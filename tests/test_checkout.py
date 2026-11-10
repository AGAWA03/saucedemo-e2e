import pytest
from playwright.sync_api import expect

def go_to_checkout(logged_in, checkout_page):
    logged_in.add_first_item()
    logged_in.open_cart()
    checkout_page.start()

def test_successful_checkout(page, logged_in, checkout_page):
    go_to_checkout(logged_in, checkout_page)
    checkout_page.fill_info("Test", "User", "44720")
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    expect(checkout_page.summary_items).to_have_count(1)
    checkout_page.finish()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(checkout_page.complete_header).to_have_text("Thank you for your order!")

@pytest.mark.parametrize("first,last,zip_code,message", [
    ("", "User", "44720", "First Name is required"),
    ("Test", "", "44720", "Last Name is required"),
    ("Test", "User", "", "Postal Code is required"),
])
def test_missing_checkout_fields(logged_in, checkout_page, first, last, zip_code, message):
    go_to_checkout(logged_in, checkout_page)
    checkout_page.fill_info(first, last, zip_code)
    expect(checkout_page.error).to_contain_text(message)

def test_checkout_overview_shows_correct_item_count(logged_in, checkout_page):
    logged_in.add_item_by_index(0)
    logged_in.add_item_by_index(1)
    logged_in.open_cart()
    checkout_page.start()
    checkout_page.fill_info("Test", "User", "44720")
    expect(checkout_page.summary_items).to_have_count(2)