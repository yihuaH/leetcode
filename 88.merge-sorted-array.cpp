/*
 * @lc app=leetcode id=88 lang=cpp
 *
 * [88] Merge Sorted Array
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        for (size_t i = m; i < nums1.size(); i++){
            nums1[i] = nums2[i-m];
        }
        for (size_t i = m; i < nums1.size(); i++)
        {
            for (size_t j = 0; j < i; j++)
            {
                if (nums1[i] < nums1[j])
                {
                    int temp = nums1[i];
                    nums1[i] = nums1[j];
                    nums1[j] = temp;
                    i = m;
                    continue;
                }
                
            }
            
        }
        
    }
};
// @lc code=end

