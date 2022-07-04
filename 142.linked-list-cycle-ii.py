#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#
from typing import *
# @lc code=start
# Definition for singly-linked list.


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: break
        else: return None  # if not (fast and fast.next): return None
        while head != slow:
            head, slow = head.next, slow.next
        return head
# @lc code=end

