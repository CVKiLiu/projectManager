#!usr/bin/python3
import unittest

from projectmanager.log import PLog
from projectmanager.storage import DefaultStorage


class TestPLog(unittest.TestCase):

    def test_withDefaultStorage(self):
        storage = DefaultStorage('test_PLog.txt')
        log = PLog(storage=storage)
        log.debug("test_bug")
        log.info("test_info")
        log.warning("test_warning")
        log.error("test_error")
