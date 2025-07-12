from abc import ABC, abstractmethod

class ComponentInterface(ABC):
    @abstractmethod
    def update(self, dt: float): pass

    @abstractmethod
    def draw(self, screen): pass

    @abstractmethod
    def handle_event(self, event): pass
