# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 22:12:14 2020

@author: USER
"""


a=int(input('輸入三個正整數:'))
b=int(input('輸入三個正整數:'))
c=int(input('輸入三個正整數:'))
def f(a,b,c):
    if a<b and a<c:
        d=a
    elif b<a and b<c:
        d=b
    else:
        d=c #求最小值
    for i in range (1,d+1):
        if ((a%i==0)and(b%i==0)and(c%i==0)):
            f=i #三個數皆要能整除
    return f 
print('最大公因數',f(a,b,c))    
