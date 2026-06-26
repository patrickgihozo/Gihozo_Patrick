#the object hides its internal data (__balance) and exposes only safe operations (deposit, withdraw, check_balance).
class Bank_Account:
    def __init__(self):
        self.__balance = 1000000
    def deposit(self,amount):
        self.__balance += amount
    def display_balance(self):
        return self.__balance      
    
Acc = Bank_Account()
Acc.deposit(100000)
print(Acc.display_balance())   
print(Acc.__balance)
    
    
    