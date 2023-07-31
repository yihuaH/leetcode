#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vewels= "aeiouAEIOU"
        index = list()
        ans = ""
        for i in range(len(s)):
            if s[i] in vewels:
                index.append(i)
        for i in range(len(s)):
            if s[i] in vewels:
                ans +=(s[index[-1]])
                index.pop()
            else:
                ans +=(s[i])
            
        
        return ans        
                
        #long time and more memory        
        '''for i in range(len(index)//2):
            temp = s[index[i]]
            s=s[:index[i]]+s[index[-i-1]]+s[index[i]+1:]
            s=s[:index[-i-1]] + temp + s[index[-i-1]+1:]
            #long time and more memory
            '''
        return s
        
# @lc code=end

