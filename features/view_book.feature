Feature: view details of a book
    In order to know about a book   
    As a visitor or user
    I want to view book details and its reviews

    Scenario: view details of a book
      Given Exists a book titled "GOOP CLEAN BEAUTY" and isbn "9781455541553"
      When Navigate to book "9781455541553"
      Then I'm viewing the book "GOOP CLEAN BEAUTY" with isbn "9781455541553"

    Scenario: view reviews of a book
      