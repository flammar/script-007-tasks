from demo.tests.myfuncs import myadd


# Test suite
class TestMyAdd:

    # Test cases
    def testcase3(self):
        assert myadd(1, 2) == 3

    def testcase2(self):
        assert myadd(4, 5) == 9

    def testcase1(self):
        assert myadd(0, 0) == 0

    def testcase4(self):
        assert myadd(11, -5) == 6
