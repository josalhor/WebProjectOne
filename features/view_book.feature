Feature: view details of a book
    In order to know about a book   
    As a visitor or user
    I want to view book details and its reviews

    Scenario: view details of a book
      Given Exists a book titled "title" and isbn "isbn"
      When  I click the book "title"
      Then I'm viewing book details
      | isbn            |  title     |
      | 9781455541553   |    GOOP CLEAN BEAUTY     |

    Scenario: view reviews of a book
      