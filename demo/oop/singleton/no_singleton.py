class NoSingleton:
    def __init__(self):
        print('NoSingleton.__init__ called')


x1 = NoSingleton()
x2 = NoSingleton()
print(id(x1))
print(id(x2))
print(x1 is x2)

x3 = x1
print(id(x3))
print(x1 is x3)
