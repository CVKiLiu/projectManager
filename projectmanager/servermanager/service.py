#!/usr/bin/python3
from abc import ABCMeta, abstractmethod


def ExecuteService(service, args=()):
    service.execute(args=args)


class Service(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self, args, **kwargs):
        pass

    def query(self, args, **kwargs):
        pass

    def progress(self, args, **kwargs):
        pass

    def Status(self, args, **kwargs):
        pass

    def stop(self, args, **kwargs):
        pass

    def exit(self, args, **kwargs):
        pass


'''
args = {
"usr": string,
"time": string,
}
'''


class MyService(Service):
    def __call__(self, args=()):
        self.execute(args)

    def execute(self, args, **kwarg):
        print("MyService executing args: %s\n" % args)

    def query(self, info='query'):
        print("MyService querying: %s" % info)

    def exit(self, info='exit'):
        print("MyService executing: %s" % info)


DefaultService = MyService()
