# Problem
# Create a class BankAccount with attributes owner and balance (default 0). Implement methods:
#● deposit(amount) (adds to balance; reject negative amounts),
#● withdraw(amount) (subtracts if sufficient funds; otherwise print an error),
#● __str__ to display "owner: balance".
#Write a short script that creates two accounts, performs a few operations, and prints results.

# A blueprint for creating bank account objects.
class BankAccount:
    """Represents a simple bank account with an owner and balance."""

    # The constructor, called when a new BankAccount object is created.
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    # Method to add a positive amount to the balance.
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful. New balance: ${self.balance:.2f}")
        else:
            print("Deposit failed. Amount must be positive.")

    # Method to subtract an amount if funds are sufficient.
    def withdraw(self, amount):
        # IMPROVEMENT: Also check if the withdrawal amount is positive.
        if amount <= 0:
            print("Withdrawal failed. Amount must be positive.")
        elif amount > self.balance:
            print("Withdrawal failed. Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: ${self.balance:.2f}")

    # Special method to define the string representation of the object.
    def __str__(self):
        # Using :.2f to format the balance as currency.
        return f"Account Owner: {self.owner}, Balance: ${self.balance:.2f}"

# A standard main block to run the test script.
# This code only runs when this file is executed directly.
if __name__ == "__main__":
    
    # --- Test Script ---
    print("--- Creating and testing Ali's account ---")
    ali_account = BankAccount("ali afarini", 100)
    print(ali_account)  # Initial state
    ali_account.deposit(50)
    ali_account.withdraw(30)
    print(ali_account)  # Final state

    print("\n--- Creating and testing Sepideh's account ---")
    sepideh_account = BankAccount("sepideh fallah", 200)
    print(sepideh_account) # Initial state
    sepideh_account.withdraw(250)      # Test insufficient funds
    sepideh_account.deposit(-20)       # Test negative deposit
    sepideh_account.withdraw(-50)      # Test negative withdrawal
    sepideh_account.deposit(100)
    print(sepideh_account) # Final state
