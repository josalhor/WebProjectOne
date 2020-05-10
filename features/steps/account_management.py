from behave import *
import time

from authentication import fill_login_form
use_step_matcher("parse")

@when(u'I change my user to "{username}"')
def step_impl(context, username):
    context.browser.click_link_by_href('/account/edit')   
    form = context.browser.find_by_tag('form')[1]
    context.browser.fill('username', username)
    form.find_by_tag('button').first.click()

@when(u'I change my email to "{email}"')
def step_impl(context, email):
    context.browser.click_link_by_href('/account/edit')   
    form = context.browser.find_by_tag('form')[1]
    context.browser.fill('email', email)
    form.find_by_tag('button').first.click()

@when(u'I change my password "{old_password}" to "{new_password}"')
def step_impl(context, old_password, new_password):
    context.browser.click_link_by_href('/change-password/')   
    form = context.browser.find_by_tag('form')[1]
    context.browser.fill('old_password', old_password)
    context.browser.fill('new_password1', new_password)
    context.browser.fill('new_password2', new_password)
    form.find_by_tag('button').first.click()

@then(u'I should see E-mail: "{email}" in  the profile')
def step_impl(context, email):
    assert context.browser.is_text_present(f"E-mail: {email}")

@then(u'I should be able to log out')
def step_impl(context):
    logout_by_url(context)

@given(u'I\'m not logged in')
def step_impl(context):
    logout_by_url(context)

def logout_by_url(context):
    context.browser.visit(context.get_url('/logout/'))

@when(u'I click logout')
def step_impl(context):
    elem = context.browser.find_by_id('logout').first
    elem.click()

@then(u'I should see login option available') # Check
def step_impl(context):
    elem = context.browser.find_by_text('Login').first

@when(u'I delete my user account')
def step_impl(context):
    form = context.browser.find_by_tag('form')[1]
    form.find_by_tag('button').first.click()
    time.sleep(0.2)
    context.browser.find_by_text('OK').first.click()

@then(u'I cannot login with user "{username}" and password "{password}"')
def step_impl(context, username, password):
    fill_login_form(context, username, password)
    assert context.browser.is_text_present("Invalid username and/or password.")
