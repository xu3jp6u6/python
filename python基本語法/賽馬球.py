# -*- coding: utf-8 -*-
"""
Created on Sun May  9 15:24:57 2021

@author: USER
"""

from tkinter import *
from random import *
import time
     
def clear(): #清除全部
    e1.delete(0,END)

tk=Tk()
tk.title('tk')
canvas=Canvas(tk,width=500,height=250)
canvas.pack()
id1=canvas.create_oval(10,50,60,100,fill='yellow')#創造二個球
id2=canvas.create_oval(10,150,60,200,fill='aqua')
label=Label(tk,text='哪一個球獲勝:').place(x=10,y=220)#文字標籤
e1=Entry(tk)#文字方塊
e1.insert(1,'1 or 2')#預留文字
btn=Button(tk,text='重置',command=clear).place(x=250,y=220)#按鈕觸發清除全部
e1.place(x=100,y=220)#文字方塊位子
for x in range(0,130):#跑0到129遍
    if randint(1,100)>60:#亂數大於60
        canvas.move(id2,5,0)#id2移動
    else:
        canvas.move(id1,5,0)#id1移動
    
    tk.update()#強制重繪畫布
    time.sleep(0.05)#間隔0.05秒
ball1=canvas.coords(id1)#取得座標
ball2=canvas.coords(id2)
if ball1[2]>ball2[2] and e1.get()=='1':#用球右側做條件式
    labe2=Label(tk,text='恭喜你贏了，ball1獲勝').place(x=300,y=220)
elif ball1[2]>ball2[2] and e1.get()=='2':
    labe2=Label(tk,text='抱歉你輸了，ball1獲勝').place(x=300,y=220)
elif ball2[2]>ball1[2] and e1.get()=='1':
    labe2=Label(tk,text='抱歉你輸了，ball2獲勝').place(x=300,y=220)
elif ball2[2]>ball1[2] and e1.get()=='2':
    labe2=Label(tk,text='恭喜你贏了，ball2獲勝').place(x=300,y=220)

mainloop()