Feature: User can edit his profile
    
    Scenario: Account Deletion
        Given I'm logged in with user "USER1" and password "USERPASSWORD1"
        When I delete my user account
        Then I cannot login with user "USER1" and password "USERPASSWORD1"

    Scenario: User Editing
        Given Exists a user "USER1" with password "USERPASSWORD1"
        When I login as user "USER1" with password "USERPASSWORD1"
        And I change my user to "USER2"
        Then I should see Hi "USER2" in the profile
    
    Scenario: Email Editing
        Given Exists a user "USER1" with password "USERPASSWORD1"
        When I login as user "USER1" with password "USERPASSWORD1"
        And I change my email to "cool@email.com"
        Then I should see E-mail: "cool@email.com" in  the profile

    Scenario: Password Change
        Given Exists a user "USER1" with password "USERPASSWORD1"
        When I login as user "USER1" with password "USERPASSWORD1"
        And I change my password "USERPASSWORD1" to "USERPASSWORD2"
        Then I should be able to log out
        And I can login as user "USER1" with password "USERPASSWORD2"
