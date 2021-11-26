import pytest


@pytest.fixture(scope='function', autouse=True)  # Fixture, which executes before and after test case implicitly
def case_implicit():
    print('case_implicit: before test-case')
    yield  # Run test case, transfer execution
    print('case_implicit: after test-case')


@pytest.fixture(scope='function')  # Fixture, which executes before and after test case explicitly
def case_explicit():
    print('case_explicit: before test-case')
    yield  # Run test case, transfer execution
    print('case_explicit: after test-case')


class TestSuite:

    def testcase_implicit_only(self):
        print('TestSuite.testcase_implicit_only')

    def testcase_implicit_explicit(self, case_explicit):
        print('TestSuite.testcase_implicit_explicit')
