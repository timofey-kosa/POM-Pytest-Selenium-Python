from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    EMAIL_FIELD = (By.ID, "id_login-username")
    PASS_FIELD = (By.ID, "id_login-password")
    FORGOT_PASS_FIELD = (By.ID, "id_login-redirect_url")
    REGISTRATION_EMAIL_FIELD = (By.ID, "id_registration-email")
    REGISTRATION_PASS_FIELD = (By.ID, "id_registration-password1")
    CONFIRM_REGISTRATION_PASS_FIELD = (By.ID, "id_registration-password2")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".add-to-basket")
    PRODUCT_ADDED_TO_BASKET = (By.CLASS_NAME, "alertinner")
    NAME_OF_PRODUCT_ADDED_TO_BASKET = (By.XPATH, "//*[@class='alertinner ']/strong")
    PRODUCT_NAME = (By.XPATH, "//*[@class='col-sm-6 product_main']/h1")








