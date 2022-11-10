#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        head1 = head2 = head
        while(head1 and head2):
            if head1.next == None:
                return False
            if head2.next == None:
                return False
            head1 = head1.next
            head2 = head2.next.next
            if(head1 == head2):
                return True
            
        return False        
# @lc code=end

