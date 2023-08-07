#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = bin(x)
        b = bin(y)
        a = a[2:]
        b = b[2:]
        ans = 0
        while (len(a) > 0 and len(b) >0):
            if a[-1] != b[-1]:
                ans += 1
            a = a[:-1]
            b = b[:-1]

        print(b)
        print (ans)
        if len(a) != 0:
            while len(a) > 0:
                if a[-1] == "1":
                    ans +=1
                a = a[:-1]
        if len(b) != 0:
            while len(b) > 0:
                if b[-1] == "1":
                    ans +=1
                b = b[:-1] 
                print(b)
        print(ans)        
        return ans

# @lc code=end

