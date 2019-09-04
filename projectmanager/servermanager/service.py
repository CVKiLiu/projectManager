#!/usr/bin/python3
from abc import ABCMeta, abstractmethod


def ExecuteService(service, args=()):
    service.execute(args=args)


# used to create a Service instance
class ServiceFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, servicename=None):
        self.name = servicename

    def createService(self, args=None):
        pass


class Service(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, args=None):
        pass

    def execute(self, args=None):
        pass

    def query(self, args=None):
        pass

    def progress(self, args=None):
        pass

    def status(self, args=None):
        pass

    def stop(self, args=None):
        pass

    def exit(self, args=None):
        pass


