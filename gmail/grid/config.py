import logging.config
import os
import sys

PATH_SEPARATOR = '/'
SELENIUM_SERVER_FILE_NAME = 'seleniumserver.jar'
PHANTOMJS = 'phantomjs'

ENV = sys.executable.rpartition(PATH_SEPARATOR)[0]

LOGGING_CONF = os.path.join(os.path.dirname(__file__),
                          "config/logger.ini")
logging.config.fileConfig(LOGGING_CONF)

SELENIUM_SERVER = os.path.join(ENV, SELENIUM_SERVER_FILE_NAME)
PHANTOM_DRIVER = os.path.join(ENV, PHANTOMJS)

