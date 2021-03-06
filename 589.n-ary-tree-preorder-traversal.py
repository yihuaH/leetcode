#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#

# @lc code=start
from typing import *
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution:
    
    def traverse(self, root: 'Node', ans: List[int]):
        if not root:
            return
        ans.append(root.val)
        for child in root.children:
            self.traverse(child, ans)
            
    def preorder(self, root: 'Node') -> List[int]:
        ans = [] 
        self.traverse(root, ans)
        return ans
    
        
# @lc code=end

