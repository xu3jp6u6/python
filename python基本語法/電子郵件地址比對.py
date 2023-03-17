# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:14:27 2021

@author: USER
"""

import re
msg='txt@deepstone.com.tw kkk@gmail.com abc@me.com mymail@qq.com abc@abc@abc'
pattern=r'''([a-zA-Z]+ #使用者帳號
             @ #@符號
             [a-zA-Z]+ #主機域名domain
             (\.|@) #.或@符號
             [a-zA-Z]+ #可能是com或edu或其他
             ([\.])? #.符號,也可能無特別是美國
             ([a-zA-Z]{2,4})?#國別
             ) '''
email=re.findall(pattern, msg, re.VERBOSE)#傳回搜尋結果
print(email)