# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 21:52:31 2020

@author: USER
"""

import numpy as np


list=[]
for i in range(3):
    n =[eval(i) for i in input().split( )]
   
    list.append(n)
list = np.array(list)
list = list.reshape(3,3)
r, c = np.where(list == np.max(list)) 
print(r,c)
t, e = np.where(list == np.min(list)) 
print(t,e)