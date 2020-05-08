Feature: Commenting

    Background: I'm logged in
        Given: I'm logged in with user "USER1" and password "USERPASSWORD1"
        And Exists a book titled "title" and isbn "1234"

    Scenario: Adding Comment
        When I add a comment to isbn "1234" with title "T1" body "B1" and stars "3"
        Then I can see a comment on isbn "1234" by "USER1" with title "T1" body "B1" and stars "3"

    Scenario: Removing Comment
        Given "USER1" has a comment on isbn "1234" with title "T1" body "B1" and stars "3"
        When I delete my comment on isbn "1234"
        Then I cannot see a comment on isbn "1234" by "USER1"
    
    Scenario: Editing Comment
        Given "USER1" has a comment on isbn "1234" with title "T1" body "B1" and stars "3"
        When I edit my comment on isbn "1234" with title "T2" body "B2" and stars "5"
        Then I can see a comment on isbn "1234" by "USER1" with title "T2" body "B2" and stars "5"

    Scenario: Hidden Button
        Given "USER1" has a comment on isbn "1234" with title "T1" body "B1" and stars "3"
        When I navigate to book "1234"
        Then I cannot see a "Add Comment" button