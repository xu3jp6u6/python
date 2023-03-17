# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:51:31 2020

@author: USER
"""

import math
a=int(input('輸入三個整數:'))
b=int(input('輸入三個整數:'))
c=int(input('輸入三個整數:'))
def compute(): #實數公式解
    f=b**2-4*a*c
    if f>0:
        x1=(-b+math.sqrt(f))/2*a
        x2=(-b-math.sqrt(f))/2*a
    if f<0:
         print('Your equation has no root.')
         return(None,None)
    return (x1,x2)
print('x=',compute())
