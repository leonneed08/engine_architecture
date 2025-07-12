from abc import ABC, abstractmethod

class EventManagerInterface(ABC):
    @abstractmethod
    def emit(self, event_type: str, **kwargs): pass

    @abstractmethod
    def subscribe(self, event_type: str, callback): pass

    @abstractmethod
    def unsubscribe(self, event_type: str, callback): pass
