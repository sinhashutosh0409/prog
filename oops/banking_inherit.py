#inheritence
class Bank:
    interest_rate = 0.05
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.statement = []

    def deposit(self,amount):
        self.balance = self.balance + amount
        self.statement.append(f"amount deposited: {amount}")

    def withdraw(self,amount):
        self.balance = self.balance - amount
        self.statement.append(f"amount debited:{amount}")

    def roi(self):
        interest_amount = self.__class__.interest_rate * self.balance
        total = self.balance + interest_amount
        self.statement.append(f"interest credited:{interest_amount}")



class SavingsAccount(Bank):
    interest_rate = 0.06

    def deposit(self,amount):
        if amount <= 0:
            raise Exception("invalid amount")
        super().deposit(amount)

    def roi(self):
        super().roi()

    def withdraw(self,amount):
        if amount > 20000:
            raise Exception("withdrawal limit exceeds")





c1 = SavingsAccount("steve",2000)
c1.roi()
# c1.deposit(100000)
c1.withdraw(10000)

print(c1.__dict__)


