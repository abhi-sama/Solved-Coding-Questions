#Greedy Approach
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin,leftMax=0,0

        for c in s:
            if c=="(":
                leftMin,leftMax=leftMin+1,leftMax+1
            elif c==")":
                leftMin,leftMax=leftMin-1,leftMax-1
            else:
                leftMin,leftMax=leftMin-1,leftMax+1
            if leftMax<0:
                return False
            if leftMin<0:
                leftMin=0    
        return leftMin==0

# TC=O(n)
# SC=O(n)

#Dynamic Bottom Up
class Solution:
    def checkValidString(self, s: str) -> bool:
        n=len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        dp[n][0] = True

        def dfs(i,open):
            if open<0:
                return False
            if i==len(s):
                return open==0
            if memo[i][open] is not None:
                return memo[i][open]
            if s[i]=='(':
                return dfs(i+1,open+1)
            elif s[i]== ')':
                return dfs(i+1,open-1)
            else:
                return (dfs(i+1,open) or dfs(i+1,open+1) or dfs(i+1,open-1))

        for i in range(n-1,-1,-1):
            for open in range(n):
                res=False
                if s[i]=='*':
                    res|=dp[i+1][open+1]
                    if open>0:
                        res|=dp[i+1][open-1]
                    res|=dp[i+1][open]
                else:
                    if s[i]=='(':
                        res|=dp[i+1][open+1]
                    elif open>0:
                        res|=dp[i+1][open-1]
                dp[i][open]=res

        return dp[0][0]

# TC=O(n^2)
# SC=O(n^2)


#Dynamic Top Down
class Solution:
    def checkValidString(self, s: str) -> bool:
        n=len(s)
        memo=[[None]*(n+1) for _ in range(n+1)]

        def dfs(i,open):
            if open<0:
                return False
            if i==len(s):
                return open==0
            if memo[i][open] is not None:
                return memo[i][open]
            if s[i]=='(':
                return dfs(i+1,open+1)
            elif s[i]== ')':
                return dfs(i+1,open-1)
            else:
                return (dfs(i+1,open) or dfs(i+1,open+1) or dfs(i+1,open-1))

        return dfs(0,0)

# TC=O(n^2)
# SC=O(n^2)


#Recursion
class Solution:
    def checkValidString(self, s: str) -> bool:

        def dfs(i,open):
            if open<0:
                return False
            if i==len(s):
                return open==0
            
            if s[i]=='(':
                return dfs(i+1,open+1)
            elif s[i]== ')':
                return dfs(i+1,open-1)
            else:
                return (dfs(i+1,open) or dfs(i+1,open+1) or dfs(i+1,open-1))

        return dfs(0,0)

# TC=O(3^n)
# SC=O(n)
               