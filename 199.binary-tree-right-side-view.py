#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return
        ans = [root.val]
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
            ans.append(temp[-1].val)
            level = temp.copy()
            temp.clear()
            print(ans)
            
        return ans
# @lc code=end

