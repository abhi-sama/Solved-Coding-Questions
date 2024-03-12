class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m=len(triangle)
        front=[0]*m
        cur=[0]*m
        for j in range(m):
            front[j] = triangle[m - 1][j]
    
        for i in range(m-2,-1,-1):
            for j in range(i,-1,-1):
                down= triangle[i][j]+front[j]
                diag= triangle[i][j]+front[j+1]
                cur[j]=min(down,diag)
            # Create a new list for front based on the values of cur
            front = cur[:]
        return front[0]

# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         m=len(triangle)
#         dp = [[0] * len(row) for row in triangle]
#         dp[m - 1] = triangle[m - 1]
#         for i in range(m-2,-1,-1):
#             for j in range(i,-1,-1):
#                 down= triangle[i][j]+dp[i+1][j]
#                 diag= triangle[i][j]+dp[i+1][j+1]
#                 dp[i][j]=min(down,diag)
#         return dp[0][0]