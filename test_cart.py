from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage

def test_add_to_cart(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_backpack_to_cart()
    expect(inventory.cart_badge).to_have_text("1")

def test_remove_from_cart(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_backpack_to_cart()
    expect(inventory.cart_badge).to_have_text("1")
    inventory.remove_backpack_from_cart()
    expect(inventory.cart_badge).to_have_count(0)

def logout(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)
    inventory.logout()
    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.locator(".login_logo")).to_have_text("Swag Labs")