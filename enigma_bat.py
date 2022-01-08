from enigma_classes import Config
from enigma_config_io import read_config_from_json


def validate_key(key):
    if not isinstance(key, str):
        raise IncorrectKeySpecifiedError
    if not len(str) == 9:
        raise IncorrectKeySpecifiedError


def retrieve_key(key):
    # Allow keys as in A01B02C03
    letters = key[::3]
    numbers = int(key[1::3] + key[2::3])
    return letters, numbers


def init_config(key):
    validate_key(key)
    retrieve_key(key)
    read_config_from_json

class IncorrectKeySpecifiedError(Exception):
    def __init__(self):
        super().__init__()
