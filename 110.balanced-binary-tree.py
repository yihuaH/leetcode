#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        diff = self.height(root.left) - self.height(root.right)
        if abs(diff) > 1:
            return False
        else:
            if self.isBalanced(root.left) and self.isBalanced(root.right):
                return True
    
    def height(self, root: Optional[TreeNode]) -> int:
        a = b = 0
        if not root:
            return 0
        if root.left == root.right == None:
            return 1
        else:
            if root.left != None:
                a = self.height(root.left)
            if root.right != None:
                b = self.height(root.right)
            return 1 + max(a,b)
        
# @lc code=end

