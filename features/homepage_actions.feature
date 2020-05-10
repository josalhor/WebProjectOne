Feature: Commenting

    Background: I'm logged in
    
    Scenario: Scrolling through next page
        Given I'm on the homepage
        And I'm on page 1
        When I click on next       
        Then I'm on page 2
    
    Scenario: Coming back previous page
        Given I'm on the homepage
        Given I'm on page 2
        When I click on previous      
        Then I'm on page 1
    
    Scenario: Book in category
        Given Exists a book category called "TestigCategory"
        And Exists a book with title "title" and isbn "1234"
        And Isbn "1234" belongs to the category called "TestigCategory"
        When I visit the category called "TestigCategory"
        Then I can see the book titled "title"
    
    