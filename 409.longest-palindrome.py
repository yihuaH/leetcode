#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        a = list(set(s))
        ans = 0
        flag = 0
        print(a)
        for i in a:
            temp = s.count(i)
            if temp % 2 == 0:
                ans += temp
            else: 
                if flag == 0:
                    flag = 1
                    ans += temp
                else:
                    if temp > 2:
                        ans += temp - 1
        return ans
            
# @lc code=end

