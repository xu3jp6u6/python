# -*- coding: utf-8 -*-
"""
Created on Sun May  9 01:05:59 2021

@author: USER
"""

from tkinter import *



tk=Tk()
tk.title('tk')
canvas=Canvas(tk,width=600,height=300)
canvas.pack()
x1 = 150 #設定變數
y1 = 150
canvas.create_line(x1,y1,x1+10,y1, fill='red')#創造一條線
def line1(): #定義線條
    canvas.create_line(x1, y1,x1-10,y1, fill='red')
def line2():
    canvas.create_line(x1, y1,x1+10,y1, fill='red')
def line3(): 
    canvas.create_line(x1, y1,x1,y1-10, fill='red')
def line4(): #定義線條
    canvas.create_line(x1, y1,x1,y1+10, fill='red')
def lineincrease(event):
    global x1, y1#是用全域變數
    if event.keysym=='Left':#左移
        line1()
        x1-=10 #取得新座標
    if event.keysym=='Right':#右移
        line2()
        x1+=10
    if event.keysym=='Up':#上移
        line3()
        y1-=10
    if event.keysym=='Down':#下移
        line4()
        y1+=10

canvas.bind_all('<KeyPress-Left>',lineincrease)
canvas.bind_all('<KeyPress-Right>',lineincrease)
canvas.bind_all('<KeyPress-Up>',lineincrease)
canvas.bind_all('<KeyPress-Down>',lineincrease)
tk.mainloop()