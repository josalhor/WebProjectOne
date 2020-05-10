# Domain specific knowledge

We've made a few changes to the models of our application since we submitted the pre-assignment:

- We've included the Category of books for best sellers: BestSellersListName (resembling the name of the NYT API)
- We've included a Best Sellers model that represents the relationship (day, list_best_sellers) -> [books]


- Visitors can browse by categories or look for a specific title, but only registered and logged in users can comment or add (and remove) books from the wish list
- Every new comment must be given a rate and a title, apart from the comment itself
- Once a comment is correctly submited, it is showed onto the screen dynamically without the need to reload the entire page
- According to the average of the valorations, every book is given its corresponding rate computed as the average and updated every time a comment is added, delated or updated
- As mentioned above, comments can be updated or permanently delated. However, a book cannot contain more than one comment coming from the same user; every comment means a rate, and any user should be given greater weight than another
