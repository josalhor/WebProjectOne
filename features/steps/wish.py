from behave import *
import time
use_step_matcher("parse")

@given(u'This user wishes the book with isbn "{isbn}"')
def step_impl(context, isbn):
    context.browser.visit(context.get_url(f'/book/{isbn}'))
    form = context.browser.find_by_tag('form')[1]
    context.browser.find_by_text('Add to my wish list').first.click()

@then(u'I can click the button "{button}"')
def step_impl(context, button):
    time.sleep(0.35)
    form = context.browser.find_by_tag('form')[1]
    context.browser.find_by_text(f'{button}').first.click()
    time.sleep(0.15)

@then(u'I can see the button "{button}" on the page of book "{isbn}"')
def step_impl(context, button, isbn):
    time.sleep(0.1)
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

@when(u'I remove the book "{isbn}" from my wish list')
def step_impl(context, isbn):
    context.browser.find_by_id(f'delete-{isbn}').first.click()
    time.sleep(0.2)
    context.browser.find_by_text('Sure').first.click()
    time.sleep(0.2)
    context.browser.find_by_text('OK').first.click()

@when(u'I visit my friend "{username_friend}" wish list')
def step_impl(context, username_friend):
    context.browser.visit(context.get_url(f'/account/{username_friend}'))
    
@when('I try to wish the book')
def step_impl(context):
    context.browser.find_by_id('list_ref').click()