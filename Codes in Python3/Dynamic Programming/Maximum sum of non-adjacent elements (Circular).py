class Solution:
    def helper(self, nums: List[int]) -> int:
        n=len(nums)
        prev2=0
        prev=nums[0]
        for index in range(n):
            pick = nums[index]
            if index>1:
                pick+=prev2
            notpick = 0 + prev
            curi = max(pick,notpick)
            prev2=prev
            prev=curi
        return prev    
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        temp1=[]
        temp2=[]
        for i in range(n):
            if i!=0:
                temp1.append(nums[i])
            if i!=(n-1):
                temp2.append(nums[i])
        return max(self.helper(temp1),self.helper(temp2))  