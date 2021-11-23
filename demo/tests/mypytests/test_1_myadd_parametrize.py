import pytest

from tests.myfuncs import myadd


@pytest.mark.parametrize("num1, num2, sum", [
    (0, 0, 0),     # test-case 1
    (1, 2, 3),     # test-case 2
    (11, -5, 6),   # test-case 3
    (11, 1, 12),   # test-case 4
    # (11, 5, 6),  # broken
])
def test_myadd(num1, num2, sum):
    assert myadd(num1, num2) == sum
