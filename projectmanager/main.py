#!/usr/bin/python3
import time
import datetime

from apscheduler.schedulers.background import BackgroundScheduler

from projectmanager.servermanager.service import MyService
from projectmanager.taskmanager.Task.task import Task, MyTask
from projectmanager.taskmanager.scheduler.scheduler import Scheduler


def timedTask():
    print(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])


if __name__ == '__main__':
    pass
