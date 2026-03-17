#Dynamic Programming
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy=prices[0]
        maxProfit=0
        for sell in prices:
            minBuy=min(minBuy,sell)
            maxProfit=max(sell-minBuy,maxProfit)
        return maxProfit

# TC=O(n)
# SC=O(1)

#Brute Force
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        for i in range(len(prices)):
            buy=prices[i]
            for j in range(i+1,len(prices)):
                sell=prices[j]
                res=max(res,sell-buy)
        return res
# TC=O(n^2)
# SC=O(1)