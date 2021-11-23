import pytest


@pytest.fixture(scope='function')
def get_driver(request):
    print('driver init')
    driver = 'mydriver'  # init
    request.cls.driver = driver
    yield
    driver = None  # deinit


class TestUserDriver1:

    @pytest.mark.usefixtures('get_driver')
    def test_case1(self):
        print('test_case1: {}'.format(self.driver))
        assert self.driver == 'mydriver'


class TestUserDriver2:

    def test_case2(self, get_driver):
        print('test_case2: {}'.format(self.driver))
        assert self.driver == 'mydriver'
