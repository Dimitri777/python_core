"""
Portfolio: Built-in Types and Type Conversion
Topic: int, float, complex, bool, str; type(); conversion; no mixing types in math
"""


def show_type(value, name: str = "value"):
    """Print value and its type."""
    print(f"  {name} = {value!r}  ->  type: {type(value).__name__}")


def main():
    print("=== Built-in Types Demo ===\n")

    # Integers
    a = 42
    show_type(a, "int_example")

    # Floats
    b = 3.14
    show_type(b, "float_example")

    # Complex
    c = 2 + 3j
    show_type(c, "complex_example")

    # Boolean
    show_type(True, "bool_true")
    show_type(False, "bool_false")

    # Strings (sequence of characters)
    s = "hello"
    show_type(s, "str_example")

    # Type conversion
    print("\n--- Type conversion ---")
    show_type(int("100"), "int('100')")
    show_type(float("3.14"), "float('3.14')")
    show_type(str(42), "str(42)")
    show_type(bool(1), "bool(1)")
    show_type(bool(0), "bool(0)")

    # Important: cannot add number and string without conversion
    print("\n--- Mixing types (error demo) ---")
    x, y = 1, "1"
    print("  a = 1, b = '1'")
    try:
        z = x + y
    except TypeError as e:
        print(f"  a + b -> TypeError: {e}")
    print("  Correct: a + int(b) =", x + int(y))
    print("  Correct: str(a) + b =", str(x) + y)


if __name__ == "__main__":
    main()
