from working import convert
import pytest


def test_time_with_minutes():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_time_without_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_wrong_minutes():
    with pytest.raises(ValueError):
        assert convert("12:60 AM to 5 PM")


def test_wrong_hours():
    with pytest.raises(ValueError):
        assert convert("13 AM to 25 PM")


def test_without_to():
    with pytest.raises(ValueError):
        assert convert("9 AM 5 PM")


def test_invalid_format():
    with pytest.raises(ValueError):
        assert convert("12:00 AM, 13:00 PM")


def test_invalid_time_format():
    with pytest.raises(ValueError):
        assert convert("9-00 AM to 5-00 PM")
