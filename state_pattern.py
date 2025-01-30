from abc import ABC, abstractmethod
from typing import override

from LightSwitchInterface import LightSwitchInterface
from LightSwitchOn import LightSwitchOn

# Context
class Context:
    def __init__(self, light_state: LightSwitchInterface):
        self.light_state = light_state

    def turn_on(self):
        self.light_state = self.light_state.turn_on()

    def turn_off(self):
        self.light_state = self.light_state.turn_off()

    def fix(self):
        self.light_state = self.light_state.fix()

light_room = Context(LightSwitchOn())
light_room.turn_on()
light_room.turn_off()
light_room.turn_off()
light_room.turn_off()
light_room.turn_off()
light_room.fix()
light_room.turn_on()
