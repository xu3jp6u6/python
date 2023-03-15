# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 14:39:12 2021

@author: USER
"""

Math= {'Peter',' Norton',' Kevin',' Mary',' John',' Ford',' Nelson',' Damon',' Ivan','Tom'}#建立集合
Computer={'Curry',' James',' Mary',' Turisa',' Tracy', 'Judy',' Lee', 'Jarmul', 'Damon','Ivan' }
Physics={ 'Eric',' Lee',' Kevin',' Mary', 'Christy',' Josh',' Nelson',' Kazil',' Linda', 'Tom'}



print('同時參加3個夏令營的名單:')

print(Math & Computer & Physics)#顯示三個交集

print('同時參加Math與Computer夏令營的名單:')

print(Math & Computer)#顯示math跟computer交集

print('同時參加Math與Physics夏令營的名單:')

print(Math & Physics)#顯示math跟physics交集

print('同時參加Physics與Computer夏令營的名單')

print(Computer & Physics)#顯示computer跟physics交集