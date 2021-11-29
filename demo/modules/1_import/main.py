
# create 'a'
# do nothing because no __init__.py
import a
print(type(a))  # type 'module'
print(dir(a))  # there is no 'aa' inside

# create 'aa'
# create 'a.aa' when a is loaded or when it will be loaded
# execute code in 'aa'
from a import aa

# create 'b'
# execute __init__.py
import b
print(type(b))  # type 'module'
print(dir(b))  # there is no 'bb' inside


# different links from different packages
# >>> id(d.e.ee.ee_func)
# 2208055599616
# >>> from d.e import ee
# >>> id(ee.ee_func)
# 2208055599616


# from . import b
# failed because no current module
# but it works from another module


# >>> import b
# b b is called
# >>> from b import *
# cc b.bb is called


# вы мен по питону объясните пожалуйста
# есть такая структура директорий:
# mypackage/
#    _init_.py
#    a.py
#    b.py              # тут какой-то класс определен например Foo
#
# __init__.py пустой
#
# когда я в интерпретаторе делаю import mypackage
# как мне достучаться до класса Foo?
# Как мне изменить _init_.py чтобы Foo был доступен?
# 1)
# from . import b
# тогда в main
# import mypackage
# foo = mypackage.b.Foo()
# 2)
# Если в mypackage/_init_.py напишешь
# from b import Foo
# тогда в main
# import mypackage
# foo = mypackage.Foo()
