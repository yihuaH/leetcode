#
# @lc app=leetcode id=671 lang=python3
#
# [671] Second Minimum Node In a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        min1 = root.val
        min2 = float('inf')
        def dfs(node: TreeNode) -> None:
            nonlocal min1, min2
            if node.val < min1:
                min2 = min1
                min1 = node.val
            # check if node value is not less than minimum value but less than second minimum value
            elif node.val != min1 and node.val < min2:
                min2 = node.val
            
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        
        dfs(root)
            
        return min2 if min2 != float('inf') else -1
                

# @lc code=end

