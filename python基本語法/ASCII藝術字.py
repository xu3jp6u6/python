# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:17:03 2020

@author: USER
"""

import sys
 
FONTCOL=4
FONTROW=5
 
zero=(" ** ",
      "*  *",
      "*  *",
      "*  *",
      " ** ")
 
one= ("  * ",
      " ** ",
      "  * ",
      "  * ",
      " ***")
 
two= (" ** ",
      "*  *",
      "  * ",
      " *  ",
      "****")
 
three=(" ** ",
       "*  *",
       "  **",
       "*  *",
       " ** ")
 
four= ("  * ",
       " ** ",
       "* * ",
       "****",
       "  * ")
 
five= ("****",
       "*   ",
       "****",
       "   *",
       "****")
 
six=  (" ** ",
       "*   ",
       "*** ",
       "*  *",
       " ** ")
 
seven=(" ***",
       "*  *",
       "  * ",
       "  * ",
       " ***")
 
eight=(" ** ",
       "*  *",
       " ** ",
       "*  *",
       " ** ")
 
nine= (" ** ",
       "*  *",
       " ***",
       "   *",
       " ** ")
digits=(zero,one,two,three,four,five,six,seven,eight,nine) 
 #ASCII藝術字
def show_number(nums):
    i=0
    while i<FONTROW:
        col=0
        while col<len(nums): 
            print(digits[int(nums[col])][i],end=" ")#顯示ASCII藝術字中的每個字符
            col+=1
        print("")
        i+=1
def show_usage():
    
    show_number('2987340')
 
if len(sys.argv)==2:
    show_number(sys.argv[1])
else:
    show_usage()





