#!usr/bin/python3
import logging


class ServiceManager(object):

    def __init__(self):
        self.factories = {}

    def register(self, service_id=None, service_factory=None):
        self.factories[service_id] = service_factory

    def search(self, service_name=None):
        factory = self.factories.get(service_name, None)
        if factory is None:
            return False, None
        else:
            return True, factory

    def createService(self, service_name=None, args=None):
        success, factory = self.search(service_name)
        if success is None or factory is None:
            return False, None
        else:
            return True, factory.createService(args)

    def deleteService(self, service_name=None):
        if service_name is not None:
            factory = self.factories.get(service_name, None)
            if factory is None:
                logging.warning("No such service!")
            else:
                del self.factories[service_name]
                logging.warning("delete service %s successfully!" % service_name)


DefaultServiceManager = ServiceManager()

