Feature: Swag Labs Login

  Scenario: Login to Swag labs page with valid parameters
    Given In launch chrome browser
    When open swag labs homepage
    And Enter username "standard_user" and password "secret_sauce"
    And click on login button
    Then user must successfully login to the dashboard page

  Scenario Outline: Login to Swag labs page with valid parameters
    Given In launch chrome browser
    When open swag labs homepage
    And Enter username "<Username>" and password "<Password>"
    And click on login button
    Then user must successfully login to the dashboard page

    Examples:
      | Username                | Password     |
      | standard_user           | secret_sauce |
      | problem_user            | secret_sauce |
      | performance_glitch_user | secret_sauce |
