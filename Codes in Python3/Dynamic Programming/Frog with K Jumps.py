from typing import *
from math import *
def minimizeCost(n : int, k : int, heights : List[int]) -> int:
    dp=[0]*n
    for i in range(1,n):
        minE=inf
        for j in range(1,k+1):
            if i-j>=0:
                minE=min(minE,dp[i-j]+abs(heights[i]-heights[i-j]))
        dp[i]=minE
    return dp[n-1]
    pass