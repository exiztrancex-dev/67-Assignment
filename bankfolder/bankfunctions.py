import random

#Forming basic bank account
class bank_account: 
    def __init__(self, name):
        self.total = 0 
        self.account_number = random.randint(1, 10000)
        self.name = name
        



    def make_deposit (self, amount_added):
        self.total += amount_added





    def make_withdrawl (self, amount_subtracted ):
        self.total -= amount_subtracted


    
    #displaying account info
    def account_info (self, amount_in_bank, name, account_number):
        print(f"Name: {name}")
        print(f"Account #: {account_number}")
        print(f"Balance: ${amount_in_bank}")