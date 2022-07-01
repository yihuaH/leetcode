#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
from typing import *
# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        myMap = {}
        ans = ''
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] not in myMap:
                    if t[i] not in myMap.values():
                        myMap[s[i]] = t[i]
                    else:
                        myMap[s[i]] = ' '
                
                ans += myMap.get(s[i])
        if ans == t:
            return True
        else:
            return False
                    
                
        
# @lc code=end

