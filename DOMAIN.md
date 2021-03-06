# What does this website offer?
- A on-the-fly updated software designed for reading lovers
- Control over unique data that gets richer as more people contribute
- Users as contributors, adding value to maintain the site


# Main functionalities
- Visitors can sign up
- Users can log in, log out and delete their profile
- Users can freely edit their profile data: username, email and password
- Users can add their favorite books to a personal wish list, as well as remove them from it
- Users can visit the personal wish list of any other user
- Visitors can browse by categories or look for a specific title, but only registered and logged in users can comment or add (and remove) books from the wish list
- Every new comment must be given a rate, a title, and a body
- Once a comment is correctly submitted, it is showed onto the screen dynamically without the need to reload the entire page
- According to the average of the assessments, every book is given its corresponding rate computed as the average and updated every time a comment is added, deleted or updated
- A book cannot contain more than one comment coming from the same user

# Implementation
- We're using the New York Times API to get the list of the best sellers
- We're using the Google Books API through Ajax to get the images and price of books
- We have created a very simple internal REST API that allows real-time interaction of wished books and comments without refreshing the page (Ajax power!)

# Testing
- Website functionality is tested with Behave and Splinter in integration tests (features folder)
- Our internal API uses Django Rest Framework for development and testing (test.py file)

# Web 3.0
- This web supports markup RDFa on:
  - The main page
  - The category page
  - The book detail page (with comments and ratings)
  - The wish list page of users