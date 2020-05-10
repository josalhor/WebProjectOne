from behave import *
from django.utils import timezone
import time

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
    assert showed == expected

@given(u'"{username}" has a comment on isbn "{isbn}"')
def step_impl(context, username, isbn):
    from book_visualizer.models import Comment, Book
    from book_visualizer.models import User
    user = User.objects.get(username=username)
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
        context.browser.fill('title', row['title'])
        context.browser.fill('body', row['comment'])
        rate = 'star-' + row['rating']
        var = context.browser.find_by_xpath(f'//*[@id="rate required"]/a[@class="{rate}"]')
        var.click()
        context.browser.find_by_text('Submit').first.click()

@then('Complains that stars are required')
def step_impl(context):
    assert context.browser.is_text_present('Please, give a rate before submiting')

@when('I complete the application form without stars')
def step_impl(context):
    for row in context.table:
        context.browser.fill('title', row['title'])
        context.browser.fill('body', row['comment'])
        context.browser.find_by_text('Submit').first.click()

@then(u'I\'m viewing a reviews list containing my comment')
def step_impl(context):
    for row in context.table:
        user = row['author']
        id_comment = f'comment-{user}'
        context.browser.find_by_id(id_comment)

@when(u'I delete my comment on isbn "{isbn}"')
def step_impl(context, isbn):
    context.browser.visit(context.get_url(f'/book/{isbn}'))
    context.browser.find_by_xpath('//*[@title="Delete"]').click()
    time.sleep(0.2)
    context.browser.find_by_text('Sure').first.click()
    time.sleep(0.2)

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

