from behave import *

use_step_matcher("parse")

@given(u'Exists a user {username} with password {password}')
def step_impl(context, username, password):
    from book_visualizer.models import User
    User.objects.create_user(username=username, email='user@example.com', password=password)

@given(u'Not registered username {username}')
def step_impl(context, username):
    #from django.contrib.auth.models import User
    #if(username.User.Exists):
        #eliminar usuari
        #pass
    #else:
        pass

@when(u'I login as user {username} with password {password}')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('/login/'))
    form = context.browser.find_by_tag('form')[1]
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_tag('button').first.click()

@when(u'I go to signup url')
def step_impl(context):
    context.browser.visit(context.get_url('/sign_up/'))

@when(u'I signup as user {username} with password {password}')
def step_impl(context, username, password):
    form = context.browser.find_by_tag('form')[1]
    context.browser.fill('username', username)
    context.browser.fill('email', "username@test.com")
    context.browser.fill('password1', password)
    context.browser.fill('password2', password)
    form.find_by_tag('button').first.click()

@then(u'I should be redirected to account url')
def step_impl(context, username):
    assert context.browser.url.startswith(context.get_url('/account/'))
    assert context.browser.is_text_present("Hi")

@then(u'I see a message error')
def step_impl(context):
    assert context.browser.is_text_present("Invalid username and/or password.")

@then(u'I am redirected to the login form')
def step_impl(context):
    print(context.browser.url)
    assert context.browser.url.startswith(context.get_url('/login/')) #pending to fix. expected login but got signup