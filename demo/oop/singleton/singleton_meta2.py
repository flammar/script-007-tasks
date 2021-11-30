class SingletonMeta(type):
    def __call__(cls, *args, **kwargs):
        try:
            return cls._instance
        except AttributeError:
            cls._instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            return cls._instance


class MySingletonX(metaclass=SingletonMeta):
    def __init__(self):
        print('MySingletonX.__init__ called')


class MyBaseClass:
    def __init__(self):
        print('MyBaseClass.__init__ called')


class MySingletonY(MyBaseClass, metaclass=SingletonMeta):
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
