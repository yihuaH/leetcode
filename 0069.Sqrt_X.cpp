//
// Created by Yihua Hao on 6/4/2022.
//
# include "leetcode.h"
using namespace std;

class Solution {
public:
  int mySqrt(int x) {
    long r = x;
    while(r*r > x)
      r = (r + x/r) /2;
    return r;
  }
};