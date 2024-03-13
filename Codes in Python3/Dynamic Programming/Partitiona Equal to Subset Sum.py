class Solution:
    def subsetSumToK(self,n, k, arr):
        prev=[False]*(k+1)
        cur=[False]*(k+1)       
        prev[0]=cur[0]=True
        if arr[0] <= k:
            prev[arr[0]] = True
        for i in range(1,n):
            for target in range(0,k+1):
                not_take=prev[target]
                take=False
                if arr[i]<=target:
                    take=prev[target-arr[i]]
                cur[target]=not_take or take
            prev=cur[:]
        return prev[k]

    def canPartition(self, nums: List[int]) -> bool:
        total_sum=sum(nums)
        if(total_sum%2):
            return False
        target=total_sum//2
        return self.subsetSumToK(len(nums),target,nums)