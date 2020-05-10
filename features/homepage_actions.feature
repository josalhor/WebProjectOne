Feature: Commenting

    Background: I'm logged in
        Given Exists a book titled "Fortitude2" and isbn "9781538733296"
        And Exists a book titled "Fortitude3" and isbn "9781538733297"
        And Exists a book titled "Fortitude4" and isbn "9781538733298"
        And Exists a book titled "Fortitude5" and isbn "9781538733299"
        And Exists a book titled "Fortitude6" and isbn "9781538733200"
        And Exists a book titled "Fortitude7" and isbn "9781538733201"
        And Exists a book titled "Fortitude8" and isbn "9781538733202"
        And Exists a book titled "Fortitude9" and isbn "9781538733203"
    
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
        Then I can see the book titled "title"
    
    