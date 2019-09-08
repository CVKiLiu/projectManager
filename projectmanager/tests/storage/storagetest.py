#!usr/bin/python3
import unittest

from projectmanager.storage import DefaultStorage


class TestDefaultStorage(unittest.TestCase):

    def test_append(self):
        storage = DefaultStorage('test_DefaultStorage.txt')
        for i in range(10):
            storage.append('This line %d\n' % i)

    def test_write(self):
        storage = DefaultStorage('test_DefaultStorage.txt')
        for i in range(10):
            storage.write('This line %d\n' % i)

    def test_read(self):
        storage = DefaultStorage('test_DefaultStorage.txt')
        storage.write('This line for read.')
        content = storage.read()
        print(content)