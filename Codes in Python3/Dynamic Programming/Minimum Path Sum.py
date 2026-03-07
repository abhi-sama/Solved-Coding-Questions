#Space Optimised Bottom Up Approach
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        prev=[float('inf')]*(n+1) 
        
        for i in range(m-1,-1,-1):
            curr=[float('inf')]*(n+1)
            for j in range(n-1,-1,-1):
                if i==(m-1) and j==(n-1):
                     curr[j]=grid[i][j]
                else:
                    down=prev[j]
                    right=curr[j+1]
                    curr[j]=grid[i][j]+min(down,right)
            prev=curr
                
        return prev[0]

# TC=O(m*n)
# SC=O(n)

#Bottom Up Approach
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dp=[[float('inf')]*(n+1) for _ in range(m+1)]
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==(m-1) and j==(n-1):
                     dp[i][j]=grid[i][j]
                else:
                    down=dp[i+1][j]
                    right=dp[i][j+1]
                    dp[i][j]=grid[i][j]+min(down,right)
                
        return dp[0][0]

# TC=O(m*n)
# SC=O(m*n)

#Recursive Approach
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        minSum=0
        def dfs(i,j):
            if i not in range(0,m) or j not in range(0,n):
                return float('inf')
            if i==(m-1) and j==(n-1):
                return grid[i][j]
            nonlocal minSum
            down=dfs(i+1,j)
            right=dfs(i,j+1)
            minSum=grid[i][j]+min(down,right)
            return minSum
            

        dfs(0,0)
        return minSum

# TC=O(2^(m+n))
# SC=O(m+n)       

#Top Down Approach
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dp=[[-1]*(n+1) for _ in range(m+1)]
        def dfs(i,j):
            if i not in range(0,m) or j not in range(0,n):
                return float('inf')
            if i==(m-1) and j==(n-1):
                return grid[i][j]
            if dp[i][j]!=-1:
                return dp[i][j]
            down=dfs(i+1,j)
            right=dfs(i,j+1)
            dp[i][j]=grid[i][j]+min(down,right)
            return dp[i][j]

        return dfs(0,0)

# TC=O(m*n)
# SC=O(m*n)