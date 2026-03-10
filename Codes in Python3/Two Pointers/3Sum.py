#Using Two Pointer
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=[]
        for k in range(n):
            if nums[k]>0:
                break
            if k>0 and nums[k]==nums[k-1]:
                continue
            l=k+1
            r=n-1
            while l<r:
                totalSum=nums[l]+nums[r]+nums[k]
                if totalSum<0:
                    l+=1
                elif totalSum>0:
                    r-=1
                else:
                    res.append([nums[l],nums[r],nums[k]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1

        return res
# TC=O(n^2)
# SC=O(1)
        