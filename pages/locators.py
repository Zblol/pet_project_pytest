from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BUTTON = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, 'a[href="/ru/accounts/"]')
    USER_LOGOUT = (By.CSS_SELECTOR, '#logout_link')



class CartPageLocators:
    CART_TOTAL = (By.CSS_SELECTOR, 'th[class="total align-right"]')
    EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    EMAIL_INPUT = (By.ID, 'id_registration-email')
    PASSWORD_INPUT = (By.ID, 'id_registration-password1')
    CONFIRM_PASSWORD_INPUT = (By.ID, 'id_registration-password2')
    REG_BUTTON = (By.CSS_SELECTOR, 'button[name = "registration_submit"]')


class ProductPageLocator:
    TITLE_PRODUCT = (By.CSS_SELECTOR, '.product_main h1')
    PRICE_PRODUCT = (By.CSS_SELECTOR, 'h1 + .price_color')
    ADDED_BUTTON_PRODUCT = (By.CLASS_NAME, 'btn-add-to-basket')
    TITLE_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner > strong')
    PRICE_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner > p > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
