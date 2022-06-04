//
// Created by Yihua Hao on 6/4/2022.
//
#include "leetcode.h"
using namespace std;

class Solution {
public:
  vector<int> addToArrayForm(vector<int>& num, int k) {
    /*int number = 0;
    int index = 1;
    for (int i = num.size(); i > 0; i--) {
      number += num[i-1] * index;
      index *= 10;
    }
    number = number + k;
    stringstream ss;
    ss << number;
    string temp = ss.str();
    vector<int> ans;
    for (int i = 0; i < temp.size(); ++i) {
      ans.push_back(temp[i]-'0');
    }
    return ans;*/
    string ans_str;
    stringstream ss;
    string temp;
    ss << k;
    string k_str = ss.str();
    string num_str;
    for (int i = 0; i < num.size(); ++i) {
      num_str.push_back(num[i]+'0');
    }
    if (num_str.size() > k_str.size()){
      for (int i = 0; i < num_str.size()-k_str.size(); ++i) {
        temp += "0";
      }
      k_str = temp + k_str;
    }else{
      for (int i = 0; i < k_str.size()-num_str.size(); ++i) {
        temp += "0";
      }
      num_str = temp + num_str;
    }
    int flag = 0;
    int sum;
    for (int i = k_str.size()-1; i >= 0; --i) {
      sum = (flag + k_str[i]-'0' + num_str[i]-'0');
      if (sum>9){
        flag = 1;
        temp = sum -10 + '0';
        ans_str = temp + ans_str;
      }else{
        flag = 0;
        ss << sum;
        temp = sum + '0';
        ans_str = temp + ans_str;
      }
    }
    if (flag)
      ans_str = "1" + ans_str;
    vector<int> ans;
    for (int i = 0; i < ans_str.size(); ++i) {
      ans.push_back(ans_str[i]-'0');
    }
    return ans;
  }
};