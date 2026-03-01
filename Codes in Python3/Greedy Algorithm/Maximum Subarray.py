#Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start=-1
        ansStart=-1
        ansEnd=-1
        
        maxEle=max(nums)
        if maxEle<0:
            return maxEle

        maxSum=-float('inf')
        currSum=0

        for i in range(len(nums)):
            if currSum==0:
                start=i
            
            if currSum+nums[i]>0:
                currSum+=nums[i]
                ansStart=start
                ansEnd=i
            else:
                currSum=0
            
            maxSum=max(currSum,maxSum)
    
        return maxSum

# TC=O(n)
# SC=O(1)

#Brute Force
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxSum=-float('inf')
        for i in range(n):
            sum=0
            for j in range(i,n):
                sum+=nums[j]
                maxSum=sum if sum>maxSum else maxSum
        return maxSum

# TC=O(n^3)
# SC=O(1)

        