class BankAccount:
    def __init__(self, initial_balance: float = 0):
        self.account_balance = float(initial_balance)

    def deposit(self, amount: float) -> None:
        self.account_balance += float(amount)

    def withdraw(self, amount: float) -> bool:
        amount = float(amount)
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self) -> None:
        print(f"Current Balance: ${self.account_balance}")

