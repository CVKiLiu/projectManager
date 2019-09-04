#!/usr/bin/python3
import datetime
from enum import Enum

from apscheduler.util import undefined
import time


class TaskStatus(Enum):
    init = 0
    running = 1
    stopped = 2
    abnormal = 3
    finish = 4


class Task(object):
    """
    Contains the options given when scheduling callables and its current schedule and other state.

    :var str id: the unique identifier of this Task
    :var str name: the description of this Task
    :var str|apscheduler.triggers.base.BaseTrigger trigger: trigger that determines when service is called.
    :var Service service:
    :var Scheduler scheduler:
    :var Job job:
    :var trigger: the trigger object that controls the schedule of this job
    :var time last_runt: lasted running time
    """

    def __init__(self, id=None, name=None, trigger=None, service=None, scheduler=None, runnable=True, tags=set(),
                 start_time=None, jobstore='default', executor='default', replace_existing=False, **trigger_args):
        self.id = id
        self.name = name
        self.service = service
        self.scheduler = scheduler
        self.job = None
        self.status = TaskStatus.init
        self.runnable = runnable
        self.tags = tags
        self.start_time = None  # Task Start time
        self.last_runt = None  # lasted run time
        self.create_time = datetime.datetime.now()  # create_time

    def __call__(self, args=()):
        self.run(args=args)

    # add into scheduler
    def schedule(self, trigger=None, args=None, kwargs=None, misfire_grace_time=undefined,
                 coalesce=undefined, max_instances=undefined, next_run_time=undefined, jobstore='default',
                 executor='default', replace_existing=False, **trigger_args):

        self.job = self.scheduler.add_job(trigger=trigger, args=(self.service, args), kwargs=kwargs, id=self.id,
                                          name=self.name, misfire_grace_time=misfire_grace_time, coalesce=coalesce,
                                          max_instances=max_instances, next_run_time=next_run_time, jobstore=jobstore,
                                          executor=executor, replace_existing=replace_existing, **trigger_args)

    def execute(self, args=None):
        if self.runnable:
            self.last_runt = time.time()
            self.service.execute(args=args)
    """
    :param list/tuple args: list of positional arguments to call func with
    :param dict kwargs: dict of keyword arguments to call func with
    """

    def taskProgress(self):
        return self.service.progress();

    def stop(self):
        if self.status == TaskStatus.running:
            self.service.stop()

    def exit(self):
        return self.service.exit()


DefaultTask = Task(sequence='kiliu')
