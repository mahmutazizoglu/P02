#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    valid_input = "25"
    print(f"Input data is '{valid_input}'")
    try:
        temperature: int = input_temperature(valid_input)
        print(f"Temperature is now {temperature}°C\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")

    invalid_input = "abc"
    print(f"Input data is '{invalid_input}'")
    try:
        temperature2: int = input_temperature(invalid_input)
        print(f"Temperature is now {temperature2}°C\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
