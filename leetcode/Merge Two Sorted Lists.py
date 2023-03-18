# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 12:38:54 2023

@author: USER
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode(None)
        prev = dum
        
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        
        if list1 == None:
            prev.next = list2
        elif list2 == None:
            prev.next = list1
        
        return dum.next