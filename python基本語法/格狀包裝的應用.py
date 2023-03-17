# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:07:29 2021

@author: USER
"""

from tkinter import * 

window=Tk() 
window.title('好友名單') #視窗標題
lab1=Label(window,text='Peter',bg='lightyellow',width=15) #標籤標題顏色寬度
lab2=Label(window,text='Kevin',bg='lightgreen',width=15)
lab3=Label(window,text='Tracy',bg='lightblue',width=15)
lab4=Label(window,text='John',bg='lightpink',width=15)
lab5=Label(window,text='Tommy',bg='#89CFF0',width=15)
lab6=Label(window,text='Mike',bg='Indianred',width=15)
lab7=Label(window,text='Notron',bg='#00A15C',width=15)
lab8=Label(window,text='Mary',bg='Aqua',width=15)
lab9=Label(window,text='Vicent',bg='Lightgray',width=15)
lab1.grid(row=0,column=0) #格狀包裝
lab2.grid(row=0,column=1)
lab3.grid(row=0,column=2)
lab4.grid(row=1,column=0)
lab5.grid(row=1,column=1)
lab6.grid(row=1,column=2)
lab7.grid(row=2,column=0)
lab8.grid(row=2,column=1)
lab9.grid(row=2,column=2)
window.mainloop()
