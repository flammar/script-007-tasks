import os
# from FileService import _stat_data, get_files

# filename=
# a=list(map(lambda e: ({"name": e.name, **_stat_data(e.stat)}),
#                     filter(lambda e1: (e1.name.startswith('.') and e1.is_file()), os.scandir(filename))))

# filename = None
# print(os.path.realpath("rrr/pp"))
# print(os.path.realpath("/pp"))
# print(os.path.realpath("../../pp"))
# path1 = os.path.realpath((os.path.realpath(os.getcwd()) if filename is None else filename).strip())
# print(os.path.realpath((os.path.realpath(os.getcwd()) if filename is None else filename).strip()))
# print(get_files())
# print(os.stat(path1))
#
# print(list(map(lambda e: ({"name": e.name, **_stat_data(e.stat())}),
#                     filter(lambda e1: (not e1.name.startswith('.') and e1.is_file()), os.scandir(path1)))))
import re

# print(bool(re.search(r'[^A-Za-z0-9-_/.\\%&]', "..".strip())))
# print(bool(re.search(r'[^:A-Za-z0-9-_/\.\\%&]', "C:\\work\\train\\script-007-tasks\\1\\script-007-tasks".strip())))

# FileService.change_dir("rrrr", True)
# print(FileService.get_current_dir())
# print(FileService.get_files())
from logger_setup import logger_setup
from server import FileService
logger_setup()
atr = 'gv54wye4rthbhxf6udhe7r6'
ld = "zxvdrv"
n1 = "zvzfv"
FileService.change_dir("rrrr1/../../server/" +
                       n1 +
                       "/" + ld, True)
fn = "estsdbrs"
FileService.create_file(fn, atr)
FileService.change_dir("..", True)
# FileService.change_dir(ld, True)

data = FileService.get_file_data(os.path.join(ld, fn))
print(data)
assert data["content"] == atr
FileService.delete_file(os.path.join(ld, fn))
FileService.change_dir("..")
FileService.delete_file(os.path.join(n1, ld))

FileService.delete_file(n1)




