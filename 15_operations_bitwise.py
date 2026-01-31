"""
Portfolio: Bitwise Operators
Topic: & (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), >> (right shift)
"""


def main():
    print("=== Bitwise Operators Demo ===\n")

    a, b = 12, 10  # 1100, 1010 in binary
    print("  a = 12 (binary:", bin(a), "), b = 10 (binary:", bin(b), ")")

    print("\n  a & b  (AND)  =", a & b, "->", bin(a & b))
    print("  a | b  (OR)   =", a | b, "->", bin(a | b))
    print("  a ^ b  (XOR)  =", a ^ b, "->", bin(a ^ b))
    print("  ~a     (NOT)  =", ~a, "->", bin(~a & 0xFF))
    print("  a << 1 (left) =", a << 1, "->", bin(a << 1))
    print("  a >> 1 (right)=", a >> 1, "->", bin(a >> 1))

    # Simple use: check/set flags
    print("\n--- Flags example ---")
    READ, WRITE, EXEC = 4, 2, 1
    perm = READ | WRITE
    print("  READ=4, WRITE=2, EXEC=1")
    print("  perm = READ | WRITE =", perm)
    print("  Has READ?", bool(perm & READ))
    print("  Has EXEC?", bool(perm & EXEC))


if __name__ == "__main__":
    main()
