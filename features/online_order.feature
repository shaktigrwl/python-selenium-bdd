Feature: Online Logging in to an Ecommerce Website and Ordering a product
  @Login
  Scenario: Logging with invalid credentials
    Given I am on the login page
    When I log in with invalid credentials
    Then I get "Sorry, this user has been locked out" message

  @Login
  Scenario: Adding a product to the cart
    Given I am on the login page
    When I log in with valid credentials
    And I validate I am on "Products" Page
    And I add "Sauce Labs Backpack" to the cart
    And I go to my shopping cart
    Then I should see "Sauce Labs Backpack" in the cart
    And I proceed to checkout
    And I fill in the first name as "Johnny" last name as "Depp" and zip code as "11024"
    Then I click continue to checkout overview page
    And I validate the product name "Sauce Labs Backpack" on checkout overview page
    And I click on the Finish CTA
    And I validate the "Thank you for your order!" on the checkout overview page