#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
from cmath import cos


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        if len(cost)==0:
            return 0
        cost.append(0)
        dp = [0]*(len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(cost)):
            a = dp[i-1] + cost[i]
            b = dp[i-2] + cost[i]
            dp[i] = min(a,b)
            print(i,dp[i])
        return dp[len(cost)-1]
        
# @lc code=end

