# Domain specific knowledge

What does this website offer?
    - A continually-updated software designed for reading lovers
    - Control over unique data that gets richer as more people contribute
    - Users as co-developers, adding value and contribuiting to maintain data

Main functionalities:
    - Users can log in and log out, just as visitors can sign up
    - Users can freely edit his profile data: username, email and password
    - Users can add their favorite books to a personal wish list, as well as they can remove books from it
    - Users can visit the personal wish list of any other user
    - 

We've made a few changes to the models of our application since we submitted the pre-assignment:
    - We've included the Category of books for best sellers: BestSellersListName (resembling the name of the NYT API)
    - We've included a Best Sellers model that represents the relationship (day, list_best_sellers) -> [books]


- We've included the Category of books for best sellers: BestSellersListName (resembling the name of the NYT API)
- We've included a Best Sellers model that represents the relationship (day, list_best_sellers) -> [books]


- Visitors can browse by categories or look for a specific title, but only registered and logged in users can comment or add (and remove) books from the wish list
- Every new comment must be given a rate and a title, apart from the comment itself
- Once a comment is correctly submited, it is showed onto the screen dynamically without the need to reload the entire page
- According to the average of the valorations, every book is given its corresponding rate computed as the average and updated every time a comment is added, delated or updated
- As mentioned above, comments can be updated or permanently delated. However, a book cannot contain more than one comment coming from the same user; every comment means a rate, and any user should be given greater weight than another
