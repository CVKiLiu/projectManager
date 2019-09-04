#!usr/bin/python3


class TaskManager(object):

    def __init__(self):
        self.tasks = {}

    def addTask(self, task=None):
        self.tasks[task.id] = task

    def deleteTask(self):
        pass

    def searchTask(self):
        pass
