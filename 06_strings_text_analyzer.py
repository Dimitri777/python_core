"""
Portfolio: Text Analyzer (palindrome, stats, Caesar cipher)
Topic: strings, slicing, methods, encoding
"""


def is_palindrome(text: str) -> bool:
    """Check if text is a palindrome (ignore spaces and case)."""
    cleaned = "".join(c for c in text.lower() if c.isalnum())
    return cleaned == cleaned[::-1]


def text_stats(text: str) -> dict:
    """Basic text statistics."""
    words = text.split()
    return {
        "chars": len(text),
        "chars_no_spaces": len(text.replace(" ", "")),
        "words": len(words),
        "sentences": text.count(".") + text.count("!") + text.count("?"),
    }


def caesar_cipher(text: str, shift: int, decode: bool = False) -> str:
    """Caesar cipher for Latin letters. decode=True for deciphering."""
    if decode:
        shift = -shift
    result = []
    for c in text:
        if "A" <= c <= "Z":
            result.append(chr((ord(c) - ord("A") + shift) % 26 + ord("A")))
        elif "a" <= c <= "z":
            result.append(chr((ord(c) - ord("a") + shift) % 26 + ord("a")))
        else:
            result.append(c)
    return "".join(result)


def main():
    print("=== Text Analyzer ===\n")

    while True:
        print("1 - Palindrome check")
        print("2 - Text statistics")
        print("3 - Caesar cipher (encode)")
        print("4 - Caesar cipher (decode)")
        print("0 - Quit")
        choice = input("\nChoice: ").strip()

        if choice == "0":
            break

        if choice == "1":
            text = input("Enter string: ").strip()
            if text:
                print("Yes, it's a palindrome." if is_palindrome(text) else "No, not a palindrome.")

        elif choice == "2":
            text = input("Enter text (multiple lines ok; empty line to finish):\n")
            lines = [text]
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            full = "\n".join(lines)
            stats = text_stats(full)
            print(f"Characters: {stats['chars']}, without spaces: {stats['chars_no_spaces']}")
            print(f"Words: {stats['words']}, sentences: {stats['sentences']}")

        elif choice in ("3", "4"):
            text = input("Text: ")
            try:
                shift = int(input("Shift (1-25): "))
                shift = max(1, min(25, shift))
            except ValueError:
                shift = 3
            decoded = choice == "4"
            result = caesar_cipher(text, shift, decode=decoded)
            print("Result:", result)


if __name__ == "__main__":
    main()
