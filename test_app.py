from app import add


def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, -2) == -3


def test_add_mixed():
    assert add(-1, 2) == 1


def test_add_zero():
    assert add(0, 5) == 5


def test_add_multiple():
    result = add(2, 3)
    assert result == 5
