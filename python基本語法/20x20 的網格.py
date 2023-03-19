# -*- coding: utf-8 -*-
"""
Created on Sat May  8 16:30:02 2021

@author: USER
"""

from tkinter import *



tk=Tk()#用tk當視窗Tk物件
canvas=Canvas(tk,width=404,height=404)
canvas.pack()
canvas.create_rectangle(5, 5, 404, 404, outline='blue',width=3)#建立一個正方形
x1,y1,x2,y2=[],[],[],[]#建立空串列
x3,y3,x4,y4=[],[],[],[]
for i in range(21):#形成21個新座標
    i=i*20
    x1.append(5)
    y1.append(5+i)
    x2.append(400)
    y2.append(5+i)
    x3.append(5+i)
    y3.append(5)
    x4.append(5+i)
    y4.append(400)
for i in range(21):#形成21個長方形
    canvas.create_rectangle(x1[i], y1[i], x2[i], y2[i], outline='blue',width=3)
    canvas.create_rectangle(x3[i], y3[i], x4[i], y4[i], outline='blue',width=3)
mainloop()