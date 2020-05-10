from behave import *
from django.utils import timezone

use_step_matcher("parse")

@given(u'Exists a book titled "{title}" and isbn "{isbn}"')
def step_impl(context, title, isbn):
    create_book(context, title, isbn)

@given(u'There are some registered books')
def step_impl(context):
    for row in context.table:
        create_book(context, row['title'], row['isbn'])

def create_book(context, title, isbn):
    from book_visualizer.models import Book
    book = Book(isbn, title, 'Author Example', timezone.now(), 'Publisher Example', 'Summary here')
    book.save()

@when(u'I navigate to book "{isbn}"')
def step_impl(context, isbn):
    context.browser.visit(context.get_url(f'/book/{isbn}'))

@when(u'I introduce "{key_word}" into the search bar and click')
def step_impl(context, key_word): 
    context.browser.visit(context.get_url(f'/search?n={key_word}'))

@then(u'I\'m viewing the book "{title}" with isbn "{isbn}"')
def step_impl(context, title, isbn):
    assert context.browser.is_text_present(title)
    assert context.browser.is_text_present(isbn)

@then('I can see a book titled "{title}"')
def step_impl(context, title):
    assert context.browser.is_text_present(f'{title}')
