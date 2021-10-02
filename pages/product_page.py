from pages.base_page import BasePage
from pages.locators import ProductPageLocator


class ProductPage(BasePage):

    def added_product_to_cart(self):
        added_product = self.browser.find_element(*ProductPageLocator.ADDED_BUTTON_PRODUCT)
        added_product.click()

    def should_be_title_product_in_message(self):
        title_message = self.browser.find_element(*ProductPageLocator.TITLE_MESSAGE)
        title_product = self.browser.find_element(*ProductPageLocator.TITLE_PRODUCT)

        assert title_product.text == title_message.text, "Product title wrong"

    def should_be_price_product_in_message(self):
        price_product = self.browser.find_element(*ProductPageLocator.PRICE_PRODUCT)
        price_message = self.browser.find_element(*ProductPageLocator.PRICE_MESSAGE)

        assert price_product.text == price_message.text, "Product price wrong"

