# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 15:10:26 2023

@author: USER
"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))