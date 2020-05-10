from behave import *
from book_visualizer.models import BestSellersListName, BestSellers, Book
from django.utils import timezone

use_step_matcher("parse")

@given(u'I\'m on the homepage')
def step_impl(context):
    context.browser.visit(context.get_url())

@given(u'I\'m on page {num:n}')
def step_impl(context, num):
    current_page(context, num)

@then(u'I\'m on page {num:n}')
def step_impl(context, num):
    current_page(context, num)

def current_page(context, num):
    page = context.browser.find_by_xpath('//ul/li[2]/a')
    expected = f'{num}'
    showed = f'{page.html}'
    assert expected == showed

@given(u'I navigate to page {num:n}')
def step_impl(context, num):
    context.browser.visit(context.get_url(f'/?page={num}'))
    
@given(u'Exists a book category called "{category}"')
def step_impl(context, category):
    category = BestSellersListName(category, category, category)
    category.save()

@given(u'Isbn "{isbn}" belongs to the category called "{category}"')
def step_impl(context, isbn, category):
    category = BestSellersListName.objects.all().filter(name=category).first()
    best_sellers_list = BestSellers(999, timezone.now(), category)
    book = Book.objects.all().filter(isbn=isbn).first()
    best_sellers_list.save()
    best_sellers_list.books.add(book)

@when(u'I click on next')
def step_impl(context):
    page = context.browser.find_by_xpath('//ul/li[3]').first
    page.click()

@when(u'I click on previous')
def step_impl(context):
    page = context.browser.find_by_xpath('//ul/li[1]').first
    page.click()

@when(u'I visit the category called "{category}"')
def step_impl(context, category):
    context.browser.visit(context.get_url(f'/category/{category}'))

@when(u'I click on the logo')
def step_impl(context):
    context.browser.find_by_id('image-logo').click()

@then('I\'m on the homepage')
def step_impl(context):
    assert not 'page' in str(context.browser.url)