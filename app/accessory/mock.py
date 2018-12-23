from .base import Accessory


class MockAccessory(Accessory):
    def set_status(self, value):
        return 1

    def set_brightness(self, value: int) -> None:
        pass

    def get_status(self):
        return 0

    def set_hue(self, hue: float) -> None:
        pass

    def get_brightness(self) -> float:
        pass

    def get_hue(self) -> float:
        pass
