from telnetlib import EC

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*ProductPageLocators.LOGIN_LINK)
        login_link.click()

    def add_to_cart(self):
        add_cart_link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_cart_link.click()

    def assert_name_and_price(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        message_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        message_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE)
        assert name.text == message_name.text, "Product name in message is invalid"
        assert price.text == message_price.text, "Price in message is invalid"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"

    def should_not_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"

