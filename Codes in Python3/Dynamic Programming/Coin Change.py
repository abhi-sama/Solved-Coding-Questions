#Space Optimised
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cur=[float('inf')]*(amount+1)
        prev=[float('inf')]*(amount+1)
        prev[0]=0
        cur[0]=0
        
        for i in range(len(coins)):
            for a in range(1,amount+1):
                take=float('inf')
                dont = prev[a] if i > 0 else float('inf')
                if a >=coins[i]:
                    take=1+cur[a-coins[i]]
                cur[a]=min(dont,take)
            prev=cur
        ans=prev[amount]
        return ans if ans!=float('inf') else -1
        
# TC=O(n*amount)
# SC=O(amount)

#Bottom's Up Approach
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[[float('inf')]*(amount+1) for _ in range(len(coins))]

        for i in range(len(coins)):
            dp[i][0]=0
        
        for i in range(len(coins)):
            for a in range(1,amount+1):
                take=float('inf')
                dont = dp[i-1][a] if i > 0 else float('inf')
                if a >=coins[i]:
                    take=1+dp[i][a-coins[i]]
                dp[i][a]=min(dont,take)
        ans=dp[len(coins)-1][amount]
        return ans if ans!=float('inf') else -1
        
            
# TC=O(n*amount)
# SC=O(n*amount)

#Top Down Approach
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[[1e9]*(amount+1) for _ in range(len(coins))]
        def dfs(i,amount):
            if i<0:
                return 1e9
            if amount==0:
                return 0
            if dp[i][amount]!=1e9:
                return dp[i][amount]
            take=1e9
            dont=0+dfs(i-1,amount)
            if amount >=coins[i]:
                take=1+dfs(i,amount-coins[i])
            dp[i][amount]=min(dont,take)

            return dp[i][amount]

        ans=dfs(len(coins)-1,amount)
        return ans if ans!=1e9 else -1
            
# TC=O(n*amount)
# SC=O(n*amount)


#Recursive Approach
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def dfs(i,amount):
            if i<0:
                return 1e9
            if amount==0:
                return 0
            
            take=1e9
            dont=0+dfs(i-1,amount)
            if amount >=coins[i]:
                take=1+dfs(i,amount-coins[i])
            res=min(dont,take)
            return res

        ans=dfs(len(coins)-1,amount)
        return ans if ans!=1e9 else -1
            
# TC=O(n^amount)
# SC=O(amount)
        
        