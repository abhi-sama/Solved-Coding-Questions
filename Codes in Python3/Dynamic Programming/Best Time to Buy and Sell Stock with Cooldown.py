#Space Optimised Bottom Up Approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        next1=[0]*2 
        next2=[0]*2
        for i in range(n-1,-1,-1):
            curr=[0]*2 
            for buy in range(1,-1,-1):
                if buy:
                    curr[buy]=max(next1[1],-prices[i]+next1[0]) 
                else:
                    curr[buy]=max(next1[0],next2[1]+prices[i])             
            next2=next1
            next1=curr
        return next1[1]

# TC=O(n)
# SC=O(1)
        

#Bottom Up Approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0]*2 for _ in range(n+2)]
        for i in range(n-1,-1,-1):
            for buy in range(1,-1,-1):
                if buy:
                    dp[i][buy]=max(dp[i+1][1],-prices[i]+dp[i+1][0]) 
                else:
                    dp[i][buy]=max(dp[i+1][0],dp[i+2][1]+prices[i])             
       
        return dp[0][1]

# TC=O(n)
# SC=O(n)
        
#Top Down Approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1]*2 for _ in range(n)]
        def f(i,buy):
            if i>=n:
                return 0
            if dp[i][buy]!=-1:
                return dp[i][buy]
            if buy:
                dp[i][buy]=max(f(i+1,1),-prices[i]+f(i+1,0))
            else:
                dp[i][buy]=max(f(i+1,0),f(i+2,1)+prices[i])
            
            return dp[i][buy]
        return f(0,1)

# TC=O(n)
# SC=O(n)
        

#Top Down Approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1]*2 for _ in range(n)]
        def f(i,buy):
            if i>=n:
                return 0
            if dp[i][buy]!=-1:
                return dp[i][buy]
            if buy:
                dp[i][buy]=max(f(i+1,1),-prices[i]+f(i+1,0))
            else:
                dp[i][buy]=max(f(i+1,0),f(i+2,1)+prices[i])
            
            return dp[i][buy]
        return f(0,1)

# TC=O(n)
# SC=O(n)
        