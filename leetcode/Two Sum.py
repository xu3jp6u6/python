# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 10:17:39 2023

@author: USER
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a=nums[i]
            for j in range(i+1,len(nums)):
                if target-nums[j]==a:
                    return(i,j)