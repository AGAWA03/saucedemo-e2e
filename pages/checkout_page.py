from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator("#checkout")
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.error = page.locator("[data-test='error']")
        self.summary_items = page.locator(".cart_item")
        self.complete_header = page.locator(".complete-header")

    def start(self):
        self.checkout_button.click()

    def fill_info(self, first: str, last: str, zip_code: str):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(zip_code)
        self.continue_button.click()

    def finish(self):
        self.finish_button.click()
