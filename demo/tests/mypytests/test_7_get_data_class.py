import pytest


@pytest.fixture(scope='function')
def get_my_data(request):
    print('driver init')
    request.cls.host = 'myhost'  # init
    request.cls.port = 5432
    yield
    del request.cls.host  # deinit
    del request.cls.port


class TestGetMyData:

    @pytest.mark.usefixtures('get_my_data')
    def test_case1(self):
        assert self.host == 'myhost'
        assert self.port == 5432
