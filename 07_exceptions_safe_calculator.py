"""
Portfolio: Safe Calculator with Input Validation
Topic: try/except, custom messages, robust input handling
"""


def get_number(prompt: str):
    """Ask user for a number; return None on error."""
    try:
        return float(input(prompt).strip().replace(",", "."))
    except ValueError:
        return None


def calculate(a: float, op: str, b: float) -> float | None:
    """Perform one operation. Return None on error (e.g. division by zero)."""
    try:
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            if b == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return a / b
        if op == "**":
            return a ** b
        return None
    except (ZeroDivisionError, OverflowError) as e:
        print(f"Calculation error: {e}")
        return None


def main():
    print("=== Safe Calculator ===\n")
    print("Supported: + - * / **")

    while True:
        a = get_number("First number (or Enter to quit): ")
        if a is None:
            choice = input("Retry or quit? (q = quit): ").strip().lower()
            if choice == "q":
                break
            continue

        op = input("Operation (+, -, *, /, **): ").strip()
        if op not in ("+", "-", "*", "/", "**"):
            print("Unknown operation.")
            continue

        b = get_number("Second number: ")
        if b is None:
            print("Enter a number.")
            continue

        result = calculate(a, op, b)
        if result is not None:
            print(f"Result: {result}")

        again = input("Another calculation? (y/n): ").strip().lower()
        if again == "n":
            break

    print("Bye.")


if __name__ == "__main__":
    main()
