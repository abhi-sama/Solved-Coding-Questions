class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=-1
        currSum=0
        start=-1
        ansStart=-1
        ansEnd=-1
        maxEle=max(nums)
        if(maxEle<=0):
            return maxEle
        for i in range(0,len(nums)):
            if currSum==0:
                start=i
            if (currSum+nums[i])>=0:
                currSum+=nums[i]
                ansStart=start
                ansEnd=i
            else:
                currSum=0
            if currSum>maxSum:
                maxSum=currSum
        
        return maxSum