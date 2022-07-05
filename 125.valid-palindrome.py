#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        ans=""
        for i in s:
            if i.isalpha() or i.isnumeric():
                ans += i
        print(ans)
        for i in range(len(ans)):
            if ans[i] != ans[len(ans)-1-i]:
                return False
        return True
            
# @lc code=end

