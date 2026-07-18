from day6_wf005_check2 import is_negative


def test_is_negative():
    assert is_negative(-5) is True
    assert is_negative(3) is False
    assert is_negative(0) is False
