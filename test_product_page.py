import time

import pytest

from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.locators import ItemDetailedLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.mark.parametrize('offer_id', [0, 1, 2, 3, 4, 5, 6,
                                      pytest.param(7, marks=pytest.mark.xfail(reason='incorrect name in the basket')),
                                      8, 9])
def test_guest_can_add_product_to_basket(browser, offer_id):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_id}'
    page = ProductPage(browser, link)
    page.open()

    # check the item doesn't added to the basket
    page.should_not_be_success_message()

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


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()

    page.go_to_login_page()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail(reason='Designed as invalid test')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()

    page.add_to_basket()

    page.should_not_be_success_message()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    basket_page = BasketPage(browser, browser.current_url)
    page.open()

    page.go_to_basket()

    # check that there are no items in the basket
    basket_page.should_not_be_items_in_basket()

    # check that the message that basket is empty is presented
    basket_page.should_be_continue_shopping_button()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()

    page.should_not_be_success_message()


@pytest.mark.xfail(reason='Designed as invalid test')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()

    page.add_to_basket()

    page.success_message_should_disappear()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page = LoginPage(browser, link)


    def test_guest_can_add_product_to_basket(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)
        page.open()

        # check the item doesn't added to the basket
        page.should_not_be_success_message()

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

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()

        page.should_not_be_success_message()

