#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        '''
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    t = t.replace(t[j],"",1)
                    break
        if t == "":
            return True
        else:
            return False
        '''
        count = [0] * 26
        for i in range(len(s)):
           count[ord(s[i]) - ord('a')] += 1
           count[ord(t[i]) - ord('a')] -= 1
           
        for i in range(26):
            if count[i] != 0:
                return False
        
        return True
                
        
        
# @lc code=end

