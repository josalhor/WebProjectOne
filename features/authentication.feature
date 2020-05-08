Feature: User can login and use authentication

    Scenario: Registered user can login
        Given Exists a user "username" with password "testpass123"
        When I login as user "username" with password "testpass123"
        Then I should be redirected to account url

    Scenario: Not registerd username cannot login
        Given Not registered username "username"
        When I login as user "username" with password "password"
        Then I see a message error

    Scenario: Registerd username types wrong password and cannot login
        Given Exists a user "username" with password "password"
        When I login as user "username" with password "wrongpassword"
        Then I see a message error

    Scenario: Not registerd username can sign up
        Given Not registered username "test"
        When I go to signup url
        And I signup as user "test" with password "userpass123"
        Then I am redirected to the login form

