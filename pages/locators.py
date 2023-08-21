from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ItemDetailedLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRICE_ON_ITEM_PAGE = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    NAME_ON_ITEM_PAGE = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')


class AlertLocators():
    ITEM_ADDED_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(1) .alertinner')
    ITEM_NAME_ON_ALERT = (By.CSS_SELECTOR, '#messages :nth-child(1) .alertinner strong')
    ITEM_PRICE_ON_ALERT = (By.CSS_SELECTOR, '.alert-info .alertinner strong')

