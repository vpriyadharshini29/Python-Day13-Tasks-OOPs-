# Base Account class
class Account:
    def __init__(self, account_number, holder_name, initial_balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.__balance = initial_balance  # Encapsulated

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New Balance: ₹{self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}. New Balance: ₹{self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

    def transfer(self, target_account, amount):
        if amount <= self.__balance:
            self.withdraw(amount)
            target_account.deposit(amount)
        else:
            print("Insufficient balance for transfer.")

# SavingsAccount with withdrawal limit
class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance=0):
        super().__init__(account_number, holder_name, balance)
        self.withdrawal_limit = 25000

    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            print(f"Cannot withdraw more than ₹{self.withdrawal_limit} from savings account.")
        else:
            super().withdraw(amount)

# CurrentAccount with overdraft allowed
class CurrentAccount(Account):
    def __init__(self, account_number, holder_name, balance=0):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = -5000

    def withdraw(self, amount):
        if self.get_balance() - amount < self.overdraft_limit:
            print("Overdraft limit reached.")
        else:
            super().withdraw(amount)

# Transaction log class (could be expanded further)
class Transaction:
    def __init__(self, txn_type, amount, account):
        self.txn_type = txn_type
        self.amount = amount
        self.account = account

    def display(self):
        print(f"{self.txn_type} of ₹{self.amount} for Account {self.account.account_number}")

# Example Usage
s_acc = SavingsAccount("S1001", "Aarav", 30000)
c_acc = CurrentAccount("C2001", "Neha", 10000)

s_acc.withdraw(20000)
s_acc.withdraw(30000)  # Exceeds limit
s_acc.deposit(5000)
print("Savings Balance:", s_acc.get_balance())

c_acc.withdraw(14000)  # Should allow (down to -4000)
c_acc.withdraw(2000)   # Exceeds overdraft
c_acc.deposit(6000)
print("Current Balance:", c_acc.get_balance())
