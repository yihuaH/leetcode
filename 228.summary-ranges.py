#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        templist=[]
        tempcount = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                tempcount += 1
            else:
                templist.append(tempcount)
                tempcount = 1
        templist.append(tempcount)
        ans = []
        indexofnums = 0
        print(templist)
        for i in range(len(templist)):
            if templist[i] == 1:
                ans.append(str(nums[indexofnums]))
                indexofnums += templist[i]
            else:
                ans.append(str(nums[indexofnums])+"->" + str(nums[indexofnums+templist[i]-1]))
                indexofnums += templist[i]
        return ans
        
                
# @lc code=end

