# -*- coding: utf-8 -*-
"""
Created on Mon May 10 00:22:43 2021

@author: USER
"""

english=('Spring', 'Summer', 'Fall', 'Winter')
chinese=('春天', '夏天', '秋天', '冬天')
zipdata=zip(english,chinese)#將2個元組打包
season=list(zipdata)#轉串列
print(season)