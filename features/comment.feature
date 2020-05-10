Feature: Commenting

    Background: I'm logged in
        Given I'm logged in with user "usernamex" and password "password"
        And Exists a book titled "Fortitude" and isbn "9781538733295"
        And Exists a user "username1" with password "password1"
        And Exists a user "username2" with password "password2"
        And Exists a user "username3" with password "password3"
        And "username1" has a comment on isbn "9781538733295" 
          | rating          | title          | comment                          |
          | 3               | Not bad        | It was too long but I liked it   |
        And "username2" has a comment on isbn "9781538733295" 
          | rating          | title          | comment                          |
          | 4               | Read it        | I found this book so interesting |
        And "username3" has a comment on isbn "9781538733295" 
          | rating          | title          | comment                          |
          | 5               | Fantastic book | Totally worth it                 |
    
    Scenario: Adding Comment Error
        When I try to register a review to the book with isbn "9781538733295"
        And I complete the application form without stars
          | title         | comment                         |
          | Sooo good     | I highly recommend this book    | 
        Then Complains that stars are required
        And There are 3 reviews 

    Scenario: Adding Comment
        When I try to register a review to the book with isbn "9781538733295"
        And I complete the application form
          | rating          | title         | comment                         |
          | 4               | Sooo good     | I highly recommend this book    |
        Then I'm viewing a reviews list containing my comment
          | rating          | title         | comment                         | author    |     
          | 4               | Sooo good     | I highly recommend this book    | username  |      
        And There are 4 reviews 

    Scenario: Removing Comment
        Given "usernamex" has a comment on isbn "9781538733295" 
          | rating          | title         | comment                         |
          | 4               | Sooo good     | I highly recommend this book    |
        When I delete my comment on isbn "9781538733295"
        Then I cannot see a comment on isbn "9781538733295" by "usernamex"
        And There are 3 reviews
        And I can see an Add Comment button
    
    Scenario: Editing Comment
        Given "usernamex" has a comment on isbn "9781538733295" 
          | rating          | title         | comment                         |
          | 4               | Sooo good     | I highly recommend this book    |
        When I try to edit my comment on isbn "9781538733295"                
        And I complete the application form
          | rating          | title         | comment                         |
          | 5               | Fabulous book | I highly recommend this book    |
        Then I'm viewing a reviews list containing my comment               
          | rating          | title         | comment                         | author     | 
          | 4               | Sooo good     | I highly recommend this book    | username   |
        And There are 4 reviews

    Scenario: Hidden Button
        Given "usernamex" has a comment on isbn "9781538733295" 
          | rating          | title         | comment                         |
          | 4               | Sooo good     | I highly recommend this book    |
        When I navigate to book with isbn "9781538733295"                   
        Then I cannot see an Add Comment button

    Scenario: Try to register a comment to a book but not logged in
        Given I'm not logged in
        When I navigate to book with isbn "9781538733295"
        And I try to register a review to the book with isbn "9781538733295"
        Then I am redirected to the login form
  