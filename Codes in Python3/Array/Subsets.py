class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        total_sub=[]
        for i in range(0,pow(2,len(nums))):
            subs=[]
            for j in range(0,len(nums)):
                if i & (1<<j):
                    subs.append(nums[j])
            total_sub.append(subs)
        
        return total_sub