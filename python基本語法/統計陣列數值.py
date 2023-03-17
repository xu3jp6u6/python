# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:51:53 2020

@author: User
"""


list=[]
for i in range(10):
    list.append(eval(input()))
a=(list[5]+list[4])/2
print('中位數:',a)
b=(list[0]+list[1]+list[2]+list[3]+list[4]+list[5]+list[6]+list[7]+list[8]+list[9])/10
print('平均數:',b)
maxc=0
for i in range(10):
      if list.count(list[i])>maxc:
        maxc=list.count(list[i])
        n=list[i]
print('眾數:',n)

        
    
   
    

