#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
from collections import deque
from typing import *
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''if not root: return []
        queue, res = deque([root]), []
        
        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            res.append(cur_level)
        return res'''
    
        if not root:
            return
        ans = [[root.val]]
        temp = []
        level = [root]
        
        while True:
            while level:
                cur_node = level.pop(0)
                if cur_node.left:
                    temp.append(cur_node.left)
                if cur_node.right:
                    temp.append(cur_node.right)
            if not temp:
                break
            temp_int = []
            for i in temp:
                temp_int.append(i.val)
            ans.append(temp_int)
            print(ans)
            level = temp.copy()
            temp.clear()
            
        return ans
        
# @lc code=end

