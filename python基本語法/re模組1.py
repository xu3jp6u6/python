# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 10:40:09 2021

@author: USER
"""

import re #導入re模組
msg1='I love Ming-Chi:是大陸手機號碼' #建立字串
msg2='0932-999-199:是大陸手機號碼'
msg3='133-1234-1234:是大陸手機號碼'

def chinaPhoneNum(string): #定義函式
    phonerule=re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')#搜尋正則表達式
    phonenum=phonerule.search(string) #搜尋字串
    if phonenum!=None: #如果有搜到
        print('%sTrue'%string) #顯示
    else: #其他
        print('%sFalse'%string) #顯示


chinaPhoneNum(msg1) #輸入參數到函式
chinaPhoneNum(msg2)
chinaPhoneNum(msg3)