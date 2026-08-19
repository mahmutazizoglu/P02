#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        result = 10 / 0
        print(result)
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        text = "text" + 5
        print(text)
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for operation_number in range(5):
        print(f"Testing operation {operation_number}...")
        try:
            garden_operations(operation_number)
            print("Operation completed successfully")
        except ValueError as err:
            print(f"Caught ValueError: {err}")
        except ZeroDivisionError as err:
            print(f"Caught ZeroDivisionError: {err}")
        except FileNotFoundError as err:
            print(f"Caught FileNotFoundError: {err}")
        except TypeError as err:
            print(f"Caught TypeError: {err}")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
