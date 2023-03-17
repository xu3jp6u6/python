# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 17:41:03 2021

@author: USER
"""


n=input('並輸入英文的星期:')#輸入英文日期
week={'Sunday':'星期天','Monday':'星期ㄧ','Tuesday':'星期二','Wednesday':'星期三','Thursday':'星期四','Friday':'星期五','Saturday':'星期六'}#建立字典
if n in week:#如果輸入有在字典裡
    print(week[n])#顯示中文星期
else:
    print('輸出錯誤資訊')#顯示輸出錯誤資訊
