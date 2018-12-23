from requests import post

from app import config

from .base import Accessory


class RGBLight(Accessory):
    def __init__(self,
                 name,
                 device_id=None,
                 access_token=None,
                 base_url=None,
                 headers=None,
                 payload_factory=None):
        self.name = name
        self.device_id = device_id or config.TV_BACKLIGHT_DEVICE_ID
        self.access_token = access_token or config.PARTICLE_ACCESS_TOKEN
        self.base_url = base_url or config.PARTICLE_BASE_URL
        self.headers = headers or {
            "Content-type": "application/x-www-form-urlencoded"
        }

    def _get_payload(self, access_token, value=None):
        payload = {'access_token': access_token}
        if value:
            payload['arg'] = value
        return payload

    def _set(self, parameter, value):
        payload = self._get_payload(self.access_token, value=value)
        url = self._get_url(parameter)
        response = post(url, data=payload, headers=self.headers)
        return response.json().get('return_value')

    def set_status(self, value):
        """1 means on, 0 means off"""
        return self._set('state', value)

    def set_brightness(self, value: int) -> None:
        """ Brightness is expected to come in as an int in the range 0-100."""
        return self._set('brightness', value)

    def set_hue(self, value: int) -> None:
        """Hue"""
        return self._set('hue', value)

    def get_status(self):
        return 0

    def get_brightness(self) -> int:
        # payload = self._get_payload(self.access_token)
        # url = self._get_url('brightness')
        # response = get(url, payload, headers=self.headers)
        return 0

    def get_hue(self) -> float:
        return 120