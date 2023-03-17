# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 10:11:33 2021

@author: USER
"""

import re
msg='''02-88223349,(02)-26669999,02-29998888 ext 123,
          12345678,02 33887766 ext. 12222,02-1234567,
          02-123456789, 02-123456789,23-123456'''
pattern=r'''(
        (\d{2}|\(\d{2}\))? #區域號碼
        (\s|-)? #區域號碼與電話號碼的分格符號
        (\d{8}|\d{7}) #電話號碼
        (\s*(ext|ext.)\s*\d{2,4})? #2-4位數的分機號碼
        )'''
phonenum=re.findall(pattern, msg, re.VERBOSE) #傳回搜尋結果
print(phonenum)