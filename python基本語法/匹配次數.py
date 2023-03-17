# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 20:57:51 2021

@author: USER
"""

import re #導入re模組
def searchstr(pattern,msg):#建立函式
    txt=re.search(pattern, msg) #搜尋字串與正則表達式
    if txt==None: #沒搜到
        print('搜尋失敗',txt) #顯示
    else: #其他
        print('搜尋成功',txt.group()) #顯示
msg1='son' 
msg2='sonson'
msg3='sonsonson'
msg4='sonsonsonson'
msg5='sonsonsonsonson'        
pattern1='(son){2,}' #建立貪婪搜尋
pattern2='(son){,5}'
print('以下用(son){2,}測試') #顯示
searchstr(pattern1,msg1) #輸入參數到函式
searchstr(pattern1,msg2)
searchstr(pattern1,msg3)
searchstr(pattern1,msg4)
searchstr(pattern1,msg5)
print('以下用(son){,5}測試') #顯示
searchstr(pattern2,msg1) #輸入參數到函式
searchstr(pattern2,msg2)
searchstr(pattern2,msg3)
searchstr(pattern2,msg4)
searchstr(pattern2,msg5)