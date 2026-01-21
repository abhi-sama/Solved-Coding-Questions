#Space Optimized
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        dp=[0]*len(nums)
        prev2=nums[0]
        prev=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            cur=max(prev,nums[i]+prev2)
            prev2=prev
            prev=cur
        return prev
# TC=O(n)
# SC=O(1)       

#Bottom Ups Approach
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-1],nums[i]+dp[i-2])
        
        return dp[-1]
# TC=O(n)
# SC=O(n)       


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo=[-1]*len(nums)

        def dfs(i):
            if i>=len(nums):
                return 0
            if memo[i]!=-1:
                return memo[i]
            memo[i]=max(dfs(i+1),nums[i]+dfs(i+2))
            return memo[i]
        return dfs(0)
# TC=O(n)
# SC=O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dfs(i):
            if i>=len(nums):
                return 0
            return max(dfs(i+1),nums[i]+dfs(i+2))
        return dfs(0)
# TC=O(2^n)
# SC=O(n)