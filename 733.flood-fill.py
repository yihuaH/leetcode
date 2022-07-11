#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        temp_color = image[sr][sc]
        if temp_color == color:
            return 
        
        def dfs(r,c):
            if image[r][c] == temp_color:
                image[r][c] = color
                if r >= 1: dfs(r-1, c)
                if r+1 < len(image): dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < len(image[0]): dfs(r, c+1)
        dfs(sr,sc)    
        
        return image
            
        
# @lc code=end

