# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 12:07:50 2023

@author: USER
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in s:
            if i == '(':
                stack.append(')')
            elif i == '[':
                stack.append(']')
            elif i == '{':
                stack.append('}')
            elif not stack or stack[-1] != i:
                return False
            else:
                stack.pop()
        if not stack:
            return True