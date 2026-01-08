class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount >= self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

bankAccount = BankAccount()
print(f"Initial Balance: {bankAccount.balance}")
bankAccount.deposit(1000)
print(f"Balance after deposit: {bankAccount.balance}")
bankAccount.withdraw(500)
print(f"Balance after withdrawal: {bankAccount.balance}")

bankAccount.balance = -1000  # Direct access to balance, breaks encapsulation
print(f"Balance after direct manipulation: {bankAccount.balance}")

### Better Approach with Encapsulation
class GoodBankAccount:
    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self,  amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount >= self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount

goodBankAccount = GoodBankAccount()
print(f"Initial Balance: {goodBankAccount.balance}")
goodBankAccount.deposit(1000)
print(f"Balance after deposit: {goodBankAccount.balance}")
goodBankAccount.withdraw(500)
print(f"Balance after withdrawal: {goodBankAccount.balance}")

# goodBankAccount.balance = -1000  # Attempt to directly access balance will raise an error
# print(f"Balance after direct manipulation attempt: {goodBankAccount.balance}")
