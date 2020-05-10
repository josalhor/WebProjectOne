Feature: Commenting

    Background: I'm logged in
        Given There are some registered books 
        | title       | isbn              | 
        | Fortitude2  | 9781538733296     |
        | Fortitude3  | 9781538733297     |
        | Fortitude4  | 9781538733298     |
        | Fortitude5  | 9781538733299     |
        | Fortitude6  | 9781538733200     |
        | Fortitude7  | 9781538733201     |
        | Fortitude8  | 9781538733202     |
        | Fortitude9  | 9781538733203     |
    
    Scenario: Scrolling through next page
        Given I'm on the homepage
        And I'm on page 1
        When I click on next
        Then I'm on page 2
    
    Scenario: Coming back previous page
        Given I'm on the homepage
        And I navigate to page 2
        When I click on previous      
        Then I'm on page 1
    
    Scenario: Click Logo
        Given I'm on the homepage
        When I click on next
        And I click on the logo
        Then I'm on the homepage
    
    Scenario: Book in category
        Given Exists a book category called "TestigCategory"
        And Isbn "9781538733297" belongs to the category called "TestigCategory"
        When I visit the category called "TestigCategory"
        Then I can see a book titled "Fortitude3"
    
    