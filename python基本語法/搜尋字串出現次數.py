# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 18:05:48 2021

@author: USER
"""




msg='我喜歡看小龍女與楊過，不僅因為小龍女美麗，楊過在戲中所扮演的角色更是讓我喜歡。'#建立字串
n=input('請輸入與搜尋字串:') #輸入字串
a=msg.count(n) #出現次數
print('所搜尋%s共出現%d次'%(n,a)) #顯示輸入字串與出現次數
z=input('是否繼續，輸入Y或y則程式繼續，否則結束:')#定義z
def txt(n): #建立函式
    n=input('請輸入與搜尋字串:') #輸入字串
    a=msg.count(n) #出現次數
    print('所搜尋%s共出現%d次'%(n,a))#顯示輸入字串與出現次數
    
while z=='Y' or z=='y': #建立迴圈
    txt(n)#輸入參數到函式
    z=input('是否繼續，輸入Y或y則程式繼續，否則結束:')#定義z
    continue

    
