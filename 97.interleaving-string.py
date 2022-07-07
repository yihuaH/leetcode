#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if len(s3) != (m+n):
            return False
    
        memo = [[False for i in range(n+1)] for j in range(m+1)]
        memo[m][n] = True
        
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i < m and s1[i] == s3[i + j]:
                    memo[i][j] |= memo[i + 1][j]
                if j < n and s2[j] == s3[i + j]:
                    memo[i][j] |= memo[i][j + 1]
        return memo[0][0]
        
# @lc code=end

