import pytest


@pytest.fixture(scope='module', autouse=True)
def module_fixture():
    print('module_fixture: before test-case')
    yield  # Run test case, transfer execution
    print('module_fixture: after test-case')


@pytest.fixture(scope='class', autouse=True)
def suite_implicit():
    print('suite_implicit: before test')


@pytest.fixture(scope='function', autouse=True)
def case_implicit():
    print('case_implicit: before test-case')
    yield  # Run test case, transfer execution
    print('case_implicit: after test-case')


class TestSuite:

    def test_case(self):
        print('TestSuite.test_case')
