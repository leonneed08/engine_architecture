# ServiceLocator
class ServiceLocator:
    _services = {}

    @classmethod
    def register(cls, name, instance):
        cls._services[name] = instance

    @classmethod
    def get(cls, name):
        return cls._services.get(name)
