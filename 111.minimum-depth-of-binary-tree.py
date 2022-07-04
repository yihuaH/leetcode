#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left == None:
            return 1+self.minDepth(root.right)
        if root.right == None:
            return 1+self.minDepth(root.left)
        return min(self.minDepth(root.left),self.minDepth(root.right))+1
        
    
# @lc code=end

