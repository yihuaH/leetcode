#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
from typing import *
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:  # then num is the left most of the consecutive sequence
                left = num
                right = num
                while right + 1 in nums:  # scan to find the right most of the consecutive sequence
                    right += 1
                res = max(res, right - left + 1)
        return res
            
# @lc code=end

