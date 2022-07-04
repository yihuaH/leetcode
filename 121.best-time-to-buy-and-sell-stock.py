#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
from typing import *
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for x in range(2)] for y in range(n)]
        print(dp)
        for i in range(n):
            if i == 0:
                dp[0][0] = 0
                dp[0][1] = -prices[0]
                continue
            dp[i][0] = max(dp[i-1][0],dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])
        return dp[n-1][0]
# @lc code=end

