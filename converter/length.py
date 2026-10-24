"""Feature A: length conversion."""

# Factors to metres
TO_METRES = {"m": 1.0, "km": 1000.0, "cm": 0.01, "mi": 1609.344, "ft": 0.3048}


def convert_length(value, from_unit, to_unit):
    if from_unit not in TO_METRES or to_unit not in TO_METRES:
        raise ValueError(f"Unsupported unit. Use one of: {sorted(TO_METRES)}")
    if value < 0:
        raise ValueError("Length cannot be negative")
    return value * TO_METRES[from_unit] / TO_METRES[to_unit]
