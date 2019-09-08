#!/usr/bin/python3
import unittest

from projectmanager.servermanager.service import Service
from projectmanager.taskmanager.Task.task import Task
from projectmanager.taskmanager.scheduler.scheduler import Scheduler


class TestService(Service):

    def execute(self, args):
        print("TestService executing: %s\n" % args)

    def query(self, args):
        print("TestService querying: %s\n" % args)

    def stop(self, args):
        print("TestService querying: %s\n" % args)

    def exit(self, args):
        print("TestService exiting: %s\n" % args)


class TestScheduler(unittest.TestCase):

    def test_init(self):
        pass

    def test_startTask(self):
        scheduler = Scheduler()
        service = TestService()
        task = Task(sequence='test_startTask', service=service)
        scheduler.add_task(task)
        scheduler.start_task(task, 'test_startTask')
        scheduler.schedule()

    def test_DynamicAddTask(self):
        scheduler = Scheduler()
        service = TestService()
        task_one = Task(sequence='DynamicAddTask_BeforeSchedule', service=service)
        scheduler.add_task(task_one)
        scheduler.start_task(task_one, 'Before Schedule')
        scheduler.schedule()

        task_two = Task(sequence='DynamicAddTask_AfterSchedule', service=service)
        scheduler.add_task(task_one)
        scheduler.start_task(task_one, 'After Schedule')

    def test_SingleServiceMultiTask(self):
        service = TestService()
        scheduler = Scheduler()
        for i in range(0, 10):
            task = Task(sequence='SingleServiceMultitask_'+str(i), service=service)
            scheduler.add_task(task)
            scheduler.start_task(task, str(i))

