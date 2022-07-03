#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#
from calendar import different_locale
from typing import *

from numpy import diff
# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)-1,0,-1):
            if nums[i] == nums[i-1]:
                del nums[i]
        
        if len(nums) == 1:
            return 1
        difference = nums[1] - nums[0]
        ans = 2
        for i in range(2, len(nums)):
            if difference * (nums[i] - nums[i-1]) < 0:
                difference = nums[i]-nums[i-1]
                ans += 1
            else:
                continue
        return ans   
        # @lc code=end

