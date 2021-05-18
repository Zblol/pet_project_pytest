from pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    browser.get(link)
    page = ProductPage(browser,link)
    page.open()
    page.added_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_title_product_in_message()
    page.should_be_price_product_in_message()