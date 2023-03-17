# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 09:37:48 2021

@author: USER
"""


import re
msg1 = '0932895453'
msg2 = '09328ss453'
pattern='^\d+$'
txt=re.findall(pattern, msg1)
print(txt)
txt=re.findall(pattern, msg2)
print(txt)