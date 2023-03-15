# -*- coding: utf-8 -*-
"""
Created on Mon May 24 09:48:26 2021

@author: USER
"""

def compute(a,x,y):
    for i in range(y): #幾列
        for i in range(x):#幾行
            print(a,end=' ')
        print()#換行
a=input("輸入變數") #輸入變數
x=int(input("輸入行"))
y=int(input("輸入列"))   
print(compute(a,x,y))