from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-group a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '##id_registration-password1')
    REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form button')


class ItemDetailedLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRICE_ON_ITEM_PAGE = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    NAME_ON_ITEM_PAGE = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')


class AlertLocators():
    ITEM_ADDED_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(1) .alertinner')
    ITEM_NAME_ON_ALERT = (By.CSS_SELECTOR, '#messages :nth-child(1) .alertinner strong')
    ITEM_PRICE_ON_ALERT = (By.CSS_SELECTOR, '.alert-info .alertinner strong')


class BasketLocators():
    CONTINUE_SHOPPING_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner p a')
    ITEMS_IN_BASKET_HEADER = (By.CSS_SELECTOR, '.basket-title .row h2')
