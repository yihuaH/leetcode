#
# @lc app=leetcode id=1465 lang=python3
#
# [1465] Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
#
from typing import *
# @lc code=start
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        max_h, max_v = 0, 0
        horizontalCuts.sort()
        verticalCuts.sort()
        for i, val in enumerate(horizontalCuts):
            if i == 0:
                max_h = val
            else:
                max_h = max(max_h, (val-horizontalCuts[i-1]))
        max_h = max(max_h, h-horizontalCuts[-1])
        print(max_h)
        for i, val in enumerate(verticalCuts):
            if i == 0:
                max_v = val
            else:
                max_v = max(max_v, (val-verticalCuts[i-1]))
        max_v = max(max_v, w-verticalCuts[-1])
        print(max_v)
        return max_h * max_v % ((10**9) +7)
        
# @lc code=end

