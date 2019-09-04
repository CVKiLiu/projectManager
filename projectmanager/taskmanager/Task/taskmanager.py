#!usr/bin/python3


class TaskManager(object):

    def __init__(self):
        self.executeQueue = []

    def addNewTask(self, task=None):
        self.executeQueue.append(task)

    def removeTask(self, task=None):
        self.executeQueue.remote(task)

    def searchTask(self, id=None, name=None, createtime=None, type=None):
        pass






