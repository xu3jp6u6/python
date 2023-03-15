# -*- coding: utf-8 -*-
"""
Created on Mon May 31 11:41:34 2021

@author: USER
"""

class Myschool: #定義類別
    def __init__ (self,title): #定義title
        self.title=title 
        self.n=[] #建立空集合
    def departments(self): #定義加入的集合
        self.n.append('資工') #加入集合
        self.n.append( '電機'  )
        self.n.append( '電機'  )
    def add(self,a):#定義加入的集合
        self.n.append(a)
    def omit(self,o):#定義刪除的集合
        self.n.pop(o)
b =  Myschool("東海大學",) #定義學校
b.departments()#加入空集合
print(b.n)#顯示集合
b.add('建築')#加入集合
print(b.n)#顯示集合
b.omit(0)#刪除集合
print(b.n)#顯示集合
