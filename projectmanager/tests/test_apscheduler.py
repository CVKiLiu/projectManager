#!/usr/bin/python3
import unittest

from apscheduler.schedulers.blocking import BlockingScheduler
from projectmanager.servermanager.service import MyService, ExecuteService
from projectmanager.taskmanager.Task.task import Task


def funcWithMultiArgs(usr='', time=''):
    print("Function with multi arguments: [%s , %s] " % (usr, time))


class TestBlockingScheduler(unittest.TestCase):

    def test_funcWithMultiArgs(self):
        scheduler = BlockingScheduler()
        scheduler.add_job(funcWithMultiArgs, args=('kiliu', 'time'))
        scheduler.start()
        scheduler.shutdown()

    def test_callableObject(self):
        scheduler = BlockingScheduler()
        myservice=MyService()
        scheduler.add_job(ExecuteService, args=(myservice, ('kiliu',)))
        scheduler.start()
        scheduler.shutdown()


if '__name__' == '__main__':
    unittest.main()
