Feature: User can login and use authentication

    Scenario: User can access login page
        When I go to "login" URL
        Then I see "Login"

    Scenario: User can login
        Given a user exists with username "UserTest" and password "testpass12345" 
        And I go to "login" URL
        And I fill in "username" with "UserTest"
        And I fill in "password" with "testpass12345"
        And I press "Login"
        Then I should see "Hi TestUser"

    Scenario: User can register a new account
        Given I go to the "sign up" URL
        And I fill "username" with "test"
        And I fill "email" with "test@test.com"
        And I fill "password1" with "testpass12345"
        And I fill "password2" with "testpass12345" 
        And I press "Sign Up" 
        Then the browser view should be "login"