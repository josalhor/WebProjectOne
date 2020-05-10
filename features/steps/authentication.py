from behave import *

use_step_matcher("parse")


@when(u'I signup as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('/sign_up/'))
    form = context.browser.find_by_tag('form')[1]
    context.browser.fill('username', username)
    context.browser.fill('email', "username@test.com")
    context.browser.fill('password1', password)
    context.browser.fill('password2', password)
    form.find_by_tag('button').first.click()

@then(u'I should see Hi "{username}" in the profile')
def step_impl(context, username):
    assert context.browser.url.startswith(context.get_url('/account/'))
    assert context.browser.is_text_present(f"Hi {username}")

@then(u'I see a message error')
def step_impl(context):
    assert context.browser.is_text_present("Invalid username and/or password.")

@then(u'I can login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('/login/'))
    form = context.browser.find_by_tag('form')[1]
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_tag('button').first.click()
    assert context.browser.url.startswith(context.get_url('/account/'))
    assert context.browser.is_text_present(f"Hi {username}")

@given(u'I\'m logged in with user "{username}" and password "{password}"')
def step_impl(context, username, password):
    from book_visualizer.models import User
    User.objects.create_user(username=username, email='user@example.com', password=password)
    context.browser.visit(context.get_url('/login/'))
    form = context.browser.find_by_tag('form')[1]
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_tag('button').first.click()

@when(u'I log out')
def step_impl(context):
    browser.find_link_by_text('logout').click()