from abc import ABC, abstractmethod

class AudioManagerInterface(ABC):
    @abstractmethod
    def play_sound(self, name: str): pass

    @abstractmethod
    def play_music(self, file: str, loop: bool = True): pass

    @abstractmethod
    def stop_music(self): pass
