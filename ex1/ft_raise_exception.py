#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)

    if temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")
    if temperature < 0:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")

    return temperature


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")

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

    input3 = "100"
    print(f"Input data is '{input3}'")
    try:
        temperature3: int = input_temperature(input3)
        print(f"Temperature is now {temperature3}°C\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")

    input4 = "-50"
    print(f"Input data is '{input4}'")
    try:
        temperature4: int = input_temperature(input4)
        print(f"Temperature is now {temperature4}°C\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
