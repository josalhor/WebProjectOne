Feature: Commenting

    Background: I'm logged in
        Given I'm logged in with user "USER1" and password "USERPASSWORD1"
        And Exists a book titled "Fortitude" and isbn "9781538733295"

    Scenario: Adding Comment
        When I add a comment to isbn "9781538733295" with title "Great book" body "Totally recommended" and stars "4"
        Then I can see a comment on isbn "9781538733295" by "USER1" with title "Great book" body "Totally recommended" and stars "4"

    Scenario: Removing Comment
        Given "USER1" has a comment on isbn "9781538733295" with title "Great book" body "Totally recommended" and stars "4"
        When I delete my comment on isbn "9781538733295"
        Then I cannot see a comment on isbn "9781538733295" by "USER1"
    
    Scenario: Editing Comment
        Given "USER1" has a comment on isbn "9781538733295" with title "Great book" body "Totally recommended" and stars "4"
        When I edit my comment on isbn "9781538733295" with title "Fabulous book" body "Totally recommended" and stars "5"
        Then I can see a comment on isbn "9781538733295" by "USER1" with title "Fabulous book" body "Totally recommended" and stars "5"

    Scenario: Hidden Button
        Given "USER1" has a comment on isbn "9781538733295" with title "Great book" body "Totally recommended" and stars "4"
        When I navigate to book "9781538733295"
        Then I cannot see an Add Comment button