
# Documentation

https://docs.pytest.org/en/latest/getting-started.html

[Naming conventions](https://docs.pytest.org/en/6.2.x/reference.html#confval-python_classes):

- files matching `test_*.py` and `*_test.py` will be considered test modules
- class names must start with `Test` and miss the `__init__` method
- pytest will consider any function prefixed with `test` as a test

# Run tests

Usage:

```console
$ pytest [options] [file_or_dir] [file_or_dir] [...]
```

Success example:

```console
$ pytest tests/mypytests
$ pytest tests/mypytests/test_0_myadd.py
```

# Capture output

https://docs.pytest.org/en/6.2.x/capture.html

Extra summary info can be shown using the '-r' option:

```console
$ pytest --help | rg -e -r -C 3
  -r chars              show extra test summary info as specified by chars:
                        (f)ailed, (E)rror, (s)kipped, (x)failed, (X)passed,
                        (p)assed, (P)assed with output, (a)ll except passed
                        (p/P), or (A)ll. Warnings are displayed at all times
```

shows the captured output of passed tests:

```console
$ pytest -rP
```

shows the captured output of failed tests (default behaviour):

```console
$ pytest -rx
```

`-s` allows seeing output as is.

# Coverage

There is a plugin [pytest-cov](https://pypi.org/project/pytest-cov/) to measure code coverage:

```console
$ pip install pytest-cov
```

Options are here:
- https://pytest-cov.readthedocs.io/en/latest/config.html#reference
- https://github.com/pytest-dev/pytest-cov/blob/master/src/pytest_cov/plugin.py

Enable coverage:

```console
$ pytest --cov tests tests\mypytests
============================= test session starts =============================
platform win32 -- Python 2.7.18, pytest-4.6.11, py-1.10.0, pluggy-0.13.1
rootdir: C:\Work\TC\Trainings\My\python\script-007\demo
plugins: cov-2.12.1
collected 12 items                                                             

tests\mypytests\test_0_myadd.py .                                        [  8%]
tests\mypytests\test_1_myadd_parametrize.py ...                          [ 33%]
tests\mypytests\test_2_before_after.py ....                              [ 66%]
tests\mypytests\test_3_conftest.py ..                                    [ 83%]
tests\mypytests\test_4_class.py ..                                       [100%]

---------- coverage: platform win32, python 2.7.18-final-0 -----------
Name                                          Stmts   Miss  Cover
-----------------------------------------------------------------
tests\__init__.py                                 0      0   100%
tests\myfuncs.py                                 11      4    64%
tests\mypytests\__init__.py                       0      0   100%
tests\mypytests\conftest.py                      10      0   100%
tests\mypytests\test_0_myadd.py                   6      0   100%
tests\mypytests\test_1_myadd_parametrize.py       4      0   100%
tests\mypytests\test_2_before_after.py           22      0   100%
tests\mypytests\test_3_conftest.py                6      0   100%
tests\mypytests\test_4_class.py                  15      0   100%
tests\myunittests\__init__.py                     0      0   100%
tests\myunittests\test_checkfile.py              14     14     0%
tests\myunittests\test_myadd.py                  11     11     0%
-----------------------------------------------------------------
TOTAL                                            99     29    71%


========================== 12 passed in 0.32 seconds ==========================
```

Create HTML report:

```console
$ pytest --cov tests --cov-report=html tests\mypytests
...
---------- coverage: platform win32, python 2.7.18-final-0 -----------
Coverage HTML written to dir htmlcov
```

Omit some modules, files:

```console
$ cat tests\mypytests\.coveragerc
[run]
omit = tests/mypytests/*
       tests/myunittests/*
       tests/__init__.py

$ pytest --cov tests tests\mypytests --cov-config=tests\mypytests\.coveragerc
```

See other possibilities of `coverage` in [config file](https://coverage.readthedocs.io/en/latest/config.html#).

