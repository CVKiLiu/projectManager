#!usr/bin/python3
import unittest

from projectmanager.servermanager import DefaultServiceManager


class TestServicesModule(unittest.TestCase):

    def test_registerAllServiceModule(self):
        import projectmanager.servermanager.services
        print(DefaultServiceManager)
        print(DefaultServiceManager.factories)
        success, ds = DefaultServiceManager.createService("DefaultService")
        ds.execute()
