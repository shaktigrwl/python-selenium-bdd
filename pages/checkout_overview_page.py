from selenium.webdriver.common.by import By
from utilities.dynamic_wait import *
from utilities.dynamic_scroll import scroll_to_element
from pages.base_page import BasePage


class CheckoutOverviewPage (BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.finish_cta_name = "finish"

    def click_finish_cta(self):
        finist_cta = dynamic_wait(self.driver, By.NAME, self.finish_cta_name, 3)
        scroll_to_element(self.driver, finist_cta)
        finist_cta.click()
