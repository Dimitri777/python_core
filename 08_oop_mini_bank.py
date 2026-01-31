"""
Portfolio: Mini Banking System (OOP)
Topic: classes, __init__, methods, encapsulation
"""


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = balance
        self._history = []

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            print("Amount must be positive.")
            return False
        self._balance += amount
        self._history.append(f"+{amount:.2f}")
        print(f"Deposited: {amount:.2f}. Balance: {self._balance:.2f}")
        return True

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Amount must be positive.")
            return False
        if amount > self._balance:
            print("Insufficient funds.")
            return False
        self._balance -= amount
        self._history.append(f"-{amount:.2f}")
        print(f"Withdrawn: {amount:.2f}. Balance: {self._balance:.2f}")
        return True

    def get_balance(self) -> float:
        return self._balance

    def show_history(self, last_n: int = 10):
        if not self._history:
            print("History is empty.")
            return
        for entry in self._history[-last_n:]:
            print(f"  {entry}")


def main():
    print("=== Mini Bank (OOP) ===\n")
    name = input("Account owner name: ").strip() or "Customer"
    account = BankAccount(name)

    while True:
        print("\n1 - Deposit")
        print("2 - Withdraw")
        print("3 - Balance")
        print("4 - Transaction history")
        print("0 - Quit")
        choice = input("Choice: ").strip()

        if choice == "0":
            print(f"Bye, {account.owner}!")
            break

        if choice == "1":
            try:
                amount = float(input("Amount: ").replace(",", "."))
                account.deposit(amount)
            except ValueError:
                print("Enter a number.")
        elif choice == "2":
            try:
                amount = float(input("Amount: ").replace(",", "."))
                account.withdraw(amount)
            except ValueError:
                print("Enter a number.")
        elif choice == "3":
            print(f"Balance: {account.get_balance():.2f}")
        elif choice == "4":
            account.show_history()


if __name__ == "__main__":
    main()
