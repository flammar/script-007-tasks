from demo.tests.myfuncs import checkfile


class TestCheckFile:

    # See `conftest.py` for fixtures definitions
    def test_existent(self, prepare_testfile):
        assert checkfile('testfile.txt')

    def test_nonexistent(self, prepare_testfile):
        assert not checkfile('testfile123.txt')
