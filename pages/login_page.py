import re
from pages.base_page import BasePage
from selenium import webdriver
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert re.search(r'login', url)

    def should_be_login_form(self):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        assert email_field.is_displayed(), "Email field is not presented"

        pass_field = self.browser.find_element(*LoginPageLocators.PASS_FIELD)
        assert pass_field.is_displayed(), "Password field is not presented"

    def should_be_register_form(self):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        assert email_field.is_displayed(), "Email field for registration is not presented"

        pass_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS_FIELD)
        assert pass_field.is_displayed(), "Password field for registration is not presented"
