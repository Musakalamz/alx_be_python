"""Bank account domain model encapsulating basic banking operations.

This class demonstrates core OOP concepts:
- Encapsulation of the `account_balance` state
- Behaviors via instance methods (deposit, withdraw, display)
"""


class BankAccount:
    """Represents a simple bank account with a balance."""

    def __init__(self, initial_balance: float = 0):
        """Initialize the account with an optional starting balance.

        Args:
            initial_balance: Starting balance for the account (defaults to 0).
        """
        self.account_balance = float(initial_balance)

    def deposit(self, amount: float) -> None:
        """Deposit funds into the account.

        Args:
            amount: The amount to add to the balance.
        """
        self.account_balance += float(amount)

    def withdraw(self, amount: float) -> bool:
        """Attempt to withdraw funds from the account.

        Performs a sufficient-funds check, returning a boolean to indicate
        success and leaving the balance unchanged if insufficient.

        Args:
            amount: The amount to withdraw.

        Returns:
            True if the withdrawal succeeded; otherwise False.
        """
        amount = float(amount)
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self) -> None:
        """Print the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")

