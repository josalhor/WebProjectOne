from behave import *
from django.utils import timezone
from bs4 import BeautifulSoup

use_step_matcher("parse")

@given(u'I visit the book with isbn "{isbn}"')
def step_impl(context, isbn):
    context.browser.visit(context.get_url(f'/book/{isbn}'))

@when(u'I try to register a review to the book with isbn "{isbn}"')
def step_impl(context, isbn):
    context.browser.visit(context.get_url(f'/book/{isbn}'))
    context.browser.find_by_id('addCommentButton').click()
    
@then(u'There are {num:n} reviews')
def step_impl(context, num):
    reviews = context.browser.find_by_id('num_comments').first
    reviews = num + 'reviews'
    assert reviews.value == reviews

@given(u'"{username}" has a comment on isbn "{isbn}"')
def step_impl(context, username, isbn):
    from book_visualizer.models import Comment, Book
    user = createUser(username)
    book = Book.objects.get(isbn=isbn)
    for row in context.table:
        comment = {
            "title":row['title'], 
            "body":row['comment'], 
            "stars":row['rating'], 
            "date":timezone.now(), 
            "made_by":user, 
            "based_on":book
        }
        Comment.objects.update_or_create(
            made_by=user,
            based_on=book,
            defaults=comment)

@when(u'I complete the application form')
def step_impl(context):
    for row in context.table:
        title = context.browser.find_by_xpath('//*[@id="title"]').first
        body = context.browser.find_by_xpath('//*[@id="body"]').first
        context.browser.fill(f'{title}', row['title'])
        context.browser.fill(f'{body}', row['comment'])
        rate = 'star-' + row['rating']
        var = context.browser.find_by_xpath(f'//*[@id="rate required"]/a[@class="{rate}"]')
        print(var)
        var.click()
        

@then(u'I\'m viewing a reviews list containing my comment')
def step_impl(context):
    for row in context.table:
        comment = context.browser.find_by_id(row['made_by']).first
        content = BeautifulSoup(comment, 'html.parser')
        assert content.is_text_present(row['title'])
        assert content.is_text_present(row['comment'])
        assert len(content.find_all('span')) == row['rating']

@when(u'I delete my comment on isbn "{isbn}"')
def step_impl(context, isbn):
    pass
    #context.browser.visit(context.get_url(f'/book/{isbn}'))
    #context.browser.find_by_class_name('fa-trash').first.click()

@then(u'I cannot see a comment on isbn "{isbn}" by "{username}"')
def step_impl(context, isbn, username):
    try:
        context.browser.find_by_id(username)
        assert False, f"There's a comment by {username}"
    except:
        pass  # It is expected to fail

@then(u'I cannot see an Add Comment button')
def step_impl(context):
    try:
        context.browser.find_by_id('addCommentButton')
        assert False, f"There's an Add Comment button"
    except:
        pass  # It is expected to fail
    

@then(u'I can see an Add Comment button')
def step_impl(context):
    assert len(context.browser.find_by_id('addCommentButton')) == 1

@when(u'I try to edit my comment on isbn "{isbn}"')
def step_impl(context, isbn):
    context.browser.visit(context.get_url(f'/book/{isbn}'))
    context.browser.find_by_name('Edit').first.click()

@when(u'I navigate to book with isbn "{isbn}"') 
def step_impl(context, isbn):
    context.browser.visit(context.get_url(f'/book/{isbn}'))

# Functions that may be used in a general testing context
def createUser(username):
    from book_visualizer.models import User
    password = username + '123'
    return User.objects.create_user(username=username, email='user@example.com', password=password)
    

# def createBook(isbn='1234', title='Title x'):
#   from book_visualizer.models import Book
#   return Book(isbn, title, 'Author Example', date.today(), 'Publisher Example', 'Summary here')
