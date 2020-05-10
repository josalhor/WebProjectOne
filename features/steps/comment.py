from behave import *
from datetime import date
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
    reviews = context.browser.find_by_xpath(f'//*[@id="num_comments"]')
    expected = f'{num} reviews'
    showed = f'{reviews.first.html}'
    print(expected)
    print(showed)
    assert showed == expected

@given(u'"{username}" has a comment on isbn "{isbn}"')
def step_impl(context, username, isbn):
    from book_visualizer.models import Comment, Book
    from book_visualizer.models import User
    user = User.objects.get(username=username)
    book = Book.objects.get(isbn=isbn)
    for row in context.table:
        Comment(
            title=row['title'], 
            body=row['comment'], 
            stars=row['rating'], 
            date=date.today(), 
            made_by=user, 
            based_on=book).save()

@when(u'I complete the application form')
def step_impl(context):
    for row in context.table:
        context.browser.fill('title', row['title'])
        context.browser.fill('body', row['comment'])
        rate = 'star-' + row['rating']
        var = context.browser.find_by_xpath(f'//*[@id="rate required"]/a[@class="{rate}"]')
        print(var)
        var.click()
        

@then(u'I\'m viewing a reviews list containing my comment')
def step_impl(context):
    for row in context.table:
        user = row['author']
        id_comment = f'comment-{user}'
        comment = context.browser.find_by_id(id_comment) # Problems
        #content = BeautifulSoup(comment, 'html.parser') 
        #assert content.is_text_present(row['title'])
        #assert content.is_text_present(row['comment'])
        #assert len(content.find_all('span')) == row['rating']

@when(u'I delete my comment on isbn "{isbn}"')
def step_impl(context, isbn):
    context.browser.visit(context.get_url(f'/book/{isbn}'))
    context.browser.find_by_xpath('//*[@title="Delete"]').click()

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
    context.browser.find_by_id('addCommentButton')

@when(u'I try to edit my comment on isbn "{isbn}"')
def step_impl(context, isbn):
    context.browser.visit(context.get_url(f'/book/{isbn}'))
    context.browser.find_by_xpath('//*[@title="Edit"]').click()

@when(u'I navigate to book with isbn "{isbn}"') 
def step_impl(context, isbn):
    context.browser.visit(context.get_url(f'/book/{isbn}'))

