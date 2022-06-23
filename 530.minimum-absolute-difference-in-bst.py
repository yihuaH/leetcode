#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    pre = -float('inf')
    res = float('inf')
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return
        
        self.getMinimumDifference(root.left)
        self.res = min(self.res, abs(root.val - self.pre))
        self.pre = root.val
		
        self.getMinimumDifference(root.right)
        return self.res
        
# @lc code=end

