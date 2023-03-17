# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 16:22:16 2020

@author: User
"""

import matplotlib.pyplot as plt
import numpy as np
left=-2*np.pi
right=2*np.pi
x=np.linspace(left, right,40)
f1 = 3 * np.sin(x)
f2 = np.sin(x)
f3 = 0.2 * np.sin(x)
#設定sin值
plt.plot(x,f1,'-o')
plt.plot(x,f2,'-x')
plt.plot(x,f3,color='red')
