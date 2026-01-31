"""
Portfolio: CSV (read, write)
Topic: csv module - read and write CSV files
"""

import csv

DATA_FILE = "csv_demo_data.csv"


def main():
    print("=== CSV Module Demo ===\n")

    # Write CSV
    rows = [
        ["name", "score", "grade"],
        ["Alice", 95, "A"],
        ["Bob", 80, "B"],
        ["Carol", 72, "C"],
    ]
    with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"  Written to {DATA_FILE}")

    # Read CSV
    print("\n--- Reading CSV ---")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print("  ", row)

    # Read as dict (header as keys)
    print("\n--- csv.DictReader ---")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print("  ", dict(row))


if __name__ == "__main__":
    main()
