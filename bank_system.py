# bank system
import random

class Account:

    def __init__(self, name, pno, mail, opening_amount):
        self.name = name
        self.pno = pno
        self.mail = mail
        self.__balance = opening_amount
        self.account_no = random.randint(518900000,598700000)

    def deposit_money(self,amount):
        self.__balance=self.__balance+amount
        print(f'{amount} got deposited into the account no. {self.account_no}')
        print('Do you want to check balance: y/n?')
        ans = input()
        if ans == 'y':
            return self.check_balance()
        else:
            return 'Thank you!'
        

    def withdraw_money(self,amount):
        if self.__balance-amount > 0:
            self.__balance=self.__balance-amount
            print(f'{amount} was withdrawn from the account no. {self.account_no}')
            print('Do you want to check balance: y/n?')
            ans = input()
            if ans == 'y':
                return self.check_balance()
            else:
                return 'Thank you!'
        return 'Insufficient balance'

    def check_balance(self):
        return f'your current balance is : {self.__balance}'
    
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