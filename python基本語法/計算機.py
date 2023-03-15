# -*- coding: utf-8 -*-
"""
Created on Sun May 16 14:45:47 2021

@author: USER
"""

def  calculator(x,y,z):#定義加減乘除
    a=x+y
    b=x-y
    c=x*y
    d=x/y
    if z==1:
        return a
    if z==2:
        return b
    if z==3:
        return c
    if z==4:
        return d
    
n=input('輸入:').split()#輸入
x=int(n[0])#轉整數
y=int(n[2])
if n[1]=='+':#如果是加，新增1
    n.append(1)
if n[1]=='-':#如果是減，新增2
    n.append(2)
if n[1]=='*':#如果是乘，新增3
    n.append(3)
if n[1]=='/':#如果是除，新增4
    n.append(4)
z=n[3] #定義變數Z的值
print('輸出:',calculator(x,y,z))