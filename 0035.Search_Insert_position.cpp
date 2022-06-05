//
// Created by Yihua Hao on 5/30/2022.
//



class Solution {
public:
  int searchInsert(vector<int>& nums, int target) {
    int ans = 0;
    int i = 0;
    int n = nums.size() - 1;
    int mid = (i + n) / 2;
    while(i<=n){
      if (nums[mid]<target){
        i = mid + 1;
      }else if(nums[mid]>target){
        n = mid - 1;
      } else{
        return mid;
      }
      mid = (i+n)/2;
    }
    return i;
  }
};