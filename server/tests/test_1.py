import datetime
import os
import random
import re
import shutil
import string
from importlib import reload

import pytest

from server import FileService

_TOLERANCE = 8


def _abs_random_filename():
    return os.path.realpath(_random_filename())


def _random_filename():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))


def _random_text(length: int = 256):
    return ''.join(random.choices(string.printable, k=length))


def _rm(path):
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)


@pytest.fixture(scope='function', autouse=True)
def in_random_wd():
    test_wd = ""
    old_cwd = os.getcwd()
    for i in range(_TOLERANCE):
        test_wd = _abs_random_filename()
        if not os.path.exists(test_wd):
            break
        else:
            test_wd = None
    if not test_wd:
        raise RuntimeError("Could not create new random directory {} times!".format(_TOLERANCE))
    os.makedirs(test_wd)
    os.chdir(test_wd)
    reload(FileService)
    yield
    os.chdir(old_cwd)
    _rm(test_wd)


file_with_content = (_random_filename(), _random_text(1234))
file_with_content_in_subdir = (os.path.join(_random_filename(), _random_filename()), _random_text(1223))


@pytest.mark.parametrize("filename, content",
                         [file_with_content, file_with_content_in_subdir])
def test_create_file(filename, content):
    file_data_check(FileService.create_file(filename, content), filename, content)


def file_data_check(file_data, filename: str, content: str, with_edit_date: bool = False):
    assert file_data["name"] == os.path.basename(filename)
    assert file_data["size"] == len(content)
    assert file_data["size"] == os.path.getsize(filename)
    assert abs(file_data["create_date"].timestamp() - datetime.datetime.now().timestamp()) < 10
    assert file_data["create_date"] == datetime.datetime.fromtimestamp(os.path.getctime(filename))
    assert file_data["content"] == content
    if with_edit_date:
        assert abs(file_data["edit_date"].timestamp() - datetime.datetime.now().timestamp()) < 10
        assert file_data["edit_date"] == datetime.datetime.fromtimestamp(os.path.getmtime(filename))
    with open(filename, 'rb') as file:
        assert content == file.read().decode()


@pytest.mark.parametrize("filename, content",
                         [file_with_content, file_with_content_in_subdir])
def test_create_file_and_get_data(filename, content):
    real_path = os.path.realpath(filename)
    real_dir = os.path.realpath(os.path.dirname(real_path))
    if not os.path.exists(real_dir):
        os.makedirs(real_dir)
    with open(real_path, mode='wb') as file:
        file.write(content.encode())
    data = FileService.get_file_data(filename)
    file_data_check(data, filename, content, with_edit_date=True)


@pytest.mark.parametrize("filename", [file_with_content_in_subdir[0]])
def test_create_file_in_non_existent_dir_fails(filename):
    with pytest.raises(RuntimeError, match="{}: directory does not exist".format(os.path.dirname(filename))):
        FileService.create_file(filename, "content", False)


@pytest.mark.parametrize("filename", [file_with_content_in_subdir[0]])
def test_create_file_if_is_dir_fails(filename):
    os.makedirs(filename)
    with pytest.raises(RuntimeError,
                       match=re.sub("\\\\", "\\\\\\\\", "{} already exists and is a directory".format(filename))):
        FileService.create_file(filename, "content", False)


@pytest.mark.parametrize("filename", [file_with_content_in_subdir[0]])
def test_create_file_with_bad_name_fails(filename):
    filename = filename + '::'
    with pytest.raises(ValueError,
                       match=re.sub("\\\\", "\\\\\\\\", ("{}: path contains invalid characters".format(filename)))):
        FileService.create_file(filename, "content", False)


@pytest.mark.parametrize("filename", [file_with_content[0]])
def test_create_file_in_up_dir_fails(filename):
    filename = os.path.join("..", filename)
    with pytest.raises(ValueError,
                       match=re.sub("\\\\", "\\\\\\\\", ("{}: path is forbidden".format(filename)))):
        FileService.create_file(filename, "content", False)
