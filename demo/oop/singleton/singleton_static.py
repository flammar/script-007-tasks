class Singleton:
    _instance = None
    _initialize = False

    def __new__(cls):
        print('Singleton.__new__ called')
        if Singleton._instance is None:
            Singleton._instance = object.__new__(cls)
        return Singleton._instance

    def __init__(self):
        print('Singleton.__init__ called')
        if not Singleton._initialize:
            print("Singleton init")
            Singleton._initialize = True


x = Singleton()
y = Singleton()

print(id(x))
print(id(y))
