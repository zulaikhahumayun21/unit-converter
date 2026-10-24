import pytest
from converter.length import convert_length


def test_km_to_m_normal():
    assert convert_length(2, "km", "m") == pytest.approx(2000)


def test_zero_length_edge_case():
    assert convert_length(0, "mi", "ft") == 0


def test_length_invalid_unit_raises():
    with pytest.raises(ValueError):
        convert_length(5, "parsec", "m")
