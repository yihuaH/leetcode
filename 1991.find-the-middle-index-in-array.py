#
# @lc app=leetcode id=1991 lang=python
#
# [1991] Find the Middle Index in Array
#

# @lc code=start
class Solution(object):
    def findMiddleIndex(self, nums):
        left = 0 
        right = sum(nums)
        for a in range(len(nums)):
            if a == 0:
                if right-nums[0] == 0:
                    return a
            if a == (len(nums)-1):
                if left == 0:
                    return a
            
            right -= nums[a]
            if left == right:
                return a
            left += nums[a]
        return -1
        
# @lc code=end

