from projectmanager.servermanager import DefaultServiceManager
from projectmanager.servermanager.service import Service, ServiceFactory


def register():
    """
    :description: This method register a factory witch create relatively service instance
    into the collections of factory.
    """
    pass


class DefaultServiceFactory(ServiceFactory):

    def __init__(self, service_name="DefaultService"):
        super().__init__(service_name)

    def createService(self, args):
        return DefaultService(args)


class DefaultService(Service):

    def __init__(self, args=None):
        super().__init__(args)

    def execute(self, args=None):
        print("DefaultService executing!")

    def query(self, args=None, **kwargs):
        print("DefaultService querying")

    def progress(self, args=None):
        print("DefaultService progress")

    def status(self, args=None):
        pass

    def stop(self, args=None):
        pass

    def exit(self, args=None):
        pass


defaultServiceFactory = DefaultServiceFactory("DefaultService")

