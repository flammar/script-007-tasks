import pytest


@pytest.fixture(scope='function', autouse=True)
def case_implicit():
    print('case_implicit: before test-case')
    yield 'CASE_IMPLICIT'
    print('case_implicit: after test-case')


@pytest.fixture(scope='function')
def case_explicit():
    print('case_explicit: before test-case')
    yield 'CASE_EXPLICIT'
    print('case_explicit: after test-case')


myvar = None


@pytest.fixture(scope='function', autouse=True)
def case_implicit_var():
    print('case_implicit_var: before test-case')
    global myvar
    myvar = 'CASE_IMPLICIT_VAR'
    yield
    myvar = None
    print('case_implicit_var: after test-case')


class TestSuite:

    def test_explicit(self, case_explicit):
        assert case_explicit == 'CASE_EXPLICIT'

    # if we need data from a fixture, then we can added it explicitly
    def test_implicit(self, case_implicit):
        assert case_implicit == 'CASE_IMPLICIT'

    # workaround using global var
    def test_var(self):
        assert myvar == 'CASE_IMPLICIT_VAR'
