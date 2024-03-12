class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        prev=[0]*n
        for i in range(m):
            temp=[0]*n
            for j in range(n):
                if i==0 and j==0:
                    temp[j]= grid[i][j]
                else:
                    up=0
                    left=0
                    up+=grid[i][j]
                    if i>0:
                        up+=prev[j]
                    else:
                        up+=float('inf')
                    left+=grid[i][j]
                    if j>0:
                        left+=temp[j-1]
                    else:
                        left+=float('inf')
                    temp[j]=min(up,left)
            prev=temp
        return prev[n-1]    
                    
# class Solution:
#     def f(self,i,j,grid: List[List[int]],dp):
#         m=len(grid)
#         n=len(grid[0])       
#         if i==0 and j==0:
#             return grid[i][j]
#         if i<0 or j<0:
#             return float('inf')
#         if dp[i][j] is not -1:
#             return dp[i][j]
#         up = grid[i][j] + self.f(i-1,j,grid,dp)
#         left= grid[i][j] + self.f(i,j-1,grid,dp)
#         dp[i][j]=min(up,left)
#         return dp[i][j]
        
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         m=len(grid)
#         n=len(grid[0])
#         dp=[[-1]*n for _ in range(m)]
#         return self.f(m-1,n-1,grid,dp)     