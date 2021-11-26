
# Работа с файловой системой

Широко используются два модуля `os` и `os.path`.

## Модуль `os`

[Документация `os`](https://docs.python.org/3/library/os.html)

Модуль используется для работы с файлами на диске:

os.chdir(path) - установить текущий каталог
os.getcwd() - получить текущий каталог
os.listdir(path='.') - получить список файлов в каталоге

os.makedirs(name, mode=0o777, exist_ok=False) - создать папку (с вложенными папками)
os.mkdir(path, mode=0o777) - создать папку (родительские папки должны быть уже созданы)

os.remove(path) - удалить файл
os.rmdir(path) - удалить пустую папку
os.removedirs(name) - удалить непустую папку

Есть также функции по переименования, переносу файлов и другие.

## Модуль `os.path`

[Документация `os.path`](https://docs.python.org/3/library/os.path.html)

Используется для работы с файловым путём:

os.path.dirname(path) - получить имя родительской папки

```python
>>> os.path.dirname('c:\\1\\2\\3.txt')
'c:\\1\\2'
```

os.path.join(path, *paths) - соединить несколько папок в один путь

```python
>>> os.path.join(os.getcwd(), 'data')
'C:\\Work\\TC\\Trainings\\My\\python\\script-007\\demo\\argparsing\\data'

>>> os.path.join(os.getcwd(), 'data', 'testfiles')
'C:\\Work\\TC\\Trainings\\My\\python\\script-007\\demo\\argparsing\\data\\testfiles'
```

os.path.lexists(path) - проверить, что файл или папка существует

```python
>>> os.path.exists('c:\\1')
False

>>> os.path.exists('c:\\')
True
```

os.path.is*(path) - проверить что объект является контретным типом

os.path.islink(path)
os.path.isdir(path)
os.path.isfile(path)


os.path.getsize(path) - получить размер файла
