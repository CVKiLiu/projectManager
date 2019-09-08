#!usr/bin/python3
import logging

from projectmanager.log import PLog
from projectmanager.storage import DefaultStorage


class ServiceManager(object):

    def __init__(self):
        self.factories = {}

    def register(self, service_id=None, service_factory=None):
        self.factories[service_id] = service_factory

    def search(self, service_name=None):
        factory = self.factories.get(service_name, None)
        if factory is None:
            log.warning('There is no such service: %s' % service_name)
            return False, None
        else:
            return True, factory

    def createService(self, service_name=None, args=None):
        success, factory = self.search(service_name)
        if success is None or factory is None:
            log.warning('Create service %s failed.' % service_name)
            return False, None
        else:
            log.info('Create service %s successfully.' % service_name)
            return True, factory.createService(args)

    def deleteService(self, service_name=None):
        if service_name is not None:
            factory = self.factories.get(service_name, None)
            if factory is None:
                log.warning("No such service!")
            else:
                del self.factories[service_name]
                log.info("delete service %s successfully!" % service_name)


ServiceManagerStorage = DefaultStorage('test.txt')
log = PLog(storage=ServiceManagerStorage)
DefaultServiceManager = ServiceManager()
DefaultServiceManager.search('test')

