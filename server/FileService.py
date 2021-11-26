import datetime
import os
import os.path
import re
from os import stat_result

_DATA_DIR = os.path.realpath(os.getcwd()).strip()


def _path_check(path: str) -> None:
    clean_path = path.strip()
    if bool(re.search(r'[^A-Za-z0-9-_/.\\%&]', clean_path)):
        raise ValueError("{}: path contains invalid characters".format(path))
    if os.path.commonpath([os.path.realpath(clean_path), _DATA_DIR]) != _DATA_DIR:
        raise ValueError("{}: path is forbidden".format(path))


def _existence_check(filename):
    if not os.path.exists(os.path.realpath(filename.strip())):
        raise RuntimeError("{}: file or directory does not exist".format(filename))


def _not_file_check(path: str) -> None:
    if os.path.isfile(os.path.realpath(path.strip())):
        raise RuntimeError("{} is a file".format(path))


def _stat_data(stat: stat_result, return_edit_date: bool = True):
    res = {"create_date": _time(stat.st_ctime), "size": stat.st_size}
    return {**res, "edit_date": _time(stat.st_mtime)} if return_edit_date else res


def get_current_dir() -> str:
    """Get current directory of app.

    Returns:
        current directory of app
    """
    return os.path.realpath(os.getcwd()).strip()


def change_dir(path: str, auto_create: bool = True) -> None:
    """Change current directory of app.

    Args:
        path (str): Path to working directory with files.
        auto_create (bool): Create folder if it doesn't exist.

    Raises:
        RuntimeError: if directory does not exist and auto_create is False.
        ValueError: if path is invalid.
    """
    _not_file_check(_str_ensure(path))
    _path_check(path)
    real_path = _dir_ensure(path, auto_create)
    os.chdir(real_path)


def get_files(filename: str = None) -> list:
    """Get info about all files in working directory.

    Returns:
        List of dicts, which contains info about each file. Keys:
        - name (str): filename
        - create_date (datetime): date of file creation.
        - edit_date (datetime): date of last file modification.
        - size (int): size of file in bytes.
    """

    real_path = os.path.realpath((os.path.realpath(os.getcwd()) if filename is None else _str_ensure(filename)).strip())
    _not_file_check(real_path)
    if filename is not None:
        _path_check(real_path)
    if not os.path.exists(real_path):
        raise RuntimeError("{}: directory does not exist".format(filename))
    return list(map(lambda e: ({"name": e.name, **_stat_data(e.stat())}),
                    filter(lambda e1: (e1.name.startswith('.') and e1.is_file()), os.scandir(real_path))))


def _time(time):
    return datetime.datetime.fromtimestamp(time)


def _str_ensure(path, allow_none=True):
    if path is None and not allow_none or not isinstance(path, str):
        raise TypeError("{} is not string".format(path))
    return path


def _dir_ensure(path: str, auto_create: bool = True) -> str:
    real_path = os.path.realpath(path.strip())
    if not os.path.exists(real_path):
        if not auto_create:
            raise RuntimeError("{}: directory does not exist".format(path))
        else:
            os.makedirs(real_path)
    return real_path


def get_file_data(filename: str) -> dict:
    """Get full info about file.

    Args:
        filename (str): Filename.

    Returns:
        Dict, which contains full info about file. Keys:
        - name (str): filename
        - content (str): file content
        - create_date (datetime): date of file creation
        - edit_date (datetime): date of last file modification
        - size (int): size of file in bytes

    Raises:
        RuntimeError: if file does not exist.
        ValueError: if filename is invalid.
    """

    _path_check(_str_ensure(filename))
    _existence_check(filename)
    path1 = os.path.realpath(filename.strip())
    if not os.path.isfile(path1):
        raise RuntimeError("{} is not a file".format(filename))
    with open(path1, mode='rb') as file:
        return {"name": os.path.basename(path1), "content": file.read().decode(), **_stat_data(os.stat(path1))}


def create_file(filename: str, content: str = None, auto_create_dir: bool = True) -> dict:
    """Create a new file.

    Args:
        auto_create_dir: Create folder for file if it doesn't exist.
        filename (str): Filename.
        content (str): String with file content.

    Returns:
        Dict, which contains name of created file. Keys:
        - name (str): filename
        - content (str): file content
        - create_date (datetime): date of file creation
        - size (int): size of file in bytes

    Raises:
        RuntimeError: if file directory does not exist and auto_create_dir is False.
        ValueError: if filename is invalid.
    """
    _path_check(_str_ensure(filename))
    real_path = os.path.realpath(filename.strip())
    if os.path.isdir(real_path):
        raise RuntimeError("{} already exists and is a directory".format(filename))
    _dir_ensure(os.path.dirname(real_path), auto_create_dir)
    with open(real_path, mode='wb') as file:
        if content is not None:
            file.write(content.encode())
    return {"name": os.path.basename(real_path), "content": "" if content is None else content,
            **_stat_data(os.stat(real_path), False)}


def delete_file(filename: str) -> None:
    """Delete file.

    Args:
        filename (str): filename

    Raises:
        RuntimeError: if file does not exist.
        ValueError: if filename is invalid.
    """
    _path_check(_str_ensure(filename))
    _existence_check(filename)
    path1 = os.path.realpath(filename.strip())
    if os.path.isdir(path1):
        os.rmdir(path1)
    else:
        os.remove(path1)
