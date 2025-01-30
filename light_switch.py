# there is a light switch
# we can turn it on / off
# if the light switch is on:
#     turn-on: nothing happens
#     turn-off: light switch is off
#     fix: nothing happens
# if the light switch is off:
#     turn-on: light switch is on
#     turn-off: light-switch will be broken
#     fix: nothing happens
# if the light switch is broken:
#     turn-on: nothing happens
#     turn-off: nothing happens
#     fix: light switch is on again
from abc import ABC, abstractmethod
from typing import override

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

class LightSwitch(LightSwitchInterface, object):
    def __init__(self, state: str):
        self.state = state

    @override
    def turn_on(self):
        pass

    @override
    def turn_off(self):
        pass

    @override
    def fix(self):
        pass

