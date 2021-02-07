from pages.base_page import BasePage
from pages.locators import ProductPageLocators
import re


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON)

    def should_be_add_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET)

    def names_should_match(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        print(name)
        name2 = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_ADDED_TO_BASKET).text
        print(name2)
        #re.match(str(name), str(self.browser.find_element(ProductPageLocators.NAME_OF_PRODUCT_ADDED_TO_BASKET).text))
        assert name == name2, 'Mismatch product with add to basket message name '
