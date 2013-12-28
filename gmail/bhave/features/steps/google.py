import logging

__author__ = 'kiryl_zayets'
from behave import *
from selenium import webdriver

@given('"{type}" browser')
def start_browser(context, type):
    pass

@when('navigate to "{url}"')
def navigate(context, url):
    context.browser.get('http://google.by')

@then('page appears with title "{title}"')
def verify(context, title):
    assert context.browser.title == 'Google'

