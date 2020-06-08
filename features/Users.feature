Feature: Admin user

  Scenario: Add new user with valid data
    When I specify "{random_name}" as user name
    And I specify "{random_email}" as user email
    And I specify "{random_phone}" as user phone number
    And click "Save" button
