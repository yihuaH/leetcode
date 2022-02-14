#include "leetcode.h"
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        int ans = 0, start = 0;
        int n = s.length();
        map<char, int> mp;
        for(int i=0;i<n;i++)
        {
            char alpha = s[i];
            if(mp.count(alpha))
            {
                start = max(start, mp[alpha]+1);
            }
            ans = max(ans, i-start+1);
            // 字符位置
            
            mp[alpha] = i;
        }
        return ans;
        //sublime push
    }
};