from abc import ABC, abstractmethod

class InputManagerInterface(ABC):
    @abstractmethod
    def poll_events(self):
        pass
