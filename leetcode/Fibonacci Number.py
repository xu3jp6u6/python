# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 21:06:26 2023

@author: USER
"""

class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)