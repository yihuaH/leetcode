//
// Created by Yihua Hao on 6/4/2022.
//
#include "leetcode.h"
using namespace std;
class Solution {
public:
  string addBinary(string a, string b) {
    /*string ans = "0";
    int a_int = stoi(a);
    int b_int = stoi(b);
    int ans_int = a_int + b_int;
    stringstream ss;
    ss << ans_int;
    string temp = ss.str();
    ans = ans + temp;
    for (int i = ans.size()-1; i >= 0; --i) {
      switch (ans[i]) {
        case '0':
        case '1':
          break ;
        case '2':
          ans[i] = '0';
          ans[i-1] ++;
          break ;
        case '3':
          ans[i] = '1';
          ans[i-1] ++;
          break ;
        }
    }
    if (ans[0]=='0')
      ans = ans.erase(0,1);
    return ans;*/
    string ans;
    string temp;
    if (a.size() > b.size()){
      for (int i = 0; i < a.size()-b.size(); ++i) {
        temp += "0";
      }
      b = temp + b;
    }else{
      for (int i = 0; i < b.size()-a.size(); ++i) {
        temp += "0";
      }
      a = temp + a;
    }
    bool flag = 0;
    for (int i = a.size()-1; i >= 0; --i) {
      if (flag){
        if ((a[i]-'0')&& (b[i]-'0')){
          flag = 1;
          temp = "1";
          ans = temp + ans;
        }else if((a[i]-'0')|| (b[i]-'0')){
          flag = 1;
          temp = "0";
          ans = temp + ans;
        }else{
          flag = 0;
          temp = "1";
          ans = temp + ans;
        }
      }else{
        if ((a[i]-'0')&& (b[i]-'0')){
          flag = 1;
          temp = "0";
          ans = temp + ans;
        }else if((a[i]-'0')|| (b[i]-'0')){
          flag = 0;
          temp = "1";
          ans = temp + ans;
        }else{
          flag = 0;
          temp = "0";
          ans = temp + ans;
        }
      }
    }
    if (flag){
      ans = "1" + ans;
    }
    return ans;
  }
};