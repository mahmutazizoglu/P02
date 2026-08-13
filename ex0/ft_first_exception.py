#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    """Convert a temperature string into an integer. May raise ValueError."""
    return int(temp_str)

def test_temperature() -> None:
    """Run tests on input_temperature(), catching failures gracefully."""
    print("=== Garden Temperature ===\n")

    valid_input = "25"
    print(f"Input data is '{valid_input}'")
    temperature = input_temperature(valid_input)
    print(f"Temperatur is now {temperature}°C\n")

    invalid_input = "abc"
    print(f"Input data is '{invalid_input}'")
    try:
        input_temperature(invalid_input)
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")

    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()