//
// Created by Yihua Hao on 6/4/2022.
//
#include "leetcode.h"
using namespace std;
class Solution {
public:
  string addStrings(string num1, string num2) {
    string ans_str;
    string temp;
    if (num1.size() > num2.size()){
      for (int i = 0; i < num1.size()-num2.size(); ++i) {
        temp += "0";
      }
      num2 = temp + num2;
    }else{
      for (int i = 0; i < num2.size()-num1.size(); ++i) {
        temp += "0";
      }
      num1 = temp + num1;
    }
    int flag = 0;
    int sum;
    for (int i = num2.size()-1; i >= 0; --i) {
      sum = (flag + num2[i]-'0' + num1[i]-'0');
      if (sum>9){
        flag = 1;
        temp = sum -10 + '0';
        ans_str = temp + ans_str;
      }else{
        flag = 0;
        temp = sum + '0';
        ans_str = temp + ans_str;
      }
    }
    if (flag)
      ans_str = "1" + ans_str;

    return ans_str;
  }
};