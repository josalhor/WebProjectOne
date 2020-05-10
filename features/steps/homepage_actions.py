from behave import *

use_step_matcher("parse")

@given(u'I\'m on the homepage')
def step_impl(context):
    context.browser.visit(context.get_url())

@given(u'I\'m on page {num:n}')
def step_impl(context, num):
    elem = context.browser.find_by_xpath('/html/body/div[2]/div/div[2]/div/div[7]/nav/ul/li[2]/a')
    print(elem.first)
    assert context.browser.find_by_xpath('//a[@href="#"]').first == num

@when(u'I click on next')
def step_impl(context):
    elem1 = context.browser.find_by_xpath('//a[@class="page-link"')[0]
    print(elem1)
    elem2 = context.browser.find_by_xpath('//a[@class="page-link"')[1]
    print(elem2)
    elem3 = context.browser.find_by_xpath('//a[@class="page-link"')[2]
    print(elem3)

@when(u'I click on previous')
def step_impl(context):
    context.browser.find_by_xpath('//a[@class="page-link"').click()

@when(u'I click on category "{cat}"')
def step_impl(context):
    context.browser.find_by_xpath('//a[@class="page-link"/a[0]').click()