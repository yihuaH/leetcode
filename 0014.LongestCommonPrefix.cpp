#include "leetcode.h"
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans;
        ans = strs[0];
        for (size_t i = 1; i < strs.size(); i++)
        {
            for (size_t j = 0; j < ans.size(); j++)
            {
                if(ans[j]==strs[i][j]){
                    continue;
                }else{
                    ans = ans.substr(0,j);
                    break;
                }
            }
        }
        return ans;
    }
};