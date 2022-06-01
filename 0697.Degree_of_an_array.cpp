//
// Created by Yihua Hao on 6/1/2022.
//
#include "leetcode.h"
using namespace std;
class Solution {
public:
  int findShortestSubArray(vector<int>& nums) {
    unordered_map<int, int> count, first;
    int res = 0, degree = 0;
    for (int i = 0; i < nums.size(); ++i) {
      //查看有没有出现过，没有的话设为i
      if (first.count(nums[i]) == 0) first[nums[i]] = i;
      //查看degree 确定答案
      if (++count[nums[i]] > degree) {
        degree = count[nums[i]];
        res = i - first[nums[i]] + 1;
      } else if (count[nums[i]] == degree)
        //如果出现了相同degree取最小值。
        res = min(res, i - first[nums[i]] + 1);
    }
    return res;
  }
};