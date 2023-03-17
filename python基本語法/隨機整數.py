# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 21:18:32 2020

@author: USER
"""

import random 

def main(n):
    
    for i in range(n):
        a=random.randint(0,100)
        if i%10==0:
            print()
            
        print(a,end=" ")
      #求0~100隨機可以被10整除的數  
n=int(input('請輸入一個整數:'))
main(n)


    
