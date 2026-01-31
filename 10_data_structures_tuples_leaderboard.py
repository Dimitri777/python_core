"""
Portfolio: Score Leaderboard (immutable records)
Topic: tuple, named records, sorting, unpacking
"""

from operator import itemgetter


def main():
    # Each record: (name, score) - immutable tuple
    leaderboard: list[tuple[str, int]] = []
    print("=== Score Leaderboard (tuples) ===\n")
    print("Commands: add, top, list, quit")

    while True:
        cmd = input("\nCommand: ").strip().lower()
        if not cmd:
            continue

        if cmd == "quit":
            print("Bye.")
            break

        if cmd == "add":
            name = input("Player name: ").strip()
            if not name:
                print("Name required.")
                continue
            try:
                score = int(input("Score: "))
            except ValueError:
                print("Enter a number.")
                continue
            leaderboard.append((name, score))
            print(f"Added: {name} = {score}")

        elif cmd == "top":
            n = input("How many (default 5): ").strip() or "5"
            try:
                k = max(1, min(len(leaderboard), int(n)))
            except ValueError:
                k = min(5, len(leaderboard))
            if not leaderboard:
                print("No entries yet.")
                continue
            sorted_board = sorted(leaderboard, key=itemgetter(1), reverse=True)
            print("Top scores:")
            for i, (player, pts) in enumerate(sorted_board[:k], 1):
                print(f"  {i}. {player}: {pts}")

        elif cmd == "list":
            if not leaderboard:
                print("No entries yet.")
                continue
            for name, score in leaderboard:
                print(f"  {name}: {score}")
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
