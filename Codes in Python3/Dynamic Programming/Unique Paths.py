#Bottom Up Space Optimised Approach
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev=[0]*n
        for i in range(0,m):
            curr=[0]*n
            for j in range(0,n):
                if i==0 and j==0:
                    curr[0]=1
                    continue
                left=curr[j-1] if j in range(0,n) else 0
                up=prev[j] if i in range(0,m) else 0
                curr[j]=left+up
            prev=curr

        return prev[n-1]

# TC=O(m*n)
# SC=O(n)            

#Bottom Up Approach
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n for _ in range(0,m)]
        for i in range(0,m):
            for j in range(0,n):
                if i==0 and j==0:
                    dp[0][0]=1
                    continue
                left=dp[i][j-1] if j in range(0,n) else 0
                up=dp[i-1][j] if i in range(0,m) else 0
                dp[i][j]=left+up

        return dp[m-1][n-1]


# TC=O(m*n)
# SC=O(m*n)            



#Recursion
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def f(i,j):
            if i==0 and j==0:
                return 1

            if i not in range(0,m) or j not in range(0,n):
                return 0
            left=f(i,j-1)
            up=f(i-1,j)
            ways=left+up
            return ways
        
        return f(m-1,n-1)
            
# TC=O(2^(m+n))
# SC=O(m+n)
        

#Top Down Approach
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n for _ in range(0,m)]
        def f(i,j):
            if i==0 and j==0:
                return 1
            if i not in range(0,m) or j not in range(0,n):
                return 0
            if dp[i][j]!=0:
                return dp[i][j]
            left=f(i,j-1)
            up=f(i-1,j)
            dp[i][j]=left+up
            return dp[i][j]

        res= f(m-1,n-1)
        return res

# TC=O(m*n)
# SC=O(m*n)            