# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 15:28:18 2020

@author: USER
"""

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-6, 6, 200)
tanh=np.tanh(x)
y1=1/(1+np.exp(-x))
y2=np.maximum(0,x)
y3=tanh
plt.title('sigmoid function')
plt.figure(1)
plt.plot(x,y1)
plt.figure(2)
plt.plot(x,y2)
plt.title('relu function')
plt.figure(3)
plt.plot(x,y3)
plt.title('tanh function')   