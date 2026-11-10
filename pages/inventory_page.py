from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.items = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_first_item(self):
        self.items.first.get_by_role("button", name="Add to cart").click()