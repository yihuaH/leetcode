//
// Created by Administrator on 4/15/2022.
//
#include "leetcode.h"
using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int count = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == val){
                count ++;
            }else{
                nums[i-count] = nums[i];
            }
        }
        return nums.size()-count;
    }
};