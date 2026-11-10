from playwright.sync_api import expect

def test_add_item_updates_badge(logged_in):
    logged_in.add_first_item()
    expect(logged_in.cart_badge).to_have_text("1")