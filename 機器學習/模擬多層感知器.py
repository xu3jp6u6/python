# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:42:07 2020

@author: USER
"""

x1=int(input('輸入x1:'))
x2=int(input('輸入x2:'))


h1= x1 + x2 - 0.5
h2 = x1 + x2 - 1.5

if h1>0 and h2<0:
    out=1

else:
    out=0

print('out=',out)