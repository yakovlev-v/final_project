from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasketLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_product = self.browser.find_element(*BasketLocators.BASKET_BUTTON)
        add_product.click()

    def product_added_to_basket(self):
        assert self.is_element_present(
            *BasketLocators.BASKET_ADDED_MESSAGE), "Нет сообщения о добавлении товара в корзину"

    def product_name_matches(self):
        added_product = self.browser.find_element(*BasketLocators.ADDED_PRODUCT_NAME)
        added_product_name = added_product.text
        product_on_page = self.browser.find_element(*BasketLocators.PRODUCT_ON_PAGE_NAME)
        product_on_page_name = product_on_page.text
        assert added_product_name == product_on_page_name, "Товар в корзине не совпадает с тем товаром, который вы добавили"

    def should_be_total_basket_price(self):
        assert self.is_element_present(*BasketLocators.BASKET_TOTAL_MESSAGE), \
            "На странице нет сообщения со стоимостью корзины"

    def basket_price_match_with_pruduct_price(self):
        basket_total_price = self.browser.find_element(*BasketLocators.BASKET_TOTAL_PRICE)
        basket_total_price_value = basket_total_price.text
        price_of_product = self.browser.find_element(*BasketLocators.PRICE_OF_PRODUCT)
        price_of_product_value = price_of_product.text
        assert basket_total_price_value == price_of_product_value, "Стоимость корзины не совпадает с ценой товара"
