# -*- coding: utf-8 -*-
"""
Created on Sat May  8 17:40:08 2021

@author: USER
"""

from tkinter import *
import time

tk=Tk()
tk.title('tk')
canvas=Canvas(tk,width=800,height=300)
canvas.pack()
canvas.create_text(0,150,text='東海大學',fill='red',anchor=W)#建立一段文字在左中間
for i in range(80):#移動80次，一步距離等於9.4，間隔0.05秒
    canvas.move(1,9.4,0)
    tk.update()
    time.sleep(0.05)


tk.mainloop()