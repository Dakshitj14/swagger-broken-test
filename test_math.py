from math_utils import divide


def test_divide():
    assert divide(10, 0) == 0
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide("10", 2) == 5
    assert divide(8, 2) == 4
