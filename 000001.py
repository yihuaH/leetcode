from re import T
from unicodedata import digit


class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        count = 0
        if len(nums) == 1:
            return [0, 1]
        check = [0] * len(nums)
        for i in range(len(nums)):
            if check[i] == 1:
                continue
            for j in range(i+1, len(nums)):
                if check[j] == 1:
                    continue
                if nums[i] == nums[j]:
                    count += 1
                    check[i] = 1
                    check[j] = 1
                    
        return [count, len(nums)-(2*count)]

class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        digit_sum = []
        temp_nums = [[]]
        for i in nums:
            sum = 0
            for digit in str(i): 
                sum += int(digit)
            if sum not in digit_sum:      
                digit_sum.append(sum)
                temp_nums.append([])
                temp_nums[digit_sum.index(sum)].append(i)
            else:
                temp_nums[digit_sum.index(sum)].append(i)
        ans = -1
        print(temp_nums)
        for i in temp_nums:
            if len(i) < 2:
                continue
            else:
                i.sort(reverse=True)
                temp_ans = i[0]+i[1]
                ans = max(ans, temp_ans)
        return ans
    
    class Solution:
    def smallestTrimmedNumbers(self, nums: list[str], queries: list[list[int]]) -> list[int]:
        ans = []
        for k, trim in queries:
            tmp = []
            for i, num in enumerate(nums):
                tmp.append([int(num[-trim:]), i])
            tmp.sort(reverse=True)
            ans.append(tmp[-k][1])
        return ans
        
        