"""
Portfolio: Password Generator & Strength Checker
Topic: for/while loops, random, strings
"""

import random
import string


def generate_password(length: int = 12, use_symbols: bool = True) -> str:
    """Generate a random password of given length."""
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    password = []
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice("!@#$%^&*"))

    while len(password) < length:
        password.append(random.choice(chars))

    random.shuffle(password)
    return "".join(password)


def check_strength(password: str) -> tuple[str, int]:
    """Rate password strength. Returns (description, score 0-100)."""
    score = 0

    if len(password) >= 8:
        score += 15
    if len(password) >= 12:
        score += 15
    if len(password) >= 16:
        score += 10

    has_upper = has_lower = has_digit = has_special = False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_special = True

    if has_upper:
        score += 15
    if has_lower:
        score += 15
    if has_digit:
        score += 15
    if has_special:
        score += 15

    if score >= 80:
        level = "Very strong"
    elif score >= 60:
        level = "Strong"
    elif score >= 40:
        level = "Medium"
    else:
        level = "Weak"

    return level, min(100, score)


def main():
    print("=== Password Generator & Strength Checker ===\n")

    while True:
        print("1 - Generate password")
        print("2 - Check your password")
        print("0 - Quit")
        choice = input("\nChoice: ").strip()

        if choice == "0":
            print("Bye.")
            break

        if choice == "1":
            try:
                length = int(input("Password length (8-32): ") or "12")
                length = max(8, min(32, length))
            except ValueError:
                length = 12
            use_sym = input("Include symbols !@#...? (y/n, default y): ").strip().lower() != "n"
            pwd = generate_password(length, use_sym)
            print(f"\nPassword: {pwd}")
            level, score = check_strength(pwd)
            print(f"Strength: {level} ({score} points)\n")

        elif choice == "2":
            pwd = input("Enter password: ")
            if not pwd:
                print("No password entered.\n")
                continue
            level, score = check_strength(pwd)
            print(f"Strength: {level} ({score} points)\n")


if __name__ == "__main__":
    main()
