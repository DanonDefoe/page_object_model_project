import pytest

from pages.basket_page import BasketPage
from pages.locators import StaticLinks
from pages.main_page import MainPage
from pages.login_page import LoginPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = StaticLinks.MAIN_PAGE
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_link()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = StaticLinks.MAIN_PAGE
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = StaticLinks.MAIN_PAGE
    page = MainPage(browser, link)
    basket_page = BasketPage(browser, browser.current_url)
    page.open()
    page.go_to_basket()

    # check that there are no items in the basket
    basket_page.should_not_be_items_in_basket()

    # check that the message that basket is empty is presented
    basket_page.should_be_continue_shopping_button()
