Feature: Commenting

    Background: I'm logged in
        Given I'm logged in with user "username" and password "password"
        And Exists a book titled "Fortitude" and isbn "9781538733295"
        And "username2" has a comment on isbn "9781538733295" 
        And "username3" has a comment on isbn "9781538733295" 
        And "username4" has a comment on isbn "9781538733295" 
        
    Scenario: Adding Comment
        When I try to register a review to the book with isbn "9781538733295"
        And I complete the application form
        | rating          | title         | comment                         |
        | 4               | Sooo good     | I highly recommend this book    |
        Then I'm viewing a reviews list containing my comment
        | rating          | title         | comment                         | author    |     
        | 4               | Sooo good     | I highly recommend this book    | username  |      
        And There are 6 reviews 

    Scenario: Removing Comment
        Given "username" has a comment on isbn "9781538733295" 
        | rating          | title         | comment                         |
        | 4               | Sooo good     | I highly recommend this book    |
        When I delete my comment on isbn "9781538733295"
        Then I cannot see a comment by "username"
        And There are 4 reviews
        And I can see an Add Comment button
    
    Scenario: Editing Comment
        Given "username" has a comment on isbn "9781538733295" 
        | rating          | title         | comment                         |
        | 4               | Sooo good     | I highly recommend this book    |
        When I try to edit my comment on isbn "9781538733295"               |
        And I complete the application form
        | rating          | title         | comment                         |
        | 5               | Fabulous book | I highly recommend this book    |
        Then I'm viewing a reviews list containing my comment               
        | rating          | title         | comment                         | author     | 
        | 4               | Sooo good     | I highly recommend this book    | username   |
        And There are 5 reviews

    Scenario: Hidden Button
        Given "username" has a comment on isbn "9781538733295" 
        | rating          | title         | comment                         |
        | 4               | Sooo good     | I highly recommend this book    |
        When I navigate to book with isbn "9781538733295"                   
        Then I cannot see an Add Comment button

    Scenario: Try to register a comment to a book but not logged in
        When I log out
        And I visit the book with isbn "9781538733295"
        And I try to register a review to the book with isbn "9781538733295"
        Then I am redirected to the login form

  