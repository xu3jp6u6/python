# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 08:51:44 2020

@author: USER
"""


import random
import matplotlib.pyplot as plt
import numpy as np
n=[] #設定空串列
b=0 #設定變數
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
k=0
l=0
for w in range(1001): #模擬兩個骰子，可以計算2-12間每個數字出現次數，請測試1000次
        x=random.randint(1, 6)
        y=random.randint(1, 6)
        a=x+y
        if a==2: #如果等於2~12，變數加1
            b+=1
        if a==3:
            c+=1
        if a==4:
            d+=1
        if a==5:
            e+=1
        if a==6:
            f+=1
        if a==7:
            g+=1
        if a==8:
            h+=1
        if a==9:
            i+=1
        if a==10:
            j+=1
        if a==11:
            k+=1
        if a==12:
            l+=1
n.append(b) #新增至串列
n.append(c)
n.append(d)
n.append(e)
n.append(f)
n.append(g)
n.append(h)
n.append(i)
n.append(j)
n.append(k)
n.append(l)
x=np.arange(2,13) #產生2~12的數
plt.bar(x,n,width=0.4,color='g') #畫長條圖
plt.show()

        
    
