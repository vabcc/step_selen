from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'no login in url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        f_email = self.browser.find_element(*LoginPageLocators.REG_EMAIL_LINK)
        f_email.send_keys(email)
        f_pass1 = self.browser.find_element(*LoginPageLocators.REG_PASS_LINK)
        f_pass1.send_keys(password)
        f_pass2 = self.browser.find_element(*LoginPageLocators.REG_PASS_RE_LINK)
        f_pass2.send_keys(password)
        btn = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        btn.click()
