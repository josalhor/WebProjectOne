from behave import *
from book_visualizer.models import BestSellersListName, BestSellers, Book
from django.utils import timezone

use_step_matcher("parse")

@given(u'I\'m on the homepage')
def step_impl(context):
    context.browser.visit(context.get_url())

@given(u'I\'m on page {num:n}')
def step_impl(context, num):
    page = context.browser.find_by_xpath('/html/body/div[2]/div/div[2]/div/div[7]/nav/ul/li[2]/a').first
    print(page.html)
    assert f'{page.html}' == num

@given(u'Exists a book category called "{category}"')
def step_impl(context, category):
    category = BestSellersListName(999, category, category, category)
    category.save()

@given(u'Isbn "1234" belongs to the category called "TestigCategory"')
def step_impl(context, isbn, category):
    category = BestSellersListName.objects.all().filter(name=category).first()
    best_sellers_list = BestSellers(999, timezone.now(), category)
    book = Book.objects.all().filter(isbn=isbn).first()
    best_sellers_list.books.add(book)

@when(u'I click on next')
def step_impl(context):
    pass

@when(u'I click on previous')
def step_impl(context):
    pass

@when(u'I click on category "{cat}"')
def step_impl(context):
    pass