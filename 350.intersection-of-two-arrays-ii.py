#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        length = len(nums2)
        shortList = nums2
        length2 = len(nums1)
        longList = nums1
        if len(nums1) < len(nums2):
            length = len(nums1)
            length2 = len(nums2)
            shortList = nums1
            longList = nums2
        for i in range(length):
                if shortList[i] in longList:
                    ans.append(shortList[i])
                    longList.remove(shortList[i])
        return ans
                    
# @lc code=end

