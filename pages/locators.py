class MainPageLocators:
    LOGIN_LINK = ('css selector', "#login_link")


class LoginPageLocators:
    LOGIN_FORM = ('id', 'login_form')
    REGISTER_FORM = ('id', 'register_form')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = ('css selector', 'button.btn-add-to-basket')
    PRODUCT_NAME = ('css selector', 'div.product_main>h1')
    PRODUCT_PRICE = ('css selector', 'p.price_color')
    ADDED_PRODUCT_NAME = ('xpath', '(// div[@ id="messages"] // strong)[1]')
    ADDED_PRODUCT_PRICE = ('xpath', '(//div[@id="messages"]//strong)[3]')


class BasePageLocators:
    LOGIN_LINK = ('css selector', "#login_link")
    LOGIN_LINK_INVALID = ('css selector', "#login_link_inc")
    BASKET_LINK = ('xpath', '//a[contains(@href, "basket")]')


class BasketPageLocators:
    BASKET_FORMSET = ('css selector', '#basket_formset')
    BASKET_EMPTY_MESSAGE = ('css selector', '#content_inner>p')
