# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 23:44:58 2021

@author: USER
"""

from PIL import Image
a=Image.new("RGB",(200,200),"LightGreen") #模式,大小,顏色
for x in range(50,151):
    for y in range(50,101):          #紅色
        a.putpixel((x,y),(255,0,0))
    for z in range(101,151):         #藍色
        a.putpixel((x,z),(0,0,255))
a.save("out1.jpg") #處存
