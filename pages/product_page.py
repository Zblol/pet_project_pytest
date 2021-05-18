from pages.base_page import BasePage
from pages.locators import ProductPageLocator


class ProductPage(BasePage):

    def added_product_to_cart(self):
        added_product = self.browser.find_element(*ProductPageLocator.ADDED_BUTTON_PRODUCT)
        added_product.click()

    # def should_be_added_product_to_cart(self):
    #     title_message  = self.browser.find_element(*ProductPageLocator.TITLE_MESSAGE)
    #     title_product = self.browser.find_element(*ProductPageLocator.TITLE_PRODUCT)
    #     price_product = self.browser.find_element(*ProductPageLocator.PRICE_PRODUCT)
    #
    #     assert alertinner

    def should_be_title_product_in_message(self):
        title_message = self.browser.find_element(*ProductPageLocator.TITLE_MESSAGE).text
        title_product = self.browser.find_element(*ProductPageLocator.TITLE_PRODUCT).text

        assert title_product in title_message, "Product title wrong"

    def should_be_price_product_in_message(self):
        price_product = self.browser.find_element(*ProductPageLocator.PRICE_PRODUCT).text
        price_message = self.browser.find_element(*ProductPageLocator.PRICE_MESSAGE).text

        assert price_product in price_message, "Product price wrong"
