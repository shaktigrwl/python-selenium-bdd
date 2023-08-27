from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def dynamic_wait(driver, by, value, timeout=10):
    """
        Wait for an element to be present in the DOM and visible using dynamic conditions.

        This method utilizes the WebDriverWait and expected_conditions modules from the Selenium library
        to wait for an element to be present and visible on the web page.

        :param driver: The WebDriver instance to use for waiting.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver

        :param by: The type of locator strategy to use (e.g., By.ID, By.XPATH, etc.).
        :type by: selenium.webdriver.common.by.By

        :param value: The value of the locator (e.g., ID, XPath expression, etc.).
        :type value: str

        :param timeout: The maximum amount of time (in seconds) to wait for the element to be present and visible.
                        Defaults to 10 seconds.
        :type timeout: int

        :return: The WebElement once it is located and visible.
        :rtype: selenium.webdriver.remote.webelement.WebElement

        :raises TimeoutException: If the element is not located and visible within the specified timeout.
        """
    return WebDriverWait(driver, timeout).until(ec.presence_of_element_located((by, value)))

def dynamic_wait_for_elements(driver, by, value, timeout=10):
    """
    Wait dynamically for a collection of web elements to be present on the page.

    This function waits for a specified amount of time for a collection of web elements
    matching the provided locator (by and value) to become present on the page.

    Args:
        driver (WebDriver): The WebDriver instance to use for interacting with the browser.
        by (str): The type of locator strategy to use, such as 'id', 'name', 'class_name', etc.
        value (str): The value of the locator to identify the elements by.
        timeout (int, optional): The maximum amount of time (in seconds) to wait for the elements.
            Defaults to 10 seconds.

    Returns:
        list of WebElement: A list containing the located web elements once they are present on the page.

    Raises:
        TimeoutException: If the specified elements are not present within the given timeout.

    Example:
        driver = webdriver.Chrome()
        elements = dynamic_wait_for_elements(driver, "class_name", "my-element", timeout=20)
        for element in elements:
            print(element.text)

    Note:
        Make sure to import WebDriverWait and expected_conditions as follows:
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as ec
    """
    return WebDriverWait(driver, timeout).until(ec.presence_of_all_elements_located((by, value)))
