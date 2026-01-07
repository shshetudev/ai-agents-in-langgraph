class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.owner}'s new balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    # Static method
    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5


account = BankAccount("Alice", 500)
account.deposit(200)

# Using static method
print(BankAccount.is_valid_interest_rate(3))  # Output: True
print(BankAccount.is_valid_interest_rate(10))  # Output: False