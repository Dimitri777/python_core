"""
Portfolio: Logical and Membership Operators
Topic: and, or, not; in, not in (for sequences, sets, dicts, strings)
"""


def main():
    print("=== Logical Operators (and, or, not) ===\n")

    a, b = True, False
    print("  a = True, b = False")
    print("  a and b =", a and b)
    print("  a or b =", a or b)
    print("  not a =", not a)
    print("  (a or b) and not (a and b) =", (a or b) and not (a and b))

    # Short-circuit
    print("\n  Condition: x > 0 and 1/x (safe when x=0):")
    x = 0
    result = x > 0 and (1 / x)  # no division by zero
    print("  x=0 -> result =", result)

    print("\n=== Membership Operators (in, not in) ===\n")

    # In string
    print("  'ab' in 'abc' =", "ab" in "abc")
    print("  'x' not in 'abc' =", "x" not in "abc")

    # In list
    lst = [1, 2, 3]
    print("  2 in [1,2,3] =", 2 in lst)
    print("  5 not in [1,2,3] =", 5 not in lst)

    # In tuple
    t = (10, 20)
    print("  10 in (10,20) =", 10 in t)

    # In set
    s = {1, 2, 3}
    print("  2 in {1,2,3} =", 2 in s)

    # In dict (checks keys)
    d = {"a": 1, "b": 2}
    print("  'a' in {'a':1,'b':2} =", "a" in d)
    print("  'c' not in d =", "c" not in d)


if __name__ == "__main__":
    main()
