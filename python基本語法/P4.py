# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 20:05:05 2021

@author: USER
"""

n=int(input('輸入一整數'))
x=0
for i in range(1,n+1,2): #建立奇數
    x+=i
    
print(x)
n=int(input('輸入一整數'))
y=1
for i in range(2,n+1): #建立2到n的整數
    if i%2==0: #如果整除於0
        b=i
    else: 
        b=-i
    
    y+=b
print(y)

n=int(input('輸入一整數'))
k=0
for i in range(1,n+1): #建立1到n的整數
    k+=(i/n)
print(k)