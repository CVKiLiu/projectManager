#!usr/bin/python3
# coding:utf-8
import logging
import time


class PHandler(logging.Handler):
    def __init__(self, storage):
        logging.Handler.__init__(self)
        self.storage = storage

    def emit(self, record):
        level = str(record.levelname)
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(record.created))
        message = '[%s---%s] %s\n' % (dt, level, record.msg)
        logging.LogRecord
        self.storage.append(message)

    def close(self):
        self.storage.close()


class PLog(object):

    def __init__(self, logger=None, storage=None):

        self.storage = storage
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        self.log_time = time.strftime("%Y_%m_%d_")
        # self.formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')

    def __console(self, level, message):
        ph = PHandler(self.storage)
        ph.setLevel(logging.DEBUG)
        # ph.setFormatter(self.formatter)
        self.logger.addHandler(ph)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        self.logger.removeHandler(ph)
        ph.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

    def search(self, args=None):
        self.storage.search(args)









