import os

import pytest


@pytest.fixture(scope='function')
def prepare_testfile(request):
    print('prepare_testfile: before test')
    with open('testfile.txt', 'w') as f:
        f.write('first line')

    yield  # Run tests

    print('prepare_testfile: after test')
    if os.path.exists('testfile.txt'):
        os.remove('testfile.txt')
