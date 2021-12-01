import os
import random
import shutil
import string
from importlib import reload

import pytest

from server import FileService
from utils.Configs import config
from utils.ObjectUtils import keys, getpath


def _abs_random_filename():
    return os.path.realpath(_random_filename())


def _random_filename():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))


def _random_text(length: int = 256):
    return ''.join(random.choices(string.printable, k=length))


_RANDOM_DIR_CREATION_FAILURE_TOLERANCE = 8


def _rm(path):
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)


@pytest.fixture(scope='function', autouse=True)
def in_random_dir():
    test_wd = ""
    old_cwd = os.getcwd()
    for i in range(_RANDOM_DIR_CREATION_FAILURE_TOLERANCE):
        test_wd = _abs_random_filename()
        if not os.path.exists(test_wd):
            break
        else:
            test_wd = None
    if not test_wd:
        raise RuntimeError("Could not create new random directory {} times!"
                           .format(_RANDOM_DIR_CREATION_FAILURE_TOLERANCE))
    os.makedirs(test_wd)
    os.chdir(test_wd)
    reload(FileService)
    yield
    os.chdir(old_cwd)
    _rm(test_wd)
