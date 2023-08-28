from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "URL is not contains 'login' word"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form isn't presented or locator invalid"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Reg form isn't presented or locator invalid"

    def register_new_user(self, browser, email, password):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        login_page = LoginPage(browser, link)
        login_page.open()
        self.should_be_register_form()

        self.browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_INPUT).send_keys(password)

        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
