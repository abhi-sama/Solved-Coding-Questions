#Bottom Up Approach
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp={0:1}
        for total in range(1,target+1):
            dp[total]=0
            for num in nums:
                dp[total]+=dp.get(total-num,0)
        
        return dp[target]
    
# TC=O(n*target)
# Sc=O(target)

#Top Down Approach
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp={0:1}
        nums.sort() #Only to optimise it further
        def dfs(total):
            if total==0:
                return 1
            if total in dp:
                return dp[total]
            res=0
            for num in nums:
                if total-num>=0:
                    res+=dfs(total-num)
            dp[total]=res
            return dp[total]
        
        return dfs(target)
    
# TC=O(n*target) , TC=O(n^target) withoout dp
# Sc=O(target)