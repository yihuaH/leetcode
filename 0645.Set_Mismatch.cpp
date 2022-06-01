//
// Created by Yihua Hao on 6/1/2022.
//
#include "leetcode.h"
using namespace std;
class Solution {
public:
  vector<int> findErrorNums(vector<int>& nums) {
    int N = nums.size(), sum = N * (N + 1) / 2;
    vector<int> ans;
    vector<bool> seen(N + 1);
    for (int num : nums) {
      sum -= num;
      if (seen[num])
        ans[0] = num;
      seen[num] = true;
    }
    ans[1] = sum + ans[0];
    return ans;
  }
};