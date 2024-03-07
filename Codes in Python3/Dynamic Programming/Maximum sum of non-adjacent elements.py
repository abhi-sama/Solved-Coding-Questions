class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        prev2=-1
        prev=-1
        for index in range(n):
            pick = nums[index]
            if index>1:
                pick+=prev2
            notpick = 0 + prev
            curi = max(pick,notpick)
            prev2=prev
            prev=curi
        return prev
########################
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n=len(nums)
#         dp=[-1]*n
#         for index in range(n):
#             pick = nums[index]
#             if index>1:
#                 pick+=dp[index-2]
#             notpick = 0 + dp[index-1]
#             dp[index] = max(pick,notpick)
#         return dp[n-1]
#########################
# class Solution:
#     def msna(self,index,nums:List[int],n:int,dp:List[int]) -> int:
#         if index==0:
#             return nums[index]
#         if index<0:
#             return 0
#         if dp[index]!=-1:
#             return dp[index]
#         pick = nums[index]+self.msna(index-2,nums,n,dp)
#         notpick = 0 + self.msna(index-1,nums,n,dp)
#         dp[index] = max(pick,notpick)
#         return dp[index]
        
#     def rob(self, nums: List[int]) -> int:
#         n=len(nums)
#         dp=[-1]*n
#         return self.msna(n-1,nums,n,dp)