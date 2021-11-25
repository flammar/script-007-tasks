import os

import pytest

# More information about exception handling
# https://docs.pytest.org/en/latest/how-to/assert.html#assertions-about-expected-exceptions


class TestExceptions:

    def test_exception(self):
        with pytest.raises(AttributeError):
            x = {'a': 1, 'b': 2}
            print(x.a)

    def test_few_exceptions(self):
        # Different exceptions are on Windows and Linux
        with pytest.raises((WindowsError, OSError)):
            os.chdir('NotExistingDirectory')
