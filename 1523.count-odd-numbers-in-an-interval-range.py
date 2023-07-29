#
# @lc app=leetcode id=1523 lang=python3
#
# [1523] Count Odd Numbers in an Interval Range
#

# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = (high - low) /2
        if low % 2 == 1:
            ans = ans +1

        if high % 2 == 1:
            ans += 1

        if high % 2 == 1 and low % 2 == 1:
            ans -= 1
        return int(ans)
# @lc code=end

