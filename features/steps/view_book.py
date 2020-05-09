from behave import *
from datetime import date

use_step_matcher("parse")

@given('Exists a book titled "{title}" and isbn "{isbn}"')
def step_impl(context, title, isbn):
    from book_visualizer.models import Book
    #book = Book.objects.get(title=title)
    #assert book existeix

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
    book = Book("3647857463546", "How to stop Covid19", 'Author Example', date.today(), 'Publisher Example', 'Summary here')
    book.save()

@when('I introduce "{Covid19}" into the search bar and click')
def step_impl(context, Covid19): # Covid19 needed here?
    context.browser.visit(context.get_url('/book/3647857463546'))

@then('I\'m viewing the book whose title contains "{Covid19}"')
def step_impl(context, Covid19):
    books = context.browser.find_by_text(Covid19) 
    assert len(books) == 1
    assert Covid19 in books[0]

