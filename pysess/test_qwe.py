import pytest


def test_login1():
    assert "qwert" == "qwe"

@pytest.mark.log
def test_m3():
    a = 1
    b = 2
    c = 3
    assert c == a + b


@pytest.mark.log
def test_login():
    assert "hello" == "hello"

