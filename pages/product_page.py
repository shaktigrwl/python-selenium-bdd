from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from utilities.dynamic_wait import *
from pages.base_page import BasePage


class ProductPage (BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.heading_class = "title"
        self.inventory_items_class = "inventory_item"
        self.inventory_item_names_class = "inventory_item_name"
        self.add_to_cart_button_class = "btn_inventory"
        self.shopping_cart_class = "shopping_cart_link"

    def validate_title(self, heading):
        try:
            page_heading = dynamic_wait(self.driver, By.CLASS_NAME, self.heading_class, 3)
            actual_result = page_heading.text
            expected_result = heading
            assert actual_result == expected_result, "Assertion Passed: The User is on the Product Page"
            print("Assertion passed and result matched")
        except TimeoutException:
            print("Timeout occurred while waiting for an element")
            assert False, "Timeout Exception Occurred"
        except Exception as e:
            self.driver.close()
            print(f"An error occurred: {e}")
            assert False, "Expected Result mismatched"

    def find_add_to_cart_button(self, product_name):
        inventory_items = dynamic_wait_for_elements(self.driver, By.CLASS_NAME, self.inventory_items_class, 3)
        for item in inventory_items:
            item_name_element = dynamic_wait_for_elements(item, By.CLASS_NAME, self.inventory_item_names_class, 3)
            item_name = item_name_element[0].text
            if product_name in item_name:
                add_to_cart = dynamic_wait(self.driver, By.CLASS_NAME, self.add_to_cart_button_class, 3)

                return add_to_cart

    def add_product_to_cart(self, product_name):
        adding_product = self.find_add_to_cart_button(product_name)
        if adding_product:
            assert True, "Selected Product found in the inventory"
            adding_product.click()

        else:
            assert False, "Selected Product not found in the inventory"

    def open_shopping_cart(self):
        shopping_cart = dynamic_wait(self.driver, By.CLASS_NAME, self.shopping_cart_class, 3)
        shopping_cart.click()
