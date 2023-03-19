# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 16:45:08 2021

@author: USER
"""

from tkinter import *
def add():
    n3.set(n1.get()+n2.get())#按+-*/按鈕時執行
def sub():
    n3.set(n1.get()-n2.get())
def mul():
    n3.set(n1.get()*n2.get())
def div():
    n3.set(n1.get()/n2.get())


window = Tk()
window.title('Calculator')
window.geometry('300x260')

n1 = IntVar() 
n2 = IntVar()
n3 = IntVar()    

e1=Entry(window,width=8,textvariable=n1)#文字方塊1
label = Label(window, width=3, text='/')#標籤
e2=Entry(window,width=8,textvariable=n2)#文字方塊2
btn1 = Button(window, width=5, text='+', command=add)#計算+-*/按鈕
btn2 = Button(window, width=5, text='-', command=sub)
btn3 = Button(window, width=5, text='*', command=mul)
btn4 = Button(window, width=5, text='/', command=div)
btn5 = Button(window, width=5, text='=')
e3=Entry(window,width=8,textvariable=n3)#文字方塊3
e1.grid(row=0,column=0)#定位
label.grid(row=0,column=1)
e2.grid(row=0,column=2)
btn1.grid(row=1,column=1)
btn2.grid(row=2,column=1)
btn3.grid(row=3,column=1)
btn4.grid(row=4,column=1)
btn5.grid(row=5,column=1)
e3.grid(row=6,column=1)
window.mainloop()