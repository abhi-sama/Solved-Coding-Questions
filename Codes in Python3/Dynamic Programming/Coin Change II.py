#Space Optimised Approach
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cur=[0]*(amount+1)
        prev=[0]*(amount+1)
        cur[0]=1
        prev[0]=1

        for i in range(len(coins)):
            for amt in range(1,amount+1):
                dont=prev[amt] if i-1>=0 else 0
                take=cur[amt-coins[i]] if amt-coins[i]>=0 else 0
                cur[amt]=dont+take
            prev=cur
        ans=cur[amount]
        return ans if ans!=0 else 0
# TC=O(n*amt)
# SC=O(amt)

#Bottom-Up Approach
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[[0]*(amount+1) for _ in range(len(coins))]

        for i in range(len(coins)):
            dp[i][0]=1
        
        for i in range(len(coins)):
            for amt in range(1,amount+1):
                dont=dp[i-1][amt] if i-1>=0 else 0
                take=dp[i][amt-coins[i]] if amt-coins[i]>=0 else 0
                dp[i][amt]=dont+take
        ans=dp[len(coins)-1][amount]
        return ans if ans!=0 else 0
# TC=O(n*amt)
# SC=O(n*amt)

#Top Bottom Approach
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[[0]*(amount+1) for _ in range(len(coins))]
        def dfs(i,amt):
            if i<0 or amt<0:
                return 0
            if amt==0:
                return 1
            if dp[i][amt]!=0:
                return dp[i][amt]
            dont=dfs(i-1,amt)
            take=dfs(i,amt-coins[i])
            dp[i][amt]=dont+take
            return dp[i][amt]

        ans=0    
        ans=dfs(len(coins)-1,amount)
        return ans if ans!=0 else 0
        
# TC=O(n*amt)
# SC=O(n*amt)