#Top Down Approach
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[[-1]*(len(nums)+1) for _ in range(len(nums)+1)]
        def f(ind,prev_ind):
            if ind==len(nums):
                return 0
            if dp[ind][prev_ind]!=-1:
                return dp[ind][prev_ind]
            LIS= f(ind+1,prev_ind) #Dont Include Current element
            if prev_ind==-1 or nums[ind]>nums[prev_ind]:
                LIS=max(LIS,1+f(ind+1,ind)) #Include Current Element
            dp[ind][prev_ind]=LIS
            return dp[ind][prev_ind]
        return f(0,-1)
    
# TC=O(n^2)
# SC=O(n^2)

#Recursive Approach
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def f(ind,prev_ind):
            if ind==len(nums):
                return 0
            
            LIS= f(ind+1,prev_ind) #Dont Include Current element
            if prev_ind==-1 or nums[ind]>nums[prev_ind]:
                LIS=max(LIS,1+f(ind+1,ind)) #Include Current Element

            return LIS

        return f(0,-1)
    
# TC=O(2^(n))
# SC=O(n)