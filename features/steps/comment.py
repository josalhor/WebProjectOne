from behave import *

use_step_matcher("parse")

@when(u'I add a comment to isbn "{isbn}" with title "{title}" body "{body}" and stars "{stars}"')
def step_impl(context, isbn, title, body, stars):
    context.browser.visit(context.get_url(f'/book/{isbn}'))
    form = context.browser.find_by_tag('form')[2]
    #context.browser.fill('title', body)
    #context.browser.fill('body', body)
    #form.find_by_tag('button').first.click()

@then(u'I can see a comment on isbn "{isbn}" by "{username}" with title "{title}" body "{body}" and stars "{stars}"')
def step_impl(context, isbn, username, title, body, stars):
    pass

@given(u'"{username}" has a comment on isbn "{isbn}" with title "{title}" body "{body}" and stars "{stars}"')
def step_impl(context, username, isbn, title, body, stars):
    pass

@when(u'I delete my comment on isbn "{isbn}"')
def step_impl(context, isbn):
    pass

@then(u'I cannot see a comment on isbn "{isbn}" by "{username}"')
def step_impl(context, isbn, username):
    pass

@when(u'I edit my comment on isbn "{isbn}" with title "{title}" body "{body}" and stars "{stars}"')
def step_impl(context, isbn, title, body, stars):
    pass

@then(u'I cannot see an Add Comment button')
def step_impl(context):
    pass



