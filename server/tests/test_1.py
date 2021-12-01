import datetime
import os
import re

import pytest

from server import FileService
from server.tests.TestUtils import _random_filename, _random_text, in_random_dir

file_with_content = (_random_filename(), _random_text(1234))
file_with_content_in_subdir = (os.path.join(_random_filename(), _random_filename()), _random_text(1223))


@pytest.mark.parametrize("filename, content",
                         [file_with_content, file_with_content_in_subdir])
def test_create_file(filename: str, content: str):
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
def test_create_file_and_get_data(filename: str, content: str):
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
