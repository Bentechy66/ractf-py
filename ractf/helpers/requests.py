import requests

from ..errors import APIError, PermissionsError


def get(api_path, ctf, *args, **kwargs):
    if ctf.auth_token:
        kwargs["headers"] = {}
        kwargs["headers"]["authorization"] = ctf.auth_token
    resp = requests.get(ctf.api_base+api_path, *args, **kwargs)
    if resp.status_code == 403:
        raise PermissionsError(resp.json())
    if resp.status_code != 200:
        raise APIError(resp.text)
    return resp.json()


def patch(api_path, values, ctf, *args, **kwargs):
    if ctf.auth_token:
        kwargs["headers"] = {}
        kwargs["headers"]["authorization"] = ctf.auth_token
    resp = requests.patch(ctf.api_base+api_path, values, *args, **kwargs)
    if resp.status_code == 403:
        raise PermissionsError(resp.json())
    if resp.status_code != 200:
        raise APIError(resp.json())
    return resp.json()
