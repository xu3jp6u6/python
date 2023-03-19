# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 13:52:30 2021

@author: USER
"""

from tkinter import *


def worm():
    n2.set(n1.get()*(9/5)+32)#按計算BMI按鈕時執行

window = Tk()
window.title('溫度轉化器')
window.geometry('300x160')

n1 = IntVar() 
n2 = IntVar()


e1 = Entry(window, width=8, textvariable=n1) #文字方塊1
label1 = Label(window, width=3, text='攝氏:')#標籤
label2 = Label(window, width=3, text='華氏:')#標籤
label3 = Label(window, width=3,textvariable=n2)#標籤
btn = Button(window, width=5, text='轉化', command=worm)#計算BMI按鈕
label1.grid(row=0,column=0)#定位
e1.grid(row=0,column=1,ipadx=5)
label2.grid(row=1,column=0)
label3.grid(row=1,column=1,ipadx=5)
btn.grid(row=3,column=3)
window.mainloop()