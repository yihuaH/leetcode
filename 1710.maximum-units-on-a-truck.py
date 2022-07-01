#
# @lc app=leetcode id=1710 lang=python3
#
# [1710] Maximum Units on a Truck
#
from typing import *

from numpy import sort
# @lc code=start
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda row: (row[1]),reverse=True)
        ans = 0
        for box, units in boxTypes:
            if truckSize > box:
                truckSize -= box
                ans += box * units
            else:
                ans += truckSize * units
                return ans
        return ans
        
# @lc code=end

