# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 12:39:49 2021

@author: USER
"""

import numpy as np #導入numpy
x=int(input('輸入任意0~9數字')) 
y=int(input('輸入任意一個數字'))
if x==0: #條件判斷
    k=np.array([[x,x,x,x],[x,' ',' ',x],[x,' ',' ',x],[x,' ',' ',x],[x,x,x,x]]) #建立矩陣
    i=k.repeat([y,y,y,y],axis=1) #axis=1的值進行重複
    j=i.repeat([y,y,y,y,y],axis=0)#axis=0的值進行重複
elif x==1:
    a=np.array([[' ',' ',x,' '],[x,x,x,' '],[' ',' ',x,' '],[' ',' ',x,' '],[x,x,x,x]])
    i=a.repeat([y,y,y,y],axis=1)
    j=i.repeat([y,y,y,y,y],axis=0)
elif x==2:
    b=np.array([[x,x,x,x],[' ',' ',' ',x],[x,x,x,x],[x,' ',' ',' '],[x,x,x,x]])
    i=b.repeat([y,y,y,y],axis=1)
    j=i.repeat([y,y,y,y,y],axis=0)
elif x==3:
    c=np.array([[x,x,x,x],[' ',' ',' ',x],[' ',x,x,x],[' ',' ',' ',x],[x,x,x,x]])
    i=c.repeat([y,y,y,y],axis=1)
    j=i.repeat([y,y,y,y,y],axis=0)
elif x==4:
    d=np.array([[x,' ',x,' '],[x,' ',x,' '],[x,x,x,x],[' ',' ',x,' '],[' ',' ',x,' ']])
    i=d.repeat([y,y,y,y],axis=1)
    j=i.repeat([y,y,y,y,y],axis=0)
elif x==5:
    e=np.array([[x,x,x,x],[x,' ',' ',' '],[x,x,x,x],[' ',' ',' ',x],[x,x,x,x]])
    i=e.repeat([y,y,y,y],axis=1)
    j=i.repeat([y,y,y,y,y],axis=0)
elif x==6:
    f=np.array([[x,x,x,x],[x,' ',' ',' '],[x,x,x,x],[x,' ',' ',x],[x,x,x,x]])
    i=f.repeat([y,y,y,y],axis=1)
    j=i.repeat([y,y,y,y,y],axis=0)
elif x==7:
    g=np.array([[x,x,x,x],[' ',' ',' ',x],[' ',' ',' ',x],[' ',' ',' ',x],[' ',' ',' ',x]])
    i=g.repeat([y,y,y,y],axis=1)
    j=i.repeat([y,y,y,y,y],axis=0)
elif x==8:
    h=np.array([[x,x,x,x],[x,' ',' ',x],[x,x,x,x],[x,' ',' ',x],[x,x,x,x]])
    i=h.repeat([y,y,y,y],axis=1)
    j=i.repeat([y,y,y,y,y],axis=0)
else:
    h=np.array([[x,x,x,x],[x,' ',' ',x],[x,x,x,x],[' ',' ',' ',x],[x,x,x,x]])
    i=h.repeat([y,y,y,y],axis=1)
    j=i.repeat([y,y,y,y,y],axis=0)
print(j.reshape(5*y,4*y)) #顯示5y x 4y的矩陣 