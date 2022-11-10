#
# @lc app=leetcode id=576 lang=python3
#
# [576] Out of Boundary Paths
#

# @lc code=start
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        '''
        def move(m: int, n: int, maxMove: int, startRow: int, startColumn: int, dirction: int, ans: int) -> int:
            if maxMove == 0:
                return ans
            if(dirction == 1):
                #up
                startRow -= 1
                if startRow < 0:
                    ans += 1
                    return ans
                else:
                    return (move(m,n,maxMove-1,startRow,startColumn,1,ans)+move(m,n,maxMove-1,startRow,startColumn,2,ans)+move(m,n,maxMove-1,startRow,startColumn,3,ans)+move(m,n,maxMove-1,startRow,startColumn,4,ans))%(10**9+7)
                    
            elif dirction == 2:
                #down
                startRow += 1
                if startRow == m:
                    ans += 1
                    return ans
                else:
                    return (move(m,n,maxMove-1,startRow,startColumn,1,ans)+move(m,n,maxMove-1,startRow,startColumn,2,ans)+move(m,n,maxMove-1,startRow,startColumn,3,ans)+move(m,n,maxMove-1,startRow,startColumn,4,ans))%(10**9+7)
            elif dirction ==3:
                #left
                startColumn -= 1
                if startColumn < 0:
                    ans += 1
                    return ans
                else:
                    return (move(m,n,maxMove-1,startRow,startColumn,1,ans)+move(m,n,maxMove-1,startRow,startColumn,2,ans)+move(m,n,maxMove-1,startRow,startColumn,3,ans)+move(m,n,maxMove-1,startRow,startColumn,4,ans))%(10**9+7)
                
            elif dirction == 4:
                #right
                startColumn += 1
                if startColumn == n:
                    ans += 1
                    return ans
                else:
                    return (move(m,n,maxMove-1,startRow,startColumn,1,ans)+move(m,n,maxMove-1,startRow,startColumn,2,ans)+move(m,n,maxMove-1,startRow,startColumn,3,ans)+move(m,n,maxMove-1,startRow,startColumn,4,ans))%(10**9+7)
        
        return (move(m,n,maxMove,startRow,startColumn,1,0)+move(m,n,maxMove,startRow,startColumn,2,0)+move(m,n,maxMove,startRow,startColumn,3,0)+move(m,n,maxMove,startRow,startColumn,4,0))%(10**9+7)   
        
        '''
        
        # define the dp array
        dp = [[[-1]*(maxMove+1) for _ in range(n+1)] for _ in range(m+1)]
        
        def solve(i, j, maxMove):
            if maxMove < 0:
                return 0
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            
			# if the dp array at this position contains some value(not -1) then it means it has been computed earlier
			# so we don't need to compute again, hence return whatever value is present in dp.
            if dp[i][j][maxMove] != -1:
                return dp[i][j][maxMove]
            
			# otherwise compute the value
            a = solve(i-1, j, maxMove - 1)
            b = solve(i+1, j, maxMove - 1)
            c = solve(i, j-1, maxMove - 1)
            d = solve(i, j+1, maxMove - 1)
            
			# store the computed value in dp array so that we do not need to compute it again when the same input occurs again.
            dp[i][j][maxMove] = a + b + c + d
            return dp[i][j][maxMove]
        
        return solve(startRow, startColumn, maxMove) % 1000000007
            
        
# @lc code=end

