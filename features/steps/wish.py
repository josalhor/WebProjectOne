from behave import *

use_step_matcher("parse")

@given(u'This user wishes the book with isbn "{isbn}"')
def step_impl(context, isbn):
    context.browser.visit(context.get_url(f'/book/{isbn}'))
    form = context.browser.find_by_tag('form')[1]
    context.browser.find_by_text('Add to my wish list').first.click()

@then(u'I can click the button "{button}"')
def step_impl(context, button):
    form = context.browser.find_by_tag('form')[1]
    context.browser.find_by_text(f'{button}').first.click()

@then(u'I can see the button "{button}" on the page of book "{isbn}"')
def step_impl(context, button, isbn):
    context.browser.visit(context.get_url(f'/book/{isbn}'))
    form = context.browser.find_by_tag('form')[1]
    assert context.browser.is_text_present(button)

@when(u'I click the button See wish List on my profile "{username}"')
def step_impl(context, username):
    context.browser.visit(context.get_url('/account/'))
    context.browser.click_link_by_href(f'/account/{username}')  

@then(u'The book titled "{title}" appears on wish list')
def step_impl(context, title):
    assert context.browser.is_text_present(title)

@when(u'I remove the first book from my wish list')
def step_impl(context):
    context.browser.find_by_tag('button')[2].click()
    context.browser.find_by_text('Sure').first.click()
    context.browser.find_by_text('OK').first.click()

@when(u'I visit my friend "{username_friend}" wish list')
def step_impl(context, username_friend):
    context.browser.visit(context.get_url(f'/account/{username_friend}'))
    