import pytest


@pytest.fixture(scope='class', autouse=True)  # Fixture, which executes before test suite implicitly
def suite_implicit(request):
    print('suite_implicit: before test')


@pytest.fixture(scope='class')  # Fixture, which executes before test suite explicitly
def suite_explicit(request):
    print('suite_explicit: before test')


@pytest.fixture(scope='function', autouse=True)  # Fixture, which executes before and after test case implicitly
def case_implicit(request):
    print('case_implicit: before test-case')
    yield  # Run test case, transfer execution
    print('case_implicit: after test-case')


@pytest.fixture(scope='function')  # Fixture, which executes before and after test case explicitly
def case_explicit(request):
    print('case_explicit: before test-case')
    yield  # Run test case, transfer execution
    print('case_explicit: after test-case')


# Test suite
class TestSuite:

    # Test cases
    def testcase3(self, case_explicit):
        print('I like cookies')

    def testcase2(self, suite_explicit):
        pass

    def testcase1(self, suite_explicit, case_explicit):  # Add fixtures to test case
        pass

    def testcase4(self):
        pass
