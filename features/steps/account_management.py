from behave import *

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
    context.browser.visit(context.get_url('/logout/'))