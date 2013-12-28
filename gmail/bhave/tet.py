from wsgiref import handlers

__author__ = 'kiryl_zayets'
from logging import handlers
import logging


def tetst():
    log = logging.getLogger(__name__)
    logging.basicConfig(level = logging.INFO)
    log.info('ffffff')


tetst()