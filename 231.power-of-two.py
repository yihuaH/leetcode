#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        if bin(n).count("1") == 1:
           return True
        return False 
# @lc code=end

