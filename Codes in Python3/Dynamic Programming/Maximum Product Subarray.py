#Optimal Solution
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix=1
        suffix=1
        maxSum=-float('inf')
        for i in range(len(nums)):
            prefix=nums[i]*(prefix or 1)
            if prefix>maxSum:
                maxSum=prefix

            suffix=nums[-(i+1)]*(suffix or 1)
            if suffix>maxSum:
                maxSum=suffix
            
        return maxSum
        
# TC=O(n)
# SC=O(1)

#Brute Force Solution
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        
        for i in range(len(nums)):
            cur=nums[i]
            res=max(res,cur)
            for j in range(i+1,len(nums)):
                cur*=nums[j]
                res=max(res,cur)

        return res
        
# TC=O(n^2)
# SC=O(1)