# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 20:48:08 2023

@author: USER
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s=0
        l=len(nums)-1
        while(l>=s):
            a=int((s+l)/2)
            if nums[a]>target:
                l=a-1
            if nums[a]<target:
                s=a+1
            if nums[a]==target:
                return a
        return -1;
