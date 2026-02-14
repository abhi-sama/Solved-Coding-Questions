# Space OptimBottom Up Approach
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        t=sum(nums)
        
        if t%2!=0 or n==1:
            return False
        target=t//2  
        next_row=[False]*(target+1)
    
        next_row[target]=True
        
        for i in range(n-1,-1,-1):
            curr_row = [False] * (target + 1)
            # Important: Even in the new row, if total == target, it's True
            curr_row[target] = True
            for total in range(target-1,-1,-1):
                dont= next_row[total]
                take=next_row[total+nums[i]] if i+1<n and total+nums[i] <=target  else False
                curr_row[total]= dont or take
            next_row=curr_row

        return next_row[0]
        
# TC=O(n*t)
# SC=O(t)

# Bottom Up Approach
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        t=sum(nums)
        
        if t%2!=0 or n==1:
            return False
        target=t//2  
        dp=[[False]*(target+1) for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][target]=True
        
        for i in range(n-1,-1,-1):
            for total in range(target-1,-1,-1):
                dont= dp[i+1][total] if i+1<n else False
                take=dp[i+1][total+nums[i]] if i+1<n and total+nums[i] <=target  else False
                dp[i][total]= dont or take

        return dp[0][0]
        
# TC=O(n*t)
# SC=O(n*t)


# Top Down Approach
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        t=sum(nums)
        
        if t%2!=0 or n==1:
            return False
        target=t//2  
        dp=[[-1]*(target+1) for _ in range(n+1)]

        def f(i,total,k):
            if k==total:
                return True
            if total > k or i==n:
                return False
            if dp[i][total]!=-1:
                return dp[i][total]
            dont= f(i+1,total,k)
            take=f(i+1,total+nums[i],k)
            dp[i][total]= dont or take
            return dp[i][total]

        return f(0,0,t//2)
        
# TC=O(n*t)
# SC=O(n*t)