#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
from typing import *
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        a = b = 0
        if root == None:
            return 0
        if root.left == root.right == None:
            return 1
        else:
            if root.left:
                a = 1+self.maxDepth(root.left)
            if root.right:
                b = 1+self.maxDepth(root.right)
            return max(a,b)
        
# @lc code=end

