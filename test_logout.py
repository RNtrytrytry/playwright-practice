from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_logout(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(page)
    inventory_page.logout()
    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.locator(".login_logo")).to_have_text("Swag Labs")