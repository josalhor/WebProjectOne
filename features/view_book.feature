Feature: view details of a book
    In order to know about a book   
    As a visitor or user
    I want to view book details and its reviews

   Scenario: view details of a book
      Given Exists a book titled "GOOP CLEAN BEAUTY" and isbn "9781455541553"
      When I navigate to book "9781455541553"
      Then I'm viewing the book "GOOP CLEAN BEAUTY" with isbn "9781455541553"

    Scenario: Look for a book
      Given Exists a book titled "How to stop Covid19" and isbn "3647857463546"
      And Exists a book titled "All about Covid19" and isbn "1247845466548"
      When  I introduce "Covid19" into the search bar and click 
      Then I can see a book titled "How to stop Covid19"
      And I can see a book titled "All about Covid19"

      
