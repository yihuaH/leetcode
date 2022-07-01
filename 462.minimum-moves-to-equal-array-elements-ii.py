#
# @lc app=leetcode id=462 lang=python3
#
# [462] Minimum Moves to Equal Array Elements II
#
from typing import *

from numpy import short 
# @lc code=start

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        ans = 0
        mid = sorted(nums)[int(len(nums) / 2)]
        for a in nums:
            ans += abs(a-mid)
        return ans
        
# @lc code=end

