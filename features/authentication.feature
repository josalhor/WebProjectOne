Feature: User can login and use authentication

    Scenario: Registered user can login
        Given Exists a user "username" with password "testpass123"
        When I login as user "username" with password "testpass123"
        Then I should see Hi "username" in the profile

    Scenario: Not registerd username cannot login
        When I login as user "inexistent" with password "password"
        Then I see a message error

    Scenario: Wrong typo, registered user cannot login
        Given Exists a user "username" with password "password"
        When I login as user "username" with password "wrongpassword"
        Then I see a message error

    Scenario: Account creation
       When I signup as user "username" with password "testpass123"
        Then I am redirected to the login form
        And I can login as user "username" with password "testpass123"

