from selenium.webdriver.common.by import By
from utilities.dynamic_wait import *
from pages.base_page import BasePage


class CartPage (BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.inventory_name = "inventory_item_name"
        self.checkout_class = "checkout_button"

    def validate_product_in_cart(self, product_name):
        fetching_product_name = dynamic_wait(self.driver, By.CLASS_NAME, self.inventory_name, 3)
        cart_item_name = fetching_product_name.text
        if cart_item_name == product_name:
            assert cart_item_name == product_name, "Your Product is in cart !"
        else:
            assert False, "Your product is not there in the cart !"

    def continue_to_checkout(self):
        checkout_button = dynamic_wait(self.driver, By.CLASS_NAME, self.checkout_class, 3)
        checkout_button.click()
