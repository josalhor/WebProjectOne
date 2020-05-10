from behave import *

use_step_matcher("parse")

@given(u'I\'m on the homepage')
def step_impl(context):
    context.browser.visit(context.get_url())

@given(u'I\'m on page {num:n}')
def step_impl(context, num):
    assert context.browser.find_by_xpath('//a[@href="#"]').first == num

@when(u'I click on next')
def step_impl(context):
    pass

@when(u'I click on previous')
def step_impl(context):
    pass

@when(u'I click on category "{cat}"')
def step_impl(context):
    pass