# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 23:16:27 2020

@author: USER
"""

import matplotlib.pyplot as plt

data1 = [1, 2, 3, 4, 5, 6, 7, 8]
data2 = [1, 4, 9, 16, 25, 36, 49, 64]
data3 = [1, 3, 6, 10, 15, 21, 28, 36]
data4 = [1, 7, 15, 26, 40, 57, 77, 100]

seq=[1,2,3,4,5,6,7,8] 

plt.subplot(2,2,1)
plt.plot(seq,data1,'-*')
plt.subplot(2,2,2)
plt.plot(seq,data2,'-o')
plt.subplot(2,2,3)
plt.plot(seq,data3,'-^')
plt.subplot(2,2,4)
plt.plot(seq,data4,'-s')
plt.show()#顯示上下左右的子圖
