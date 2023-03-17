# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 09:23:27 2021

@author: USER
"""

import re
msg='1 cat, 2 dogs, 3 pigs, 4 swans'
pattern='\w+'
txt=re.findall(pattern,msg)
print(txt)