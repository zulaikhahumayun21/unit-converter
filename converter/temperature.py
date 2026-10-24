"""Feature B: temperature conversion."""

ABSOLUTE_ZERO_C = -273.15


def _to_celsius(value, unit):
    if unit == "C":
        return value
    if unit == "F":
        return (value - 32) * 5 / 9
    if unit == "K":
        return value - 273.15
    raise ValueError("Unsupported unit. Use C, F or K")


def convert_temperature(value, from_unit, to_unit):
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError("Temperature must be a number")

    if from_unit not in ("C", "F", "K"):
        raise ValueError("Unsupported unit. Use C, F or K")

    if to_unit not in ("C", "F", "K"):
        raise ValueError("Unsupported unit. Use C, F or K")

    celsius = _to_celsius(value, from_unit)

    if celsius < ABSOLUTE_ZERO_C - 1e-9:
        raise ValueError("Temperature is below absolute zero")

    if to_unit == "C":
        return celsius
    if to_unit == "F":
        return celsius * 9 / 5 + 32
    return celsius + 273.15
