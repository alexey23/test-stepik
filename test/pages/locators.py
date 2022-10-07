from selenium.webdriver.common.by import By


class CommonLocators():
    CART_LINK = (By.CSS_SELECTOR, ".btn-group>a:nth-child(1)")


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_NAME_IN_MESSAGE = (By.XPATH, "//div[@id='messages']//div[1]//div[1]//strong")
    PRODUCT_PRICE = (By.XPATH, "//div[@class='col-sm-6 product_main']//p[@class='price_color']")
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages>div:last-child>div>p>strong")




class BasketPageLocators():
    EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")

