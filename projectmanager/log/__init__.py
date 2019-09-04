#!usr/bin/python3
# coding:utf-8
import logging


class PLog(object):

    def __init__(self, logger=None):
        self.logger = logging.getLogger(logger)


