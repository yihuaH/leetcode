//
// Created by Yihua Hao on 6/4/2022.
//
#include "leetcode.h"
using namespace std;

class Solution {
public:
  vector<int> plusOne(vector<int>& digits) {
        /*int num = 0;
        int index = 1;
        for (int i = digits.size(); i > 0; i--) {
          num += digits[i-1] * index;
          index *= 10;
        }
        num ++;
        string ans_str = to_string(num);
        vector<int> ans;
        int temp ;
        for (int i = 0; i < ans_str.size(); ++i) {
          temp = ans_str[i]-'0';
          ans.push_back(temp);
        }
        return ans;*/
        int n = digits.size();
        for (int i = n - 1; i >= 0; --i)
        {
          if (digits[i] == 9)
          {
            digits[i] = 0;
          }
          else
          {
            digits[i]++;
            return digits;
          }
        }
        digits[0] =1;
        digits.push_back(0);
  }
};