//
// Created by Yihua Hao on 5/31/2022.
//
// The API isBadVersion is defined for you.
bool isBadVersion(int version);

class Solution {
public:
  int firstBadVersion(int n) {
        int ans;
        int i = 1;
        int i2 = i+((n-i)/2);
        while(i<=){
          if(isBadVersion(i2)){
            n = i2 - 1;
          }else{
            i = i2 + 1;
          }
          i2 = i+((n-i)/2);
        }
        return i;
  }
};