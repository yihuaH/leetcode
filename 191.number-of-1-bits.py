#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#
from typing import *
# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        print(n)
        while n != 0:
            if n&1 == 1:
                count += 1
            n >>= 1
        return count
# @lc code=end

