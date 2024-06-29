from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/2") == 50
    assert convert("100/100") == 100

    with pytest.raises(ZeroDivisionError):
        convert("2/0")

    with pytest.raises(ValueError):
        convert("cat/Dog")


def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(23) == "23%"
