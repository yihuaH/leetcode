/*
 * @lc app=leetcode id=830 lang=cpp
 *
 * [830] Positions of Large Groups
 */

// @lc code=start
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<vector<int>> largeGroupPositions(string s) {
        vector<vector<int>> ans;
        bool flag;
        int length = 0;
        int start=0;
        for (size_t i = 1; i < s.length(); i++)
        {
            if (s[i] == s[i-1])
            {     
                //flag = true;
                length ++;
                if ((i==(s.size()-1))&&(length>=2))
                {
                    vector<int> temp;
                    //temp.push_back(i-length<0? 0:i-length);
                    temp.push_back(start);
                    temp.push_back(start+length);
                    ans.push_back(temp);
                }
                
            }else  
            {
                //flag = false;
                if (length>=2)
                {
                    vector<int> temp;
                    temp.push_back(start);
                    temp.push_back(start+length);
                    ans.push_back(temp);
                }
                length = 0;
                start = i;
                
            }
        }
        return ans;
        
    }
};
// @lc code=end

