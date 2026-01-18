#Solution 2
class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        res=set()
        subset=[]
        def backtrack(ind):
            if ind == len(nums):
                return res.add(tuple(subset))
            
            subset.append(nums[ind])
            backtrack(ind+1)
            subset.pop()
            while ind+1<len(nums) and nums[ind]==nums[ind+1]:
                ind+=1
            backtrack(ind+1)
        backtrack(0)
        return [list(s) for s in res]
# TC=O(n.2^n)
# SC=O(n)
        
#Solution 1
# class Solution(object):
#     def subsetsWithDup(self, nums):
#         res = set()

#         def backtrack(i, subset):
#             if i == len(nums):
#                 res.add(tuple(subset))
#                 return

#             subset.append(nums[i])
#             backtrack(i + 1, subset)
#             subset.pop()
#             backtrack(i + 1, subset)

#         nums.sort()
#         backtrack(0, [])
#         return [list(s) for s in res]
        