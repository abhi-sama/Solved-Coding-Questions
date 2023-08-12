from math import *

class Solution:
    def matrixMultiplication(self, N, arr):
        dp=[[0]*N for _ in range(N)]
        for i in range(N-1,0,-1):
            for j in range(i+1,N):
                dp[i][j]=inf
                for k in range(i,j):
                    dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+arr[i-1]*arr[k]*arr[j])
        
        return dp[1][N-1]