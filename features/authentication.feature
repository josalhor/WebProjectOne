Feature: User can login and use authentication

    Scenario: User can login
        Given Exists a user "username" with password "password"
        When I login as user "username" with password "password"
        Then I should see "Hi username"
