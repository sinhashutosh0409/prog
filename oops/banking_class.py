class BankAccount:

    interest_rate = 0.05

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.statement = []

    def Deposit(self,amount):
        self.balance = self.balance + amount
        self.statement.append(f"amount deposited:{amount}")
        return self.balance

    def Withdraw(self,amount):
        self.balance = self.balance - amount
        self.statement.append(f"amount withdrawn:{amount}")
        return self.balance


    def Passbook(self):
        for transaction in self.statement:
            print(transaction)

    def roi(self):
        interest = self.balance * BankAccount.interest_rate
        self.balance = self.balance + interest
        self.statement.append(f"interest credited:{interest}")
        return self.balance




p1 = BankAccount("mark", 2000)
p2 = BankAccount("peter", 1500)
print(p2.roi())

# print(p1.Deposit(1200))
# print(p1.Withdraw(100))
# print(p1.Withdraw(100))
# print(p1.Deposit(1200))
# print(p1.Deposit(1210))
# print(p1.Deposit(12120))
#
# print(BankAccount.Passbook(p1))



