import pytest
from converter.weight import convert_weight


def test_kg_to_g_normal():
    assert convert_weight(1.5, "kg", "g") == pytest.approx(1500)


def test_same_unit_returns_same_value_edge_case():
    assert convert_weight(7, "lb", "lb") == pytest.approx(7)


def test_negative_weight_raises():
    with pytest.raises(ValueError):
        convert_weight(-1, "kg", "lb")
