"""Command-line entry point: python main.py <category> <value> <from> <to>"""
import sys

from converter.length import convert_length
from converter.temperature import convert_temperature
from converter.weight import convert_weight

CATEGORIES = {
    "length": convert_length,
    "temperature": convert_temperature,
    "weight": convert_weight,
}


def main(argv):
    if len(argv) != 5 or argv[1] not in CATEGORIES:
        print("Usage: python main.py <length|temperature|weight> <value> <from> <to>")
        return 1
    try:
        result = CATEGORIES[argv[1]](float(argv[2]), argv[3], argv[4])
    except ValueError as err:
        print(f"Error: {err}")
        return 1
    print(f"{argv[2]} {argv[3]} = {result:.4f} {argv[4]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
