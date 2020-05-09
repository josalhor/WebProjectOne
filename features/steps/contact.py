from behave import *

use_step_matcher("parse")

@when(u'I click Contact button and send a message with email "{email}" and subject "{subject}" and message "{message}"')
def step_impl(context,email, subject, message):
    context.browser.visit(context.get_url('/contact/'))
    form = context.browser.find_by_tag('form')[1]
    context.browser.fill('email_adress', email)
    context.browser.fill('subject', subject)
    context.browser.fill('message', message)
    form.find_by_tag('button').first.click()


@then(u'I see a the message "{message}"')
def step_impl(context, message):
    assert context.browser.is_text_present(f"{message}")
    