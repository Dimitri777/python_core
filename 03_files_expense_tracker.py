"""
Portfolio: Simple Expense Tracker (file-based)
Topic: work with files (read, write, append), text processing
"""

from datetime import datetime

DATA_FILE = "expenses.txt"


def load_expenses():
    """Load expense records from file."""
    expenses = []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) >= 3:
                    expenses.append({
                        "date": parts[0],
                        "category": parts[1],
                        "amount": float(parts[2]),
                        "comment": parts[3] if len(parts) > 3 else ""
                    })
    except FileNotFoundError:
        pass
    return expenses


def save_expenses(expenses):
    """Save all records to file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for e in expenses:
            comment = e.get("comment", "")
            f.write(f"{e['date']}|{e['category']}|{e['amount']}|{comment}\n")


def add_expense(expenses):
    category = input("Category (food, transport, entertainment, other): ").strip() or "other"
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Error: enter a number.")
        return
    comment = input("Comment (optional): ").strip()
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    expenses.append({"date": date, "category": category, "amount": amount, "comment": comment})
    save_expenses(expenses)
    print("Entry added.")


def show_summary(expenses):
    if not expenses:
        print("No entries yet.")
        return
    total = sum(e["amount"] for e in expenses)
    by_category = {}
    for e in expenses:
        cat = e["category"]
        by_category[cat] = by_category.get(cat, 0) + e["amount"]
    print(f"\nTotal expenses: {total:.2f}")
    print("By category:")
    for cat, amount in sorted(by_category.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {amount:.2f}")


def show_history(expenses, limit=10):
    if not expenses:
        print("No entries yet.")
        return
    print("\nRecent entries:")
    for e in reversed(expenses[-limit:]):
        print(f"  {e['date']} | {e['category']} | {e['amount']:.2f} | {e.get('comment', '')}")


def main():
    expenses = load_expenses()
    print("=== Expense Tracker (file-based) ===\n")

    while True:
        print("1 - Add expense")
        print("2 - Summary by category")
        print("3 - Entry history")
        print("0 - Quit")
        choice = input("\nChoice: ").strip()

        if choice == "0":
            break
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_summary(expenses)
        elif choice == "3":
            show_history(expenses)


if __name__ == "__main__":
    main()
