@login @regression
Feature: Verify login flow

    @smoke @LG0001
    Scenario: Verify user login with valid data
        Given User on the homepage
        When  User click login button
        And   User enter correct registred email
        And   User enter correct registred password
        And   User click on sign in button
        Then  User successfuly login to website
        And   Take screenshot "success_login"

    @LG0002
    Scenario: Verify user login with invalid data
        Given User on the homepage
        When  User click login button
        And   User enter inccorect email
        And   User enter inccorect password
        And   User click on sign in button
        Then  User unsuccessfuly login to website
        And   Take screenshot "failed_login"



