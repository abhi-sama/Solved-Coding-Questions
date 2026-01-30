from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dfs(i, amt):
            # Base Case: Success
            if amt == 0:
                return 0
            # Base Case: Failure
            if i == len(coins) or amt < 0:
                return float('inf')
            
            # Option 1: Don't take the current coin
            res = dfs(i + 1, amt)
            
            # Option 2: Take the current coin (stay at index i for infinite supply)
            take = 1 + dfs(i, amt - coins[i])
            
            return min(res, take)

        result = dfs(0, amount)
        return result if result != float('inf') else -1
