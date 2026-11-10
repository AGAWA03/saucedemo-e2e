from playwright.sync_api import Page


class LoginPage:
    URL = "https://www.saucedemo.com"

    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.submit = page.locator("#login-button")
        self.error = page.locator("[data-test='error']")

    def open(self):
        self.page.goto(self.URL)

    def login(self, user: str, pwd: str):
        self.username.fill(user)
        self.password.fill(pwd)
        self.submit.click()
