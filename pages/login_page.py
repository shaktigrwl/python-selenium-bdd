from selenium.webdriver.common.by import By
from utilities.dynamic_wait import dynamic_wait
from utilities.data_loader import load_json
from pages.base_page import BasePage


class LoginPage (BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.username_id = "user-name"
        self.password_id = "password"
        self.login_button_id = "login-button"
        self.error_message_class = "error-message-container"

    def get_homepage(self):
        url = load_json('base_url', 'resources/data.json')
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def set_valid_username(self):
        username_input = dynamic_wait(self.driver, By.ID, self.username_id, 3)
        credentials = load_json('valid_credentials', 'resources/data.json')
        username_input.send_keys(credentials['username'])

    def set_valid_password(self):
        password_input = dynamic_wait(self.driver, By.ID, self.password_id, 3)
        credentials = load_json('valid_credentials', 'resources/data.json')
        password_input.send_keys(credentials['password'])

    def set_invalid_username(self):
        username_input = dynamic_wait(self.driver, By.ID, self.username_id, 3)
        credentials = load_json('invalid_credentials', 'resources/data.json')
        username_input.send_keys(credentials['username'])

    def set_invalid_password(self):
        password_input = dynamic_wait(self.driver, By.ID, self.password_id, 3)
        credentials = load_json('invalid_credentials', 'resources/data.json')
        password_input.send_keys(credentials['password'])

    def click_login(self):
        login_button = dynamic_wait(self.driver, By.ID, self.login_button_id, 3)
        login_button.click()

    def validate_error_message(self, error_message):
        actual_message = dynamic_wait(self.driver, By.CLASS_NAME, self.error_message_class, 3)
        actual_message = actual_message.text
        if error_message in actual_message:
            assert error_message in actual_message, "Assertion Passed: Got Error while Logging in"
        else:
            assert False, "Assertion Failed: Failed to retrieve error message"
