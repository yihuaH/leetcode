#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
from inspect import stack
from re import T
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root:
            p = root.left
            q = root.right
            stack = [[p,q]]
            while len(stack) > 0:
                pair = stack.pop()
                left = pair[0]
                right = pair[1]
                
                if not left and not right:
                    continue
                if not left or not right:
                    return False
                if left.val == right.val:
                    stack.append([left.left, right.right])
                    stack.append([left.right, right.left])
                else:
                    return False
        return True        
        
            
        
# @lc code=end

