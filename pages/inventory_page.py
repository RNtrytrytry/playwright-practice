from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_badge = page.locator("[data-test=\"shopping-cart-badge\"]")

    def add_backpack_to_cart(self):
        self.page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()

    def remove_backpack_from_cart(self):
        self.page.locator("[data-test=\"remove-sauce-labs-backpack\"]").click()