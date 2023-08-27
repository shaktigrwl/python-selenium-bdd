from behave import *


@given('I am on the login page')
def step_impl(context):
    context.loginPage.get_homepage()


@when('I log in with valid credentials')
def step_impl(context):
    context.loginPage.set_valid_username()
    context.loginPage.set_valid_password()
    context.loginPage.click_login()


@when('I log in with invalid credentials')
def step_impl(context):
    context.loginPage.set_invalid_username()
    context.loginPage.set_invalid_password()
    context.loginPage.click_login()


@when('I validate I am on "{page_title}" Page')
def step_impl(context, page_title):
    context.productPage.validate_title(page_title)


@when('I add "{product_name}" to the cart')
def step_impl(context, product_name):
    context.productPage.add_product_to_cart(product_name)


@when('I go to my shopping cart')
def step_impl(context):
    context.productPage.open_shopping_cart()

@then('I get "{error}" message')
def step_impl(context, error):
    context.loginPage.validate_error_message(error)


@then('I should see "{product_name}" in the cart')
def step_impl(context, product_name):
    context.cartPage.validate_product_in_cart(product_name)


@then('I proceed to checkout')
def step_impl(context):
    context.cartPage.continue_to_checkout()


@then('I fill in the first name as "{first_name}" last name as "{last_name}" and zip code as "{zipcode}"')
def step_impl(context, first_name, last_name, zipcode):
    context.checkoutPage.set_firstname(first_name)
    context.checkoutPage.set_lastname(last_name)
    context.checkoutPage.set_zipcode(zipcode)


@then('I click continue to checkout overview page')
def step_impl(context):
    context.checkoutPage.click_continue()


@then('I validate the product name "{product_name}" on checkout overview page')
def step_impl(context, product_name):
    context.cartPage.validate_product_in_cart(product_name)


@then('I click on the Finish CTA')
def step_impl(context):
    context.checkoutOverviewPage.click_finish_cta()


@then('I validate the "{message}" on the checkout overview page')
def step_impl(context, message):
    context.orderCompletion.validate_message(message)
