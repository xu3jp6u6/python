# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 22:22:23 2020

@author: USER
"""


class CreateBankAccount:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.balance = 0

    

    def deposit(self, amount):
        if amount <= 0:
            print('必須要是正數')
        self.balance += amount
    
    
    def withdraw(self, amount): 
        if amount <= self.balance:
            self.balance -= amount
        else:
            print('餘額不足')


    def transfor(self,b):
        self.balance-=100
        b.balance+=100    

a = CreateBankAccount('123456', 'a') 
a.deposit(300)
a.withdraw(30)
print(a.balance) 

b = CreateBankAccount('789102', 'b') 
b.deposit(200)
b.withdraw(40)
print(b.balance) 


    


a.transfor(b)
print(a.balance)
print(b.balance) 

            
            
