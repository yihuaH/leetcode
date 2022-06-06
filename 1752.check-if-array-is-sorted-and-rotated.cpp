/*
 * @lc app=leetcode id=1752 lang=cpp
 *
 * [1752] Check if Array Is Sorted and Rotated
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    bool check(vector<int>& nums) {
        bool ans = true;
        int flag;
        vector<int> new_nums;
        for (size_t i = 0; i < nums.size()-1; i++)
        {
            if (nums[i+1]<nums[i])
            {
                flag = i+1;
                break;
            }
        }
        for (size_t i = flag; i < nums.size(); i++)
        {
            new_nums.push_back(nums[i]);
        }
        for (size_t i = 0; i < flag; i++)
        {
            new_nums.push_back(nums[i]);
        }
        for (size_t i = 0; i < new_nums.size()-1; i++)
        {
            if (new_nums[i+1]<new_nums[i])
            {
                ans = false;
                break;
            }
        }
        return ans;
        
        
    }
};
// @lc code=end

