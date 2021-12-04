from .pages.product_page import ProductPage
from .pages.main_page import MainPage
import time
import pytest


@pytest.mark.parametrize('offer_number', [0, 1, 2, 3, 4, 5, 6,
                                          pytest.param(7, marks=pytest.mark.xfail(reason="this bug will never fixed")),
                                          8, 9])
def test_guest_can_add_product_to_basket(browser, offer_number):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer" + str(offer_number)
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.product_added_to_basket()
    page.product_name_matches()
    page.should_be_total_basket_price()
    page.basket_price_match_with_pruduct_price()
    # time.sleep(600)
