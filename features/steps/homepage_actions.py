from behave import *

use_step_matcher("parse")

@given(u'I\'m on the homepage')
def step_impl(context):
    context.browser.visit(context.get_url())

@given(u'I\'m on page {num:n}')
def step_impl(context, num):
    page = context.browser.find_by_xpath('/html/body/div[2]/div/div[2]/div/div[7]/nav/ul/li[2]/a').first
    print(page.html)
    assert f'{page.html}' == num

@when(u'I click on next')
def step_impl(context):
    pass

@when(u'I click on previous')
def step_impl(context):
    pass

@when(u'I click on category "{cat}"')
def step_impl(context):
    pass