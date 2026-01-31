"""
Portfolio: Bytes and Bytearray
Topic: bytes (immutable), bytearray (mutable), encode/decode
"""


def main():
    print("=== Bytes and Bytearray Demo ===\n")

    # String to bytes (encode)
    text = "Hello"
    encoded = text.encode("utf-8")
    print("String:", repr(text))
    print("Encoded (bytes):", encoded)
    print("Type:", type(encoded).__name__)

    # Bytes back to string (decode)
    decoded = encoded.decode("utf-8")
    print("Decoded:", repr(decoded))

    # bytes is immutable
    print("\n--- bytes is immutable ---")
    b = b"abc"
    try:
        b[0] = 65
    except TypeError as e:
        print("  b[0] = 65 -> TypeError:", e)

    # bytearray is mutable
    print("\n--- bytearray is mutable ---")
    ba = bytearray(b"abc")
    print("  Before:", ba)
    ba[0] = 65
    print("  After ba[0] = 65:", ba)
    print("  As string:", ba.decode("utf-8"))

    # Create from list of ints (0-255)
    ba2 = bytearray([72, 105])
    print("\n  bytearray([72, 105]):", ba2.decode("utf-8"))


if __name__ == "__main__":
    main()
