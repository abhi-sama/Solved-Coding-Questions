#Space Optimised Bottom Up Recursion
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        SUM=sum(nums)
        if (SUM - target) < 0 or (SUM - target) % 2 != 0:
            return 0
        x = (SUM - target) // 2
        prev=[0]*(x+1)
        prev[0]=1

        for i in range(1,len(nums)+1):
            next=[0]*(x+1)
            for amt in range(x+1):
                dont=prev[amt]
                take=0
                if nums[i-1]<=amt:
                    take=prev[amt-nums[i-1]]
                next[amt]=take+dont
            prev=next

        return prev[x]

# TC=O(n*m)
# SC=O(m)
# where n is no. of elements and m is the sum of all the elements

#Bottom Up Recursion
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        SUM=sum(nums)
        if (SUM - target) < 0 or (SUM - target) % 2 != 0:
            return 0
        x = (SUM - target) // 2
        dp=[[0]*(x+1) for _ in range(len(nums)+1)]
        dp[0][0]=1

        for i in range(1,len(nums)+1):
            for amt in range(x+1):
                dont=dp[i-1][amt]
                take=0
                if nums[i-1]<=amt:
                    take=dp[i-1][amt-nums[i-1]]
                dp[i][amt]=take+dont


        return dp[len(nums)][x]

# TC=O(n*m)
# SC=O(n*m)
# where n is no. of elements and m is the sum of all the elements

#Top Down Recursion
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        SUM = sum(nums)
        # Standard subset sum reduction
        if (SUM - target) < 0 or (SUM - target) % 2 != 0:
            return 0
        
        x = (SUM - target) // 2
        memo = {}

        def f(i, amt):
            # Base Case: If we have processed all elements (reached index 0)
            if i == 0:
                return 1 if amt == 0 else 0
            
            if (i, amt) in memo:
                return memo[(i, amt)]
            
            # Since we are starting from the back, the "current" element is at i-1
            # Option 1: Don't take nums[i-1]
            dont = f(i - 1, amt)
            
            # Option 2: Take nums[i-1]
            take = 0
            if nums[i - 1] <= amt:
                take = f(i - 1, amt - nums[i - 1])
            
            memo[(i, amt)] = dont + take
            return dont + take

        return f(len(nums), x)

# TC=O(n*m)
# SC=O(n*m)
# where n is no. of elements and m is the sum of all the elements


#Recursion
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        SUM=sum(nums)
        if (SUM - target) < 0 or (SUM - target) % 2 != 0:
            return 0
        x = (SUM - target) // 2

        def f(i,amt):
            if i==len(nums):
                return 1 if amt==0 else 0
            
            dont=f(i+1,amt)
            take=0
            if nums[i]<=amt:
                take=f(i+1,amt-nums[i])
            return take+dont

        return f(0,x)

# TC=O(2^n)
# SC=O(n)