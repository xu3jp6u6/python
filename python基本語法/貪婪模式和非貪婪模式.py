# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 22:01:08 2021

@author: USER
"""

import re  #導入re模組
def searchstr(pattern,msg): #建立函式
    txt=re.search(pattern, msg) #搜尋字串與正則表達式
    if txt==None: #沒搜到
        print('搜尋失敗',txt) #顯示
    else: #其他
        print('搜尋成功',txt.group()) #顯示
msg='sonsonsonsonson' #建立字串
pattern1 = '(son){3,5}' #建立貪婪搜尋
pattern2 = '(son){3,5}?' #建立非貪婪搜尋
searchstr(pattern1,msg) #輸入參數到函式
searchstr(pattern2,msg)