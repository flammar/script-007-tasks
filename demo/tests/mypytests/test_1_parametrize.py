import pytest

from demo.tests.myfuncs import myadd


@pytest.mark.parametrize("num1, num2, sum", [
    (0, 0, 0),     # test-case 1
    (1, 2, 3),     # test-case 2
    (11, -5, 6),   # test-case 3
    (11, 1, 12),   # test-case 4
    # (11, 5, 6),  # broken
])
def test_myadd_nns(num1, num2, sum):
    assert myadd(num1, num2) == sum


@pytest.mark.parametrize("sum, num1, num2", [
    (0, 0, 0),     # test-case 1
    (3, 1, 2),     # test-case 2
    (6, 11, -5),   # test-case 3
    (12, 11, 1),   # test-case 4
    # (6, 11, 5, 6),  # broken
])
def test_myadd_snn(sum, num1, num2):
    assert myadd(num1, num2) == sum


@pytest.mark.parametrize(
    argnames=("num1", "num2", "sum"),
    argvalues=(
            (1, 2, 3),
            (-4, -5, -9),
    ),
    ids=(
            "positive numbers",
            "negative numbers",
    ),
)
def test_myadd(num1, num2, sum):
    assert myadd(num1, num2) == sum
