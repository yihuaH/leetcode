#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        templist = []
        while head:
            templist.append(head.val)
            head = head.next
        print(templist)
        if len(templist) == 2:
            if templist[0] == templist[1]:
                return True
            else:
                return False
        elif len(templist) == 1:
           return True 
        for i in range(int(len(templist)/2)+1):
            #print (str(templist[i]) + " " +str(templist[-i-1])+ " "+ str(int(len(templist)/2)+1))
            if templist[i] != templist[-i-1]:
                return False
            
        return True
# @lc code=end

