from demo.tests.myfuncs import myadd


def test_myadd():
    myadd_dataset = [
        0, 0, 0,
        1, 2, 3,
        11, -5, 6,
        # 11, 5,  6,  # broken
    ]

    for i in range(0, len(myadd_dataset), 3):
        a, b, c = myadd_dataset[i:i + 3]
        # assert is not a function!
        assert c == myadd(a, b)
