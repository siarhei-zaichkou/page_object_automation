from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_added_message(self, product_name):
        assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT_NAME), "Added message is not presented"
        assert self.driver.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text ==\
               product_name, "Added product name is not match"

    def should_be_price_message(self, product_price):
        assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT_PRICE), "Added product price is not presented"
        assert self.driver.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text == \
               product_price, "Added product price is not match"

    def get_product_name(self):
        return self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.driver.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_NAME),\
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_PRODUCT_NAME)
