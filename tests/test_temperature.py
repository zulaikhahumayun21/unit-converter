import pytest
from converter.temperature import convert_temperature


def test_boiling_point_c_to_f():
    assert convert_temperature(100, "C", "F") == pytest.approx(212)


def test_absolute_zero_boundary():
    assert convert_temperature(0, "K", "C") == pytest.approx(-273.15)


def test_below_absolute_zero_raises():
    with pytest.raises(ValueError):
        convert_temperature(-300, "C", "K")

def test_fahrenheit_to_celsius():
    assert convert_temperature(32, "F", "C") == pytest.approx(0)

def test_celsius_to_kelvin():
    assert convert_temperature(0, "C", "K") == pytest.approx(273.15)


def test_kelvin_to_fahrenheit():
    assert convert_temperature(273.15, "K", "F") == pytest.approx(32)


def test_unsupported_unit_raises():
    with pytest.raises(ValueError):
        convert_temperature(10, "X", "C")

   
