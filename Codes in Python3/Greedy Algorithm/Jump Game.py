#Greedy Approach 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        goal=n-1

        for i in range(n-2,-1,-1):
            if i+nums[i]>=goal:
                goal=i
        
        return goal==0

# TC=O(n)
# SC=O(1)
        

#Bottom Up Approach
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[False]*n
        dp[-1]=True

        for i in range(n-2,-1,-1):
            end=min(n-1,i+nums[i])
            for j in range(i+1,end+1):
                if dp[j]:
                    dp[i]=True
                    break
        
        return dp[0]

# TC=O(n^2)
# SC=O(n)

#Top Down Approach
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        memo={}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i==n-1:
                return True
            if nums[i]==0:
                return False
            end=min(n-1,i+nums[i])
            for j in range(i+1,end+1):
                if dfs(j):
                    memo[i]=True
                    return True
            memo[i]=False
            return False
        
        return dfs(0)

# TC=O(n^2)
# SC=O(n)

        
#Recursion
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        def dfs(i):
            if i==n-1:
                return True
            end=min(n-1,i+nums[i])
            for j in range(i+1,end+1):
                if dfs(j):
                    return True
            return False
        
        return dfs(0)

# TC=O(n!)
# SC=O(n)

        