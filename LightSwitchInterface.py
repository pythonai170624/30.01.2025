from abc import ABC, abstractmethod


class LightSwitchInterface(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def fix(self):
        pass
