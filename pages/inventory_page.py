from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.items = page.locator(".inventory_item")
        self.item_names = page.locator(".inventory_item_name")
        self.item_prices = page.locator(".inventory_item_price")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.sort_dropdown = page.locator(".product_sort_container")

    def add_first_item(self):
        self.items.first.get_by_role("button", name="Add to cart").click()

    def add_item_by_index(self, index: int):
        self.items.nth(index).get_by_role("button", name="Add to cart").click()

    def remove_item_by_index(self, index: int):
        self.items.nth(index).get_by_role("button", name="Remove").click()

    def sort_by(self, option: str):
        self.sort_dropdown.select_option(label=option)

    def open_cart(self):
        self.cart_link.click()