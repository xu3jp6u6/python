# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 10:17:39 2023

@author: USER
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()

        for index, value in enumerate(nums):  
            if target - value in records:  
                return [records[target- value], index]
            records[value] = index    
        return []
