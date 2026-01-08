#Optimized using early stop 
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        subset=[]
        nums.sort()

        def dfs(i,sum):
            if target==sum:
                res.append(subset.copy())
                return
            for j in range(i,len(nums)):
                if sum+nums[i]>target:
                    return
                subset.append(nums[j])
                dfs(j,nums[j]+sum)
                subset.pop()
            
        dfs(0,0)
        return res

#  Solution 1
#--------------
# class Solution:
#     def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
#         res=[]
#         subset=[]

#         def dfs(i,sum):
#             if target==sum:
#                 res.append(subset.copy())
#                 return
#             if i>=len(nums) or sum>target:
#                 return
            
#             subset.append(nums[i])
#             dfs(i,nums[i]+sum)
#             subset.pop()
#             dfs(i+1,sum)
            
#         dfs(0,0)
#         return res
            