from selenium.webdriver.common.by import By
from utilities.dynamic_wait import *
from utilities.dynamic_scroll import scroll_to_element
from pages.base_page import BasePage


class CheckoutPage (BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.first_name_id = "first-name"
        self.last_name_id = "last-name"
        self.zipcode_id = "postal-code"
        self.continue_button_id = "continue"

    def set_firstname(self, first_name):
        first_name_input = dynamic_wait(self.driver, By.ID, self.first_name_id, 3)
        first_name_input.send_keys(first_name)

    def set_lastname(self, last_name):
        last_name_input = dynamic_wait(self.driver, By.ID, self.last_name_id, 3)
        last_name_input.send_keys(last_name)

    def set_zipcode(self, zipcode):
        zipcode_input = dynamic_wait(self.driver, By.ID, self.zipcode_id, 3)
        zipcode_input.send_keys(zipcode)

    def click_continue(self):
        continue_btn = dynamic_wait(self.driver, By.ID, self.continue_button_id, 3)
        scroll_to_element(self.driver, continue_btn)
        continue_btn.click()
