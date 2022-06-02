# -- FILE: features/example.feature
Feature: Login Feature

  Scenario: Success test for login
    Given I navigate to login page
    And I enter valid <username> and <password>

    When I click on Submit button
    Then login is successful
    
    Examples:
    | username  | password   |
    | 4a8g0105  | a8787      |
    | stust     | university |
    | city      | tainan     |


  