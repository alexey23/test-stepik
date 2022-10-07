from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def assert_empty_text(self):
        # assert self.is_element_present(*BasketPageLocators.EMPTY_TEXT), "Text 'empty basket is not presented'"
        self.browser.find_element(*BasketPageLocators.EMPTY_TEXT)
        assert self.browser.find_element(*BasketPageLocators.EMPTY_TEXT).text == 'Your basket is empty. Continue shopping', \
            "Text 'empty basket is not presented'"

    def should_not_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "There are some items in basket"

