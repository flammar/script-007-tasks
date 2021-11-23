import os


def myadd(a, b):
    if a > 100:
        return 100
    return a + b


def tricky_func():
    a = 1
    b = a + 1
    return b


def checkfile(filename):
    return os.path.isfile(filename)
