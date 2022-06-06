//
// Created by Yihua Hao on 6/2/2022.
//


class Solution {
public:
  int lengthOfLastWord(string s) {
        int index = s.size()-1;
        while(s[index] == ' '){
          index--;
        }
        int ans = 0;
        while(index >= 0 && s[index]!=' '){
          ans++;
          index--;
        }
        return ans;
  }
};