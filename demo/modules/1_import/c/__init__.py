print(f'c {__name__} is called')

# other good examples:
# https://github.com/pallets/flask/blob/main/src/flask/__init__.py
from . import cc

c_var = 'cc'


def c_func():
    return 33


cc.c_func()  # avoid removing of dummy by PyCharm
