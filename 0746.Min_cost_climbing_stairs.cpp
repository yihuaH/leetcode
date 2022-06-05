//
// Created by Yihua Hao on 6/4/2022.
//
#include "leetcode.h"
using namespace std;
class Solution {
public:
  int minCostClimbingStairs(vector<int>& cost) {
    vector<int> dp(cost.size()+1);

    for (int i = 2; i <= cost.size(); ++i) {
      int jump_one_step = dp[i-1] + cost[i-1];
      int jump_two_step = dp[i-2] + cost[i-2];
      dp[i] = min(jump_one_step,jump_two_step);
    }
    return dp[cost.size()];
  }
};