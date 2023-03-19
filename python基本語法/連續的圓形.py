# -*- coding: utf-8 -*-
"""
Created on Sat May  8 15:12:00 2021

@author: USER
"""

from tkinter import *



tk=Tk()#用tk當視窗Tk物件
canvas=Canvas(tk,width=400,height=250)#建立畫布
canvas.pack()#將畫布完成包裝
for i in range(10):
    i*=10
    canvas.create_oval(10+i,10,100+i,100)
mainloop()