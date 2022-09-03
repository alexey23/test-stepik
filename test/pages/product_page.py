from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        add_cart_link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_cart_link.click()
