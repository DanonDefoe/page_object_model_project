from pages.base_page import BasePage
from pages.locators import BasketLocators


class BasketPage(BasePage):
    def should_be_continue_shopping_button(self):
        assert self.is_element_present(
            *BasketLocators.CONTINUE_SHOPPING_BASKET_MESSAGE), 'continue button is not presented'

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(
            *BasketLocators.ITEMS_IN_BASKET_HEADER), 'items in basket header is present, but should not be'
