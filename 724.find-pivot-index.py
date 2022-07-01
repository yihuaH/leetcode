#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

from typing import *
# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0 
        right = sum(nums)
        for a in range(len(nums)):
            if a == 0:
                if right-nums[0] == 0:
                    return a
            if a == (len(nums)-1):
                if left == 0:
                    return a
            
            right -= nums[a]
            if left == right:
                return a
            left += nums[a]
        return -1
# @lc code=end

