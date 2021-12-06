from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasketLocators


class BasketPage(BasePage):
    def go_to_basket_page(self):
        link = self.browser.find_element(*BasketLocators.BASKET_PAGE_LINK)
        link.click()

    def should_not_be_product(self):
        assert self.is_not_element_present(*BasketLocators.PRODUCT_IN_BASKET), "В корзине есть продукты"

    def should_be_empty_text(self):
        assert self.is_element_present(*BasketLocators.BASKET_IS_EMPTY_TEXT), "Нет текста о том что корзина пуста"