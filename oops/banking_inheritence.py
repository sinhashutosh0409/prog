class Bank:
    interest_rate=0.05

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.passbook = []

    def deposit(self,amount):
        if amount <=0:
            raise Exception("invalid amount")
        self.balance = self.balance+amount
        self.passbook.append(f"amount deposited:{amount}")

    def withdraw(self,amount):
        if amount > self.balance:
            raise Exception("insufficient funds")
        self.balance = self.balance - amount
        self.passbook.append(f"amount debited: {amount}")

    def transfer(self,to_account,amount):
        if amount > self.balance:
            raise Exception("insufficient funds")
        self.balance = self.balance - amount
        to_account.deposit(amount)
        self.passbook.append(f"amount transferred:{amount}")


    def statement(self):
        for transaction in self.passbook:
            print(transaction)


    def roi(self):
        interest = self.__class__.interest_rate * self.balance
        interest_added = self.balance + interest
        self.passbook.append(f"interest credited: {interest}")


class SavingsAccount(Bank):
    interest_rate = 0.06

    def withdraw(self,amount):
        if amount >= 20000:
            raise Exception("limit exceeds")
        super().withdraw(amount)

    def roi(self):
        super().roi()


class SalaryAccount(Bank):
    max_draft_amount = 10000
    first_month_bonus = 1000

    def __init__(self,name):
        self.draft_amount = 0
        self.is_first_month = True
        super().__init__(name,0)


    def deposit(self,amount):
        if self.is_first_month:
            super().deposit(amount + self.__class__.first_month_bonus)
            self.is_first_month = False
        else:
            super().deposit(amount)

    def over_draft(self,amount):
        if self.draft_amount + amount <= SalaryAccount.max_draft_amount:
            super().deposit(amount)
            self.draft_amount += amount
        else:
            raise Exception("limit exceeds")

c1 = SalaryAccount("steve")
c1.over_draft(1500)
c1.deposit(5000)
c1.deposit(1000)
print(c1.__dict__)
