from behave import *
from datetime import date
from bs4 import BeautifulSoup
from functools import reduce
import operator
import os

use_step_matcher("parse")

@given(u'I visit the book with isbn "{isbn}"')
def step_impl(context, isbn):
    context.browser.visit(context.get_url(f'/book/{isbn}'))

@when(u'I try to register a review to the book with isbn "{isbn}"')
def step_impl(context, isbn):
    context.browser.find_by_id('addCommentButton').first.click

@then(u'I am redirected to the login form') 
def step_impl(context):
    assert context.browser.url.startswith(context.get_url('/login/'))
    
@then(u'There are {count:n} reviews')
def step_impl(context, count):
    reviews = context.browser.find_by_css('span#num_comments')
    assert reviews.value == '0 reviews'

@when(u'I complete the application form')
def step_impl(context):
    form = context.browser.find_by_css('form#comment_form.was-validated').first
    for row in context.table:
        rate = 'star-' + row['rating']
        form.find_by_class_name(rate).first.click()
        context.browser.fill('title', row['title'])
        context.browser.fill('body', row['comment'])

@then(u'I\'m viewing a reviews list containing my comment')
def step_impl(context):
    for row in context.table:
        comment = context.browser.find_by_id(row['made_by']).first
        content = BeautifulSoup(comment, 'html.parser')
        print(content.prettify())
        assert content.is_text_present(row['title'])
        assert content.browser.is_text_present(row['comment'])
        assert len(content.find_all('span')) == row['rating']

@given(u'"{username}" has a comment on isbn "{isbn}"')
def step_impl(context, username, isbn):
    from book_visualizer.models import Comment
    print("hereee")
    print(context.table)
    for row in context.table:
        comment = Comment(row['title'], row['comment'], row['rating'], date.today(), username, isbn)
        comment.save()

@when(u'I delete my comment on isbn "{isbn}"')
def step_impl(context, isbn):
    context.browser.visit(context.get_url(f'/book/{isbn}'))
    context.browser.find_by_class_name('fa fa-trash').first.click()

@then(u'I cannot see a comment on isbn "{isbn}" by "{username}"')
def step_impl(context, isbn, username):
    assert len(context.browser.find_by_id(username)) == 0

@then(u'I cannot see an Add Comment button')
def step_impl(context):
    assert len(context.browser.find_by_id('addCommentButton')) == 0

@then(u'I can see an Add Comment button')
def step_impl(context):
    assert len(context.browser.find_by_id('addCommentButton')) == 1

@when(u'I try to edit my comment on isbn "{isbn}"')
def step_impl(context, isbn):
    context.browser.visit(context.get_url(f'/book/{isbn}'))
    context.browser.find_by_class_name('float-right btn btn-success btn-sm rounded-5 mr-1').first.click()

@when(u'I navigate to book with isbn "{isbn}"') 
def step_impl(context, isbn):
    context.browser.visit(context.get_url(f'/book/{isbn}'))
    context.browser.find_by_class_name('fa fa-trash').first.click()

# Functions that may be used in a general testing context
# def createUser(username, password):
#    from django.contrib.auth.models import User
#   email = "%s@gmail.com" % username
#    return User(username, password, email)

# def createBook(isbn='1234', title='Title x'):
#   from book_visualizer.models import Book
#   return Book(isbn, title, 'Author Example', date.today(), 'Publisher Example', 'Summary here')

