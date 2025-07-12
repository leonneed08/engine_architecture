from abc import ABC, abstractmethod

class AssetManagerInterface(ABC):
    @abstractmethod
    def get_image(self, name: str): pass

    @abstractmethod
    def get_sound(self, name: str): pass

    @abstractmethod
    def get_font(self, name: str, size: int): pass
