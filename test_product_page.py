import time

import pytest

from pages.base_page import BasePage
from pages.locators import ItemDetailedLocators
from pages.product_page import ProductPage


@pytest.mark.parametrize('offer_id', [0, 1, 2, 3, 4, 5, 6,
                                      pytest.param(7, marks=pytest.mark.xfail(reason='incorrect name in the basket')),
                                      8, 9])
def test_guest_can_add_product_to_basket(browser, offer_id):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_id}'
    page = ProductPage(browser, link)
    page.open()

    # capture book's name and price
    book = browser.find_element(*ItemDetailedLocators.NAME_ON_ITEM_PAGE).text
    price = browser.find_element(*ItemDetailedLocators.PRICE_ON_ITEM_PAGE).text

    # add book to the basket
    page.should_be_add_to_basket_button()
    page.add_to_basket()

    # solve a quiz
    BasePage(browser, link).solve_quiz_and_get_code()

    # chek that the book has been added to the basket
    page.should_be_confirmation_message()

    # check book's name and price
    page.the_added_books_name_is_correct(book)
    page.check_basket_price(price)

    time.sleep(1)


