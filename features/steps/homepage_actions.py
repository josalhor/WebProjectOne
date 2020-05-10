from behave import *
from book_visualizer.models import BestSellersListName, BestSellers, Book
from django.utils import timezone

use_step_matcher("parse")

@given(u'I\'m on the homepage')
def step_impl(context):
    context.browser.visit(context.get_url())

@given(u'I\'m on page {num:n}')
def step_impl(context, num):
    page = context.browser.find_by_xpath('//ul/li[2]/a')
    expected = f'{page.html}'
    showed = f'{num}'
    print('Expected:', expected)
    print('Showed:', showed)
    assert expected == showed

@given(u'Exists a book category called "{category}"')
def step_impl(context, category):
    category = BestSellersListName(999, category, category, category)
    category.save()

@given(u'Isbn "{isbn}" belongs to the category called "{category}"')
def step_impl(context, isbn, category):
    category = BestSellersListName.objects.all().filter(name=category).first()
    best_sellers_list = BestSellers(999, timezone.now(), category)
    book = Book.objects.all().filter(isbn=isbn).first()
    best_sellers_list.books.add(book)
    best_sellers_list.save()

@when(u'I click on next')
def step_impl(context):
    page = context.browser.find_by_xpath('//ul/li[3]/a').first
    print('NEXT:', page.html.text)
    page.click()
    

@when(u'I click on previous')
def step_impl(context):
    page = context.browser.find_by_xpath('//ul/li[1]/a').first.click()
    print('PREVIOUS:', page.html.text)
    page.click()

@when(u'I click on category "{cat}"')
def step_impl(context):
    pass

@when(u'I click I click the logo')
def step_impl(context):
    context.browser.find_by_id('image-logo').click()

@then('I\'m on the homepage')
def step_impl(context):
    pass
    #print('URL', context.browser.url)
    #assert 