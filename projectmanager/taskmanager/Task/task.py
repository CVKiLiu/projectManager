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


class TaskInfo(object):
    """
    Contains the information and inherent attributes about corresponding Task.

    :var str id: the unique identifier of this Task
    :var str name: the description of this Task
    :var TaskStatus status: the status of task
    :var bool runnable: tag of runnable
    :var set tags: extra tags about this task
    """
    def __init__(self, id=None, name=None, status=TaskStatus.init, runnable=True, tags=set()):
        self.__id = id
        self.__created = datetime.datetime.now()
        self.name = name
        self.status = status
        self.runnable = runnable
        self.tags = tags

    def getId(self):
        return self.__id

    def getCreateTime(self):
        return self.__created

    def setName(self, name=None):
        self.name = name

    def setStatus(self, status=None):
        if status is not None:
            self.status = status

    def tagsContains(self, tags=None):
        pass


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

    def __init__(self, id=None, name=None, runnable=True, tags=set(), trigger=None, service=None, scheduler=None,
                 start_time=None, jobstore='default', executor='default', replace_existing=False, **trigger_args):
        self.taskInfo = TaskInfo(id, name, TaskStatus.init, runnable, tags)
        self.service = service
        self.scheduler = scheduler
        self.job = None
        self.start_time = None  # Task Start time
        self.last_runt = None  # lasted run time

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

    def taskProgress(self):
        return self.service.progress();

    def stop(self):
        if self.status == TaskStatus.running:
            self.service.stop()

    def exit(self):
        return self.service.exit()


