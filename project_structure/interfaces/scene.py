from abc import ABC, abstractmethod

class SceneInterface(ABC):
    @abstractmethod
    def enter(self): pass

    @abstractmethod
    def exit(self): pass

    @abstractmethod
    def update(self, dt: float): pass

    @abstractmethod
    def draw(self, screen): pass

    @abstractmethod
    def handle_event(self, event): pass
