Feature: User can login and use authentication

    Scenario: Registered user can login
        Given Exists a user "username" with password "testpass123"
        When I login as user "username" with password "testpass123"
        Then I should see Hi "username" in the profile

    Scenario: Not registerd username cannot login
        When I login as user "inexistent" with password "password"
        Then I cannot login

    Scenario: Wrong typo, registered user cannot login
        Given Exists a user "username" with password "password"
        When I login as user "username" with password "wrongpassword"
        Then I cannot login

    Scenario: Account creation
       When I signup as user "username" with password "testpass123"
        Then I am redirected to the login form
        And I can login as user "username" with password "testpass123"
    
    Scenario:
        Given Exists a book titled "Fortitude" and isbn "9781538733295"
        And I'm not logged in
        When I navigate to book "9781455541553"
        And Click Add Comment
        Then I'm in the login page
