Feature: Swag Labs

  Scenario: Login to Swag labs page
    Given open launch chrome browser
    When open swag labs homepage
    And Enter username "standard_user" and password "secret_sauce"
    And click on login button
    Then user must successfully login to the dashboard page

  Scenario: Login to Swag labs page with valid parameters
    Given In launch chrome browser
    When open swag labs homepage
    And Enter username "standard_user" and password "secret_sauce"
    And click on login button
    Then user must successfully login to the dashboard page

  Scenario: Login to Swag labs page with valid parameters
    Given In launch chrome browser
    When open swag labs homepage
    And Enter username "standard_user" and password "secret_sauce"
    And click on login button
    Then user must successfully login to the dashboard page