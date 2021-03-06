from behave import *

use_step_matcher("parse")

@given(u'Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    create_user(context, username, password)

@when(u'I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    fill_login_form(context, username, password)

@then(u'I am redirected to the login form')
def step_impl(context):
    assert context.browser.url.startswith(context.get_url('/login/'))

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

@then(u'I cannot login')
def step_impl(context):
    assert context.browser.is_text_present("Invalid username and/or password.")

@then(u'I can login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    fill_login_form(context, username, password)
    assert context.browser.url.startswith(context.get_url('/account/'))
    assert context.browser.is_text_present(f"Hi {username}")

@given(u'I\'m logged in with user "{username}" and password "{password}"')
def step_impl(context, username, password):
    create_user(context, username, password)
    fill_login_form(context, username, password)

def create_user(context, username, password):
    from book_visualizer.models import User
    if User.objects.all().filter(username__exact=username).exists():
        u = User.objects.get(username__exact=username)
        u.set_password(password)
        return u
    return User.objects.create_user(username=username, email='user@example.com', password=password)

def fill_login_form(context, username, password):
    context.browser.visit(context.get_url('/login/'))
    form = context.browser.find_by_tag('form')[1]
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_tag('button').first.click()
