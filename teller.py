
class Teller:
    def deposit(self,amount, account):
        account.deposit(amount)

class CorruptTeller(Teller):
    def __init__(self):
        self.coffers = 0

    def deposit(self, amount, account):
        self.coffers += amount * 0.01
        super().deposit(amount * 0.99, account)

class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount


bayo = Account()

print(bayo.balance)

Teller().deposit(100,  bayo)

print(bayo.balance)

CorruptTeller().deposit(20.25, bayo)

print(bayo.balance)

