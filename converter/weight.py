"""Feature C: weight conversion."""

# Factors to kilograms
TO_KG = {"kg": 1.0, "g": 0.001, "lb": 0.45359237, "oz": 0.028349523125}


def convert_weight(value, from_unit, to_unit):
    if from_unit not in TO_KG or to_unit not in TO_KG:
        raise ValueError(f"Unsupported unit. Use one of: {sorted(TO_KG)}")
    if value < 0:
        raise ValueError("Weight cannot be negative")
    return value * TO_KG[from_unit] / TO_KG[to_unit]
