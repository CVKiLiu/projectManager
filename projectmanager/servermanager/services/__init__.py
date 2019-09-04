#!usr/bin/python3
import json
import importlib
import pkgutil

from projectmanager.servermanager import DefaultServiceManager


def registerAllServiceModule():
    """
    :description: parse config file and register all service modules into service manager
    """
    config_bytes = pkgutil.get_data(__package__, 'config.json')
    config = json.loads(config_bytes.decode())
    for service in config["services"]:
        moduleName = service["module"]
        serviceName = service["service"]
        path = service["path"]
        description = service["description"]
        serviceModule = importlib.import_module(path)
        DefaultServiceManager.register(serviceName, serviceModule.defaultServiceFactory)


if '__name__' == '__main__':
    registerAllServiceModule()

registerAllServiceModule()
