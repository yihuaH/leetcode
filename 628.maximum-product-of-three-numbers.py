#
# @lc app=leetcode id=628 lang=python3
#
# [628] Maximum Product of Three Numbers
#

# @lc code=start
class Solution:
    

    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0]*nums[1]*nums[2]
        nagList = []
        posList = []
        for i in range(len(nums)):
            if nums[i] >= 0:
                posList.append(nums[i])
            else:
                nagList.append(nums[i])
        nagList.sort()
        posList.sort()
        print(nagList)
        print(posList)
        if len(nagList) < 2:
            return posList[-1]*posList[-2]*posList[-3]
        if len(posList) < 3:
            if len(posList)== 0:
                return nagList[-3]*nagList[-1]*nagList[-2]
            return nagList[0]*nagList[1]*posList[-1]
        if nagList[0]*nagList[1] < posList[-3]*posList[-2]:
            return posList[-1]*posList[-2]*posList[-3]
        else:
            return nagList[0]*nagList[1]*posList[-1]
        
# @lc code=end

