Feature: Swag labs logo
  Scenario: Logo presence on Swag labs home page
    Given launch chrome browser
    When open swag labs homepage
    Then verify that the logo present on page
    And close the browser

