#!/usr/bin/env python3
"""Convert temperatures between Celsius and Fahrenheit."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("value", type=float, help="temperature value")
    parser.add_argument("--from-unit", choices=("c", "f"), default="c")
    args = parser.parse_args()

    if args.from_unit == "c":
        result = (args.value * 9 / 5) + 32
        print(f"{args.value:.1f}°C = {result:.1f}°F")
    else:
        result = (args.value - 32) * 5 / 9
        print(f"{args.value:.1f}°F = {result:.1f}°C")


if __name__ == "__main__":
    main()
