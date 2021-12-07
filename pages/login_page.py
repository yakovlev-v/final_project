from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators, LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "Подстроки login нет в данном URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Формы логина на странице нет"


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Формы регистрации на странице нет"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        pass1_fields = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD1)
        pass1_fields.send_keys(password)
        pass2_fields = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD2)
        pass2_fields.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGIST_BUTTON)
        register_button.click()
        assert self.is_element_present(*LoginPageLocators.SUCCESS_REGIST), "Регистрация не удалась"
