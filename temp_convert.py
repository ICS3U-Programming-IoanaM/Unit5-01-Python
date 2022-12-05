#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu

# Date: Dec. 4, 2022
# a program that converts from celsius to fahrenheit


def celsius_to_fahrenheit():
    # getting user input
    temp_celsius_str = input("Enter temperature (celsius): ")

    # exception handling
    try:
        temp_celsius_float = float(temp_celsius_str)

    # input is invalid
    except Exception:
        print("Input invalid! Make sure your input is a number.")

    # input is valid
    else:
        # calculates fahrenheit
        temp_fahrenheit = 1.8 * temp_celsius_float + 32

        # displays results
        print(
            f"{temp_celsius_float:.2f}° celsius is {temp_fahrenheit:.2f}° fahrenheit."
        )


def main():
    # celsius to fahrenheit conversion function
    celsius_to_fahrenheit()


if __name__ == "__main__":
    main()
