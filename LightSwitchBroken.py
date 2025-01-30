from typing import override

from LightSwitchInterface import LightSwitchInterface
from LightSwitchOn import LightSwitchOn

class LightSwitchBroken(LightSwitchInterface):

    @override
    def turn_on(self):
        print('Light switch is broken...')
        return self

    @override
    def turn_off(self):
        print('Light switch is broken...')
        return self

    @override
    def fix(self):
        print('Light switch is now fix and On')
        return LightSwitchOn()
