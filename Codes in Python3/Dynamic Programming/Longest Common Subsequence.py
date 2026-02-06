#DP Space Optimised Bottom-Up Approach
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1)<len(text2):
            text1,text2=text2,text1
        #Whichever is shorter string that size dp array should
        #be created to optimised space
        prev=[0]*(len(text2)+1) 
        
        for i in range(1,len(text1)+1):
            curr=[0]*(len(text2)+1) 
            for j in range(1,len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    curr[j]=prev[j-1]+1
                else:
                    curr[j]=max(curr[j-1],prev[j])  
            prev=curr       

        return prev[len(text2)]
# TC=O(m*n)
# SC=O(min(m,n))
        
#DP Bottom-Up Approach
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])         

        return dp[len(text1)][len(text2)]
# TC=O(m*n)
# SC=O(m*n)
        
#DP Top-Down Approach
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[-1]*(len(text2)+1) for _ in range(len(text1)+1)]
        
        def f(i,j):
            if i not in range(0,len(text1)) or j not in range(0,len(text2)):
                return 0

            if dp[i][j]!=-1:
                return dp[i][j]

            if text1[i]==text2[j]:
                dp[i][j]=f(i-1,j-1)+1
            else:
                dp[i][j]=max(f(i,j-1),f(i-1,j))
            return dp[i][j]

        return f(len(text1)-1,len(text2)-1)
# TC=O(m*n)
# SC=O(m*n)
        

#Recursion
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def f(i,j):
            if i not in range(0,len(text1)) or j not in range(0,len(text2)):
                return 0
            res=-float("inf")
            if text1[i]==text2[j]:
                res=f(i-1,j-1)+1
            else:
                res=max(f(i,j-1),f(i-1,j))
            return res
        ans=f(len(text1)-1,len(text2)-1)
        return ans
# TC=O(2^(m+n))
# SC=O(m+n)
        