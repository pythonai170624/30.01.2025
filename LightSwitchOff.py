from typing import override
from LightSwitchBroken import LightSwitchBroken
from LightSwitchInterface import LightSwitchInterface
from LightSwitchOn import LightSwitchOn

class LightSwitchOff(LightSwitchInterface):
    @override
    def turn_on(self):
        print('Light switch will now be On')
        return LightSwitchOn()

    @override
    def turn_off(self):
        print('Light switch is already Off ... you broke it ... ')
        return LightSwitchBroken()

    @override
    def fix(self):
        print('Light switch is not broken. cannot fix')
        return self