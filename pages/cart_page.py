from pages.base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):

    def should_not_be_products_in_cart(self):
        assert self.is_not_element_present(*CartPageLocators.CART_TOTAL), "Cart has some product , but should not be"

    def should_be_empty_cart(self):
        assert self.is_element_present(
            *CartPageLocators.EMPTY_MESSAGE), "The message is not present, but should be"
