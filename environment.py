from selenium import webdriver
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.order_completion import OrderCompletion


def before_scenario(context, scenario):
    tag = str(scenario.tags)
    print(tag)
    # Get browser from command-line or use 'chrome' by default
    browser = context.config.userdata.get("browser", "chrome")

    if browser.lower() == "chrome":
        context.driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        context.driver = webdriver.Firefox()
    elif browser.lower() == "edge":
        context.driver = webdriver.Edge()
    elif browser.lower() == "safari":
        context.driver = webdriver.Safari()
    else:
        raise Exception(f"Unsupported browser: {browser}")
    basepage = BasePage(context.driver)
    context.loginPage = LoginPage(basepage)
    context.productPage = ProductPage(basepage)
    context.cartPage = CartPage(basepage)
    context.checkoutPage = CheckoutPage(basepage)
    context.checkoutOverviewPage = CheckoutOverviewPage(basepage)
    context.orderCompletion = OrderCompletion(basepage)
    context.step_id = 1


def after_step(context, step):
    print("Executing Step: ", step)
    attach(context.driver.get_screenshot_as_png(), name=context.step_id, attachment_type=AttachmentType.PNG)
    context.step_id = context.step_id + 1


def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        print("After scenario", scenario)
        context.driver.quit()
