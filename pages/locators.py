from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocator:
    TITLE_PRODUCT = (By.CSS_SELECTOR, '.product_main h1')
    PRICE_PRODUCT = (By.CLASS_NAME, 'price_color')
    ADDED_BUTTON_PRODUCT = (By.CLASS_NAME, 'btn-add-to-basket')
    TITLE_MESSAGE = (By.CSS_SELECTOR, '.alert-success .alertinner')
    PRICE_MESSAGE = (By.CSS_SELECTOR, '.alert-info .alertinner')
