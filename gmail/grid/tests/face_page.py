import logging
from nose.tools import istest
import os
from selenium import webdriver
from hamcrest import *
import time
import config
from config import PHANTOM_DRIVER

logger = logging.getLogger(__name__)

class TestBasic(object):
    _multiprocess_can_split_ = True
    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Firefox()

    @istest
    def go_browser(self):
        self.driver.get('http://google.com')
        logger.debug(os.getpid())
        assert_that(self.driver.title, equal_to('Google'))

    def teardown(self):
        self.driver.close()


class TestBasic2(object):
    _multiprocess_can_split_ = True
    def __init__(self):
        self.phantom = None

    def setup(self):
        self.phantom = webdriver.PhantomJS(config.PHANTOM_DRIVER)

    @istest
    def get_tut(self):
        logger.debug(os.getpid())
        self.phantom.get('http://tut.by')
        assert_that(self.phantom.title, equal_to('Белорусский портал TUT.BY'))

    def teardown(self):
        self.phantom.close()


class TestBasic3(object):
    _multiprocess_can_split_ = True
    def __init__(self):
        self.driver = None
        logger.debug(os.getpid())

    def setup(self):
        self.driver = webdriver.Firefox()

    @istest
    def go_browser(self):
        self.driver.get('http://google.com')
        assert_that(self.driver.title, equal_to('Google'))

    def teardown(self):
        self.driver.close()