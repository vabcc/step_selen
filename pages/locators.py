from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, 'input[name="login-username"')
    LOGIN_PASSWORD_LINK = (By.CSS_SELECTOR, 'input[name="login-password"')
    REG_EMAIL_LINK = (By.CSS_SELECTOR, 'input[name="registration-email"')
    REG_PASS_LINK = (By.CSS_SELECTOR, 'input[name="registration-password1"')
    REG_PASS_RE_LINK = (By.CSS_SELECTOR, 'input[name="registration-redirect_url"')
    LOGIN_FORM = (By.CSS_SELECTOR, 'form[id="login_form"]')
    REGISTER_FORM = (By.CSS_SELECTOR, 'form[id="register_form"]')

    
    