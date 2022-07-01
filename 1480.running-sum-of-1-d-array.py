#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#
from typing import *
# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        for a in range(len(nums)):
            if a == 0:
                ans.append(nums[a])
            else:
                ans.append(nums[a]+ans[a-1])
        return ans
# @lc code=end

