//
// Created by Yihua Hao on 6/4/2022.
//
#include "leetcode.h"
using namespace std;
class Solution {
public:
  bool isPerfectSquare(int num) {
    long r = num;
    while(r*r > num)
      r = (r + num/r) /2;
    if (r * r ==num){
      return true;
    }else
      return false;
  }
};