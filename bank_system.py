# bank system
import random

class Account:

    def __init__(self, name, pno, mail, opening_amount):
        self.name = name
        self.pno = pno
        self.mail = mail
        self.balance = opening_amount
        self.account_no = random.randint(518900000,598700000)

    def delete_account(self):
        pass

    def deposit_money(self,amount):
        self.balance=self.balance+amount
        return f'your current balance is : {self.balance}'

    def withdraw_money(self,amount):
        if self.balance-amount > 0:
            self.balance=self.balance-amount
            return f'your current balance is : {self.balance}'
        return 'Insufficient balance'

    def check_balance(self):
        return f'your current balance is : {self.balance}'
    
    def __str__(self):
        return f"Name: {self.name}\nPhone no.: {self.pno}\nMail ID: {self.mail}\nBalance: {self.balance}"


if __name__=='__main__':
    
    ah1 = Account('vipul','1234567890','vipul@gmail.com',12000)
    print(ah1)

'''
input = name, no, mail id, account balance = 10,000
generate acoount no. for that person
and store the ah details in a list -> class variable
create these 4 functions -
1. delete account
2. deposit money
3. withdraw money
4. check balance

'''