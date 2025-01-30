from typing import override
from LightSwitchInterface import LightSwitchInterface
from LightSwitchOff import LightSwitchOff

class LightSwitchOn(LightSwitchInterface):
    @override
    def turn_on(self):
        print('Light switch is already On')
        return self

    @override
    def turn_off(self):
        print('Light switch will now be Off')
        return LightSwitchOff()

    @override
    def fix(self):
        print('Light switch is not broken. cannot fix')
        return self
