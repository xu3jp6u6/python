# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 17:51:09 2021

@author: USER
"""

import re#導入re模組

msg1='Please call my secretary using 0930-919-919 or 0952-001-001'#建立字串
msg2='請明天17:30和我一起參加明志科大教師節晚餐'
msg3='請明天17:30和我一起參加明志科大教師節晚餐,可用0933-080-080聯絡我'
def parestring(string):#定義函式
    pattern=r'(\d{4})-(\d{3})-(\d{3})'
    phonenum=re.findall(pattern, string)#搜尋字串與正則表達式

    print('電話號碼是:%s'%phonenum)#顯示結果
    
        

parestring(msg1) #輸入參數到函式
parestring(msg2)
parestring(msg3)