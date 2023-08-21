from pages.base_page import BasePage
from pages.locators import ItemDetailedLocators, AlertLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ItemDetailedLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ItemDetailedLocators.ADD_TO_BASKET_BUTTON), "The button is not presented"

    def should_be_confirmation_message(self):
        confirmation_message = self.browser.find_element(*AlertLocators.ITEM_ADDED_MESSAGE).text
        assert "has been added to your basket." in confirmation_message, "Item hasn't been added to the basket"

    def the_added_books_name_is_correct(self, book_name):
        added_book_name = self.browser.find_element(*AlertLocators.ITEM_NAME_ON_ALERT).text
        assert book_name == added_book_name, f'{added_book_name} has been added instead {book_name}'

    def check_basket_price(self, book_price):
        displayed_price = self.browser.find_element(*AlertLocators.ITEM_PRICE_ON_ALERT).text
        assert book_price == displayed_price, f"The item's price is {book_price}, but {displayed_price}"

