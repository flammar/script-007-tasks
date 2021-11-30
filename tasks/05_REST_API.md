
# Общие моменты

Делайте изменения в ветке `05_rest_api`.

# Реализуйте web-сервер

1. Добавьте параметр `-p/--port` со значением по умолчанию 8080.
Дополните конфигурационный файл парамтером `port`, если таковой имеется.

2. Дополните `requirements.txt` пакетами `aiohttp` и `requests`.

3. Добавьте в `main.py` использование класса `WebHandler`, как обработчик HTTP-запросов со следующей маршрутизацией:

| POST     | URL                 | Handler                 |
| -------- | ------------------- | ----------------------- |
| `POST`   | `/change_dir`       | `handler.change_dir`    |
| `GET`    | `/files`            | `handler.get_files`     |
| `GET`    | `/files/{filename}` | `handler.get_file_data` |
| `POST`   | `/files`            | `handler.create_file`   |
| `DELETE` | `/files/{filename}` | `handler.delete_file`   |

4. В файле `server/WebHandler.py` реализуйте корутины для обработки HTTP-запросов.

5. Для проверки используйте скрипты из папки `test_web`.

6. Напишите автотесты для проверки функциональности.
