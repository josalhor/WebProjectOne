Feature: Account management
    Scenario: Account Creation
        When I sign up a user "USER1" with password "USERPASSWORD1"
        Then I can login with user "USER1" with password "USERPASSWORD1"

    Scenario: Account Deletion
        Given I'm logged in with user "USER1" and password "USERPASSWORD1"
        When I delete the user
        Then I cannot login with user "USER1" and password "USERPASSWORD1"

    Scenario: User Editing
        Given I'm logged in with user "USER1" and password "USERPASSWORD1"
        When I change my user to "USER2"
        Then I should see "Hi USER2" in the profile
    
    Scenario: Email Editing
        Given I'm logged in with user "USER1" and password "USERPASSWORD1"
        When I change my email to "cool@email.com"
        Then I should see "E-mail: cool@email.com" in  the profile

    Scenario: Password Change
        Given I'm logged in with user "USER1" and password "USERPASSWORD1"
        When I change my password to "USERPASSWORD1"
        Then I should be able to log out
        And I can login with user "USER1" with password "USERPASSWORD2"
