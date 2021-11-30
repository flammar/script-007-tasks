def singleton(cls):
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance


@singleton
class MySingletonX:
    def __init__(self):
        print('MySingletonX.__init__ called')


class MyBaseClass:
    def __init__(self):
        print('MyBaseClass.__init__ called')


@singleton
class MySingletonY(MyBaseClass):
    def __init__(self):
        super().__init__()
        print('MySingletonY.__init__ called')


x1 = MySingletonX()
x2 = MySingletonX()
print(id(x1))
print(id(x2))

y1 = MySingletonY()
y2 = MySingletonY()
print(id(y1))
print(id(y2))
