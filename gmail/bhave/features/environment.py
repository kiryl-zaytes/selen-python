import re
import behave

__author__ = 'kiryl_zayets'

from selenium import webdriver
from behave.log_capture import capture
import logging

@capture(level=logging.DEBUG)
def before_feature(context, feature):
    browser = [feature.split('=')[1] for feature in feature.tags if re.match('browser', feature)]
    if 'firefox' in browser:
        context.browser = webdriver.Firefox()

def after_feature(context, feature):
    context.browser.quit()
