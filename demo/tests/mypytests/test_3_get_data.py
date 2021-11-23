import pytest

myvar = None


@pytest.fixture(scope='function', autouse=True)
def case_implicit_var(request):
    print('case_implicit_var: before test-case')
    global myvar
    myvar = 'CASE_IMPLICIT_VAR'
    yield myvar
    print('case_implicit_var: after test-case')


@pytest.fixture(scope='function', autouse=True)
def case_implicit(request):
    print('case_implicit: before test-case')
    yield 'CASE_IMPLICIT'
    print('case_implicit: after test-case')


@pytest.fixture(scope='function')
def case_explicit(request):
    print('case_explicit: before test-case')
    yield 'CASE_EXPLICIT'
    print('case_explicit: after test-case')


class TestSuite:

    def testcase1(self):
        print('testcase1: {}'.format(myvar))

    def testcase2(self, case_explicit):
        print('testcase2: {}'.format(case_explicit))

    # if we need data from a fixture, then we can added it explicitly
    def testcase3(self, case_implicit):
        print('testcase3: {}'.format(case_implicit))
