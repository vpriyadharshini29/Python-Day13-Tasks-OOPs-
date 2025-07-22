# Account class with private balance and PIN
class Account:
    def __init__(self, account_number, name, pin, balance=0):
        self.account_number = account_number
        self.name = name
        self.__pin = pin
        self.__balance = balance

    def verify_pin(self, pin):
        return self.__pin == pin

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

# Transaction class
class Transaction:
    @staticmethod
    def transfer(from_acc, to_acc, amount):
        if from_acc.withdraw(amount):
            to_acc.deposit(amount)
            return True
        return False

# ATM class
class ATM:
    def __init__(self, account):
        self.account = account

    def withdraw(self, *args):
        """Overloaded withdraw method: allows single or multiple withdrawals."""
        for amount in args:
            if not self.account.withdraw(amount):
                print(f"Failed to withdraw ₹{amount}. Insufficient balance.")
            else:
                print(f"Withdrew ₹{amount} successfully.")

    def deposit(self, amount):
        if self.account.deposit(amount):
            print(f"Deposited ₹{amount} successfully.")
        else:
            print("Deposit failed.")

    def check_balance(self):
        print(f"Current Balance: ₹{self.account.get_balance()}")

# Example usage
acc1 = Account("123456", "John Doe", "4321", 5000)
acc2 = Account("789012", "Jane Smith", "1234", 3000)

atm = ATM(acc1)

if acc1.verify_pin("4321"):
    atm.deposit(1000)
    atm.withdraw(500, 800)  # Multiple withdrawals using *args
    atm.check_balance()
    print("\nTransferring ₹1500 to another account...")
    if Transaction.transfer(acc1, acc2, 1500):
        print("Transfer successful.")
    else:
        print("Transfer failed.")
else:
    print("Invalid PIN.")

print("\nRecipient Account Balance:", acc2.get_balance())
