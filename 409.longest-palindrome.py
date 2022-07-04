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
        a = list(set(s))#去重
        ans = 0
        flag = 0#可以加一次奇数
        print(a)
        for i in a:
            temp = s.count(i)
            #如果是偶数可以直接加入到答案里面
            if temp % 2 == 0:
                ans += temp
            else: 
                #如果没有加过奇数，可以加一次奇数
                if flag == 0:
                    flag = 1
                    ans += temp
                else:
                    #如果加过奇数后，并且是大于二的奇数，可以加这个数减一
                    if temp > 2:
                        ans += temp - 1
        return ans
            
# @lc code=end

