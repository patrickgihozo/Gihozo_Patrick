class Transaction:
    def __init__(self, employee_name, balance):
        self.employee_name = employee_name
        self.balance = balance

    def process(self):
        print("Processing transaction...")

class Deposit(Transaction):
    def deposit(self, amount, bonus=0):
        self.balance += amount + bonus
        print(f"Deposited: {amount}")
        if bonus:
            print(f"Bonus Added: {bonus}")
            
    def process(self):
        print("Processing Deposit Transaction")

class Withdrawal(Transaction):

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient funds")

    # Method Overriding
    def process(self):
        print("Processing Withdrawal Transaction")


# Transfer Transaction
class Transfer(Transaction):

    def transfer(self, receiver, amount):
        if amount <= self.balance:
            self.balance -= amount
            receiver.balance += amount

            print(
                f"{self.employee_name} transferred {amount} to {receiver.employee_name}"
            )
        else:
            print("Insufficient funds")

    # Method Overriding
    def process(self):
        print("Processing Transfer Transaction")


# -----------------------------------
# DEMONSTRATION
# -----------------------------------

employee1 = Transfer("Patrick", 5000)
employee2 = Transfer("Belinda", 2000)

print("Initial Balances")
print(employee1.employee_name, employee1.balance)
print(employee2.employee_name, employee2.balance)

print("\n--- Deposit ---")
deposit_txn = Deposit("Patrick", employee1.balance)

deposit_txn.process()      # Overridden method
deposit_txn.deposit(1000)  # Normal deposit
deposit_txn.deposit(500, 100)  # Overloaded version with bonus

employee1.balance = deposit_txn.balance

print("Balance:", employee1.balance)

print("\n--- Withdrawal ---")
withdraw_txn = Withdrawal("Patrick", employee1.balance)

withdraw_txn.process()     # Overridden method
withdraw_txn.withdraw(1500)

employee1.balance = withdraw_txn.balance

print("Balance:", employee1.balance)

print("\n--- Transfer ---")
employee1.process()        # Overridden method

employee1.transfer(employee2, 2000)

print("\nFinal Balances")
print(employee1.employee_name, employee1.balance)
print(employee2.employee_name, employee2.balance)