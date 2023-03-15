# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 17:20:50 2021

@author: USER
"""

import numpy as np #導入numpy
list=[] #建立空串列
for i in range(2):#迴圈二次
    n =[eval(i) for i in input().split( )] #n=i
    list.append(n) #導入n至字串
list = np.array(list) #建立矩陣
list = list.reshape(2,2) #等於2x2的矩陣
a=list[0][0]*list[1][1]-list[0][1]*list[1][0] #計算行列式
print('矩陣的行列式值:',a)#顯示行列式