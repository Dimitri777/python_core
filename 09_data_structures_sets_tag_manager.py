"""
Portfolio: Unique Tag Manager (set operations)
Topic: set, add, remove, union, intersection, difference
"""


def main():
    tags: set[str] = set()
    print("=== Unique Tag Manager (sets) ===\n")
    print("Commands: add, remove, list, union, intersect, diff, clear, quit")

    while True:
        cmd = input("\nCommand: ").strip().lower()
        if not cmd:
            continue

        if cmd == "quit":
            print("Bye.")
            break

        if cmd == "add":
            line = input("Tags (space-separated): ").strip()
            for t in line.split():
                tags.add(t.strip())
            print(f"Tags: {tags}")

        elif cmd == "remove":
            t = input("Tag to remove: ").strip()
            if t in tags:
                tags.discard(t)
                print(f"Removed. Tags: {tags}")
            else:
                print("Tag not found.")

        elif cmd == "list":
            print(f"Tags ({len(tags)}): {sorted(tags) if tags else '(empty)'}")

        elif cmd == "union":
            line = input("Second set (space-separated): ").strip()
            other = set(line.split())
            result = tags | other
            print(f"Union: {result}")

        elif cmd == "intersect":
            line = input("Second set (space-separated): ").strip()
            other = set(line.split())
            result = tags & other
            print(f"Intersection: {result}")

        elif cmd == "diff":
            line = input("Second set (space-separated): ").strip()
            other = set(line.split())
            result = tags - other
            print(f"Difference (current - other): {result}")

        elif cmd == "clear":
            tags.clear()
            print("Tags cleared.")
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
