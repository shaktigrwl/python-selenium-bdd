from selenium.webdriver.common.by import By
from utilities.dynamic_wait import *
from pages.base_page import BasePage


class OrderCompletion (BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.order_completion_message_class = "complete-header"

    def validate_message(self, message):
        complete_message = dynamic_wait(self.driver, By.CLASS_NAME, self.order_completion_message_class, 3)
        actual_message = complete_message.text
        if actual_message == message:
            assert actual_message == message, "Assertion Passed: Order Successfully Paid"
        else:
            assert False, "Assertion Failed: Something went wrong."
