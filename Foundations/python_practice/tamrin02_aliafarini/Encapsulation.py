"""
Problem:
Refactor BankAccount to make balance private, and provide a getter,
validation, and an is_overdrawn property.
"""

# Represents a bank account with a private balance.
class BankAccount:
    # Constructor to initialize owner and private balance.
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.__balance = balance

    # Method to add money with validation.
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit successful. New balance: ${self.__balance:.2f}")
        else:
            print("Deposit failed. Amount must be positive.")

    # Method to remove money with validation.
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal failed. Amount must be positive.")
        elif amount > self.__balance:
            print("Withdrawal failed. Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrawal successful. New balance: ${self.__balance:.2f}")

    # Read-only accessor for the private balance.
    def get_balance(self):
        return self.__balance

    # Property to check if the account is overdrawn.
    @property
    def is_overdrawn(self):
        return self.__balance < 0

    # String representation of the account.
    def __str__(self):
        return f"Account Owner: {self.owner}, Balance: ${self.__balance:.2f}"

# --- Test Script ---
# This block runs only when the script is executed directly.
if __name__ == "__main__":
    account1 = BankAccount("Ali Afarini", 500)
    print(account1)
    account1.withdraw(600)
    print(f"Is overdrawn? {account1.is_overdrawn}")