from .pages.product_page import ProductPage
from .pages.main_page import MainPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.product_added_to_basket()
    page.product_name_matches()
    # time.sleep(600)