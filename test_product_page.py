import random
import time
from random import randint

import pytest
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage

url_product = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
email = f"test{random.randint(1, 100)}@fakemail.org"


@pytest.mark.need_review
@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"{url_product}?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.added_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_title_product_in_message()
    page.should_be_price_product_in_message()

@pytest.mark.need_review
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url_product)
    page.open()
    page.added_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, url_product)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url_product)
    page.open()
    page.added_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, url_product)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, url_product)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = CartPage(browser, url_product)
    page.open()
    page.go_to_cart_page()
    page.should_not_be_products_in_cart()
    page.should_be_empty_cart()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, url_product)
        page.open()
        page.go_to_login_page()
        page.register_new_user(f"test{random.randint(1, 100)}@fakemail.org", "feff241234ewqdsfdrew423r31")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, url_product)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, url_product)
        page.open()
        page.added_product_to_cart()
        page.should_be_title_product_in_message()
        page.should_be_price_product_in_message()
