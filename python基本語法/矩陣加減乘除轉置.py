# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 23:36:54 2020

@author: USER
"""

import numpy as np

A = np.array([2,2,2,2,2,2])

c = A.reshape(3,2)


B = np.array([1,4,2,5,3,6])

d = B.reshape(3,2)

f=c+d #相加

g=c-d #相減

h=c*d #相乘

i=c/d #相除

j=c.T #轉置

k=d.T #轉置

print(c)
print()
print(d)
print()
print(f)
print()
print(g)
print()
print(h)
print()
print(i)
print()
print(j)
print()
print(k)
