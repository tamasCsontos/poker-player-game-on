from helpers import add


def test_add():
    assert add.sum_two_numbers(5, 6) == 11
    assert add.sum_two_numbers(8, 9) == 17
    assert add.sum_two_numbers(8, -2) == 6