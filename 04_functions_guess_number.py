"""
Portfolio: Guess the Number Game
Topic: functions, parameters, return values, random
"""

import random


def get_secret(low: int = 1, high: int = 100) -> int:
    """Return a random number in range [low, high]."""
    return random.randint(low, high)


def get_guess(low: int, high: int) -> int | None:
    """Ask user for a number; return None on invalid input."""
    try:
        value = int(input(f"Your guess ({low}-{high}): "))
        if low <= value <= high:
            return value
    except ValueError:
        pass
    return None


def play_round(low: int = 1, high: int = 100, max_attempts: int = 10) -> bool:
    """
    One round of the game. Returns True if the user guessed correctly.
    """
    secret = get_secret(low, high)
    attempts = 0

    print(f"\nA number from {low} to {high} is chosen. You have up to {max_attempts} attempts.")

    while attempts < max_attempts:
        guess = get_guess(low, high)
        if guess is None:
            print("Enter an integer in the given range.")
            continue

        attempts += 1

        if guess == secret:
            print(f"Congratulations! You guessed in {attempts} attempts.")
            return True
        if guess < secret:
            print("Higher.")
        else:
            print("Lower.")

    print(f"Out of attempts. The number was {secret}.")
    return False


def main():
    print("=== Guess the Number ===\n")
    wins = 0
    rounds = 0

    while True:
        print("1 - Play (1-100)")
        print("2 - Play (custom range)")
        print("0 - Quit")
        choice = input("\nChoice: ").strip()

        if choice == "0":
            if rounds > 0:
                print(f"\nRounds: {rounds}, Wins: {wins}")
            print("Bye.")
            break

        if choice == "1":
            rounds += 1
            if play_round():
                wins += 1
        elif choice == "2":
            try:
                low = int(input("Minimum: "))
                high = int(input("Maximum: "))
                if low >= high:
                    print("Minimum must be less than maximum.")
                    continue
                rounds += 1
                if play_round(low, high):
                    wins += 1
            except ValueError:
                print("Enter integers.")


if __name__ == "__main__":
    main()
