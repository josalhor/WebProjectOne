Feature: Contact tool 

Scenario: a visitor can send a message successfully
    When I click Contact button and send a message with email "contact@cpntact.com" and subject "proposal" and message "It would be useful if users could sell and buy books too"
    Then I see a the message "Your message has been successfully submitted. Thank you!"

Scenario: warn wrong email 
    When I click Contact button and send a message with email "contact" and subject "proposal" and message "It would be useful if users could sell and buy books too"
    Then I see a the message "Enter a valid email address."