#Space Optimised Bottom Up Approach
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n,m,o=len(s1),len(s2),len(s3)
        if n+m!=o:
            return False
        if m<n:
            s1,s2=s2,s1
            n,m=m,n
            
        next_row = [False] * (m + 1)
        next_row[m]=True

        for i in range(n,-1,-1):
            curr_row = [False] * (m + 1)
            if i == m:
                curr_row[n] = True
            for j in range(m,-1,-1):
                if i==n and j==m:
                    curr_row[j]=True
                if i<n and s1[i]==s3[i+j] and next_row[j]:
                    curr_row[j]=True
                if j<m and s2[j]==s3[i+j] and curr_row[j+1]:
                    curr_row[j]=True
            next_row=curr_row
        return next_row[0]

# TC=O(m*n)
# SC=O(min(m,n))


#Bottom Up Approach
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n,m,o=len(s1),len(s2),len(s3)
        if n+m!=o:
            return False
        dp=[[False]*(m+1) for _ in range(n+1)]
        dp[n][m]=True

        for i in range(n,-1,-1):
            for j in range(m,-1,-1):
                if i<n and s1[i]==s3[i+j] and dp[i+1][j]:
                    dp[i][j]=True
                if j<m and s2[j]==s3[i+j] and dp[i][j+1]:
                    dp[i][j]=True

        return dp[0][0]

# TC=O(m*n)
# SC=O(m+n)


#Top Down Approach
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n,m,o=len(s1),len(s2),len(s3)
        dp=[[-1]*(m+1) for _ in range(n+1)]
        def f(i,j,k):
            if k==o:
                return i==n and j==m
            if dp[i][j]!=-1:
                return dp[i][j]
            res=False
            if i<n and s1[i]==s3[k]:
                res=f(i+1,j,k+1)
            if not res and j<m and s2[j]==s3[k]:
                res=f(i,j+1,k+1)

            dp[i][j]= res
            return dp[i][j]

        return f(0,0,0) 

# TC=O(m*n)
# SC=O(m+n)


#Recursion
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n,m,o=len(s1),len(s2),len(s3)
        
        def f(i,j,k):
            if k==o:
                return i==n and j==m
            if i<n and s1[i]==s3[k]:
                if f(i+1,j,k+1):
                    return True
            if j<m and s2[j]==s3[k]:
                if f(i,j+1,k+1):
                    return True
            return False

        return f(0,0,0) 

# TC=O(2^(m+n))
# SC=O(m+n)