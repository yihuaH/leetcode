#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        
        ans = 0
        for i in nums:
            ans ^= i
        return ans
            
        
# @lc code=end

