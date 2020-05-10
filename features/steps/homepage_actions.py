from behave import *

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

@when(u'I click on next')
def step_impl(context):
    page = context.browser.find_by_xpath('//ul/li[3]/a').first
    print('NEXT:', page.htm.text)
    page.click()
    

@when(u'I click on previous')
def step_impl(context):
    page = context.browser.find_by_xpath('//ul/li[1]/a').first.click()
    print('PREVIOUS:', page.htm.text)
    page.click()

@when(u'I click on category "{cat}"')
def step_impl(context):
    pass