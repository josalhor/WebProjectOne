from behave import *

use_step_matcher("parse")

@given('Exists a book titled {title} and isbn {isbn}')
def step_impl(context, title, isbn):
    from book_visualizer.models import Book
    #book = Book.objects.get(title=title)
    #assert book existeix
    

@when('Navigate to book {isbn}')
def step_impl(context, isbn):
    context.browser.visit(context.get_url('/book/{isbn}'))

@then('I\'m viewing book details')
def step_impl(context, title, isbn):
    assert context.browser.is_text_present('GOOP CLEAN BEAUTY')
    assert context.browser.is_text_present('9781455541553')