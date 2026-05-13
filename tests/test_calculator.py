from calculator import add, multiply, sub, divide, remainder, power


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3


def test_remainder():
    assert remainder(10, 3) == 1
    assert remainder(8, 4) == 0


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
