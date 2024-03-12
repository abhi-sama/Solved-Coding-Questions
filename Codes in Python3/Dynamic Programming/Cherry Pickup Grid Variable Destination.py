
from os import *
from sys import *
from collections import *
from math import *
import sys
from typing import List


def maximumChocolates(n: int, m: int, grid: List[List[int]]) -> int:
    front=[[0]*m for i in range(m)]
    cur=[[0]*m for i in range(m)]
    for j1 in range(m):
        for j2 in range(m):
            if j1 == j2:
                front[j1][j2] = grid[n - 1][j1]
            else:
                front[j1][j2] = grid[n - 1][j1] + grid[n - 1][j2]

    for i in range(n - 2, -1, -1):
        for j1 in range(m):
            for j2 in range(m):
                maxi = -sys.maxsize

                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ans = 0
                        if j1 == j2:
                            ans = grid[i][j1]
                        else:
                            ans = grid[i][j1] + grid[i][j2]

                        if ((j1 + di < 0 or j1 + di >= m) or (j2 + dj < 0 or j2 + dj >= m)):
                            ans += int(-1e9) 
                        else:
                            ans += front[j1 + di][j2 + dj]  

                        maxi = max(ans, maxi)

                cur[j1][j2] = maxi
        front=[row[:] for row in cur]

    return front[0][m - 1]
    pass

# from os import *
# from sys import *
# from collections import *
# from math import *
# import sys
# from typing import List


# def maximumChocolates(n: int, m: int, grid: List[List[int]]) -> int:
#     dp = [[[0 for _ in range(m)] for _ in range(m)] for _ in range(n)]

#     for j1 in range(m):
#         for j2 in range(m):
#             if j1 == j2:
#                 dp[n - 1][j1][j2] = grid[n - 1][j1]
#             else:
#                 dp[n - 1][j1][j2] = grid[n - 1][j1] + grid[n - 1][j2]

#     for i in range(n - 2, -1, -1):
#         for j1 in range(m):
#             for j2 in range(m):
#                 maxi = -sys.maxsize

#                 for di in range(-1, 2):
#                     for dj in range(-1, 2):
#                         ans = 0
#                         if j1 == j2:
#                             ans = grid[i][j1]
#                         else:
#                             ans = grid[i][j1] + grid[i][j2]

#                         if ((j1 + di < 0 or j1 + di >= m) or (j2 + dj < 0 or j2 + dj >= m)):
#                             ans += int(-1e9) 
#                         else:
#                             ans += dp[i + 1][j1 + di][j2 + dj]  

#                         maxi = max(ans, maxi)

#                 dp[i][j1][j2] = maxi

#     return dp[0][0][m - 1]
#     pass


# from os import *
# from sys import *
# from collections import *
# from math import *

# from typing import List
# def f(i,j1,j2,r: int, c: int, grid: List[List[int]],dp)->int:
#     if j1<0 or j1>=c or j2<0 or j2>=c:
#         return float('-inf')
#     if i==r-1:
#         if j1==j2:
#             return grid[i][j1]
#         else:
#             return grid[i][j1]+grid[i][j2]
#     if not dp[i][j1][j2]== -1:
#         return dp[i][j1][j2]
#     maxi= float('-inf')
#     for delj1 in range(-1,2):
#         for delj2 in range(-1,2):
#             ans=0
#             if j1==j2:
#                 ans=grid[i][j1]+f(i+1,j1+delj1,j2+delj2,r,c,grid,dp)
#             else:
#                 ans=grid[i][j1]+grid[i][j2]+f(i+1,j1+delj1,j2+delj2,r,c,grid,dp)
#             maxi=max(maxi,ans)
#     dp[i][j1][j2]=maxi
#     return maxi

# def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
#     dp=[[[-1 for i in range(c)] for j in range(c)] for k in range(r)]
#     return f(0,0,c-1,r,c,grid,dp)
#     pass
