#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
from tkinter.tix import Tree
from typing import *
from unittest import result
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        self.tracersal(root, 0, ans)
        return ans
    
    def tracersal(self, root: Optional[TreeNode], level, ans:List[List[int]]):
        if not root:
            return
        if len(ans) <= level:
            ans.append([])
        ans[level].append(root.val)
            
        self.tracersal(root.left, level+1,ans)
        self.tracersal(root.right, level +1,ans)
        
# @lc code=end

