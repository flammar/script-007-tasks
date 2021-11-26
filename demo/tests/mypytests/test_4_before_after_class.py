import pytest


@pytest.fixture(scope='class', autouse=True)  # Fixture, which executes before test suite implicitly
def suite_implicit():
    print('suite_implicit: before test-suite')
    yield
    print('suite_implicit: after test-suite')


@pytest.fixture(scope='class')  # Fixture, which executes before test suite explicitly
def suite_explicit():
    print('suite_explicit: before test-suite')
    yield
    print('suite_explicit: after test-suite')


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


class TestSuiteImplicit:

    def test_dummy(self):
        print('TestSuiteImplicit.test_dummy')


class TestSuiteExplicit:

    def test_dummy1(self, suite_explicit):  # must present in any test-case to be applied
        print('TestSuiteExplicit.test_dummy1')

    def test_dummy2(self, suite_explicit):  # second and further occurences doesn't matter
        print('TestSuiteExplicit.test_dummy2')

    def test_case_explicit(self, case_explicit):
        print('TestSuiteExplicit.test_case_explicit')

    def test_dummy3(self):
        print('TestSuiteExplicit.test_dummy3')
