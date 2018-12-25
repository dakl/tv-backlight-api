from .base import Accessory


class MockAccessory(Accessory):
    def set_status(self, value) -> int:
        return 1

    def set_brightness(self, value: int) -> int:
        return 100

    def set_hue(self, hue: float) -> int:
        return 120

    def get_status(self):
        return 0

    def get_brightness(self) -> float:
        pass

    def get_hue(self) -> float:
        pass
