import pytest
from playwright.sync_api import expect

def test_valid_login(page, login_page):
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_locked_out_user(login_page):
    login_page.login("locked_out_user", "secret_sauce")
    expect(login_page.error).to_contain_text("locked out")

@pytest.mark.parametrize("user,pwd", [("", ""), ("standard_user", ""), ("bad", "bad")])
def test_invalid_credentials(login_page, user, pwd):
    login_page.login(user, pwd)
    expect(login_page.error).to_be_visible()