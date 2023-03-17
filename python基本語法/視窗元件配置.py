# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 13:43:08 2021

@author: USER
"""

from tkinter import * 

window=Tk() 
window.geometry("400x300")
window.title('台灣企業') #視窗標題
lab1=Label(window,text='台塑企業',bg='lightyellow',width=20,height=5) #標籤標題顏色寬度
lab2=Label(window,text='台積電',bg='lightgreen',width=20,height=5)
lab3=Label(window,text='聯發科',bg='lightblue',width=20,height=5)
lab4=Label(window,text='華碩電腦',bg='lightpink',width=20,height=5)
lab5=Label(window,text='宏碁電腦',bg='#89CFF0',width=20,height=5)

lab1.pack() #包裝與定位元件
lab2.pack()
lab3.pack()
lab4.pack()
lab5.pack()

window.mainloop()