#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        ans = ""
        flg = 0
        if num < 0:
            flg = 1
            num = -num
        while num > 0:
            ans+= str(num%7)
            num //= 7
            print(ans)
        if flg == 1:
            ans+=("-")
        return ans[::-1]
# @lc code=end

