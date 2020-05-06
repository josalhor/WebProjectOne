from behave import *

use_step_matcher("parse")

@given(u'Exists a user "username" with password "password"')
def step_impl(context, username, password):
    from django.contrib.auth.models import User
    User.objects.create_user(username=username, email='test@test.com', password=password)

@given(u'I login as user "username" with password "password"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('/login/'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_value('Login').first.click()

@given(u'I\'m not logged in')
def step_impl(context):
    context.browser.visit(context.get_url(''))
    assert context.browser.is_text_present('Login')

