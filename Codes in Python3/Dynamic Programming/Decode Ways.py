#DP Bottom-Up Space Omptimized Approach
# Key Observation anything starting from 0 will
# not be part part of any sequence
class Solution:
    def numDecodings(self, s: str) -> int:
        next_one=1 #Corresponds to dp[len(s))
        next_two=0
        
        for i in range(len(s)-1,-1,-1):
            current=0
            if s[i]=="0":
                current=0
            else:
                current=next_one
            if i+1<len(s):
                if (s[i]=="1" or (s[i]=="2" and s[i+1]<="6")):
                    current+=next_two
            next_two=next_one
            next_one=current
            
        return next_one   

# TC=O(n^2)
# Sc=O(1)

#DP Bottom-Up Approach
# Key Observation anything starting from 0 will
# not be part part of any sequence
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}
        
        for i in range(len(s)-1,-1,-1):
            if s[i]=="0":
                dp[i]=0
            else:
                dp[i]=dp[i+1]
            if i+1<len(s):
                if (s[i]=="1" or (s[i]=="2" and s[i+1]<="6")):
                    dp[i]+=dp[i+2]
        return dp[0]   

# TC=O(n^2)
# Sc=O(n)


#DP Recursion Approach
# Key Observation anything starting from 0 will
# not be part part of any sequence
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}
        def dfs(i:int):
            if i in dp:
                return dp[i]
            if s[i]=="0":
                return 0
            dp[i]=dfs(i+1)
            if i+1<len(s):
                if (s[i]=="1" or (s[i]=="2" and s[i+1]<="6")):
                    dp[i]+=dfs(i+2)
            res=dp[i]
            return res
        return dfs(0)
# TC=O(n^2)
# Sc=O(n)

#Recursion Approach
# Key Observation anything starting from 0 will
# not be part part of any sequence
class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(i:int):
            if i==len(s):
                return 1
            if s[i]=="0":
                return 0
            res=dfs(i+1)
            if i+1<len(s):
                if (s[i]=="1" or (s[i]=="2" and s[i+1]<="6")):
                    res+=dfs(i+2)
            return res
        return dfs(0)
# TC=O(2^n)
# Sc=O(n)