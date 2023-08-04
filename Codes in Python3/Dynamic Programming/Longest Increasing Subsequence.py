class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        t=[1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    t[i]=max(t[j]+1,t[i])
        return max(t)