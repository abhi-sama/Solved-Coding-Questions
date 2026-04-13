class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix,postfix=1,1
        res=[1]*n

        for i in range(n):
            res[i]=prefix
            prefix*=nums[i]
        
        for i in range(n-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res

# TC=O(n)
# SC=O(n)