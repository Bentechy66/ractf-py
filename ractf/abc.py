from abc import ABC, abstractmethod

from .helpers.requests import get, patch


class APIBaseObject(ABC):
    def __init__(self, ctf, data=None):
        self._ctf = ctf
        self._fill_attrs(data=data)

    @abstractmethod
    def get_api_path(self):
        raise NotImplementedError()

    def _set_attrs(self, values):
        patch(self.get_api_path(), values, self._ctf)

    def _set_attr(self, name, value):
        self._set_attrs({name: value})

    def _get_object(self):
        return get(self.get_api_path(), self._ctf)

    def _fill_attrs(self, data=None):
        if not data:
            data = self._get_object()
        for k, v in data.items():
            setattr(self, k, v)
