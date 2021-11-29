
# Documentation

https://docs.python.org/3/library/logging.html Стандартный модуль
https://docs.python.org/3/howto/logging-cookbook.html Интересные примеры
https://docs.python.org/3/howto/logging.html HOWTO

# TODO

- Писать в разные файлы с разными настройками
  https://stackoverflow.com/questions/11232230/logging-to-two-files-with-different-settings

- Чтение конфига из файла

## Подмодули

1) Показываем, что если изменить значения по умолчанию в main, то на других модулях это не скажется.
Потому что они загружаются раньше. Можно print показать.

2) Инициализация в main дефолтный логгер, а потом в подмодулях используем logging и это работает

3) Делаем отдельный модуль для логирования и его все наши модули используют
Он тоже может быть как singleton

тут есть уже заготовка
https://stackoverflow.com/a/15727525/3364871
