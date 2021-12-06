from selenium.webdriver.common.by import By

class MainPageLocators():
    pass


class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, ".register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class BasketLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .in:first-of-type strong")
    BASKET_ADDED_MESSAGE = (By.CSS_SELECTOR, "#messages .in:first-of-type")
    PRODUCT_ON_PAGE_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "#messages .in:nth-of-type(3)")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, "#messages .in:nth-of-type(3) strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")