from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasketLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_product = self.browser.find_element(*BasketLocators.BASKET_BUTTON)
        add_product.click()

    def get_text_of_add_to_basket_message(self):
        text_with_added_prod_name = self.browser.find_element(*BasketLocators.ADDED_PRODUCT_NAME)
        text_of_add_to_basket_message = text_with_added_prod_name.text
        return text_of_add_to_basket_message

    def get_name_product_on_page(self):
        name_product = self.browser.find_element(*BasketLocators.PRODUCT_ON_PAGE_NAME)
        name_product_on_page = name_product.text
        return name_product_on_page

    def product_added_to_basket(self):
        assert self.is_element_present(*BasketLocators.BASKET_ADDED_MESSAGE), "Нет сообщения о добавлении товара в корзину"

    def product_name_matches(self):
        assert name_product_on_page == text_of_add_to_basket_message, "Название товара в сообщении не совпадает с тем товаром, который вы добавили"

