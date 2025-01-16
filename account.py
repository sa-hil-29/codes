class Account:
    def __init__(self, balance, account_no):
        self.account_no = account_no
        self.balance = balance

    def credit(self,amount):
        if (amount > 0):
            self.balance += amount
            print("rs.",amount," credited in account")
            print("Total balance is: ",self.get_balance())
        else:
            print("Not a valid amount to credit")

    def debit(self,amount):
        if (amount > 0 and amount <= self.balance):
            self.balance -= amount
            print("rs.",amount," debited from your account")
            print("Remaining balance is: ",self.get_balance())

        else:
            print("Not a valid amount to debit")

    def get_balance(self):
        return self.balance

acc1 = Account(500.00,1234)
print(acc1.get_balance())

