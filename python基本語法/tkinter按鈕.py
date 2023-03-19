# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 11:05:58 2021

@author: USER
"""

from tkinter import *

def printa():
    label['text']='Hello,World!'#按顯示訊息按鈕時執行

window=Tk()
window.title('tk')         #視窗標題
window.geometry('300x160') #視窗寬300高160
label=Label(window)       #標籤內容
Button(window,text='顯示訊息',command=printa).pack() #按鈕
label.pack()
window.mainloop()
