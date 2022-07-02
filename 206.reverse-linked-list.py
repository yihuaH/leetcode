#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
from typing import *
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        ans.reverse()
        ans_node = []
        for i in ans:
            new_node = ListNode(i, None)
            ans_node.append(new_node)
        for i in range(len(ans_node)-1):   
            ans_node[i].next = ans_node[i+1]
        return ans_node[0]
            
                    
        
# @lc code=end

