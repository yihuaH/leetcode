#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tempStr = ''
        if s in t:
            return True
        for char in s:
            for char2 in t:
                if char2 not in s:
                    t = t.replace(char2, "")
                    continue
                if char == char2:
                    tempStr += char2
                    t = t.replace(char2, "", 1)
                    break
                t = t.replace(char2, "", 1)
        if tempStr == s:
            return True
        else:
            return False
                    
                    
# @lc code=end

