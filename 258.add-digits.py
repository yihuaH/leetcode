#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        ans = str(num)
        ansNum = 0
        if len(ans) != 1:
            for i in range(len(ans)):
                ansNum += int(ans[i])
            return self.addDigits(ansNum)
        else:
            return int(num)
# @lc code=end

