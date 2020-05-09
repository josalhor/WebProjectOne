from behave import *
from datetime import date

use_step_matcher("parse")

@given('Exists a book titled "{title}" and isbn "{isbn}"')
def step_impl(context, title, isbn):
    from book_visualizer.models import Book
    book = Book(isbn, title, 'Author Example', date.today(), 'Publisher Example', 'Summary here')
    book.save()

@when('Navigate to book "{isbn}"')
def step_impl(context, isbn):
    context.browser.visit(context.get_url(f'/book/{isbn}'))

@then('I\'m viewing the book "{title}" with isbn "{isbn}"')
def step_impl(context, title, isbn):
    assert context.browser.is_text_present(title)
    assert context.browser.is_text_present(isbn)

@given('Exists a book title containing "{Covid19}"')
def step_impl(context, Covid19):
    from book_visualizer.models import Book
