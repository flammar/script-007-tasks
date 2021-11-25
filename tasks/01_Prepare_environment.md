
# Задание 1: Настройка окружения

## Обновление README

Обновите файл `README.md`:

- заполните название проекта `PROJECT_NAME`
- заполните автора проекта `AUTHOR_NAME`

## Создание виртуального окружения

Если виртуальное окружение ещё не было создано, то выполните следующие шаги, иначе пропустите этот раздел.

Для Windows:

```console
> python -m venv venv
> c:\Python310\python.exe -m venv venv  # вариант с явным выбором интерпретатора
> venv\Scripts\activate.bat
> c:\Python310\python.exe -m pip install --upgrade pip
```

Для Linux:

```console
$ python3 -m venv venv
$ source venv/bin/activate
```

## Добавление файла завимостей проекта

Добавьте пустой файл `requirements.txt` в корень репозитория.

## Настройка Git

Установите параметры пользователя для текущего проекта. Например:

```console
$ git config user.name "Maxim Suslov"
$ git config user.email maxim.suslov@dxc.com
```

Добавьте файл `.gitignore` в корень репозитория. Ниже представлено типовое содержимое данного файла:

```gitignore
# python
*.pyc
__pycache__/

# virtual environment
.venv*/
venv*/

# Pycharm IDE
/.idea/

# VS Code IDE
/.vscode/
*.code-workspace
```
