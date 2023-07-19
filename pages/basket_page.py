from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            "There is no basket empty message"

    def should_be_basket_formset(self):
        self.is_element_present(*BasketPageLocators.BASKET_FORMSET)
