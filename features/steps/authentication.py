from behave import *

use_step_matcher("parse")

@given('Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    from django.contrib.auth.models import User
    u = User(username=username, email='test@test.com')
    u.set_password(password)

@when('I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('/login/'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_value('Login').first.click()

@then(u'I should see "Hi username"')
def step_impl(context):
    br = context.browser
    response = br.response()
    assert response.code == 200
    assert context.browser.is_text_present('Hi username')