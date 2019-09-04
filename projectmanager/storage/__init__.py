#!usr/bin/python3
from abc import ABCMeta, abstractmethod


class Storage(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    def write(self, args=None):
        pass

    def read(self, args=None):
        pass


class DefaultStorage(Storage):

    def __init__(self, file):
        self.__file = file

    def write(self, args=None):
        with open(self.__file, 'a', encoding='utf-8') as f:
            f.write(args)

    def read(self, args=None):
        with open(self.__file, 'r', encoding='utf-8') as f:
            return f.read()
