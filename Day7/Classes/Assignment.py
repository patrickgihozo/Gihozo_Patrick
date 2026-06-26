class MobileMoney:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount} UGX")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount} ")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        return self.__balance


account = MobileMoney()

account.deposit(50000)
print("Balance:", account.check_balance())

account.withdraw(20000)
print("Balance after withdrawal:", account.check_balance())

account.withdraw(10000)
print("Balance after second withdrawal:", account.check_balance())