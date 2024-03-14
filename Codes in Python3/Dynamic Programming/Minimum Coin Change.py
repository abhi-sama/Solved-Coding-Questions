class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        prev=[0]*(amount +1)
        cur=[0]*(amount +1)
        for i in range(amount+1):
            if (i%coins[0])==0:
                prev[i]= i//coins[0]
            else:
                prev[i]= int(1e9)
        for i in range(1,len(coins)):
            for W in range(amount+1):
                not_pick=prev[W]
                pick= int(1e9)
                if coins[i]<=W:
                    pick=1+ cur[W-coins[i]]
                cur[W]=min(pick,not_pick)
            prev=cur[:]
        ans=prev[amount]
        if(ans>=int(1e9)):
            return -1
        return ans