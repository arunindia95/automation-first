import pytest


def test_m1():
    a = 1
    b = 2
    assert b == a + 2


def test_m2():
    assert "admin" == "admiin"

@pytest.mark.log
def test_login():
    assert "Arun" == "hello"


def test_logout():
    assert "cvcv" == "cvcv"

