#
# @lc app=leetcode id=1394 lang=python3
#
# [1394] Find Lucky Integer in an Array
#

# @lc code=start
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        result = [0] * 501
        
        for i in range(len(arr)):
            result[arr[i]] += 1
        
        for i in range(1,len(result)):
            if i == result[i]:
                ans = i
        print(result)
        return int(ans)
# @lc code=end

