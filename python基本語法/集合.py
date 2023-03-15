# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 20:36:25 2020

@author: USER
"""

a=[] #建立空串列

for i in range(1, 100, 2): #以間隔2加入集合
    a.append(i)
  

b=[] 

for i in range(0,101,5):#以間隔5加入集合
    b.append(i)
a=set(a) #建立集合
b=set(b)
print(a&b,end="\n\n") #顯示交集
print(a|b,end="\n\n") #顯示聯集
print(a-b,end="\n\n") #顯示A-B、B-A、A-B對稱差集
print(b-a,end="\n\n")
print(a^b,end="\n\n")
print(b^a,end="\n\n")