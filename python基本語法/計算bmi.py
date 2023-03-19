# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 11:27:24 2021

@author: USER
"""

from tkinter import *


def bmi():
    n3.set(n1.get()/((n2.get()/100)*(n2.get()/100)))#按計算BMI按鈕時執行


window = Tk()
window.title('tk')
window.geometry('300x160')

n1 = IntVar() 
n2 = IntVar()
n3 = IntVar()

e1 = Entry(window, width=8, textvariable=n2) #文字方塊1
label1 = Label(window, width=3, text='請輸入身高(公分)')#標籤
e2 = Entry(window, width=8, textvariable=n1)#文字方塊2
label2 = Label(window, width=3, text='請輸入體重(公斤)')#標籤
btn = Button(window, width=5, text='計算BMI', command=bmi)#定位計算BMI按鈕
e3 = Entry(window, width=5, textvariable=n3)#文字方塊3
label1.grid(row=0, column=4, ipadx=40,padx=40)#定位
e1.grid(row=1, column=4, ipadx=40, padx=40)
label2.grid(row=2, column=4, ipadx=40, padx=40)
e2.grid(row=3, column=4, ipadx=40, padx=40)
btn.grid(row=4, column=4,ipadx=50, padx=40)
e3.grid(row=5, column=4,ipadx=50, padx=40)

window.mainloop()
