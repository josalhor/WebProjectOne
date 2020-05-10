Feature: A registered user can manage his personal wish list and consult other users whishes lists

    Background: I'm registered and I wish a book
        Given I'm logged in with user "USER1" and password "USERPASSWORD1"
        And Exists a book titled "Fortitude" and isbn "9781538733295"
        And Exists a book titled "Secret garden" and isbn "9781780671062"
        And This user wishes the book with isbn "9781538733295"

    Scenario: User can remove a book from his wish list
        When I navigate to book "9781538733295"
        Then I can click the button "Remove from my wish list"
        And I can see the button "ADD TO MY WISH LIST" on the page of book "9781538733295"

    Scenario: User can add a book on his wish list
        When I navigate to book "9781780671062"
        Then I can click the button "Add to my wish list"
        And I can see the button "REMOVE FROM MY WISH LIST" on the page of book "9781780671062"

    Scenario: User can consult his wish list
        When I click the button See wish List on my profile "USER1"
        Then The book titled "Fortitude" appears on wish list

    Scenario: User can consult his wish list and remove a book
        When I click the button See wish List on my profile "USER1"
        And I remove the book "9781538733295" from my wish list
        Then I can see the button "ADD TO MY WISH LIST" on the page of book "9781538733295"

    Scenario: User consults de wish list of his friend
        Given I'm logged in with user "USER2" and password "USERPASSWORD2"
        When I visit my friend "USER1" wish list
        Then The book titled "Fortitude" appears on wish list
    
    Scenario: Try to wish an item but not logged in
        Given I'm not logged in
        When I navigate to book with isbn "9781538733295"
        And I try to wish the book
        Then I am redirected to the login form