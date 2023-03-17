# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 16:20:48 2020

@author: User
"""

import matplotlib.pyplot as plt

Benz=[ 3367, 4120 ,5539 , 6020 , 6620]
BMW =[4000   ,  3590   ,   4423  ,    4900  ,    4590]
Lexus=[5200  ,   4930   ,   5350   ,   6200    ,  6930]

seq=[2018,2019,2020,2021,2022]
plt.xticks(seq)
plt.plot(seq,Benz,label='Benz')
plt.plot(seq,BMW,label='BMW')
plt.plot(seq,Lexus,label='Lexus')
plt.legend(loc='best')
plt.show()
#2018~2022汽車銷量折線圖
